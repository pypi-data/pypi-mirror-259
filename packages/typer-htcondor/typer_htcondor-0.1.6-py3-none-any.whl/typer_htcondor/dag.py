import typer
import htcondor

JSM_HTC_DAG_SUBMIT = 4

app = typer.Typer()

@app.command()
def submit():
    """
    Submits a job when given a submit file
    """
    typer.echo("Submitting a job")

@app.command()
def status():
    """
    Shows current status of a DAG when given a DAG id
    """
    typer.echo("Checking the status of a job")