"""
Semantic Parser - Converte linguaggio naturale in IR
"""

import os
import json
from typing import Dict, Any, Optional
from openai import OpenAI
from dotenv import load_dotenv

from .errors import ParseError, ValidationError
from .validator import IRValidator
from .languages import LanguageDetector, Language

# Carica variabili ambiente
load_dotenv()


class SemanticParser:
    """
    Parser semantico che usa LLM per capire intent
    """
    
    def __init__(self, api_key: str = None, language: str = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY non trovata")
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = "gpt-4-turbo-preview"
        
        # Componenti
        self.validator = IRValidator()
        self.lang_detector = LanguageDetector()
        self.language = language  # Lingua forzata (opzionale)
    
    def parse(self, code: str) -> Dict[str, Any]:
        """
        Converte codice naturale in Intermediate Representation
        
        Args:
            code: Codice in linguaggio naturale (italiano o inglese)
            
        Returns:
            IR in formato dict validato
            
        Raises:
            ParseError: Se il parsing fallisce
            ValidationError: Se l'IR non è valido
        """
        print(f"🔍 Parsing: {code[:50]}...")
        
        try:
            # Rileva lingua
            language = self._detect_language(code)
            
            # Costruisci prompt
            prompt = self._build_prompt(code)
            system_prompt = language.get_system_prompt()
            
            # Chiama LLM con retry
            ir = self._call_llm_with_retry(system_prompt, prompt, max_retries=2)
            
            # Valida IR
            self.validator.validate(ir)
            
            print(f"✅ Parsed: {len(ir.get('operations', []))} operazioni")
            
            return ir
            
        except json.JSONDecodeError as e:
            raise ParseError(f"Risposta LLM non è JSON valido: {e}", code=code)
        except Exception as e:
            if isinstance(e, (ParseError, ValidationError)):
                raise
            raise ParseError(f"Errore durante parsing: {e}", code=code)
    
    def _detect_language(self, code: str) -> Language:
        """Rileva lingua del codice"""
        if self.language:
            # Lingua forzata
            return self.lang_detector.get_language(self.language)
        else:
            # Auto-detect
            return self.lang_detector.detect(code)
    
    def _call_llm_with_retry(self, system_prompt: str, user_prompt: str, 
                             max_retries: int = 2) -> Dict[str, Any]:
        """Chiama LLM con retry su errori"""
        last_error = None
        
        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=0.1,
                    response_format={"type": "json_object"},
                    timeout=30
                )
                
                # Estrai e parse JSON
                ir_text = response.choices[0].message.content
                ir = json.loads(ir_text)
                
                return ir
                
            except Exception as e:
                last_error = e
                if attempt < max_retries - 1:
                    print(f"⚠️  Tentativo {attempt + 1} fallito, riprovo...")
                    continue
        
        # Tutti i tentativi falliti
        raise ParseError(f"LLM fallito dopo {max_retries} tentativi: {last_error}")

    def _build_prompt(self, code: str) -> str:
        """Costruisce prompt per parsing"""
        return f"""Converti questo codice in IR:

```
{code}
```

Rispondi con JSON valido."""


if __name__ == "__main__":
    # Test
    parser = SemanticParser()
    
    code = """
Carica il file vendite.csv.
Mostra le prime 5 righe.
Calcola la media della colonna importo.
Stampa il risultato.
"""
    
    ir = parser.parse(code)
    print("\n📦 IR Generato:")
    print(json.dumps(ir, indent=2, ensure_ascii=False))
