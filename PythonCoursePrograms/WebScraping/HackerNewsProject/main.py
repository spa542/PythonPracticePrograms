# Hacker News Project
import requests # Allows the ability for grabbing data
from bs4 import BeautifulSoup # Use the data thats gathered and scrape it
import pprint # Used for pretty printing

def create_custom_hn(links, subtext):
    '''
    Takes in a list of links and a list of subtexts returned from the API
    '''
    hn = []
    for index, item in enumerate(links): # We use enumerate because we need the index 
        title = item.getText()          # so that we can iterate over two different lists
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

def sort_stories_by_votes(hnlist):
    '''
    Will receive a hacker news list and then will sort the list by points
    '''
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def main():
    res = requests.get('https://news.ycombinator.com/news')
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.storylink') # Using css selectors
    subtext = soup.select('.subtext')

    pprint.pprint(create_custom_hn(links, subtext))

if __name__ == '__main__':
    main()
