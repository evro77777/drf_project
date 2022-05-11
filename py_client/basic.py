import requests

endpoint = 'http://127.0.0.1:8000/api/'
print(f'endpoint={endpoint}')
get_response = requests.post(endpoint, json={"title": "hello_world",
                                             "content": "conte_hello",
                                             "tratata":"12311234"})
print(get_response.json())

