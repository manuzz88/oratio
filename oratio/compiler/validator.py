"""
IR Validator - Valida Intermediate Representation
"""

from typing import Dict, Any, List
from .errors import ValidationError


class IRValidator:
    """Valida IR prima dell'esecuzione"""
    
    REQUIRED_FIELDS = ['version', 'operations']
    SUPPORTED_VERSIONS = ['1.0']
    
    def validate(self, ir: Dict[str, Any]) -> bool:
        """
        Valida IR completo
        
        Args:
            ir: Intermediate Representation
            
        Returns:
            True se valido
            
        Raises:
            ValidationError se non valido
        """
        # Check campi richiesti
        self._check_required_fields(ir)
        
        # Check versione
        self._check_version(ir)
        
        # Check operations
        self._check_operations(ir)
        
        # Check variabili
        self._check_variables(ir)
        
        return True
    
    def _check_required_fields(self, ir: Dict[str, Any]):
        """Verifica campi richiesti"""
        for field in self.REQUIRED_FIELDS:
            if field not in ir:
                raise ValidationError(f"Campo richiesto mancante: {field}")
    
    def _check_version(self, ir: Dict[str, Any]):
        """Verifica versione supportata"""
        version = ir.get('version')
        if version not in self.SUPPORTED_VERSIONS:
            raise ValidationError(
                f"Versione non supportata: {version}. "
                f"Supportate: {', '.join(self.SUPPORTED_VERSIONS)}"
            )
    
    def _check_operations(self, ir: Dict[str, Any]):
        """Verifica operazioni"""
        operations = ir.get('operations', [])
        
        if not isinstance(operations, list):
            raise ValidationError("'operations' deve essere una lista")
        
        if len(operations) == 0:
            raise ValidationError("Nessuna operazione da eseguire")
        
        for i, op in enumerate(operations):
            self._check_operation(op, i)
    
    def _check_operation(self, op: Dict[str, Any], index: int):
        """Verifica singola operazione"""
        if not isinstance(op, dict):
            raise ValidationError(f"Operazione {index} non è un dict")
        
        # Check type
        if 'type' not in op:
            raise ValidationError(f"Operazione {index}: manca 'type'")
        
        op_type = op['type']
        if not isinstance(op_type, str) or '.' not in op_type:
            raise ValidationError(
                f"Operazione {index}: type deve essere 'categoria.nome' (es: 'io.read_csv')"
            )
        
        # Check params
        if 'params' in op and not isinstance(op.get('params'), dict):
            raise ValidationError(f"Operazione {index}: params deve essere un dict")
    
    def _check_variables(self, ir: Dict[str, Any]):
        """Verifica riferimenti variabili"""
        variables = ir.get('variables', {})
        operations = ir.get('operations', [])
        
        # Raccogli tutte le variabili definite
        defined_vars = set(variables.keys())
        for op in operations:
            if 'output' in op:
                defined_vars.add(op['output'])
        
        # Verifica che tutte le variabili usate siano definite
        for op in operations:
            params = op.get('params', {})
            for value in params.values():
                if isinstance(value, str) and value.startswith('$'):
                    # È un riferimento a variabile
                    if value not in defined_vars:
                        raise ValidationError(
                            f"Variabile non definita: {value} in operazione {op['type']}"
                        )
