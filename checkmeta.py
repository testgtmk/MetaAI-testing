import requests
import re
from bs4 import BeautifulSoup

def get_youtube_links_from_playlist(playlist_url):
    # Headers to mimic a real browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    
    # Send a GET request to the playlist page
    response = requests.get(playlist_url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to retrieve page. Status code: {response.status_code}")
        return []
    
    pattern = r'{"url":"(/watch\?v=[^"]+)"'
    #pattern = r"/watch\?v=([^&]+)"
    matches = re.findall(pattern, response.text)
    #matches = match = re.search(r"v=([^&]+)", matches)
    #print(matches)
    return matches

# Example usage
geog_url = "https://www.youtube.com/playlist?list=PLHPDRwuGud4VhvaZsxpdcwmKcsnH4XKaB"
playlist_url = "https://www.youtube.com/playlist?list=PLVOgwA_DiGzr4qkdqR78JnRCzEuq-jKnC"
links = get_youtube_links_from_playlist(geog_url)

prefix = "https://www.youtube.com"
# Output the extracted links
for link in links:
    decoded_url = link.replace(r'\u0026', '&')
    match = re.search(r"/watch\?v=([^&]+)", decoded_url)
    vid = match.group(0)
    #print(match.group(0),match.group(1))
    print(prefix+vid)
