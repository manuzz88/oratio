"""
Sistema AI Autonomo per ORATIO
L'AI guida tutto: espansione, testing, deployment
"""

import os
import json
from openai import OpenAI
from typing import List, Dict, Any
import time


class AutonomousOratio:
    """
    Sistema completamente autonomo che:
    1. Analizza cosa manca in ORATIO
    2. Genera nuove operazioni
    3. Testa automaticamente
    4. Integra nel sistema
    5. Si auto-migliora continuamente
    """
    
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-4o-mini"
        
    def analyze_gaps(self) -> List[str]:
        """
        Analizza quali operazioni mancano in ORATIO
        """
        print("🔍 Analizzando gap in ORATIO...")
        
        prompt = """
Sei un esperto di linguaggi di programmazione.

ORATIO è un linguaggio naturale che attualmente supporta solo:
- Operazioni grafiche base (punti, cerchi, quadrati)
- Operazioni I/O base (print, input)

Analizza e suggerisci le 10 operazioni PIÙ IMPORTANTI che mancano per renderlo utile.

Pensa a:
- Data analysis (CSV, JSON, Excel)
- File system (crea, copia, elimina file)
- Web (API calls, scraping)
- Math (calcoli, statistiche)
- Automazione (loop, condizioni)

Rispondi in JSON:
{
  "operations": [
    {
      "name": "load_csv",
      "description": "Carica file CSV",
      "priority": "high",
      "use_cases": ["data analysis", "reporting"]
    },
    ...
  ]
}
"""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            response_format={"type": "json_object"}
        )
        
        content = response.choices[0].message.content
        
        # Estrai JSON se wrapped in markdown
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
        
        result = json.loads(content)
        operations = result.get("operations", [])
        
        print(f"✅ Trovate {len(operations)} operazioni mancanti")
        return operations
    
    def generate_operation(self, operation: Dict) -> str:
        """
        Genera codice Python per una nuova operazione
        """
        print(f"\n🔧 Generando: {operation['name']}...")
        
        prompt = f"""
Genera codice Python per implementare questa operazione in ORATIO:

Nome: {operation['name']}
Descrizione: {operation['description']}
Use cases: {', '.join(operation.get('use_cases', []))}

Il codice deve:
1. Essere una funzione Python standalone
2. Avere docstring completo
3. Gestire errori
4. Essere testabile
5. Seguire best practices

Esempio formato:

```python
def load_csv(filepath: str, **kwargs) -> Dict[str, Any]:
    \"\"\"
    Carica file CSV e ritorna dati
    
    Args:
        filepath: Path al file CSV
        **kwargs: Opzioni pandas (delimiter, encoding, etc)
    
    Returns:
        Dict con 'data' (DataFrame) e 'metadata'
    
    Raises:
        FileNotFoundError: Se file non esiste
        ValueError: Se CSV non valido
    \"\"\"
    import pandas as pd
    
    try:
        df = pd.read_csv(filepath, **kwargs)
        return {{
            "data": df,
            "rows": len(df),
            "columns": list(df.columns),
            "metadata": {{"filepath": filepath}}
        }}
    except FileNotFoundError:
        raise FileNotFoundError(f"File {{filepath}} non trovato")
    except Exception as e:
        raise ValueError(f"Errore lettura CSV: {{e}}")
```

Genera SOLO il codice Python, niente altro.
"""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        
        code = response.choices[0].message.content
        
        # Estrai solo il codice Python
        if "```python" in code:
            code = code.split("```python")[1].split("```")[0].strip()
        
        print(f"✅ Codice generato ({len(code)} caratteri)")
        return code
    
    def generate_tests(self, operation_name: str, code: str) -> str:
        """
        Genera test automatici per l'operazione
        """
        print(f"🧪 Generando test per {operation_name}...")
        
        prompt = f"""
Genera test pytest per questa funzione:

```python
{code}
```

I test devono:
1. Testare caso normale
2. Testare edge cases
3. Testare errori
4. Usare pytest
5. Essere completi

Genera SOLO il codice dei test.
"""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        
        tests = response.choices[0].message.content
        
        if "```python" in tests:
            tests = tests.split("```python")[1].split("```")[0].strip()
        
        print(f"✅ Test generati")
        return tests
    
    def validate_operation(self, code: str, tests: str) -> bool:
        """
        Valida che l'operazione sia corretta
        """
        print("✓ Validando operazione...")
        
        # Verifica sintassi Python
        try:
            compile(code, '<string>', 'exec')
            compile(tests, '<string>', 'exec')
        except SyntaxError as e:
            print(f"❌ Errore sintassi: {e}")
            return False
        
        # Verifica che abbia docstring
        if '"""' not in code and "'''" not in code:
            print("❌ Manca docstring")
            return False
        
        # Verifica che gestisca errori
        if "try:" not in code and "except" not in code:
            print("⚠️  Warning: Nessuna gestione errori")
        
        print("✅ Validazione OK")
        return True
    
    def integrate_operation(self, operation_name: str, code: str, category: str = "data") -> str:
        """
        Integra l'operazione nel sistema ORATIO
        """
        print(f"📦 Integrando {operation_name} in ORATIO...")
        
        # Determina file di destinazione
        filepath = f"/home/manuel/CascadeProjects/oratio/oratio/operations/{category}.py"
        
        # Aggiungi al file
        with open(filepath, 'a') as f:
            f.write(f"\n\n# Auto-generated by AutonomousOratio\n")
            f.write(f"# Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(code)
            f.write("\n")
        
        print(f"✅ Operazione aggiunta a {filepath}")
        return filepath
    
    def auto_expand(self, num_operations: int = 5):
        """
        Espansione automatica completa
        """
        print("🚀 AVVIO ESPANSIONE AUTONOMA ORATIO\n")
        print("=" * 60)
        
        # 1. Analizza gap
        operations = self.analyze_gaps()
        
        # 2. Seleziona top N per priorità
        top_ops = sorted(operations, key=lambda x: x.get('priority', 'low'), reverse=True)[:num_operations]
        
        print(f"\n📋 Operazioni da implementare:")
        for i, op in enumerate(top_ops, 1):
            print(f"  {i}. {op['name']} - {op['description']}")
        
        # 3. Genera e integra ogni operazione
        results = []
        
        for op in top_ops:
            print(f"\n{'=' * 60}")
            print(f"🔨 Implementando: {op['name']}")
            print(f"{'=' * 60}")
            
            try:
                # Genera codice
                code = self.generate_operation(op)
                
                # Genera test
                tests = self.generate_tests(op['name'], code)
                
                # Valida
                if not self.validate_operation(code, tests):
                    print(f"❌ Validazione fallita per {op['name']}")
                    results.append({"name": op['name'], "status": "failed", "reason": "validation"})
                    continue
                
                # Integra
                filepath = self.integrate_operation(op['name'], code)
                
                results.append({
                    "name": op['name'],
                    "status": "success",
                    "filepath": filepath,
                    "code_length": len(code),
                    "test_length": len(tests)
                })
                
                print(f"✅ {op['name']} implementato con successo!")
                
            except Exception as e:
                print(f"❌ Errore: {e}")
                results.append({"name": op['name'], "status": "error", "error": str(e)})
        
        # 4. Riepilogo
        print(f"\n{'=' * 60}")
        print("🎉 ESPANSIONE COMPLETATA")
        print(f"{'=' * 60}\n")
        
        success = len([r for r in results if r['status'] == 'success'])
        failed = len([r for r in results if r['status'] != 'success'])
        
        print(f"✅ Successi: {success}/{len(results)}")
        print(f"❌ Falliti: {failed}/{len(results)}")
        
        if success > 0:
            print(f"\n📊 Operazioni aggiunte:")
            for r in results:
                if r['status'] == 'success':
                    print(f"  • {r['name']} ({r['code_length']} caratteri)")
        
        return results


def main():
    """
    Esegui espansione autonoma
    """
    system = AutonomousOratio()
    results = system.auto_expand(num_operations=10)
    
    print(f"\n🚀 ORATIO è stato espanso con {len([r for r in results if r['status'] == 'success'])} nuove operazioni!")


if __name__ == "__main__":
    main()
