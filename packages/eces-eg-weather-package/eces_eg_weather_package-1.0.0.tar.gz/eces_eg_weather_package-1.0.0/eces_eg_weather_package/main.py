import requests 
import pandas as pd


class Weather:
    """
    Here goes my detailed docs 
    """
    def __init__(self, apikey, city=None):
        url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}'
        r = requests.get(url)
        self.raw_data = r.json()
        if r.status_code != 200:
            raise ValueError('Incorrect City of API Key')

    def temp_next_5_days(self):
        """
        doc
        """
        data = []
        for row in self.raw_data['list']:
            row['main']['time'] = pd.to_datetime(row['dt'], unit = 's')
            data.append(row['main'])
        return pd.DataFrame(data)
    
    def wind_next_5_days(self):
        """
        doc
        """
        data = []
        for row in self.raw_data['list']:
            data.append(row['wind'])
        return pd.DataFrame(data)




