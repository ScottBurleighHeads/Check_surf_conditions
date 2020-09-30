import requests
from datetime import datetime
from bs4 import BeautifulSoup

class Surf():
    
    #The time_holder is an input that gives updates to weather outputs depending 
    #on the time of the day. time.hour returns the hour of the day.
    time = datetime.now()
    time_holder = 0
    if time.hour < 2:
        time_holder = 0 
    elif time.hour >= 2 and time.hour < 5:
        time_holder = 1 
    elif time.hour >= 5  and time.hour < 8:
        time_holder = 2
    elif time.hour >= 8  and time.hour < 11:
        time_holder = 3
    elif time.hour >= 11  and time.hour < 14:
        time_holder = 4
    elif time.hour >= 14  and time.hour < 17:
        time_holder = 5
    elif time.hour >= 17  and time.hour < 20:
        time_holder = 6
    elif time.hour >= 20  and time.hour < 25:
        time_holder = 7
    
    def __init__(self,coordinates):
        """ This method initiallises all method att"""
        url = f'http://api.worldweatheronline.com/premium/v1/marine.ashx?key=e76a15e1269541aab92105556202109&format=xml&q={coordinates}&tides=yes'
        response = requests.get(url)
        soup = BeautifulSoup(response.text,"html.parser")
        self.wind_speed = soup.find_all("windspeedkmph")[Surf.time_holder].text
        self.wind_direction = soup.find_all("winddir16point")[Surf.time_holder].text
        self.surf_size = soup.find_all("swellheight_m")[Surf.time_holder].text
        self.water_temp = soup.find_all("watertemp_c")[Surf.time_holder].text
        self.swell_direction = soup.find_all("swelldir16point")[2].text.strip()
        self.word_surf = ""
        self.word_paddle = ""
        
    
    
    @property
    def surf_str_entry(self):
        """ This method is used as an AI feature that interacts with the user depending 
            on the results it gets back from the api"""
        if float(self.surf_size) < 1.3 and "w" in self.wind_direction.lower():
            self.word_surf = f"pretty small with a swell of {self.surf_size}m but offshore winds from the {self.wind_direction} so probably worth a surf."
        elif float(self.surf_size) < 1.3:
            self.word_surf = f"pretty small with a swell of {self.surf_size}m and onshore winds from the {self.wind_direction}. Better off going to the gym."
        elif float(self.surf_size) > 1.3 and "w" in self.wind_direction.lower():
            self.word_surf = f"decent swell of {self.surf_size}m and offshore winds from the {self.wind_direction}. Get out there now"
        else:
            self.word_surf = f"a decent swell of {self.surf_size}m from the {self.swell_direction} but onshore."
        return self.word_surf

    @property 
    def paddleBoard_str_entry(self):
        if float(self.wind_speed) < 20 and float(self.water_temp) > 20:
            self.word_paddle = f"The wind is only {self.wind_speed}km/h and the water temp is a nice {self.water_temp}C. Go for a paddle board."
        elif float(self.wind_speed) < 20 and float(self.water_temp) < 20:
            self.word_paddle = f"The wind is only {self.wind_speed}km/h but the water temp is a chilly {self.water_temp}C. Chuck a wetty on and go for a paddle board."
        elif float(self.wind_speed) >= 20:
            self.word_paddle = f"Its a bit windy to go paddle boarding. The wind is {self.wind_speed}"
        return self.word_paddle




