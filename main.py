import requests
import re

params = {
  'access_key': '459e61878d08703f89f0a077e85fef87',
  'url': 'https://www.npr.org/sections/goatsandsoda/2020/08/21/787921856/photos-the-hidden-lives-of-teen-moms'
}

api_result = requests.get('http://api.scrapestack.com/scrape', params)
website_content = api_result.content

result = re.findall('<p>.+?</p>',website_content)
["<p>I'd like to find the string between the two paragraph tags.</p>", '<p>And also this string</p>']
print(result)

#print(website_content)
