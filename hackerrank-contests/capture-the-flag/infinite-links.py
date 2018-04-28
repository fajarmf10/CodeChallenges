from pyquery import PyQuery
import requests

url_tracker = {}
secret_phrases = []
base_url = "https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/"
start_link = "qds.html"


def extract(link):
    url = base_url + link
    pq = PyQuery(url)

    fonts = pq('body').find('font')

    if fonts:
        global secret_phrases
        secret_phrases.append(fonts.text().split(': '))

    return pq('body').find('a')


def run(cur_link):
    global url_tracker
    url_tracker[cur_link] = True
    extracted_links = extract(cur_link)

    for linkel in extracted_links:
        link = linkel.attrib['href']
        if url_tracker.get(link, False) == True:
            continue
        url_tracker[link] = True
        run(link)
    return


if __name__ == "__main__":
    print('Processing....')
    run(start_link)
    secret_phrases.sort()
    for list in secret_phrases:
        print(list[1])