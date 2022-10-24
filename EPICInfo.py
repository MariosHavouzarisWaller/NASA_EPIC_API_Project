# This class creates the earth object
class EarthInfo():

    def __init__(self, id, earthImage, date, earthDist, sunDist, sunEarthDist):
        self.id = id 
        self.earthImage = earthImage
        self.date = date
        self.earthDist = earthDist
        self.sunDist = sunDist
        self.sunEarthDist = sunEarthDist
        
    # This is implementation to test that the data being input into the object was the correct information and correctly formatted
    # def __str__(self):
    #     return f"{self.earthImage} on date {self.date}\nDistance of satellite to Earth: {self.earthDist}\nDistance of satellite to Sun: {self.sunDist}\nDistance of Earth to Sun: {self.sunEarthDist}"
        