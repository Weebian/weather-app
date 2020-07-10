import pyowm
from datetime import date, datetime, timedelta

#Add API key
owm = pyowm.OWM('xxxxxxxx')

#obtain weather manager
weather_mgr = owm.weather_manager()

#declare location
loc = weather_mgr.weather_at_place('Ottawa,CA')

#obtain data
weather = loc.weather #weather object
forecast_3h = weather_mgr.forecast_at_place('Ottawa,CA', '3h').forecast #forcast in 3h intervals (5 days)

temp = weather.temperature(unit='celsius') #temperature
temp_min = temp['temp_min']
temp_max = temp['temp_max']
wind_speed = weather.wind()['speed'] #wind speed
sunrise = weather.sunrise_time(timeformat='date') - timedelta(hours=4) #sunrise time
sunset = weather.sunset_time(timeformat='date')  - timedelta(hours=4) #sunset time
today = date.today().strftime("%b-%d-%Y")

#print data
print("Current forcast: ")
print(f'\tDate: {today}')
print(f'\tWeather\'s current status: {weather.detailed_status}')
print(f'\tMin temp: {temp_min}')
print(f'\tMax temp: {temp_max}')
print(f'\tWind: {wind_speed} m/s')
print(f'\tSunrise: {sunrise}')
print(f'\tSunset: {sunset}')

print(f'\nNext 24 hours forecast:')
last_day = datetime.today().date()
for forcast in forecast_3h:
    currentday = forcast.reference_time('date') - timedelta(hours=4)
    if last_day != currentday.date():
        last_day = currentday.date()
        print('\n')
    print(f"Time: {currentday} - Status: {forcast.detailed_status}")
