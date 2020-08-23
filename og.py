import requests
import re

params = {
  'access_key': '459e61878d08703f89f0a077e85fef87',
  'url': 'https://www.cnn.com/2020/08/22/politics/what-matters-august-21/index.html'
}

api_result = requests.get('http://api.scrapestack.com/scrape', params)
website_content = api_result.content

print(website_content)
