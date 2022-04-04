#Python program utilizing ipgelocation.io to extract geolocation
import requests

while True:
    try:
        ip_address = input(">_Enter IP Here: ")
        URL = "https://api.ipgeolocation.io/ipgeo?apiKey=INSERT_API_KEY_HERE!!!!&ip=" + ip_address

        r = requests.get(URL)
        response = r.json()

        org =response["organization"]
        country = response["country_name"]

        #details = print("[*] The IP " + str(ip_address) + " is owned by " + str(org) + " and located in " + str(country))
        print('Organization:' + str(org))
        print('Country:' + str(country))
        print('-----------------------------------------')
    except Exception as e:
        print("[?]\tpython error",e)

