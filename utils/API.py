import requests
import logging

url = "https://youtube-music1.p.rapidapi.com/v2/search"

headers = {
	"X-RapidAPI-Key": "33e7460782msh1b9bcc2a0f5e680p1d5772jsn5e0bc9a6df77",
	"X-RapidAPI-Host": "youtube-music1.p.rapidapi.com"
}


async def audio_download(youtube_url):
    
	response = requests.request("POST", url, headers=headers)
	
	return response.json()['response']['youtube_url']