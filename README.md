# Porthole

Read comfortably, analyze skeptically | An article viewer and annotator written for the HFTP Hackathon's "Political" track

Porthole will eventually be deployed on the web for use as an article parser for easy viewing, (and/or to evade adblocker detectors) as well as for annotating for bias in the form of subjectivity, opinion, and bullshit. It will then run calculations on the ratio of bias detected out of the sum total of article content, and display this data both with an assigned score and a visual. It will also include available data about the article's author, scraped from elsewhere on the web for background-checking. Currently Porthole must be run from the command-line, and it minimally annotates for the three mentioned categories.

You may wonder why I didn't use a cli app such as html2text to start from. Unfortunately it is hard to pick out consistent symbols to determine the bounds of the actual article content from that of the entire page, whereas html tags supply patterns that can be isolated programmatically. Considering how I only want to print the actual article content, and that I need to scan the content for patterns and phrases, it may be better curated in this format.

Requires insertion of a key from the Scrapestack API, (until deployed for web/server) as well as a desired URL to an article.  

Only tested with articles from NPR and Reuters so far.
