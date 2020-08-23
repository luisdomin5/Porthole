import requests
import re

params = {
  'access_key': '459e61878d08703f89f0a077e85fef87',
  'url': 'https://www.npr.org/2020/08/22/905099950/the-worst-is-not-behind-us-california-continues-to-burn'
}

api_result = requests.get('http://api.scrapestack.com/scrape', params)
website_content = api_result.content

print(website_content)
