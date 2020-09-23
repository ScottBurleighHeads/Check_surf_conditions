import requests
from datetime import datetime
from bs4 import BeautifulSoup

url = 'http://api.worldweatheronline.com/premium/v1/marine.ashx?key=e76a15e1269541aab92105556202109&format=xml&q=-28.0291,153.431381'
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

print(soup.find_all("swelldir16point")[2].text.strip())
# wind = soup.find('hourly')
# for num,item in enumerate(wind):
#     print(item)
#     if "watertemp_c" in str(item):
#         print("yay")
#         holder = item
#         break

# print(holder.text)
    

# # if "waterTemp_C" in  "<watertemp_c>21</watertemp_c>":
# #     print("yay")