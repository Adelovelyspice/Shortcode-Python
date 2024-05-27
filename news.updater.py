import requests
from bs4 import BeautifulSoup

def fetch_news_updates(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the headlines (you may need to adjust the class or tag based on the website structure)
        headlines = soup.find_all('h3', class_='gs-c-promo-heading__title')
        
        # Print the headlines
        print("Latest News Headlines:")
        for idx, headline in enumerate(headlines, start=1):
            print(f"{idx}. {headline.get_text()}")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Example usage
url = "https://www.bbc.com/news"  # Replace with the URL of the news website you want to scrape
fetch_news_updates(url)
