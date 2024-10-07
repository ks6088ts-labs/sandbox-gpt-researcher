import asyncio

import typer
from dotenv import load_dotenv
from gpt_researcher import GPTResearcher

app = typer.Typer()


async def _run(query: str):
    researcher = GPTResearcher(query=query, report_type="research_report")
    # Conduct research on the given query
    research_result = await researcher.conduct_research()
    typer.echo(research_result)

    # Write the report
    report = await researcher.write_report()
    typer.echo(report)


@app.command()
def run(query: str = "why is Nvidia stock going up?"):
    asyncio.run(_run(query=query))


if __name__ == "__main__":
    load_dotenv()
    app()
