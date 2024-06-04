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
    
    # Build celeb URL
    def build_celeb_url(self, celeb_id):
        url = "https://www.imdb.com/name/" + celeb_id
        
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
    
    # Scrape celeb Details
    def scrape_celeb_details(self, celeb_id):
        url = self.build_celeb_url(celeb_id)
        response = self.make_api(url)
        
        return response.content
    
    # Get Celeb Filmography
    def get_celeb_filmography(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        
        all_writer_elements = soup.find('div', id='accordion-item-writer-previous-projects')
        all_producer_elements = soup.find('div', id='accordion-item-producer-previous-projects')
        all_director_elements = soup.find('div', id='accordion-item-director-previous-projects')

        writer_films = self.process_film_details(all_writer_elements)
        producer_films = self.process_film_details(all_producer_elements)
        director_films = self.process_film_details(all_director_elements)

        return {
            "writer": writer_films,
            "producer": producer_films,
            "director": director_films
        }

    # Process Film Details
    def process_film_details(self, all_films_element):
        if not all_films_element:
            return {
                "titles": [],
                "links": [],
                "covers": [],
                "ratings": []
            }

        titles = []
        links = []
        covers = []
        ratings = []

        film_elements = all_films_element.find_all('li')

        for film_element in film_elements:
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
                else:
                    ratings.append("") 

                cover = film_element.find('img', class_='ipc-image')

                if cover:
                    covers.append(cover.get('src'))
                else:
                    covers.append("") 

        # Find the maximum length of any list
        max_length = max(len(lst) for lst in [titles, links, covers, ratings])

        # Pad shorter lists with empty strings
        for lst in [titles, links, covers, ratings]:
            lst.extend([""] * (max_length - len(lst)))

        return {
            "titles": titles,
            "links": links,
            "covers": covers,
            "ratings": ratings
        }


       