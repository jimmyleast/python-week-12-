print("Welcome to the Weather Program!")
import requests
import json
# Enter your API key here
api_key = "2851f418494ad3cccd9c3742ab2bcbc8"
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

#weather detail organization and printing
def printOutput(weather_Output):
   temp=weather_Output.get('main').get('temp')
   temp_max=weather_Output.get('main').get('temp_max')
   temp_min=weather_Output.get('main').get('temp_min')
   humidity=weather_Output.get('main').get('humidity')
   pressure=weather_Output.get('main').get('pressure')
   sky=weather_Output['weather'][0]['main']
   wind=weather_Output.get('wind').get('speed')
   wind_deg=weather_Output.get('deg')

#printing the weather details
   print(" Temperature (in kelvin unit) = " +
                   str(temp) +
         "\n and the max tem is  = " +
                   str(temp_max) +
         "\n and the tem min is = " +
                   str(temp_min) +
         "\n your humidity is = " +
                   str(humidity)+
         "\n your pressure is = " +
                   str(pressure)+
         "\n your sky is = " +
                   str(sky)+
         "\n your wind is = " +
                   str(wind)+
         "\n your wind direction is = " +
                   str(wind_deg))

#assigning the main to the machine
def main():
    while True:
      location = input("\n Please enter a city or zipcode to search for or type exit to stop. ")
      #checking if the user entered anything from the request
      if location == "":
         print("You didn't enter anything!")
         continue
         #allowing the user to exit if they want
      if location == "exit":
        break
      else:
          try:
             zip_num = int(location)
             complete_url = base_url + "appid=" + api_key + "&q=" + location
             response = requests.get(complete_url)
             x = response.json()
             if x["cod"] != "404":
				 #calling the weather function toprint out the details
                 printOutput(x)
             else:
                print(" City Not Found ")
             continue
          except:
              city_name = str(location)
              complete_url = base_url + "appid=" + api_key + "&q=" + city_name
              response = requests.get(complete_url)
              x = response.json()
              if x["cod"] != "404":
                  printOutput(x)
              else:
                print(" City Not Found ")
              continue

# run the program here
main()
