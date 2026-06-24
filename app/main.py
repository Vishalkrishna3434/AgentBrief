from fastapi import FastAPI

app=FastAPI(title="AgentBrief", version="1.0.0")

@app.get("/")
def home():
  return{"Message":"AgentBrief Running"}