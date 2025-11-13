"""
Runtime Executor - Esegue IR
"""

import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, Any
from pathlib import Path
import sys
import os

# Import errori
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from compiler.errors import RuntimeError as OratioRuntimeError


class Runtime:
    """
    Runtime che esegue Intermediate Representation
    """
    
    def __init__(self):
        self.memory = {}  # Variabili in memoria
        self.operations = self._register_operations()
    
    def execute(self, ir: Dict[str, Any]) -> Any:
        """
        Esegue IR operation per operation
        
        Args:
            ir: Intermediate Representation
            
        Returns:
            Risultato ultima operazione
        """
        print(f"\n⚡ Esecuzione {len(ir['operations'])} operazioni...\n")
        
        result = None
        
        for op in ir['operations']:
            print(f"  ▶ {op['type']}...")
            result = self._execute_operation(op)
            
            # Salva output in memoria
            if 'output' in op and op['output']:
                self.memory[op['output']] = result
        
        print(f"\n✅ Esecuzione completata\n")
        return result
    
    def _execute_operation(self, op: Dict[str, Any]) -> Any:
        """Esegue singola operazione"""
        op_type = op['type']
        params = op.get('params', {})
        
        try:
            # Risolvi variabili nei parametri
            resolved_params = self._resolve_params(params)
            
            # Ottieni handler
            handler = self.operations.get(op_type)
            if not handler:
                raise OratioRuntimeError(
                    f"Operazione non supportata: {op_type}",
                    operation=op_type
                )
            
            # Esegui
            return handler(**resolved_params)
            
        except OratioRuntimeError:
            raise
        except Exception as e:
            raise OratioRuntimeError(
                f"Errore durante esecuzione: {e}",
                operation=op_type
            )
    
    def _resolve_params(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Risolve variabili nei parametri"""
        resolved = {}
        for key, value in params.items():
            if isinstance(value, str) and value.startswith('$'):
                # È una variabile
                resolved[key] = self.memory.get(value)
            else:
                resolved[key] = value
        
        # Gestisci alias comuni (data -> source, etc)
        if 'data' in resolved and 'source' not in resolved:
            resolved['source'] = resolved.pop('data')
        
        return resolved
    
    def _register_operations(self) -> Dict:
        """Registra operazioni supportate"""
        return {
            # I/O
            'io.read_csv': self._op_read_csv,
            'io.write_csv': self._op_write_csv,
            'io.print': self._op_print,
            # Data - Base
            'data.show': self._op_show,
            'data.filter': self._op_filter,
            'data.sort': self._op_sort,
            'data.group': self._op_group,
            # Data - Generated
            'data.head': self._op_data_head,
            'data.tail': self._op_data_tail,
            'data.sample': self._op_data_sample,
            'data.describe': self._op_data_describe,
            'data.info': self._op_data_info,
            'data.columns': self._op_data_columns,
            'data.shape': self._op_data_shape,
            'data.unique': self._op_data_unique,
            'data.value_counts': self._op_data_value_counts,
            'data.drop': self._op_data_drop,
            'data.rename': self._op_data_rename,
            'data.fillna': self._op_data_fillna,
            'data.dropna': self._op_data_dropna,
            # Math - Base
            'math.mean': self._op_mean,
            'math.sum': self._op_sum,
            'math.count': self._op_count,
            # Math - Generated
            'math.min': self._op_math_min,
            'math.max': self._op_math_max,
            'math.median': self._op_math_median,
            'math.std': self._op_math_std,
            'math.var': self._op_math_var,
            # String
            'string.upper': self._op_string_upper,
            'string.lower': self._op_string_lower,
            # Visualization
            'viz.plot': self._op_plot,
            'viz.bar': self._op_bar_chart,
        }
    
    # === OPERAZIONI ===
    
    def _op_read_csv(self, file_path: str, **kwargs) -> pd.DataFrame:
        """Carica CSV"""
        df = pd.read_csv(file_path)
        print(f"    ✓ Caricato: {len(df)} righe, {len(df.columns)} colonne")
        return df
    
    def _op_print(self, value: Any = None, template: str = None, args: list = None, 
                  message: str = None, variables: dict = None, **kwargs):
        """Stampa output"""
        if message:
            # Messaggio con variabili da sostituire
            output = message
            
            # Sostituisci $var_X direttamente nel messaggio
            import re
            for var_match in re.finditer(r'\$var_\d+', output):
                var_ref = var_match.group()
                var_value = self.memory.get(var_ref, var_ref)
                output = output.replace(var_ref, str(var_value))
            
            # Sostituisci {nome} con valore da variables dict
            if variables:
                for var_name, var_ref in variables.items():
                    if isinstance(var_ref, str) and var_ref.startswith('$'):
                        var_value = self.memory.get(var_ref, var_ref)
                    else:
                        var_value = var_ref
                    output = output.replace(f"{{{var_name}}}", str(var_value))
        elif template and args:
            # Template con argomenti
            resolved_args = []
            for arg in args:
                if isinstance(arg, str) and arg.startswith('$'):
                    resolved_args.append(self.memory.get(arg, arg))
                else:
                    resolved_args.append(arg)
            output = template.format(*resolved_args)
        elif value is not None:
            output = value
        else:
            # Prendi ultima variabile
            last_var = list(self.memory.values())[-1] if self.memory else None
            output = last_var
        
        print(f"    📄 {output}")
        return output
    
    def _op_show(self, source=None, n: int = 5, **kwargs):
        """Mostra dati"""
        if source is None:
            # Mostra ultima variabile
            source = list(self.memory.values())[-1] if self.memory else None
        
        if isinstance(source, pd.DataFrame):
            print(f"\n{source.head(n)}\n")
        else:
            print(f"\n{source}\n")
        
        return source
    
    def _op_filter(self, source=None, condition: Any = None, column: str = None, 
                   operator: str = None, value: Any = None, **kwargs) -> pd.DataFrame:
        """Filtra dati"""
        if source is None:
            source = list(self.memory.values())[-1] if self.memory else None
        
        # Gestisci condition come stringa (es: "importo > 100")
        if condition and isinstance(condition, str):
            import re
            # Parse "colonna operatore valore"
            match = re.match(r'(\w+)\s*([><=!]+)\s*(.+)', condition)
            if match:
                column = match.group(1)
                operator = match.group(2)
                value = match.group(3).strip()
                # Converti valore in numero se possibile
                try:
                    value = float(value)
                except:
                    pass
        # Gestisci condition come dict
        elif condition and isinstance(condition, dict):
            column = condition.get('column', column)
            operator = condition.get('operator', operator)
            value = condition.get('value', value)
        
        if not all([column, operator, value is not None]):
            raise ValueError(f"Filtro richiede column, operator e value")
        
        if operator == '>':
            result = source[source[column] > value]
        elif operator == '<':
            result = source[source[column] < value]
        elif operator == '==':
            result = source[source[column] == value]
        elif operator == '>=':
            result = source[source[column] >= value]
        elif operator == '<=':
            result = source[source[column] <= value]
        else:
            raise ValueError(f"Operatore non supportato: {operator}")
        
        print(f"    ✓ Filtrate: {len(result)} righe")
        return result
    
    def _op_mean(self, source=None, column: str = None, **kwargs) -> float:
        """Calcola media"""
        # Se source non specificato, usa ultima variabile
        if source is None:
            source = list(self.memory.values())[-1] if self.memory else None
        
        if isinstance(source, pd.DataFrame):
            if column:
                result = source[column].mean()
            else:
                result = source.mean().mean()
        elif isinstance(source, (list, tuple)):
            result = sum(source) / len(source)
        else:
            # È già un numero singolo
            result = float(source)
        
        print(f"    ✓ Media: {result:.2f}")
        return result
    
    def _op_sum(self, source=None, column: str = None, **kwargs) -> float:
        """Calcola somma"""
        if source is None:
            source = list(self.memory.values())[-1] if self.memory else None
        
        if isinstance(source, pd.DataFrame):
            if column:
                result = source[column].sum()
            else:
                result = source.sum().sum()
        else:
            result = sum(source)
        
        print(f"    ✓ Somma: {result:.2f}")
        return result
    
    def _op_count(self, source=None, **kwargs) -> int:
        """Conta righe"""
        if source is None:
            source = list(self.memory.values())[-1] if self.memory else None
        
        if isinstance(source, pd.DataFrame):
            result = len(source)
        elif isinstance(source, (list, tuple, str)):
            result = len(source)
        else:
            # È un numero singolo
            result = 1
        
        print(f"    ✓ Conteggio: {result}")
        return result
    
    def _op_write_csv(self, source=None, file_path: str = "output.csv", **kwargs):
        """Salva CSV"""
        if source is None:
            source = list(self.memory.values())[-1] if self.memory else None
        
        if isinstance(source, pd.DataFrame):
            source.to_csv(file_path, index=False)
            print(f"    ✓ Salvato: {file_path}")
        else:
            raise ValueError("Source deve essere un DataFrame")
        
        return file_path
    
    def _op_sort(self, source=None, column: str = None, ascending: bool = True, **kwargs):
        """Ordina dati"""
        if source is None:
            source = list(self.memory.values())[-1] if self.memory else None
        
        if isinstance(source, pd.DataFrame):
            if column:
                result = source.sort_values(by=column, ascending=ascending)
            else:
                result = source.sort_values(by=source.columns[0], ascending=ascending)
        else:
            result = sorted(source, reverse=not ascending)
        
        print(f"    ✓ Ordinato: {len(result) if hasattr(result, '__len__') else 'OK'}")
        return result
    
    def _op_group(self, source=None, by: str = None, **kwargs):
        """Raggruppa dati"""
        if source is None:
            source = list(self.memory.values())[-1] if self.memory else None
        
        if isinstance(source, pd.DataFrame) and by:
            result = source.groupby(by)
            print(f"    ✓ Raggruppato per: {by}")
            return result
        else:
            raise ValueError("Serve DataFrame e colonna 'by'")
    
    def _op_plot(self, source=None, x: str = None, y: str = None, 
                 title: str = "Grafico", save_as: str = None, **kwargs):
        """Crea grafico a linee"""
        if source is None:
            source = list(self.memory.values())[-1] if self.memory else None
        
        plt.figure(figsize=(10, 6))
        
        if isinstance(source, pd.DataFrame):
            if x and y:
                plt.plot(source[x], source[y])
            elif y:
                plt.plot(source[y])
            else:
                source.plot()
        else:
            plt.plot(source)
        
        plt.title(title)
        plt.grid(True, alpha=0.3)
        
        if save_as:
            plt.savefig(save_as, dpi=150, bbox_inches='tight')
            print(f"    ✓ Grafico salvato: {save_as}")
        else:
            plt.show()
            print(f"    ✓ Grafico mostrato")
        
        plt.close()
        return save_as if save_as else "displayed"
    
    def _op_bar_chart(self, source=None, x: str = None, y: str = None,
                      title: str = "Grafico a Barre", save_as: str = None, **kwargs):
        """Crea grafico a barre"""
        if source is None:
            source = list(self.memory.values())[-1] if self.memory else None
        
        plt.figure(figsize=(10, 6))
        
        if isinstance(source, pd.DataFrame):
            if x and y:
                plt.bar(source[x], source[y])
            elif y:
                plt.bar(range(len(source)), source[y])
            else:
                source.plot(kind='bar')
        else:
            plt.bar(range(len(source)), source)
        
        plt.title(title)
        plt.grid(True, alpha=0.3, axis='y')
        
        if save_as:
            plt.savefig(save_as, dpi=150, bbox_inches='tight')
            print(f"    ✓ Grafico salvato: {save_as}")
        else:
            plt.show()
            print(f"    ✓ Grafico mostrato")
        
        plt.close()
        return save_as if save_as else "displayed"
    
    # === OPERAZIONI GENERATE AUTOMATICAMENTE ===
    
    def _op_data_head(self, source=None, n: int = 5, **kwargs):
        """Mostra le prime N righe"""
        if source is None:
            source = list(self.memory.values())[-1] if self.memory else None
        
        if isinstance(source, pd.DataFrame):
            result = source.head(n)
            print(f"    ✓ Prime {n} righe")
        elif isinstance(source, (list, tuple)):
            result = source[:n]
            print(f"    ✓ Primi {n} elementi")
        else:
            result = source
        
        return result
    
    def _op_data_tail(self, source=None, n: int = 5, **kwargs):
        """Mostra le ultime N righe"""
        if source is None:
            source = list(self.memory.values())[-1] if self.memory else None
        
        if isinstance(source, pd.DataFrame):
            result = source.tail(n)
            print(f"    ✓ Ultime {n} righe")
        else:
            result = source
        
        return result
    
    def _op_math_min(self, source=None, column: str = None, **kwargs):
        """Valore minimo"""
        if source is None:
            source = list(self.memory.values())[-1] if self.memory else None
        
        if isinstance(source, pd.DataFrame):
            if column:
                result = source[column].min()
            else:
                result = source.min().min()
        elif isinstance(source, (list, tuple)):
            result = min(source)
        else:
            result = source
        
        print(f"    ✓ Minimo: {result}")
        return result
    
    def _op_math_max(self, source=None, column: str = None, **kwargs):
        """Valore massimo"""
        if source is None:
            source = list(self.memory.values())[-1] if self.memory else None
        
        if isinstance(source, pd.DataFrame):
            if column:
                result = source[column].max()
            else:
                result = source.max().max()
        elif isinstance(source, (list, tuple)):
            result = max(source)
        else:
            result = source
        
        print(f"    ✓ Massimo: {result}")
        return result
    
    def _op_math_median(self, source=None, column: str = None, **kwargs):
        """Mediana"""
        if source is None:
            source = list(self.memory.values())[-1] if self.memory else None
        
        if isinstance(source, pd.DataFrame):
            if column:
                result = source[column].median()
            else:
                result = source.median().median()
        elif isinstance(source, (list, tuple)):
            sorted_data = sorted(source)
            n = len(sorted_data)
            result = sorted_data[n//2] if n % 2 else (sorted_data[n//2-1] + sorted_data[n//2]) / 2
        else:
            result = float(source)
        
        print(f"    ✓ Mediana: {result:.2f}")
        return result
    
    def _op_data_shape(self, source=None, **kwargs):
        """Dimensioni"""
        if source is None:
            source = list(self.memory.values())[-1] if self.memory else None
        
        if isinstance(source, pd.DataFrame):
            result = source.shape
            print(f"    ✓ Dimensioni: {result[0]} righe × {result[1]} colonne")
        elif isinstance(source, (list, tuple)):
            result = (len(source),)
            print(f"    ✓ Lunghezza: {result[0]}")
        else:
            result = (1,)
        
        return result
    
    def _op_data_columns(self, source=None, **kwargs):
        """Nomi colonne"""
        if source is None:
            source = list(self.memory.values())[-1] if self.memory else None
        
        if isinstance(source, pd.DataFrame):
            result = list(source.columns)
            print(f"    ✓ Colonne: {', '.join(result)}")
        else:
            result = []
        
        return result
    
    # Placeholder per le altre operazioni generate
    def _op_data_sample(self, source=None, n: int = 5, **kwargs):
        return self._op_data_head(source, n, **kwargs)
    
    def _op_data_describe(self, source=None, **kwargs):
        if source is None:
            source = list(self.memory.values())[-1] if self.memory else None
        if isinstance(source, pd.DataFrame):
            print(source.describe())
        return source
    
    def _op_data_info(self, source=None, **kwargs):
        return self._op_data_shape(source, **kwargs)
    
    def _op_data_unique(self, source=None, column: str = None, **kwargs):
        return source
    
    def _op_data_value_counts(self, source=None, column: str = None, **kwargs):
        return source
    
    def _op_data_drop(self, source=None, columns: list = None, **kwargs):
        return source
    
    def _op_data_rename(self, source=None, columns: dict = None, **kwargs):
        return source
    
    def _op_data_fillna(self, source=None, value=0, **kwargs):
        return source
    
    def _op_data_dropna(self, source=None, **kwargs):
        return source
    
    def _op_math_std(self, source=None, column: str = None, **kwargs):
        return 0.0
    
    def _op_math_var(self, source=None, column: str = None, **kwargs):
        return 0.0
    
    def _op_string_upper(self, source=None, column: str = None, **kwargs):
        return source
    
    def _op_string_lower(self, source=None, column: str = None, **kwargs):
        return source


if __name__ == "__main__":
    # Test
    runtime = Runtime()
    
    # IR di test
    ir = {
        "version": "1.0",
        "operations": [
            {
                "id": "op_1",
                "type": "io.read_csv",
                "params": {"file_path": "test.csv"},
                "output": "$var_0"
            },
            {
                "id": "op_2",
                "type": "data.show",
                "params": {"source": "$var_0", "n": 3}
            }
        ]
    }
    
    runtime.execute(ir)
