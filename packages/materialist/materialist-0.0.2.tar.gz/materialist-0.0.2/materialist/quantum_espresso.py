import requests
from materialist.client import stream_job, get_job_result, HOST, PORT

def pwx(qe_input_fn):
    with open(qe_input_fn, "r") as f:
        qe_input = f.read()

    args = {"qe_input": qe_input}
    response = requests.post(f"http://{HOST}:{PORT}/qe/pwx", json=args).json()
    job_id = response["job_id"]
    stream_job(job_id)
    return get_job_result(job_id)
