# This acts as our main class
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
import uvicorn

from routers import web, earth
from routers.earth import BadDateException

# Sets up the FastAPI "web service" and the APIRouter router's
app = FastAPI(title= "Earth Sim")
app.include_router(earth.router)
app.include_router(web.router)

# Exception handler set up in advance for when we have a date picker
@app.exception_handler(earth.BadDateException)
async def unicorn_exception_handler(request: Request, exc: BadDateException):
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={"message": "Invalid Date"},
    )

# Allows us to hot reload the program as it runs through the uvicorn framework
if __name__ == "__main__":
    uvicorn.run("earthsim:app", reload=True)