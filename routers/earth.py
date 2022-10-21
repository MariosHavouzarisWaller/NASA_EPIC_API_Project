from fastapi import APIRouter, Request
from requests.auth import HTTPBasicAuth
import requests as requests
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from EPICInfo import EarthInfo
from distanceCalculator import distance

router = APIRouter(prefix="/api/earth")
templates = Jinja2Templates(directory="templates")

auth = HTTPBasicAuth('apikey', '2E3gS1S09YEfmSbU3VrjJzKxOL9ogRkQjv82I7cm')
response = requests.get("https://epic.gsfc.nasa.gov/api/natural/date/2022-10-10", auth=auth)

class BadDateException(Exception):
    pass

@router.get("/", response_class=HTMLResponse)
async def get_earth(request: Request, date: str|None = None):
    earthCoordsX = 0
    earthCoordsY = 0
    earthCoordsZ = 0

    objList = list()

    for item in response.json():
        _image = item['image']
        _date = item['date']
        satCoordsX = item['dscovr_j2000_position']['x']
        satCoordsY = item['dscovr_j2000_position']['y']
        satCoordsZ = item['dscovr_j2000_position']['z']
        sunCoordsX = item['sun_j2000_position']['x']
        sunCoordsY = item['sun_j2000_position']['y']
        sunCoordsZ = item['sun_j2000_position']['z']
        earthSatDist = distance(earthCoordsX, earthCoordsY, earthCoordsZ, satCoordsX, satCoordsY, satCoordsZ)
        sunSatDist = distance(sunCoordsX, sunCoordsY, sunCoordsZ, satCoordsX, satCoordsY, satCoordsZ)
        sunEarthDist = distance(sunCoordsX, sunCoordsY, sunCoordsZ, earthCoordsX, earthCoordsY, earthCoordsZ)
        earthObj = EarthInfo(_image, _date, earthSatDist, sunSatDist, sunEarthDist)
        objList.append(earthObj)

    return templates.TemplateResponse("home.html", {"request": request, "objList": objList})