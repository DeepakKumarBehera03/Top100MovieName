from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best"
                        "-movies-2/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')
title = soup.find_all(name="h3", class_ = "title")
top_100_movie = []
for moviename in title:
    movie = (moviename.getText())
    top_100_movie.append(movie)

top_100_movie.reverse()
for eachMovie in range(len(top_100_movie)):
    with open("MovieFile.txt", "a+") as f:
        f.writelines(f"{top_100_movie[eachMovie]}\n")

