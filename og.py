import requests
import re

params = {
  'access_key': '459e61878d08703f89f0a077e85fef87',
  'url': 'https://apnews.com/86d91a180f6e5351872a1125735be8da'
}

api_result = requests.get('http://api.scrapestack.com/scrape', params)
website_content = api_result.content

print(website_content)
