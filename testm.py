import requests

url = "https://google-news13.p.rapidapi.com/latest"

querystring = {"lr": "en-US"}

headers = {
    "X-RapidAPI-Key": "68747a1260msh6a464c1447004ffp1ce22ejsna6365ab76ff1",
    "X-RapidAPI-Host": "google-news13.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract titles from the JSON response
    news_data = response.json()
    if 'data' in news_data:
        titles = [news['title'] for news in news_data['data']]
        for title in titles:
            print(title)
else:
    print("Failed to fetch news updates. Status code:", response.status_code)
