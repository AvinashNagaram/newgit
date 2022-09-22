# this is the simple change for testing git
# this is the change in the new branch

# # approach one use free resources with out the API keys
#
# import  requests
#
# city = input('enter the city name')
#
# print ('you are looking data for city ' + city)
#
# url = 'https://wttr.in/{}'.format(city)
#
# res = requests.get(url)
#
# print (res.text)

# -----------------------------------------------------------------

import requests

# using the openweather api in this case
base_url = "http://api.openweathermap.org/data/2.5/weather?"
apikey = 'this has to be retrieved from the paid subscription to the website http://openweathermap.org/ '
city = input('enter city name : ')

url = base_url + 'appid=' + apikey + '&q=' + city


res = requests.get(url)
out = res.json()

print ('max temperature is : ' + out['temp_max'])
print ('min temperature is : ' + out['temp_min'])
print ('pressure is : ' + out['pressure'])
print ('humidity is : ' + out['humidity'])
print ('windspeed is : ' + out['wind'])
print ('Sunrise at: ' + out['sunrise'])
print ('Sunset at : ' + out['sunset'])
print ('cloud status : ' + out['cloudiness'])


# I am trying to attach the sample api response including all the fields output parms from the service

#
# {
#     "lat": 33.44,
#     "lon": -94.04,
#     "timezone": "America/Chicago",
#     "timezone_offset": -21600,
#     "current": {
#         "dt": 1618317040,
#         "sunrise": 1618282134,
#         "sunset": 1618333901,
#         "temp": 284.07,
#         "feels_like": 282.84,
#         "pressure": 1019,
#         "humidity": 62,
#         "dew_point": 277.08,
#         "uvi": 0.89,
#         "clouds": 0,
#         "visibility": 10000,
#         "wind_speed": 6,
#         "wind_deg": 300,
#         "weather": [
#             {
#                 "id": 500,
#                 "main": "Rain",
#                 "description": "light rain",
#                 "icon": "10d"
#             }
#         ],
#         "rain": {
#             "1h": 0.21
#         }
#     },
#     "minutely": [
#         {
#             "dt": 1618317060,
#             "precipitation": 0.205
#         },
#         ...
# },
# "hourly": [
#     {
#         "dt": 1618315200,
#         "temp": 282.58,
#         "feels_like": 280.4,
#         "pressure": 1019,
#         "humidity": 68,
#         "dew_point": 276.98,
#         "uvi": 1.4,
#         "clouds": 19,
#         "visibility": 306,
#         "wind_speed": 4.12,
#         "wind_deg": 296,
#         "wind_gust": 7.33,
#         "weather": [
#             {
#                 "id": 801,
#                 "main": "Clouds",
#                 "description": "few clouds",
#                 "icon": "02d"
#             }
#         ],
#         "pop": 0
#     },
#     ...
# }
# "daily": [
#     {
#         "dt": 1618308000,
#         "sunrise": 1618282134,
#         "sunset": 1618333901,
#         "moonrise": 1618284960,
#         "moonset": 1618339740,
#         "moon_phase": 0.04,
#         "temp": {
#             "day": 279.79,
#             "min": 275.09,
#             "max": 284.07,
#             "night": 275.09,
#             "eve": 279.21,
#             "morn": 278.49
#         },
#         "feels_like": {
#             "day": 277.59,
#             "night": 276.27,
#             "eve": 276.49,
#             "morn": 276.27
#         },
#         "pressure": 1020,
#         "humidity": 81,
#         "dew_point": 276.77,
#         "wind_speed": 3.06,
#         "wind_deg": 294,
#         "weather": [
#             {
#                 "id": 500,
#                 "main": "Rain",
#                 "description": "light rain",
#                 "icon": "10d"
#             }
#         ],
#         "clouds": 56,
#         "pop": 0.2,
#         "rain": 0.62,
#         "uvi": 1.93
#     },
#     ...
# },
# "alerts": [
#     {
#         "sender_name": "NWS Tulsa",
#         "event": "Heat Advisory",
#         "start": 1597341600,
#         "end": 1597366800,
#         "description": "...HEAT ADVISORY REMAINS IN EFFECT FROM 1 PM THIS AFTERNOON TO\n8 PM CDT THIS EVENING...\n* WHAT...Heat index values of 105 to 109 degrees expected.\n* WHERE...Creek, Okfuskee, Okmulgee, McIntosh, Pittsburg,\nLatimer, Pushmataha, and Choctaw Counties.\n* WHEN...From 1 PM to 8 PM CDT Thursday.\n* IMPACTS...The combination of hot temperatures and high\nhumidity will combine to create a dangerous situation in which\nheat illnesses are possible."
#     },
#     ...
# ]



