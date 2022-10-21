from multiprocessing.resource_tracker import ResourceTracker
from fastapi import APIRouter, Request, Cookie
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from EPICInfo import EarthInfo
from routers.earth import get_earth

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def home(request: Request, earth_cookie: str|None = Cookie(None)):
    print(earth_cookie)
    return templates.TemplateResponse("home.html", {"request": request})