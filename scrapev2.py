import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_nyt_saved_articles():
    # Replace 'YOUR_NYT_ACCOUNT_PAGE_URL' with the URL of your saved articles page on NYT.
    url = 'https://www.nytimes.com/saved'

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Replace 'title_class' and 'url_class' with the actual class names of the HTML elements
        # that contain the article titles and URLs respectively.
        titles = soup.find_all('h3', class_='title_class')
        urls = soup.find_all('a', class_='url_class')

        article_data = []
        for title, url in zip(titles, urls):
            article_data.append({
                'Title': title.text.strip(),
                'URL': url['href']
            })

        return article_data

    else:
        print("Error: Unable to fetch the page.")
        return None


if __name__ == "__main__":
    articles = scrape_nyt_saved_articles()

    if articles:
        df = pd.DataFrame(articles)
        df.to_csv('NYT_Saved_Articles.csv', index=False)
        print("Data saved to NYT_Saved_Articles.csv")
