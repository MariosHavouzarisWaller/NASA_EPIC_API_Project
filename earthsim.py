from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
import uvicorn

from routers import web, earth
from routers.earth import BadDateException

app = FastAPI(title= "Earth Sim")
app.include_router(earth.router)
app.include_router(web.router)

@app.exception_handler(earth.BadDateException)
async def unicorn_exception_handler(request: Request, exc: BadDateException):
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={"message": "Invalid Date"},
    )

if __name__ == "__main__":
    uvicorn.run("earthsim:app", reload=True)