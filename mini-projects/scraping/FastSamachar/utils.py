from bs4 import BeautifulSoup
import requests

# Scrap Class
class ScrapNews:
    # Call the API
    def make_api(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        }

        return requests.get(url, headers=headers)

    # Check Response
    def check_response(self, response):
        if response.status_code == 200:
            return response.content
        else:
            print("Error: ", response.status_code)
            return None

    # Scrape News
    def scrape_sources(self, html_content, source):
        if source == 'TOI':
            toi_news = self.scrape_TOI(html_content)

        return [toi_news]

    # Scrape TOI
    def scrape_TOI(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')

        # News name
        name_elements = soup.find_all('div', class_='col_l_6')

        titles = []
        links = []
        covers = []

        for element in name_elements:
            # Find the figcaption element within the current 'col_l_6' element
            figcaption_element = element.find('figcaption')
            # Extract caption text if the figcaption element exists
            if figcaption_element:
                title_text = figcaption_element.text.strip()
                titles.append(title_text)

                # Find the anchor tag (a element) within the 'yCs_c' class div
                link_element = element.find('a') 
                # Extract the 'href' attribute from the anchor tag if it exists
                if link_element:
                    link = link_element.get('href')
                    links.append(link)
                else:
                    links.append("")

                # Find the img tag (img element)
                cover_element = element.find('img') 
                # Extract the 'src' attribute from the img tag if it exists
                if cover_element:
                    cover = cover_element.get('data-src')
                    covers.append(cover)
                else:
                    covers.append("")

        return {
            'source': 'TOI',
            'titles': titles,
            'links': links,
            'covers': covers
        }
