import requests
from datetime import datetime
from bs4 import BeautifulSoup

class Surf():
    url = 'http://api.worldweatheronline.com/premium/v1/marine.ashx?key=e76a15e1269541aab92105556202109&format=xml&q=-28.0291,153.431381'
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    time = datetime.now()

    #The time_holder is an input that gives updates to weather outputs depending 
    #on the time of the day.
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
    
    def __init__(self):
        self.wind_speed = None
        self.wind_direction = None
        self.surf_size = None
        self.date = None
        self.water_temp = None
        self.swell_direction = None
   
    def get_wind_speed(self):
        self.wind_speed = Surf.soup.find_all("windspeedkmph")[Surf.time_holder].text
    
    def get_wind_direction(self):
        self.wind_direction = Surf.soup.find_all("winddir16point")[Surf.time_holder].text

    def get_water_temp(self):
        self.water_temp = Surf.soup.find_all("watertemp_c")[Surf.time_holder].text
    
    def get_swell_direction(self):
        self.swell_direction = Surf.soup.find_all("swelldir16point")[2].text.strip()
    
    def get_surf_size(self):
        self.surf_size = Surf.soup.find_all("swellheight_m")[Surf.time_holder].text

scott = Surf()
scott.get_wind_speed()
scott.get_wind_direction()
scott.get_water_temp()
scott.get_swell_direction()
scott.get_surf_size()

print(scott.wind_speed)
print(scott.wind_direction)
print(scott.water_temp)
print(scott.swell_direction)
print(scott.surf_size)




# print(soup.find('sunrise').text)
# print(soup.find("windspeedkmph").text)
# print(soup.find("date").text)
# print(soup.find("winddir16point").text)

