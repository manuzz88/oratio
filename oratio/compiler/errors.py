"""
ORATIO Error Classes
"""


class OratioError(Exception):
    """Base exception per ORATIO"""
    pass


class ParseError(OratioError):
    """Errore durante il parsing"""
    def __init__(self, message: str, line: int = None, code: str = None):
        self.message = message
        self.line = line
        self.code = code
        
        error_msg = f"❌ Errore di Parsing: {message}"
        if line:
            error_msg += f"\n   Riga {line}"
        if code:
            error_msg += f"\n   Codice: {code[:50]}..."
        
        super().__init__(error_msg)


class RuntimeError(OratioError):
    """Errore durante l'esecuzione"""
    def __init__(self, message: str, operation: str = None):
        self.message = message
        self.operation = operation
        
        error_msg = f"❌ Errore di Esecuzione: {message}"
        if operation:
            error_msg += f"\n   Operazione: {operation}"
        
        super().__init__(error_msg)


class ValidationError(OratioError):
    """Errore di validazione IR"""
    def __init__(self, message: str, ir: dict = None):
        self.message = message
        self.ir = ir
        
        error_msg = f"❌ IR Non Valido: {message}"
        super().__init__(error_msg)
