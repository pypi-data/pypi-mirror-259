import typer
from typer_htcondor import eventlog
from typer_htcondor import job
from typer_htcondor import dag
app = typer.Typer()
app.add_typer(eventlog.app, name="eventlog", help="Interacts with eventlogs")
app.add_typer(job.app, name="job", help="Run operations on HTCondor jobs")
app.add_typer(dag.app, name="dag", help="Run operations on HTCondor DAGs")

if __name__ == "__main__":
    app()
