import typer #to develop CLI
import json #to store bookmark
from pathlib import Path #to make readadble and useable in different OS

app = typer.Typer()

BOOKMARKS_FILE = Path("bookmarks.json")

def load_bookmarks():
    if BOOKMARKS_FILE.exists():
        with open(BOOKMARKS_FILE, "r") as f:
            return json.load(f)
    return{}

def save_bookmarks(bookmarks):
    with open(BOOKMARKS_FILE, "w") as f:
        json.dump(bookmarks, f, indent=4)
        
        
@app.command()
def add(name: str, url:str):
    
    """Add a bookmark with a name and a URL."""
    
    bookmarks = load_bookmarks()
    bookmarks[name] = url
    save_bookmarks(bookmarks)
    typer.echo(f"Bookmark '{name} added successfully!")
    
    
@app.command()
def list():
    """List all saved bookmarks."""
    bookmarks = load_bookmarks()
    if not bookmarks:
        typer.echo("No bookmarks found.")
        return
    typer.echo("Saved bookmarks:")
    for name, url in bookmarks.items():
     typer.echo(f"{name}:{url}")
     
     
@app.command()
def delete(name:str):
    """Delete a bookmark by name."""
    bookmarks = load_bookmarks()
    if name in bookmarks:
        del bookmarks[name]
        save_bookmarks(bookmarks)
        typer.echo(f"Bookmark '{name}' deleted successfully!")
    else:
        typer.echo(f" No bookmark found  with the name '{name}.")
        
@app.command()
def help():
    """Show help on how to use the CLI."""
    typer.echo("""
               Bookmarks CLI
               ============= 

               Commands:
               add [NAME] [URL] - Add a bookmark with a name and a URL
               list - List all saved bookmarks
               delete [Name] - Delete a bookmark by name
               help - show this help message
               =============
               """)
    
if __name__ =="__main__":
    app()
     
        
