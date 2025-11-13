"""
Semantic Parser - Converte linguaggio naturale in IR
"""

import os
import json
from typing import Dict, Any
from openai import OpenAI
from dotenv import load_dotenv

# Carica variabili ambiente
load_dotenv()


class SemanticParser:
    """
    Parser semantico che usa LLM per capire intent
    """
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY non trovata")
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = "gpt-4-turbo-preview"
    
    def parse(self, code: str) -> Dict[str, Any]:
        """
        Converte codice naturale in Intermediate Representation
        
        Args:
            code: Codice in linguaggio naturale italiano
            
        Returns:
            IR in formato dict
        """
        print(f"🔍 Parsing: {code[:50]}...")
        
        # Costruisci prompt
        prompt = self._build_prompt(code)
        
        # Chiama LLM
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self._system_prompt()},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1,
            response_format={"type": "json_object"}
        )
        
        # Estrai IR
        ir_text = response.choices[0].message.content
        ir = json.loads(ir_text)
        
        print(f"✅ Parsed: {len(ir.get('operations', []))} operazioni")
        
        return ir
    
    def _system_prompt(self) -> str:
        """System prompt per LLM"""
        return """Sei un compiler per un linguaggio di programmazione naturale italiano.

Il tuo compito è convertire codice in linguaggio naturale in una rappresentazione intermedia (IR) eseguibile.

REGOLE:
1. Analizza il codice riga per riga
2. Identifica l'intent di ogni operazione
3. Genera IR in formato JSON
4. Usa operazioni standard della stdlib

OPERAZIONI SUPPORTATE:

I/O:
- io.read_csv: Carica file CSV
- io.write_csv: Salva file CSV
- io.print: Stampa output

Data:
- data.show: Mostra dati
- data.filter: Filtra righe
- data.sort: Ordina dati
- data.group: Raggruppa dati

Math:
- math.mean: Calcola media
- math.sum: Calcola somma
- math.count: Conta righe

Visualizzazione:
- viz.plot: Grafico a linee
- viz.bar: Grafico a barre

FORMATO IR:
{
  "version": "1.0",
  "operations": [
    {
      "id": "op_1",
      "type": "io.read_csv",
      "params": {"file_path": "file.csv"},
      "output": "$var_0"
    }
  ],
  "variables": {
    "$var_0": {"type": "DataFrame", "source": "op_1"}
  }
}

Rispondi SOLO con JSON valido, nient'altro."""

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
