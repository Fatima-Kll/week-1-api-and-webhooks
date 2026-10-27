
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        json_response = response.json()

        print("Title:", json_response["title"])
        print("Body:", json_response["body"])
    else:
        print("Request failed. Status code:", response.status_code)

except requests.exceptions.RequestException as error:
    print("A request error occurred:", error)
