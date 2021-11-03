import requests, os


api_key = os.environ['API_IBM']

headers = {'Content-Type': 'application/json',}

params = (('version', '2018-05-01'),)

url = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/cfddb54c-e4b3-4ea4-8e6f-a249b42be0d7/v3/translate'


def get(text:str, lg:str) -> str:
    result = ""
    if text:
        lg_from = 'ru' if lg == 'en' else 'en'
        data = f'{{"text": "{text}", "model_id":"{lg_from}-{lg}"}}'
        response = requests.post(url, headers=headers, params=params, data=data, auth=('apikey', api_key))
        try:
            result = response.json()['translations'][0]['translation']
        except:
            result = response.text
    return {"source": text, "result": result}

if __name__ == "__main__":
    print("Test: (HI)", get("hi","ru"))