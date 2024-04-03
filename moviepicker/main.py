import random
import requests
from bs4 import BeautifulSoup

# crawl IMDB Top 250 and randomly select a movie
URL = 'http://www.imdb.com/chart/top'

def main():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Update selectors based on the current structure of the IMDb page
    movietags = soup.select('td.titleColumn')
    inner_movietags = soup.select('td.titleColumn a')
    ratingtags = soup.select('td.imdbRating strong')

    titles = [tag.text for tag in inner_movietags]
    years = [tag.text.strip('()') for tag in movietags]
    ratings = [float(tag.text) for tag in ratingtags]

    n_movies = len(titles)

    while True:
        if n_movies == 0:
            print("No movies found. Exiting.")
            break
        
        idx = random.randrange(0, n_movies)
        
        print(f'{titles[idx]} ({years[idx]}), Rating: {ratings[idx]:.1f}')

        user_input = input('Do you want another movie (y/[n])? ').strip().lower()
        if not user_input or user_input == 'n':
            break

if __name__ == '__main__':
    main()
