import requests  # allows us to download initially that html
from bs4 import BeautifulSoup
# BeautifulSoup allows us to use the html and grab different data,
# allows us to use that data that we have gathered to do whether we want
import pprint

# if you want to do for more pages,
# just duplicate the below and change the name of the variables but dun need to change the function
res = requests.get('https://news.ycombinator.com/news')
# the function is like a web browser that we are using without actual browse
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
# the string that contain all the data we want
# print(soup.find_all('div'))
links = soup.select('.storylink') # .(class)
subtext = soup.select('.subtext') # dun use .score becoz some links dun have votes
# css selector: use to target some html element


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText() # index of each link
        # #using getText() becoz in the class(storylink) the title is the only text
        href = links[idx].get('href', None) # href refer to the link
        vote = subtext[idx].select('.score') # we use the index to access the subtext
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(links, subtext))
