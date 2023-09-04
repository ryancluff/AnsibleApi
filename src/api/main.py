from fastapi import FastAPI
import ansible_runner

app = FastAPI()

@app.get("/")
def get_root():
    return {"Hello": "World"}

@app.get("/play/{host}/{state}")
def get_play(host: str, state: str):
    if host == "chimaera":
        playbook = "chimaera.yml"
    elif host == "executor":
        playbook = "executor.yml"
    else:
        return {"error": "Host not found"}
    
    if state == "up":
        tags = "uncordon"
    elif state == "down":
        tags = "drain"
    else:
        return {"error": "State not found"}
    
    r = ansible_runner.run(
        private_data_dir='/tmp/demo',
        inventory='',
        playbook=playbook, 
        extravars={"node": host, "tags": tags}
        )

    return {"playbook": playbook}