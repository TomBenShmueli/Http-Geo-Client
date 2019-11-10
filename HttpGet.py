import requests

#  A function that formats a string into a Google accepted string by replacing special characters with "+"
def formattogooglestring(string):
    specialchars = '-+ ~`,./_'
    for char in specialchars:
        string = string.replace(char, "+")
    return string

def successfulrequest(request):
    if data is None:
        return True
    else:
        return False

place = "Tel Aviv Israel Rabin Square"
place = formattogooglestring(place)
print(place)

#  Location is a string in the form of "Country+City+Street"
#  Can be formatted by the
location = "XXXXXXXXXXXXXXXXXXXX"
location = formattogooglestring(location)

#  API Key for communicating with Google
#  Must be received from Google's Developer Portal
API_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

#  Target URL - includes location and API key
url = ('https://maps.googleapis.com/maps/api/geocode/json?address=' +location+ '&key=' + API_KEY)

print(url)
#  Parameters dictionary in order to define the API key
params = {'address' : location}

#  send a GET request to the url
inforequest = requests.get(url=url, params=params)

#  convert request into json
data = inforequest.json()

latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']

latitude = str(latitude)
longitude = str(longitude)
formatted_address= str(formatted_address)

# printing the output
print(data)
print("\nLatitude: {}\nLongitude {}\nFormatted Address:{}" .format(latitude, longitude, formatted_address))
