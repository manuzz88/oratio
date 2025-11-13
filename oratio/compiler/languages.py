"""
Language Support - Supporto multilingua
"""

from typing import Dict
import re


class Language:
    """Base class per supporto lingua"""
    
    def __init__(self, code: str, name: str):
        self.code = code  # 'it', 'en', etc
        self.name = name  # 'Italiano', 'English', etc
    
    def get_system_prompt(self) -> str:
        """System prompt per LLM in questa lingua"""
        raise NotImplementedError
    
    def get_keywords(self) -> Dict[str, list]:
        """Keywords tipiche della lingua"""
        raise NotImplementedError
    
    def detect(self, code: str) -> float:
        """
        Rileva probabilità che il codice sia in questa lingua
        
        Returns:
            Score 0-1 (1 = molto probabile)
        """
        keywords = self.get_keywords()
        code_lower = code.lower()
        
        score = 0.0
        total_keywords = sum(len(words) for words in keywords.values())
        
        for category, words in keywords.items():
            for word in words:
                if word in code_lower:
                    score += 1.0 / total_keywords
        
        return min(score, 1.0)


class ItalianLanguage(Language):
    """Supporto lingua italiana"""
    
    def __init__(self):
        super().__init__('it', 'Italiano')
    
    def get_system_prompt(self) -> str:
        return """Sei un compiler per ORATIO, un linguaggio di programmazione naturale italiano.

Converti codice in linguaggio naturale italiano in IR (Intermediate Representation) JSON.

OPERAZIONI SUPPORTATE:

I/O:
- io.read_csv: Carica file CSV
- io.write_csv: Salva file CSV  
- io.print: Stampa output

Data:
- data.show: Mostra dati
- data.head: Prime N righe
- data.filter: Filtra righe
- data.sort: Ordina dati

Math:
- math.mean: Media
- math.sum: Somma
- math.count: Conteggio
- math.min: Minimo
- math.max: Massimo

Viz:
- viz.plot: Grafico linee
- viz.bar: Grafico barre
- viz.draw_point: Disegna punto
- viz.draw_circle: Disegna cerchio
- viz.draw_line: Disegna linea
- viz.create_canvas: Crea tela
- viz.save_image: Salva immagine

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
  ]
}

Rispondi SOLO con JSON valido."""
    
    def get_keywords(self) -> Dict[str, list]:
        return {
            'io': ['carica', 'leggi', 'salva', 'stampa', 'mostra'],
            'data': ['filtra', 'ordina', 'raggruppa', 'prime', 'ultime'],
            'math': ['calcola', 'media', 'somma', 'conta', 'minimo', 'massimo'],
            'viz': ['grafico', 'visualizza', 'plot'],
            'common': ['dove', 'per', 'della', 'delle', 'con', 'il', 'la', 'le', 'i']
        }


class EnglishLanguage(Language):
    """English language support"""
    
    def __init__(self):
        super().__init__('en', 'English')
    
    def get_system_prompt(self) -> str:
        return """You are a compiler for ORATIO, a natural language programming language.

Convert natural English code into IR (Intermediate Representation) JSON.

SUPPORTED OPERATIONS:

I/O:
- io.read_csv: Load CSV file
- io.write_csv: Save CSV file
- io.print: Print output

Data:
- data.show: Show data
- data.head: First N rows
- data.filter: Filter rows
- data.sort: Sort data

Math:
- math.mean: Average
- math.sum: Sum
- math.count: Count
- math.min: Minimum
- math.max: Maximum

Viz:
- viz.plot: Line chart
- viz.bar: Bar chart
- viz.draw_point: Draw point
- viz.draw_circle: Draw circle
- viz.draw_line: Draw line
- viz.create_canvas: Create canvas
- viz.save_image: Save image

IR FORMAT:
{
  "version": "1.0",
  "operations": [
    {
      "id": "op_1",
      "type": "io.read_csv",
      "params": {"file_path": "file.csv"},
      "output": "$var_0"
    }
  ]
}

Reply ONLY with valid JSON."""
    
    def get_keywords(self) -> Dict[str, list]:
        return {
            'io': ['load', 'read', 'save', 'print', 'show'],
            'data': ['filter', 'sort', 'group', 'first', 'last'],
            'math': ['calculate', 'average', 'mean', 'sum', 'count', 'min', 'max'],
            'viz': ['chart', 'plot', 'visualize', 'graph'],
            'common': ['where', 'for', 'of', 'the', 'with', 'and', 'or']
        }


class LanguageDetector:
    """Rileva automaticamente la lingua del codice"""
    
    def __init__(self):
        self.languages = {
            'it': ItalianLanguage(),
            'en': EnglishLanguage()
        }
    
    def detect(self, code: str) -> Language:
        """
        Rileva lingua del codice
        
        Returns:
            Language object della lingua rilevata
        """
        scores = {}
        for lang_code, language in self.languages.items():
            scores[lang_code] = language.detect(code)
        
        # Lingua con score più alto
        best_lang = max(scores, key=scores.get)
        
        print(f"🌍 Lingua rilevata: {self.languages[best_lang].name} (score: {scores[best_lang]:.2f})")
        
        return self.languages[best_lang]
    
    def get_language(self, code_or_hint: str) -> Language:
        """
        Ottieni lingua da codice o hint
        
        Args:
            code_or_hint: Codice da analizzare o hint ('it', 'en')
        """
        # Se è un hint diretto
        if code_or_hint in self.languages:
            return self.languages[code_or_hint]
        
        # Altrimenti rileva
        return self.detect(code_or_hint)
