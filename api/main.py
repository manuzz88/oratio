"""
ORATIO Playground API
FastAPI backend per eseguire codice ORATIO dal browser
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys
import os
import io
import base64
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from oratio.compiler.parser import SemanticParser
from oratio.runtime.executor import Runtime
from oratio.compiler.errors import ParseError, ValidationError, OratioError

app = FastAPI(
    title="ORATIO Playground API",
    description="Execute ORATIO natural language code",
    version="0.2.0"
)

# CORS per permettere richieste dal sito
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In produzione: solo il tuo dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CodeRequest(BaseModel):
    code: str
    language: str = "it"  # 'it' o 'en'


class CodeResponse(BaseModel):
    success: bool
    output: str = ""
    error: str = ""
    image: str = ""  # Base64 se c'è un'immagine
    execution_time: float = 0.0


@app.get("/")
def root():
    """Health check"""
    return {
        "status": "ok",
        "service": "ORATIO Playground API",
        "version": "0.2.0"
    }


@app.post("/execute", response_model=CodeResponse)
async def execute_code(request: CodeRequest):
    """
    Esegue codice ORATIO e ritorna il risultato
    """
    import time
    start_time = time.time()
    
    # Cattura output
    output_buffer = io.StringIO()
    old_stdout = sys.stdout
    
    try:
        # Redirect stdout
        sys.stdout = output_buffer
        
        # Parse
        parser = SemanticParser(language=request.language)
        ir = parser.parse(request.code)
        
        # Execute
        runtime = Runtime()
        result = runtime.execute(ir)
        
        # Restore stdout
        sys.stdout = old_stdout
        output = output_buffer.getvalue()
        
        # Check se c'è un'immagine generata
        image_base64 = ""
        if isinstance(result, str) and result.endswith('.png'):
            # C'è un'immagine
            if os.path.exists(result):
                with open(result, 'rb') as f:
                    image_bytes = f.read()
                    image_base64 = base64.b64encode(image_bytes).decode('utf-8')
                # Rimuovi file temporaneo
                os.remove(result)
        
        execution_time = time.time() - start_time
        
        return CodeResponse(
            success=True,
            output=output,
            image=image_base64,
            execution_time=execution_time
        )
        
    except (ParseError, ValidationError, OratioError) as e:
        sys.stdout = old_stdout
        return CodeResponse(
            success=False,
            error=str(e),
            execution_time=time.time() - start_time
        )
    
    except Exception as e:
        sys.stdout = old_stdout
        return CodeResponse(
            success=False,
            error=f"Errore inaspettato: {str(e)}",
            execution_time=time.time() - start_time
        )


@app.get("/examples")
def get_examples():
    """Ritorna esempi predefiniti"""
    return {
        "examples": [
            {
                "title": "Hello World",
                "code": 'Stampa "Ciao Mondo!"',
                "language": "it"
            },
            {
                "title": "Puntino Rosso",
                "code": "Crea un puntino rosso.\nSalva come output.png.",
                "language": "it"
            },
            {
                "title": "Cerchio Blu",
                "code": "Crea un cerchio blu.\nSalva come output.png.",
                "language": "it"
            },
            {
                "title": "English Example",
                "code": 'Print "Hello World!"',
                "language": "en"
            }
        ]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
