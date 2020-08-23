import requests
import re

params = {
  'access_key': '459e61878d08703f89f0a077e85fef87',
  'url': 'https://www.npr.org/2020/08/22/905099950/the-worst-is-not-behind-us-california-continues-to-burn'
}

api_result = requests.get('http://api.scrapestack.com/scrape', params)
website_content = api_result.content

result = re.findall('<p>.+?</p>',website_content)
test = ""
test = listToStr = ' '.join([str(elem) for elem in result])
if (len(test) < 500):
    result = re.findall('</cite>.+?\.</div></div>',website_content)
test = listToStr = ' '.join([str(elem) for elem in result])
test = re.sub('<a href=.+?<em>', '', test)
test = re.sub('data-cfemail=.+?<em>', '', test)
test = re.sub('<div class=".+?\"', '', test)
test = re.sub('data-ad-text=.+?>', '', test)
test = re.sub('<div data.+?>', '', test)
test = re.sub('<ul class=.+?>', '', test)
test = re.sub('"https.+?"', '', test)
test = re.sub('//.+?"', '', test)
test = re.sub('data-src.+?"', '', test)
test = re.sub('data-.+?/script', '', test)
test = re.sub('data-.+?"', '', test)
test = re.sub('class=".+?"', '', test)
test = re.sub('<div id=".+?"', '', test)
test = re.sub('<div.+?alt=', '', test)
test = re.sub('click".+?"', '', test)
test = re.sub('id=.+?>', '', test)
test = test.replace("<p>", "\n")
test = test.replace("</p>", "\n")
test = test.replace("    ", "\n")
test = test.replace("<h1>", "\n")
test = test.replace("<h2>", "\n")
test = test.replace("<h3>", "\n")
test = test.replace("</h1>", "")
test = test.replace("</h2>", "")
test = test.replace("</h3>", "")
test = test.replace("<strong>", "    ")
test = test.replace("</strong>", "")
test = test.replace("</ul> >", "")
test = test.replace("<span class=", "")
test = test.replace("<em>", "")
test = test.replace("</em>", "")
test = test.replace("</a>", "")
test = test.replace("</ul", "")
test = test.replace("&ldquo;", "\"")
test = test.replace("&rdquo;", "\"")
test = test.replace("<a href=", "")
test = test.replace("target=", "")
test = test.replace("</cite>", "")
test = test.replace("</div> >", "")
test = test.replace("</div>", "")
test = test.replace("</span>=", "")
test = test.replace("<span>=", "")
test = test.replace("</span>", "")
test = test.replace("<span>", "")
test = test.replace("\"_blank\"", "")
test = test.replace("\">", "\"")
test = test.replace(">", "")
test = test.replace("\"\"", "")




print test
    
#print(website_content)
