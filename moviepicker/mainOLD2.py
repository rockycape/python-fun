import random
import requests
from bs4 import BeautifulSoup

# crawl IMDB Top 250 and randomly select a movie
URL = 'http://www.imdb.com/chart/top'

def main():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    movietags = soup.select('td.titleColumn')
    inner_movietags = soup.select('td.titleColumn a')
    ratingtags = soup.select('td.posterColumn span[name=ir]')

    print(f"Number of movietags: {len(movietags)}")
    print(f"Number of inner_movietags: {len(inner_movietags)}")
    print(f"Number of ratingtags: {len(ratingtags)}")

    def get_year(movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1] # last item 
        return year

    years = [get_year(tag) for tag in movietags]
    actors_list = [tag['title'] for tag in inner_movietags]  # access attribute 'title'
    titles = [tag.text for tag in inner_movietags]
    ratings = [float(tag['data-value']) for tag in ratingtags]  # access attribute 'data-value'

    print(f"Number of titles: {len(titles)}")
    print(f"Number of years: {len(years)}")
    print(f"Number of ratings: {len(ratings)}")

    n_movies = len(titles)

    while True:
        if n_movies == 0:
            print("No movies found. Exiting.")
            break
        
        idx = random.randrange(0, n_movies)
        
        print(f'{titles[idx]} {years[idx]}, Rating: {ratings[idx]:.1f}, Starring: {actors_list[idx]}')

        user_input = input('Do you want another movie (y/[n])? ').strip().lower()  # convert input to lowercase and remove leading/trailing whitespace
        if not user_input or user_input == 'n':
            break

if __name__ == '__main__':
    main()

