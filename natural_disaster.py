class NaturalDisaster:
    def __init__(self, title, lon, lat, date):
        self.title = title
        self.lon = lon
        self.lat = lat
        self.date = date

class Volcano(NaturalDisaster):
    def __init__(self, title, lon, lat, date):
        super().__init__(title, lon, lat, date)

class Storm(NaturalDisaster):
    def __init__(self, title, lon, lat, date):
        super().__init__(title, lon, lat, date)

class Earthquake(NaturalDisaster):
    def __init__(self, title, lon, lat, date):
        super().__init__(title, lon, lat, date)

class Wildfire(NaturalDisaster):
    def __init__(self, title, lon, lat, date):
        super().__init__(title, lon, lat, date)

class Tsunami(NaturalDisaster):
    def __init__(self, title, lon, lat, date):
        super().__init__(title, lon, lat, date)

