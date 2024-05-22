from bs4 import BeautifulSoup
import pandas as pd
import requests

# Call the API
def make_api(url):
    url = "https://www.amazon.in/dp/B0CX59H5W7"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    return requests.get(url, headers=headers)

# Check Response
def check_response(response):
    if response.status_code == 200:
        return response.content
    else:
        print("Error: ", response.status_code)
        return None

# Scrap Produt Details
def scrape_product_details(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Product name
    name_element = soup.find('span', id='productTitle')
    if name_element:
        name = name_element.text.strip()
    else:
        name = "Product name not found"
    
    # Product price
    price_element = soup.find('span', class_='a-price-whole')
    if price_element:
        price = price_element.text.strip()[:-1]
    else:
        price = "Product price not found"
    
    return {
        "name": name,
        "price": price
    }
