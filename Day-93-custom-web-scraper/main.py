import requests
from bs4 import BeautifulSoup

def scrape_arr_music_data():
    url = "https://en.wikipedia.org/wiki/A._R._Rahman_discography"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        # Need to adjust the following selectors based on the webpage structure
        albums_section = soup.find("span", {"id": "Studio_albums"}).find_parent("h2")
        albums_list = albums_section.find_next("ul").find_all("li")

        arr_music_data = []

        for album in albums_list:
            album_title = album.get_text(strip=True)
            arr_music_data.append(album_title)

        return arr_music_data
    else:
        print("Failed to fetch data")

if __name__ == "__main__":
    arr_music_data = scrape_arr_music_data()
    for album in arr_music_data:
        print(album)
