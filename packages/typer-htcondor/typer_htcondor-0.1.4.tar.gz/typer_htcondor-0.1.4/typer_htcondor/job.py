import typer
import logging
from typer_htcondor import dagman

app = typer.Typer()


@app.command()
def submit(
    submit_file: str = typer.Argument(..., help="Submit file"),
    resource: str = typer.Option(
        None, "--resource", help="Resource to run this job. Supports Slurm and EC2"),
    runtime: int = typer.Option(
        None, "--runtime", help="Runtime for the given resource (seconds)"),
    email: str = typer.Option(
        None, "--email", help="Email address to receive notifications"),
    annex_name: str = typer.Option(
        None, "--annex-name", help="Annex name that this job must run on"),
):
    """
    Submits a job when given a submit file.
    """
    # Your command implementation goes here. @TODO
    print(f"Submitting job with submit file: {submit_file}")
    if resource:
        print(f"Resource: {resource}")
    if runtime is not None:
        print(f"Runtime: {runtime}")
    if email:
        print(f"Email: {email}")
    if annex_name:
        print(f"Annex name: {annex_name}")


@app.command()
def status(
    job_id: str = typer.Argument(..., help="Job ID"),
    skip_history: bool = typer.Option(
        False, "--skip-history", help="Skip checking history for completed or removed jobs"),
):
    """
    Shows current status of a job when given a job id.
    """

    # Split job id into cluster and proc
    if "." in job_id:
        cluster_id, proc_id = [int(i) for i in job_id.split(".")][:2]
    else:
        cluster_id = int(job_id)
        proc_id = 0

    # Get schedd
    schedd = htcondor.Schedd()

    # Query schedd
    constraint = f"ClusterId == {cluster_id} && ProcId == {proc_id}"
    projection = ["JobStartDate", "JobStatus", "QDate", "CompletionDate", "EnteredCurrentStatus",
                  "RequestMemory", "MemoryUsage", "RequestDisk", "DiskUsage", "HoldReason",
                  "ResourceType", "TargetAnnexName", "NumShadowStarts", "NumJobStarts", "NumHolds",
                  "JobCurrentStartTransferOutputDate", "TotalSuspensions", "NumRestarts", "CommittedTime"]
    try:
        job = schedd.query(constraint=constraint,
                           projection=projection, limit=1)
    except IndexError:
        raise RuntimeError(f"No job found for ID {job_id}.")
    except Exception as e:
        raise RuntimeError(f"Error looking up job status: {str(e)}")

    # Check the history if no jobs found
    if len(job) == 0 and not skip_history:
        try:
            job = list(schedd.history(constraint=constraint,
                       projection=projection, match=1))
        except KeyboardInterrupt:
            job = []

    if len(job) == 0:
        raise RuntimeError(f"No job found for ID {job_id}.")

    resource_type = job[0].get("ResourceType", "htcondor") or "htcondor"
    resource_type = resource_type.casefold()

    if resource_type == "htcondor":

        job_ad = job[0]

        try:
            job_status = job_ad["JobStatus"]
        except IndexError as err:
            logger.error(f"Job {job_id} has unknown status")
            raise err

        # Get annex info
        annex_info = ""
        target_annex_name = job_ad.get('TargetAnnexName')
        if target_annex_name is not None:
            annex_info = f" on the annex named '{target_annex_name}'"

        # Get some common numbers
        job_queue_time = datetime.now(
        ) - datetime.fromtimestamp(job_ad["QDate"])
        job_atts = job_ad.get("NumShadowStarts", 0)
        job_execs = job_ad.get("NumJobStarts", 0)
        job_holds = job_ad.get("NumHolds", 0)
        job_suspends = job_ad.get("TotalSuspensions", 0)
        job_committed_time = job_ad.get("CommittedTime")
        goodput = None
        if job_committed_time is not None:
            goodput = job_committed_time / 3600

        # Compute memory and disk usage if available
        memory_usage, disk_usage = None, None
        if "MemoryUsage" in job_ad:
            memory_usage = (f"{readable_size(job_ad.eval('MemoryUsage')*10**6)} out of "f"{readable_size(job_ad.eval('RequestMemory') * 10**6)} requested")
        if "DiskUsage" in job_ad:
            disk_usage = (f"{readable_size(job_ad.eval('DiskUsage')*10**3)} out of "f"{readable_size(job_ad.eval('RequestDisk')*10**3)} requested")

        # Print information relevant to each job status
        if job_status == htcondor.JobStatus.IDLE:
            logger.info(f"Job {job_id} is currently idle.")
            logger.info(f"It was submitted {readable_time(job_queue_time.seconds)} ago.")
            logger.info(f"It requested {readable_size(
                job_ad.eval('RequestMemory')*10**6)} of memory.")
            logger.info(f"It requested {readable_size(
                job_ad.eval('RequestDisk')*10**3)} of disk space.")
            if job_holds > 0:
                logger.info(f"It has been held {job_holds} time{s(job_holds)}.")
            if job_atts > 0:
                logger.info(f"HTCondor has attempted to start the job {job_atts} time{s(job_atts)}.")
                logger.info(f"The job has started {job_execs} time{s(job_execs)}.")

        elif job_status == htcondor.JobStatus.RUNNING:
            job_running_time = datetime.now(
            ) - datetime.fromtimestamp(job_ad["JobStartDate"])
            logger.info(f"Job {job_id} is currently running{annex_info}.")
            logger.info(f"It started running {readable_time(job_running_time.seconds)} ago.")
            logger.info(f"It was submitted {readable_time(job_queue_time.seconds)} ago.")
            if memory_usage:
                logger.info(f"Its current memory usage is {memory_usage}.")
            if disk_usage:
                logger.info(f"Its current disk usage is {disk_usage}.")
            if job_suspends > 0:
                logger.info(f"It has been suspended {job_suspends} time{s(job_suspends)}.")
            if job_holds > 0:
                logger.info(f"It has been held {job_holds} time{s(job_holds)}.")
            if job_atts > 1:
                logger.info(f"HTCondor has attempted to start the job {job_atts} time{s(job_atts)}.")
                logger.info(f"The job has started {job_execs} time{s(job_execs)}.")

        elif job_status == htcondor.JobStatus.SUSPENDED:
            job_suspended_time = datetime.now(
            ) - datetime.fromtimestamp(job_ad["EnteredCurrentStatus"])
            logger.info(f"Job {job_id} is currently suspended{annex_info}.")
            logger.info(f"It has been suspended for {readable_time(job_suspended_time.seconds)}.")
            logger.info(f"It has been suspended {job_suspends} time{s(job_suspends)}.")
            logger.info(f"It was submitted {readable_time(job_queue_time.seconds)} ago.")
            if memory_usage:
                logger.info(f"Its last memory usage was {memory_usage}.")
            if disk_usage:
                logger.info(f"Its last disk usage was {disk_usage}.")

        elif job_status == htcondor.JobStatus.TRANSFERRING_OUTPUT:
            job_transfer_time = datetime.now(
            ) - datetime.fromtimestamp(job_ad["JobCurrentStartTransferOutputDate"])
            logger.info(
                f"Job {job_id} is currently transferring output{annex_info}.")
            logger.info(f"It started transferring output {readable_time(job_transfer_time.seconds)} ago.")
            if memory_usage:
                logger.info(f"Its last memory usage was {memory_usage}.")
            if disk_usage:
                logger.info(f"Its last disk usage was {disk_usage}.")

        elif job_status == htcondor.JobStatus.HELD:
            job_held_time = datetime.now(
            ) - datetime.fromtimestamp(job_ad["EnteredCurrentStatus"])
            logger.info(f"Job {job_id} is currently held.")
            logger.info(f"It has been held for {readable_time(job_held_time.seconds)}.")
            logger.info(f"""It was held because "{job_ad['HoldReason']}".""")
            logger.info(f"It has been held {job_holds} time{s(job_holds)}.")
            logger.info(f"It was submitted {readable_time(job_queue_time.seconds)} ago.")
            if job_execs >= 1:
                if memory_usage:
                    logger.info(f"Its last memory usage was {memory_usage}.")
                if disk_usage:
                    logger.info(f"Its last disk usage was {disk_usage}.")
            if job_atts >= 1:
                logger.info(f"HTCondor has attempted to start the job {job_atts} time{s(job_atts)}.")
                logger.info(f"The job has started {job_execs} time{s(job_execs)}.")

        elif job_status == htcondor.JobStatus.REMOVED:
            job_removed_time = datetime.now(
            ) - datetime.fromtimestamp(job_ad["EnteredCurrentStatus"])
            logger.info(f"Job {job_id} was removed.")
            logger.info(f"It was removed {readable_time(
                job_removed_time.seconds)} ago.")
            logger.info(f"It was submitted {readable_time(job_queue_time.seconds)} ago.")
            if memory_usage:
                logger.info(f"Its last memory usage was {memory_usage}.")
            if disk_usage:
                logger.info(f"Its last disk usage was {disk_usage}.")

        elif job_status == htcondor.JobStatus.COMPLETED:
            job_completed_time = datetime.now(
            ) - datetime.fromtimestamp(job_ad["CompletionDate"])
            logger.info(f"Job {job_id} has completed.")
            logger.info(f"It completed {readable_time(
                job_completed_time.seconds)} ago.")
            logger.info(f"It was submitted {readable_time(job_queue_time.seconds)} ago.")
            if memory_usage:
                logger.info(f"Its last memory usage was {memory_usage}.")
            if disk_usage:
                logger.info(f"Its last disk usage was {disk_usage}.")
            if job_committed_time is not None:
                goodput = job_committed_time / 3600
                logger.info(f"Goodput is {goodput:.1f} hours.")
        else:
            logger.info(
                f"Job {job_id} is in an unknown state (JobStatus = {job_status}).")

    # Jobs running on provisioned Slurm or EC2 resources need to retrieve
    # additional information from the provisioning DAGMan log
    elif resource_type in ["slurm", "ec2"]:

        # Variables specific to jobs running on Slurm clusters
        jobs_running = 0
        job_started_time = None
        provisioner_cluster_id = None
        provisioner_job_submitted_time = None
        slurm_cluster_id = None
        slurm_nodes_requested = None
        slurm_runtime = None

        dagman_dag, dagman_out, dagman_log = DAGMan.get_files(job_id)

        if dagman_dag is None:
            raise RuntimeError(
                f"No {resource_type} job found for ID {job_id}.")

        # Parse the .dag file to retrieve some user input values
        with open(dagman_dag, "r") as dagman_dag_file:
            for line in dagman_dag_file.readlines():
                if "annex_runtime =" in line:
                    slurm_runtime = int(line.split("=")[1].strip())

        # Parse the DAGMan event log for useful information
        dagman_events = htcondor.JobEventLog(dagman_log)
        for event in dagman_events.events(0):
            if "LogNotes" in event.keys() and event["LogNotes"] == "DAG Node: B":
                provisioner_cluster_id = event.cluster
                provisioner_job_submitted_time = datetime.fromtimestamp(
                    event.timestamp)
                job_status = "PROVISIONING REQUEST PENDING"
            elif "LogNotes" in event.keys() and event["LogNotes"] == "DAG Node: C":
                slurm_cluster_id = event.cluster
            elif event.cluster == slurm_cluster_id and event.type == htcondor.JobEventType.EXECUTE:
                job_status = "RUNNING"
                jobs_running += 1
                if job_started_time is None:
                    job_started_time = datetime.fromtimestamp(event.timestamp)
            elif event.cluster == slurm_cluster_id and event.type == htcondor.JobEventType.JOB_TERMINATED:
                jobs_running -= 1
                if jobs_running == 0:
                    job_status = "COMPLETE"
            elif event.type == htcondor.JobEventType.JOB_HELD or event.type == htcondor.JobEventType.EXECUTABLE_ERROR:
                job_status = "ERROR"

        # Calculate how long job has been in its current state
        current_time = datetime.now()
        time_diff = None
        if job_status == "PROVISIONING REQUEST PENDING":
            time_diff = current_time - provisioner_job_submitted_time
        elif job_status == "RUNNING":
            time_diff = current_time - job_started_time

        # Now that we have all the information we want, display it
        if job_status == "COMPLETED":
            logger.info("Job has completed")
        else:
            if job_status == "PROVISIONING REQUEST PENDING":
                logger.info(f"Job is waiting for {resource_type.upper()} to provision pending request", end='')
            else:
                info_str = f"Job is {job_status}"
                if time_diff is not None:
                    info_str = f"{info_str} since {
                        round(time_diff.seconds/60)}m{(time_diff.seconds % 60)}s"
                logger.info(info_str)

    else:
        raise ValueError(f"Error: The 'job status' command does not support {resource_type} resources.")
