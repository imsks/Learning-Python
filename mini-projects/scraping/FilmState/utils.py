import json
from bs4 import BeautifulSoup
import requests

# Scrap Class
class ScrapeFilm:
    # Call the API
    def make_api(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        }

        return requests.get(url, headers=headers)

    # Check Response
    def check_response(self, response):
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            print("Error: ", response.status_code)
            return None

    # Build IMDB Suggestion URL
    def build_imdb_suggestion_url(self, search_query):
        # Encode the search query for safe inclusion in the URL
        encoded_query = requests.utils.quote(search_query)
        
        # Base URL for IMDB suggestion API
        base_url = "https://v3.sg.media-imdb.com/suggestion/x/"
        
        # Construct the final URL with encoded query
        url = base_url + encoded_query + ".json" + "?includeVideos=1"
        
        return url
    
    # Build Director URL
    def build_diretor_url(self, director_id):
        url = "https://www.imdb.com/name/" + director_id
        
        return url
    
    # Make IMDB Suggestion API
    def make_imdb_suggestion_api(self, search_query):
        url = self.build_imdb_suggestion_url(search_query)
        response = self.make_api(url)
        
        return self.check_response(response)
    
    # Parse IMDB Suggestion API Response
    def parse_imdb_suggestion_response(self, api_response, index = 0):
        if "d" not in api_response:
            return None  # Handle invalid response (missing "d" key)

        # Get the list of suggestions from the "d" key
        suggestions = api_response["d"]
        
        # Check if there are any suggestions
        if not suggestions:
            return None  # No suggestions found

        # Return the first suggestion (assuming the list is not empty)
        return suggestions[index]
    
    # Scrape Director Details
    def scrape_director_details(self, director_id):
        url = self.build_diretor_url(director_id)
        response = self.make_api(url)
        
        return response.content

    # Process Director Details
    def process_director_details(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')

        titles = []
        links = []
        covers = []
        ratings = []

        # # Product name
        all_films_element = soup.find('div', id='accordion-item-director-previous-projects')
        
        film_elements = all_films_element.find_all('li')

        for film_element in film_elements:
            cover = film_element.find('img')

            if cover:
                covers.append(cover.get('src'))

            link = film_element.find('a', class_='ipc-metadata-list-summary-item__t')

            if link:
                title  = link.text.strip()
                titles.append(title)

                anchor = link.get('href').split('?')[0]
                if anchor:
                    links.append(anchor)

                rating = film_element.find('span', class_='ipc-rating-star')

                if rating:
                    ratings.append(rating.text.strip())

        return {
            "titles": titles,
            "links": links,
            "covers": covers,
            "ratings": ratings
        }

       