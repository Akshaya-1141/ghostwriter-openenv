from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Required Pydantic Models for OpenEnv
class Observation(BaseModel):
    text: str

class Action(BaseModel):
    suggested_text: str

@app.get("/")
def health_check():
    return {"status": "running"}

@app.post("/reset")
def reset():
    # Validator MUST get a 200 OK from this endpoint
    return Observation(text="Environment reset. Style guide: Professional. Draft: Hello world.")

@app.post("/step")
def step(action: Action):
    # Validator calls this to simulate a step
    return {"observation": Observation(text=action.suggested_text), "reward": 1.0, "done": True, "info": {}}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
# Inside server/app.py
def main():
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860, reload=False)

if __name__ == "__main__":
    main()
