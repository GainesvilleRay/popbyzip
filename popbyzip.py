#manipulate dataframes in python
import pandas as pd

#make API calls with python
import requests

#allows us to store results of API call cleanly
import json

#gets access to my Census api key
#import apiKey.py

#get list of zipcodes I want to tally separated by commas
myZips = open('myZips.txt', 'r').readlines()
myZips = [z.replace('\n', '') for z in myZips]
myZips = ','.join(myZips)

#put your census API key here
myKey = "e4f0736a36ab40486c0c550aa714ba41d58db5d8"

#construct the API call we will use
baseURL = "https://api.census.gov/data/2017/acs/acs5?key="
addURL = "&get=B01003_001E&for=zip%20code%20tabulation%20area:"
calledAPI = f"{baseURL}{myKey}{addURL}{myZips}"

#call the API and collect the response
response = requests.get(calledAPI)

#load the response into a JSON, ignoring the first element which is just field labels
formattedResponse = json.loads(response.text)[1:]

#flip the order of the response from [population, zipcode] -> [zipcode, population]
formattedResponse = [item[::-1] for item in formattedResponse]

#store the response in a dataframe
myZipPopulations = pd.DataFrame(columns=['zipcode', 'population'], data=formattedResponse)

#save that dataframe to a CSV spreadsheet
myZipPopulations.to_csv('myZipPopulations.csv', index=False)
