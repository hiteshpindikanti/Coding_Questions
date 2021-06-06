import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor


def get_weather(city_name: str):
    API_KEY = '27eb3c794abc8cd023ae76bdc090b757'
    API_URL = 'http://api.openweathermap.org/data/2.5/weather?'

    complete_url = API_URL + "appid=" + API_KEY + "&q=" + city_name

    response = requests.get(complete_url)

    offensive_classifier_response = requests.post(url=self.OFFENSIVESPEECH_API_URL, json={'text': responses}, timeout=1)
    json_sample = """{"text": ["I Love You", "I hate you"]}"""
    URL = "http://cobot-LoadB-1LKDN0F11E0ZO-1148271128.us-east-1.elb.amazonaws.com"
    x = response.json()
    print(x)


if __name__ == "__main__":

    start_time = time.time()
    with ThreadPoolExecutor() as executor:
        # Option 1
        for _ in range(10):
            executor.submit(get_weather, 'Los Angeles')

    end_time = time.time()
    print('time taken: {}'.format(end_time - start_time))

    start_time = time.time()
    with ThreadPoolExecutor() as executor:
        # Option 2
        executor.map(get_weather, ['Los Angeles']*10)

    end_time = time.time()
    print('time taken: {}'.format(end_time - start_time))



