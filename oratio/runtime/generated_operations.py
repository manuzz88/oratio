"""\nOperazioni generate automaticamente da OpenAI\n"""\n\nimport pandas as pd\nfrom typing import Any\n\n# data.head: Mostra le prime N righe di un DataFrame

def _op_data_head(self, source=None, n: int = 5, **kwargs):
    """Mostra le prime N righe di un DataFrame"""
    if source is None:
        source = list(self.memory.values())[-1] if self.memory else None
    
    if isinstance(source, pd.DataFrame):
        result = source.head(n)
    elif isinstance(source, (list, tuple)):
        result = source[:n]
    else:
        result = source
    
    print(f"    ✓ Prime {n} righe mostrate")
    return result

\n\n# data.tail: Mostra le ultime N righe di un DataFrame

def _op_data_tail(self, source=None, n: int = 5, **kwargs):
    """Mostra le ultime N righe di un DataFrame"""
    if source is None:
        source = list(self.memory.values())[-1] if self.memory else None
    
    if isinstance(source, pd.DataFrame):
        result = source.tail(n)
    else:
        result = f"L'operazione data.tail non è supportata per il tipo {type(source).__name__}"
    
    print(f"    ✓ Ultimi {n} elementi mostrati")
    return result

\n\n# data.sample: Mostra N righe casuali di un DataFrame

import pandas as pd

def _op_data_sample(self, source=None, n: int = 1, **kwargs):
    """Mostra N righe casuali di un DataFrame"""
    if source is None:
        source = list(self.memory.values())[-1] if self.memory else None
    
    if isinstance(source, pd.DataFrame):
        result = source.sample(n)
    else:
        raise TypeError("L'operazione è supportata solo per DataFrame")
    
    print(f"    ✓ Mostrate {n} righe casuali")
    return result

\n\n# data.describe: Mostra statistiche descrittive di un DataFrame

def _op_data_describe(self, source=None, **kwargs):
    """Mostra statistiche descrittive di un DataFrame"""
    if source is None:
        source = list(self.memory.values())[-1] if self.memory else None

    if isinstance(source, pd.DataFrame):
        result = source.describe()
    elif isinstance(source, (list, tuple)):
        result = pd.Series(source).describe()
    else:
        result = f"Tipo di dato non supportato per la descrizione: {type(source)}"

    print("    ✓ Statistiche descrittive mostrate")
    return result

\n\n# data.info: Mostra informazioni su un DataFrame

def _op_data_info(self, source=None, **kwargs):
    """Mostra informazioni su un DataFrame"""
    if source is None:
        source = list(self.memory.values())[-1] if self.memory else None
    
    if isinstance(source, pd.DataFrame):
        info_str = []
        info_str.append(f"Dimensioni: {source.shape[0]} righe, {source.shape[1]} colonne")
        info_str.append(f"Colonne: {', '.join(source.columns)}")
        info_str.append(f"Tipi di dati:\n{source.dtypes.to_string()}")
        result = '\n'.join(info_str)
    else:
        result = f"Tipo di dato non supportato: {type(source).__name__}"
    
    print(f"    ✓ Informazioni: \n{result}")
    return result

\n\n# data.columns: Mostra i nomi delle colonne

def _op_data_columns(self, source=None, **kwargs):
    """Mostra i nomi delle colonne"""
    if source is None:
        source = list(self.memory.values())[-1] if self.memory else None

    if isinstance(source, pd.DataFrame):
        result = list(source.columns)
    else:
        result = "L'operazione non è supportata per il tipo di dato fornito."

    print(f"    ✓ Nomi delle colonne: {result}")
    return result

\n\n# data.shape: Mostra dimensioni (righe, colonne)

def _op_data_shape(self, source=None, **kwargs):
    """Mostra dimensioni (righe, colonne)"""
    if source is None:
        source = list(self.memory.values())[-1] if self.memory else None

    if isinstance(source, pd.DataFrame):
        result = source.shape
    elif isinstance(source, (list, tuple)) and all(isinstance(i, (list, tuple)) for i in source):
        row_count = len(source)
        col_count = len(source[0]) if row_count > 0 else 0
        result = (row_count, col_count)
    else:
        result = "Tipo non supportato per la dimensione"

    print(f"    ✓ Dimensioni: {result}")
    return result

\n\n# data.unique: Mostra valori unici di una colonna

def _op_data_unique(self, source=None, **kwargs):
    """Mostra valori unici di una colonna"""
    if source is None:
        source = list(self.memory.values())[-1] if self.memory else None
    
    if isinstance(source, pd.DataFrame):
        result = source.apply(lambda x: x.unique())
    elif isinstance(source, (list, tuple, set)):
        result = set(source)
    else:
        result = {source}
    
    print(f"    ✓ Valori unici: {len(result)} trovati")
    return result

\n\n# data.value_counts: Conta occorrenze di ogni valore

def _op_data_value_counts(self, source=None, **kwargs):
    """Conta occorrenze di ogni valore"""
    if source is None:
        source = list(self.memory.values())[-1] if self.memory else None

    if isinstance(source, pd.DataFrame):
        result = source.apply(pd.Series.value_counts).fillna(0).astype(int)
    elif isinstance(source, (list, tuple)):
        result = {val: source.count(val) for val in set(source)}
    else:
        result = {source: 1}
    
    print("    ✓ Conteggio occorrenze completato")
    return result

\n\n# data.drop: Elimina colonne o righe

def _op_data_drop(self, source=None, axis=0, labels=None, **kwargs):
    """Elimina colonne o righe"""
    if source is None:
        source = list(self.memory.values())[-1] if self.memory else None

    if isinstance(source, pd.DataFrame):
        result = source.drop(labels=labels, axis=axis)
    else:
        print("    ✗ Operazione non supportata su questo tipo di dato")
        return source

    print(f"    ✓ Elementi eliminati")
    return result

