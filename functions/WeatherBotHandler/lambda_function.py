import os
import json
import logging
import requests 

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

CLOUDY = "Clouds"
CLEAR = "Clear"
RAIN = "Rain"
SNOW = "Snow"

def lambda_handler(event, context):
    city_name = event["currentIntent"]["slots"]["City"]
    
    try:
        req_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            'q':city_name,
            'appid':os.environ["WEATHER_API"]
        }
        response = requests.get(req_url, params).json()
        if "weather" not in response:
            return {
            "sessionAttributes": event["sessionAttributes"],
            "dialogAction":{
                "type":"Close",
                "fulfillmentState":"Fulfilled",
                "message":{
                    "contentType":"PlainText",
                    "content":"Sorry Couldnot find the requested place"
                }
            }
        }

        weather_report = ""
        for weather_status in response['weather']:
            status = weather_status['main']
            if status == CLOUDY:
                if response["clouds"]:
                    extra_report_cloud = "There is possibility of rain." if response["clouds"]["all"] > 40 else ""
                weather_report+="The sky is cloudy.{0} ".format(extra_report_cloud)
            elif status == RAIN:
                if response["rain"]:
                    extra_report_rain = "heavily" if response["rain"]['1h'] > 4 else "mildly."
                weather_report+="It is raining {0}. ".format(extra_report_rain)
            elif status == SNOW:
                weather_report+='It is snowing.'
        
        min_temp_cs = response['main']['temp_min'] - 273.15
        max_temp_cs = response['main']['temp_max'] - 273.15
        if min_temp_cs == max_temp_cs:
            weather_report+= "Current temperature is {0} degree celsius".format(min_temp_cs)
        else:
            weather_report+="The minimum temperature is about {0} and maximum temperature is about {1} degree celsius".format(min_temp_cs,max_temp_cs)
        
        return {
            "sessionAttributes": event["sessionAttributes"],
            "dialogAction":{
                "type":"Close",
                "fulfillmentState":"Fulfilled",
                "message":{
                    "contentType":"PlainText",
                    "content":weather_report
                }
            }
        }
    except requests.exceptions.Timeout as e:
        logger.debug("Request Time Out") 
    except requests.exceptions.TooManyRedirects as e:
        logger.debug("Bad request url")
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    

       