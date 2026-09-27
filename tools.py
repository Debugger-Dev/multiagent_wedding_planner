from langchain.tools import tool
from tavily import TavilyClient
from dotenv import load_dotenv
import logging
from pathlib import Path


logging.basicConfig(
        level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

load_dotenv()
tavily_client=TavilyClient()

@tool
def search_tool(topic:str)->str:
    """Search the web for a given topic and return the results."""
    logging.info(f"Searching the web for topic: {topic}")
    return tavily_client.search(topic)

@tool
def write_plan(plan: str, filename: str = "plan.txt") -> str:
    """
    Write the agent's plan to a local text file.
    """

    plans_dir = Path("plans")
    plans_dir.mkdir(exist_ok=True)

    file_path = plans_dir / filename

    file_path.write_text(plan, encoding="utf-8")

    return f"Plan written successfully to: {file_path.resolve()}"