class EarthInfo():

    def __init__(self, earthImage, date, earthDist, sunDist, sunEarthDist):
        self.earthImage = earthImage
        self.date = date
        self.earthDist = earthDist
        self.sunDist = sunDist
        self.sunEarthDist = sunEarthDist

    def __str__(self):
        return f"{self.earthImage} on date {self.date}\nDistance of satellite to Earth: {self.earthDist}\nDistance of satellite to Sun: {self.sunDist}\nDistance of Earth to Sun: {self.sunEarthDist}"
        