import requests as req
import time
import pandas as pd

class NYTArticleScraper:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_articles(self, topic, num_pages=10):
        articles = []
        page = 1
        articleNum = 1
        for i in range(num_pages):
            url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?q={topic}&api-key={self.api_key}&page={i}'
            response = req.get(url).json()
            # Extract the necessary fields from the response.
            docs = response.get('response', {}).get('docs', [])

            print("\033[34m" + "Page " + str(page) + ": " + "\033[0m")
            page+=1
            for doc in docs:
                filtered_doc = {
                    'title': doc['headline']['main'],
                    'date': doc['pub_date'],
                    'abstract': doc['abstract'],
                    'section': doc['section_name'],
                    'paragraph': doc['lead_paragraph'],
                    'URL': doc['web_url']
                }
                cleanedDate = doc['pub_date']
                cleanedDate = cleanedDate[0:10]
                #print("\033[1m" + str(articleNum) + ": " + "\033[0m" + str(cleanedDate) + ", Title: " + filtered_doc['title'])
                print("\033[1m" + str(articleNum) + ": " + "\033[0m" + str(cleanedDate) + ", \033[32mTitle: " + "\033[0m" + filtered_doc['title'])

                articleNum+=1
                articles.append(filtered_doc)

            time.sleep(2) # Done to avoid hitting the API request limit. Optional,
        return articles

    def save_to_csv(self, topic, num_pages=10):
        output_file = 'Articles on ' + str(topic) + '.csv'
        articles = self.fetch_articles(topic, num_pages)
        df = pd.DataFrame(data=articles)
        df.to_csv(output_file, index=False)
        print(f'Data saved to "{output_file}"')

if __name__ == "__main__":
    API_KEY = 'API key should be just a mix of random characters' # Replace with your actual API key
    TOPIC = 'NATO Summit' #insert key word

    scraper = NYTArticleScraper(API_KEY)
    scraper.save_to_csv(TOPIC)
