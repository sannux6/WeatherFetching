import requests

Api = ""  # set your API here
Baseurl = "http://api.openweathermap.org/data/2.5/weather"
print("Welcome to Weather fetcher!")
city = input("Please enter a location to see weather.\nLocation:\t")
requesturl = f"{Baseurl}?appid={Api}&q={city}"

response = requests.get(requesturl)

if response.status_code == 200:
    data = response.json()
    # print(data)
    weather = data['weather'][0]['description']
    
    temperature = round(data ['main']['temp'] - 273,2) 
    print(f"\n\t The weather of {city} : {weather}")
    print(f"\t Temperature: {temperature}\n")
   

else:
    print("An error occured. Entered Location couldn't find.")