\n\n# data.rename: Rinomina colonne

def _op_data_rename(self, source=None, **kwargs):
    """Rinomina colonne"""
    if source is None:
        source = list(self.memory.values())[-1] if self.memory else None
    
    if isinstance(source, pd.DataFrame):
        source.rename(columns=kwargs, inplace=True)
        result = source
    else:
        print("    ✗ L'operazione è supportata solo su DataFrame")
        return source
    
    print(f"    ✓ Colonne rinominate: {', '.join(kwargs.values())}")
    return result

\n\n# data.fillna: Riempie valori mancanti

def _op_data_fillna(self, source=None, value=0, **kwargs):
    """Riempie valori mancanti"""
    if source is None:
        source = list(self.memory.values())[-1] if self.memory else None
    
    if isinstance(source, pd.DataFrame):
        result = source.fillna(value)
    elif isinstance(source, (list, tuple)):
        result = [x if x is not None else value for x in source]
    else:
        result = source if source is not None else value
    
    print(f"    ✓ Valori mancanti riempiti con: {value}")
    return result

\n\n# data.dropna: Elimina righe con valori mancanti

def _op_data_dropna(self, source=None, **kwargs):
    """Elimina righe con valori mancanti"""
    if source is None:
        source = list(self.memory.values())[-1] if self.memory else None

    if isinstance(source, pd.DataFrame):
        result = source.dropna()
    else:
        print("    ✗ Operazione supportata solo su DataFrame")
        return source

    print("    ✓ Righe con valori mancanti eliminate")
    return result

\n\n# math.min: Trova valore minimo

def _op_math_min(self, source=None, **kwargs):
    """Trova valore minimo"""
    if source is None:
        source = list(self.memory.values())[-1] if self.memory else None

    if isinstance(source, pd.DataFrame):
        result = source.min().min()
    elif isinstance(source, (list, tuple)):
        result = min(source)
    else:
        result = float(source)

    print(f"    ✓ Valore Minimo: {result}")
    return result

\n\n# math.max: Trova valore massimo

def _op_math_max(self, source=None, **kwargs):
    """Trova valore massimo"""
    if source is None:
        source = list(self.memory.values())[-1] if self.memory else None
    
    if isinstance(source, pd.DataFrame):
        result = source.max().max()
    elif isinstance(source, (list, tuple)):
        result = max(source)
    else:
        result = source
    
    print(f"    ✓ Valore massimo: {result}")
    return result

\n\n# math.median: Calcola mediana

def _op_math_median(self, source=None, **kwargs) -> float:
    """Calcola mediana"""
    if source is None:
        source = list(self.memory.values())[-1] if self.memory else None

    if isinstance(source, pd.DataFrame):
        result = source.median().median()
    elif isinstance(source, (list, tuple)):
        sorted_source = sorted(source)
        n = len(sorted_source)
        midpoint = n // 2
        if n % 2 == 0:
            result = (sorted_source[midpoint - 1] + sorted_source[midpoint]) / 2.0
        else:
            result = sorted_source[midpoint]
    else:
        result = float(source)

    print(f"    ✓ Mediana: {result:.2f}")
    return result

\n\n# math.std: Calcola deviazione standard

import pandas as pd
import numpy as np

def _op_math_std(self, source=None, **kwargs) -> float:
    """Calcola deviazione standard"""
    if source is None:
        source = list(self.memory.values())[-1] if self.memory else None

    if isinstance(source, pd.DataFrame):
        result = source.std().mean()
    elif isinstance(source, (list, tuple)):
        result = np.std(source, ddof=1)
    else:
        result = 0.0  # La deviazione standard di un singolo valore è 0

    print(f"    ✓ Deviazione standard: {result:.2f}")
    return result

\n\n# math.var: Calcola varianza

def _op_math_var(self, source=None, **kwargs) -> float:
    """Calcola varianza"""
    if source is None:
        source = list(self.memory.values())[-1] if self.memory else None
    
    if isinstance(source, pd.DataFrame):
        result = source.var().mean()
    elif isinstance(source, (list, tuple)):
        mean = sum(source) / len(source)
        result = sum((x - mean) ** 2 for x in source) / len(source)
    else:
        result = 0.0  # Varianza di un singolo numero è sempre 0
    
    print(f"    ✓ Varianza: {result:.2f}")
    return result

\n\n# string.upper: Converti testo in maiuscolo

def _op_string_upper(self, source=None, **kwargs) -> str:
    """Converti testo in maiuscolo"""
    if source is None:
        source = list(self.memory.values())[-1] if self.memory else None
    
    if isinstance(source, pd.DataFrame):
        result = source.applymap(lambda x: x.upper() if isinstance(x, str) else x)
    elif isinstance(source, str):
        result = source.upper()
    else:
        raise TypeError("Il tipo di source non è supportato per l'operazione string.upper")
    
    print(f"    ✓ Testo convertito in maiuscolo")
    return result

\n\n# string.lower: Converti testo in minuscolo

def _op_string_lower(self, source=None, **kwargs):
    """Converti testo in minuscolo"""
    if source is None:
        source = list(self.memory.values())[-1] if self.memory else None

    if isinstance(source, pd.DataFrame):
        result = source.applymap(lambda x: x.lower() if isinstance(x, str) else x)
    elif isinstance(source, str):
        result = source.lower()
    else:
        raise TypeError("Il tipo di source non è supportato per l'operazione string.lower")

    print(f"    ✓ Convertito in minuscolo")
    return result

