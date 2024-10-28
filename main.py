from fastapi import FastAPI
from fastapi.responses import  RedirectResponse

app = FastAPI(title= "SkillGapFinder Backend")

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")