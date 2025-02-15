import requests
import random

def fetch_random_jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
    response = requests.get(url)
    data = response.json()

    if "success" in data and data["success"] and "data" in data:
        user_data = data["data"]["data"]
        jokes = []
        for datas in user_data:
            jokes.append(datas["content"])
        return random.choice(jokes)
    else: 
        raise Exception("Failed to Fetch Data")
    
def main():
    try:
        jokes = fetch_random_jokes()
        print("\n")
        print("*"*20)
        print(f"{jokes}")
        print("*"*20)
        print("\n")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()