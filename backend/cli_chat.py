import sys
import os
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from backend.rag.retriever import Retriever
from backend.rag.llm import LLMWrapper
from backend.rag.utils import log_info, log_error

console = Console()

class ChipathonChatbot:
    def __init__(self):
        # Load retriever (loads DB)
        self.retriever = Retriever()
        # Initialize LLM
        self.llm = LLMWrapper()

    def ask(self, query):
        # 1. Retrieve context
        context, sources = self.retriever.get_context(query)
        
        if not context:
            return "No relevant information found.", []

        # 2. Get LLM response
        answer = self.llm.get_response(context, query)
        
        # 3. Collect unique sources
        source_filenames = sorted(list(set([src["source"] for src in sources])))
        
        return answer, source_filenames

def main():
    chatbot = ChipathonChatbot()
    
    console.print(Panel("[bold cyan]Ask Chipathon Chatbot[/bold cyan]\nType 'exit' or 'quit' to end the session.", 
                      title="Chipathon Knowledge Hub", expand=False))
    
    while True:
        try:
            query = console.input("[bold yellow]Ask Chipathon > [/bold yellow]")
            
            if query.lower() in ["exit", "quit"]:
                console.print("[bold green]Goodbye! Happy designing![/bold green]")
                break

            if not query.strip():
                continue

            with console.status("Retrieving information..."):
                answer, sources = chatbot.ask(query)

            console.print("\n[bold blue]Answer:[/bold blue]")
            console.print(Markdown(answer))
            
            if sources:
                console.print("\n[bold magenta]Sources:[/bold magenta]")
                for source in sources:
                    console.print(f"- {source}")
            else:
                console.print("\n[italic red]No relevant information found in the documents.[/italic red]")
            
            console.print("-" * 50)
            
        except KeyboardInterrupt:
            console.print("\n[bold green]Goodbye! Happy designing![/bold green]")
            break
        except Exception as e:
            console.print(f"[bold red]An error occurred: {str(e)}[/bold red]")
            log_error(f"Chat execution failed: {str(e)}")

if __name__ == "__main__":
    main()
