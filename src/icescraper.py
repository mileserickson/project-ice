'''Scrape ice thickness data for project-ice.'''

import requests
from bs4 import BeautifulSoup


def fetch_soup(url):
    r"""
    Retrieve the document at url and return a BeautifulSoup object

    Parameters
    ----------
    url : string
        The URL of the document to retrieve.

    Returns
    -------
    soup : BeautifulSoup
        The text of the retrieved document, with all HTML tags removed.


    Example
    -------
    >>> s = fetch_soup('http://www.nenanaakiceclassic.com/2015%20Ice.htm')
    >>> s.get_text().split('\n')[6]
    u'2015 Ice Measurement '

    """

    return BeautifulSoup(requests.get(url).text, 'lxml')


def get_ice_urls(soup):
    r"""
    Return all ice observations URLs in soup.

    Example:
    >>> ice_soup = fetch_soup('http://www.nenanaakiceclassic.com/ice.htm')
    >>> urls = get_ice_urls(ice_soup)
    >>> urls[-1:]
    ['1989.htm']
    """

    all_urls = [link.get('href') for link in soup.find_all('a')]
    ice_urls = [url for url in all_urls if url[:2] in ('19', '20')]

    return ice_urls


def get_ice_observations(soup):
    pass
