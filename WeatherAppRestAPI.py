import requests

baseUrl = "http://api.openweathermap.org/data/2.5/weather"
params = {"q": "London, uk",
          "APPID": "0fd076e7a1d95f835765e366df50bbc9"
          }
#Make the GET request
try:
    response = requests.get(baseUrl, params=params)

   
    if response.status_code==200:

        responseJson = response.json()
        print(responseJson["main"]["temp"])
        print(responseJson["wind"]["speed"])
        print(responseJson["weather"][0]["description"])
        print(responseJson)

except:
    responseJson = None
    print("Something went wrong")












