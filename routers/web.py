from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import time

from EPICInfo import EarthInfo
from routers.earth import get_earth

# Router used to set up the actual website
router = APIRouter()

# Jinja templates used for more easily integrating python code with HTML
templates = Jinja2Templates(directory="templates")

# Get request for all the information that will be displayed and available on the web page
@router.get("/", response_class=HTMLResponse)
def home(request: Request, i: int|None=None):
    earthList = get_earth()
    if i != None:
        earthDisplay = earthList[i]
        return templates.TemplateResponse("home.html", {"request": request,"earthList": earthList, "earthDisplay": earthDisplay})
    else:
        while i == None:
            for item in earthList:
                showEarth = item.earthImage
                time.sleep(0.5)
                print(showEarth)
        return templates.TemplateResponse("home.html", {"request": request, "earthList": earthList, "showEarth": showEarth}) # Smol bug
