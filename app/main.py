import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()


@app.get(path="/", name="Demo")
async def demo() -> HTMLResponse:
    return HTMLResponse(content="Hello World!", status_code=200)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="127.0.0.1",
        port=8000,
        workers=workers if (workers := os.cpu_count()) else 8,
        debug=False,
        log_config=None,
    )
