import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.053570000000036&lon=-118.24544999999995#.YkHI2efMLIU')
soup = BeautifulSoup(page.content,'html.parser')
#to find tags
#print(soup.find_all('a'))
week = soup.find(id='seven-day-forecast-body')
#print(week)

# to print out the first Div
# item list contain all these
items = week.find_all(class_='tombstone-container')
# print(items[0])

# print(items[0].find(class_='period-name').get_text())
# print(items[0].find(class_='short-desc').get_text())
# print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-names').get_text() for item in items]
short_description = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]


# print(period_names)
# print(short_description)
# print(temperatures)

weather_stuff = pd.DataFrame (
    {
        'period': period_names,
        'short-descriptions': short_description,
        'temperatures': temperatures
    }
)

print(weather_stuff)

#weather_stuff.to_csv('weather.csv')