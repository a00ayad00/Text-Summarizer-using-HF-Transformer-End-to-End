from fastapi import FastAPI
import uvicorn
from starlette.responses import RedirectResponse
from src.pipeline.summarize import summarize


app = FastAPI()

@app.get('/')
async def home():
    return RedirectResponse(url='/docs')


@app.post('/summarize')
async def gen_summary(text):
    try:
        return summarize(text)
    except Exception as e:
        raise e


if __name__=="__main__":
    uvicorn.run('app', host="0.0.0.0", port=8080)