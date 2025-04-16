import requests
import json
import time
import os
from dotenv import load_dotenv

load_dotenv()

URL_BASE = "https://api.weatherapi.com/v1/"
API_KEY = os.getenv("WEATHERAPI_KEY")
# print(API_KEY)

# Current weather
# current
# Forecast
# forecast
# Search or Autocomplete
# search
# History
# history
# Time Zone
# timezone
# Sports
# sports
# Astronomy
# astronomy
# IP Lookup
# ip

# request type
# json or xml

# air quality
# aqi = "yes" or "no"

# date = "yyyy-MM-dd"

# location
# q
# Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name
#
#
#
def current(req_format:str="json", location:str="Lisboa", aqi:str="yes")->dict:
	"""
    Get the current weather for the location provided
	req_format: The output format
	location: The location to get the weather for
	aqi: If the AQI (Air Quality Index) should be returned or not
    """
		
	req_type = "current"
	url = "{}{}.{}".format(URL_BASE, req_type, req_format)

	params = dict()
	params["key"] = API_KEY
	params["q"] = location
	params["aqi"] = aqi

	req = requests.get(url, params=params)

	resp = req.json()
	# print(json.dumps(resp, indent=4))
	return resp
#
#
#
def forecast(req_format="json", location="Lisboa", aqi="yes", days=1, alerts="yes"):
	req_type = "forecast"
	url = "{}{}.{}".format(URL_BASE, req_type, req_format)

	params = dict()
	params["key"] = API_KEY
	params["q"] = location
	params["aqi"] = aqi
	params["days"] = days
	params["alerts"] = alerts

	req = requests.get(url, params=params)

	resp = req.json()
	# print(json.dumps(resp, indent=4))
	return resp
#
#
#
def history(req_format="json", location="Lisbon", date=time.strftime("%Y-%m-%d")):
	req_type = "history"
	url = "{}{}.{}".format(URL_BASE, req_type, req_format)

	params = dict()
	params["key"] = API_KEY
	params["q"] = location
	params["dt"] = date

	req = requests.get(url, params=params)

	resp = req.json()
	# print(json.dumps(resp, indent=4))
	return resp
#
#
#
def timezone(req_format="json", location="Lisbon"):
	req_type = "timezone"
	url = "{}{}.{}".format(URL_BASE, req_type, req_format)

	params = dict()
	params["key"] = API_KEY
	params["q"] = location

	req = requests.get(url, params=params)

	resp = req.json()
	# print(json.dumps(resp, indent=4))
	return resp
#
#
#
def sports(req_format="json", location="Lisbon"):
	req_type = "sports"
	url = "{}{}.{}".format(URL_BASE, req_type, req_format)

	params = dict()
	params["key"] = API_KEY
	params["q"] = location

	req = requests.get(url, params=params)

	resp = req.json()
	# print(json.dumps(resp, indent=4))
	return resp
#
#
#
def astronomy(req_format="json", location="Lisbon", date=time.strftime("%Y-%m-%d")):
	req_type = "astronomy"
	url = "{}{}.{}".format(URL_BASE, req_type, req_format)

	params = dict()
	params["key"] = API_KEY
	params["q"] = location
	params["dt"] = date

	req = requests.get(url, params=params)

	resp = req.json()
	# print(json.dumps(resp, indent=4))
	return resp
#
#
#
def ip(req_format="json", location="Lisbon"):
	req_type = "ip"
	url = "{}{}.{}".format(URL_BASE, req_type, req_format)

	params = dict()
	params["key"] = API_KEY
	params["q"] = location

	req = requests.get(url, params=params)

	resp = req.json()
	# print(json.dumps(resp, indent=4))
	return resp
#
#
#
if __name__ == "__main__":
	location = "Sardinia"

	date = time.strftime("%Y-%m-%d")
	w = current(location=location)
	print(json.dumps(w, indent=4))

	w = forecast(location=location)
	# print(json.dumps(w, indent=4))

	# w = history(location="Lisbon", date="2020-05-26")
	# w = timezone(location="Lisbon")
	# w = sports()
	# w = astronomy(location="Lisbon")
	# w = ip(location="31.22.151.193")
	# print(json.dumps(w, indent=4))
#
#
#