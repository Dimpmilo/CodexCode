

from sys import argv
import requests 

API_KEY = 'key(private key here)' 
#api key for newsapi.org

URL = ('https://newsapi.org/v2/top-headlines?')

def get_articles_by_category(category):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": "us",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def get_articles_by_query(query):
    query_parameters = {
        "q": query,
        "sortBy": "top",
        "country": "us",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def _get_articles(params):
        response = requests.get(URL, params=params)

        articles = response.json()['articles']
        results = []
        
        for article in articles:
            results.append({"title": article["tittle"], "url": article["url"]})
            
        for result in results:
            print(result['title'])
            print(result['url'])
            print('')

def get_sources_by_category(category):
    query_parameters = {
         "source": category,
         "sortBy": "top",
         "country": "us",
         "apiKey": API_KEY
    }

argv[0] = input(str("Insert Category type: "))

if __name__ == "__main__":
     print(f"Getting news for {argv[0]}...\n")
     get_articles_by_category (argv[0])
     print(f"successfully retrieved top {argv[0]} headlines")
     
    
     
    # get_articles_by_query("")
    #print_sources_by_category("technology")

