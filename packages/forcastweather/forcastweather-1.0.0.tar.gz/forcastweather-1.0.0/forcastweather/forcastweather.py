import requests


class Weather:
    """
    Creates a weather object getting an apikey as input
    and either a city name or lat and lon coordinates.
    """
    def __init__(self, apikey, city, lat=None, lon=None):
        if city is not None:
            url = (f'https://api.openweathermap.org/data/2.5/'
                   f'forecast?q={city}&APPID={apikey}&'
                   f'units=imperial')
        elif lat is not None and lon is not None:
            url = (f'https://api.openweathermap.org/data/2.5/'
                   f'forecast?lat={lat}&lon={lon}&APPID={apikey}&'
                   f'units=imperial')
        else:
            raise TypeError("provide either a city or lat and lon arguments.")

        r = requests.get(url)
        self.data = r.json()
        if self.data['cod'] != "200":
            raise ValueError(self.data["message"])

    def next_12h(self):
        """Returns 3-hour data for the next 12 hours as a dict"""
        return self.data['list'][:4]

    def next_12h_simplified(self):
        """
        Returns date, temperature, and sky condition every 3 hours
        for the next 12 hours as a list of tuples.
        """
        result = []
        for dict_ in self.data['list'][:4]:
            result.append((dict_['dt_txt'],
                           dict_['main']['temp'],
                           dict_['weather'][0]['description']))
        return result
