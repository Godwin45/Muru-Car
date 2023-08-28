import requests

url = "https://subtitles-for-youtube.p.rapidapi.com/subtitles/%7BvideoId%7D.srt"

headers = {
	"X-RapidAPI-Key": "07c652e4bcmsh79d638ce38187d6p1c70eajsnf74aebad9585",
	"X-RapidAPI-Host": "subtitles-for-youtube.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())