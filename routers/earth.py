from fastapi import APIRouter
from requests.auth import HTTPBasicAuth
import requests as requests

from EPICInfo import EarthInfo
from distanceCalculator import distance

# This sets up the router that will allow us to view the json data
router = APIRouter(prefix="/api/earth")

# This provides us access to the NASA EPIC satellite database and API
auth = HTTPBasicAuth('apikey', '2E3gS1S09YEfmSbU3VrjJzKxOL9ogRkQjv82I7cm')
response = requests.get("https://epic.gsfc.nasa.gov/api/natural/date/2022-10-04", auth=auth)

# Error Handling
class BadDateException(Exception):
    pass

# Get request for the information stored in the NASA database 
@router.get("/jsoninfo")
def get_earth(date: str|None = None):
    print("I'm being run")  # Used for testing/debugging
    earthCoordsX = 0
    earthCoordsY = 0
    earthCoordsZ = 0

    objList = list()

    # Fills up list
    for item in response.json():
        _id = item['identifier']
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
        earthObj = EarthInfo(_id, _image, _date, earthSatDist, sunSatDist, sunEarthDist)
        objList.append(earthObj)
    print(objList[0]) # Used for testing/debugging
    return objList