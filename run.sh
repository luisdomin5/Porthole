urlF="url.txt"

story="story.txt"

while read line
do
	url=$line
done < $urlF 

http $url > story.txt; python main.py
