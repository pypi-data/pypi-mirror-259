import requests

# from sunnyday import sunnyday


# url = "https://api.openweathermap.org/data/2.5/forecast?q=Madrid&APIID=eeef35d0901d6e5de86f84b62779dfc7&units=imperial"
# r = requests.get(url)
# print(r.json())

class Weather:
    """Creates a Weather Object getting an apikey as input
    and either a city name or Lat and lon coordinates

    # Create weather Object with City Name
    weather = Weather(apikey="yourAPI_KEY", city="Madrid")

    # Using latitude and longitude coordinates
    # weather = Weather(apikey="yourAPI_KEY", lat=41.1, lon=-4.1)

    # Get complete weather data for the next 12 hours:
    weather,next_12h()

    # Simplified data for the next 12 hours:
    weather.next12h_simplified()

    Sample url to get sky condition icons:
    https://openweathermap.org/img/wn/10d@2x.png


    """
    def __init__(self, apikey, city=None, lat=None, lon=None):
        if city:
            url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={apikey}&units=imperial"
            r = requests.get(url)
            self.data = r.json()
        elif lat and lon:
            url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&APPID={apikey}&units=imperial"
            r = requests.get(url)
            self.data = r.json()
        else:
            # print("Provide either a city or lat and lon arguments")
            raise TypeError("Provide either a city or lat and lon arguments")
        if self.data["cod"] != "200":
            raise ValueError(self.data["message"])

    def next_12h(self):
        """Returns 3-hour data for the next 12 hours as a dict"""
        return self.data['list'][:4]

    def next_12h_simplified(self):
        """ Returns date, temperature, and sky condition every 3 hours
        for the next 12 hours as a tuple of tuples
        """
        # Weather below is a "list". That is why we had to have "weather[0]..."
        simple_data = []
        for dicty in self.data['list'][:4]:
            simple_data.append((dicty['dt_txt'], dicty['main']['temp'],
                    dicty['weather'][0]['description'], dicty['weather'][0]['icon']))

        return simple_data
        # return (self.data['list'][0]['dt_txt'], self.data['list'][0]['main']['temp'],
        # self.data['list'][0]['weather'][0]['description'])

