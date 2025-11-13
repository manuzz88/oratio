#!/usr/bin/env python3
"""
Lingua CLI - Command Line Interface
"""

import sys
import os
from pathlib import Path
from typing import Optional
import typer
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.progress import Progress, SpinnerColumn, TextColumn

# Aggiungi parent directory al path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from oratio.compiler import SemanticParser
from oratio.runtime import Runtime

app = typer.Typer(
    name="oratio",
    help="🎤 ORATIO - L'eloquenza del codice",
    add_completion=False
)
console = Console()


@app.command()
def run(
    file: Path = typer.Argument(..., help="File .ora da eseguire"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Output dettagliato"),
    show_ir: bool = typer.Option(False, "--show-ir", help="Mostra IR generato"),
):
    """
    Esegue un file .ora
    
    Esempio:
        oratio run examples/primo.ora
    """
    
    # Check file exists
    if not file.exists():
        console.print(f"[red]❌ File non trovato:[/red] {file}")
        raise typer.Exit(1)
    
    # Header
    if verbose:
        console.print(Panel.fit(
            f"[bold cyan]🎤 ORATIO[/bold cyan]\n"
            f"[dim]Esecuzione: {file.name}[/dim]",
            border_style="cyan"
        ))
    
    try:
        # Leggi codice
        code = file.read_text()
        
        if verbose:
            console.print("\n[bold]📝 Codice:[/bold]")
            syntax = Syntax(code, "text", theme="monokai", line_numbers=True)
            console.print(Panel(syntax, border_style="green"))
        
        # Parse
        if verbose:
            console.print("\n[bold yellow]1️⃣  Parsing...[/bold yellow]")
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
            transient=True
        ) as progress:
            task = progress.add_task("Parsing semantico...", total=None)
            parser = SemanticParser()
            ir = parser.parse(code)
            progress.update(task, completed=True)
        
        if show_ir:
            import json
            console.print("\n[bold]📦 IR Generato:[/bold]")
            console.print(Panel(
                json.dumps(ir, indent=2, ensure_ascii=False),
                border_style="blue"
            ))
        
        # Execute
        if verbose:
            console.print("\n[bold yellow]2️⃣  Esecuzione...[/bold yellow]")
        
        # Cambia directory al file per path relativi
        original_dir = Path.cwd()
        os.chdir(file.parent)
        
        try:
            runtime = Runtime()
            result = runtime.execute(ir)
        finally:
            os.chdir(original_dir)
        
        if verbose:
            console.print("\n[bold green]✅ Completato![/bold green]")
        
    except FileNotFoundError as e:
        console.print(f"[red]❌ File non trovato:[/red] {e}")
        raise typer.Exit(1)
    except Exception as e:
        console.print(f"[red]❌ Errore:[/red] {e}")
        if verbose:
            import traceback
            console.print("\n[dim]Traceback:[/dim]")
            console.print(traceback.format_exc())
        raise typer.Exit(1)


@app.command()
def repl():
    """
    Avvia REPL interattivo
    
    Esempio:
        oratio repl
    """
    console.print(Panel.fit(
        "[bold cyan]🎤 ORATIO REPL[/bold cyan]\n"
        "[dim]Modalità interattiva - Parla e premi Invio[/dim]\n"
        "[dim]Comandi: .exit (esci), .clear (pulisci), .help (aiuto)[/dim]",
        border_style="cyan"
    ))
    
    parser = SemanticParser()
    runtime = Runtime()
    
    while True:
        try:
            # Input
            code = console.input("\n[bold cyan]oratio>[/bold cyan] ")
            
            if not code.strip():
                continue
            
            # Comandi speciali
            if code.strip() == ".exit":
                console.print("[dim]Arrivederci! 👋[/dim]")
                break
            elif code.strip() == ".clear":
                console.clear()
                continue
            elif code.strip() == ".help":
                console.print("""
[bold]Comandi disponibili:[/bold]
  .exit   - Esci dal REPL
  .clear  - Pulisci schermo
  .help   - Mostra questo aiuto
  
[bold]Esempi:[/bold]
  Carica vendite.csv
  Mostra le prime 5 righe
  Calcola la media
""")
                continue
            
            # Parse ed esegui
            ir = parser.parse(code)
            runtime.execute(ir)
            
        except KeyboardInterrupt:
            console.print("\n[dim]Usa .exit per uscire[/dim]")
        except EOFError:
            break
        except Exception as e:
            console.print(f"[red]❌ Errore:[/red] {e}")


@app.command()
def check(
    file: Path = typer.Argument(..., help="File .ora da controllare"),
):
    """
    Controlla sintassi di un file .ora
    
    Esempio:
        oratio check examples/primo.ora
    """
    if not file.exists():
        console.print(f"[red]❌ File non trovato:[/red] {file}")
        raise typer.Exit(1)
    
    try:
        code = file.read_text()
        
        console.print(f"[bold]Controllo:[/bold] {file.name}")
        
        # Parse
        parser = SemanticParser()
        ir = parser.parse(code)
        
        # Validazioni
        ops_count = len(ir.get('operations', []))
        
        console.print(f"[green]✅ Sintassi valida[/green]")
        console.print(f"[dim]Operazioni: {ops_count}[/dim]")
        
    except Exception as e:
        console.print(f"[red]❌ Errore di sintassi:[/red] {e}")
        raise typer.Exit(1)


@app.command()
def version():
    """Mostra versione"""
    from oratio import __version__
    console.print(f"[bold cyan]ORATIO[/bold cyan] versione {__version__}")


@app.command()
def examples():
    """Lista esempi disponibili"""
    examples_dir = Path(__file__).parent.parent.parent / "examples"
    
    if not examples_dir.exists():
        console.print("[yellow]Nessun esempio trovato[/yellow]")
        return
    
    console.print("[bold]📚 Esempi disponibili:[/bold]\n")
    
    for file in sorted(examples_dir.glob("*.ora")):
        console.print(f"  [cyan]•[/cyan] {file.name}")
        # Mostra prima riga come descrizione
        first_line = file.read_text().split('\n')[0]
        if first_line:
            console.print(f"    [dim]{first_line[:60]}...[/dim]")
    
    console.print(f"\n[dim]Esegui con: oratio run examples/nome.ora[/dim]")


def main():
    """Entry point"""
    app()


if __name__ == "__main__":
    main()
