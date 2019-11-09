import requests

#Location is a string in the form of "Country+City+Street"
#Can be formatted 
location = 'XXXXXXXXXXXXXXX'

#API Key for communicating with Google
#Must be received from Google's Developer Portal 
API_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

#Target URL - includes location and API key
url = ('https://maps.googleapis.com/maps/api/geocode/json?address=' +location+ '&key=' + API_KEY )

print(url)
#Parameters dictionary in order to define the API key
params = {'address' : location}

#send a GET request to the url
inforequest = requests.get(url=url, params=params)

#convert request into json
data = inforequest.json()

latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']

latitude = str(latitude)
longitude = str(longitude)
formatted_address= str(formatted_address)

# printing the output
print(data)
print("\nLatitude: {}\nLongtiude {}\nFormatted Address:{}" .format(latitude, longitude, formatted_address))