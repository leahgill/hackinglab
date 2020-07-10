__problem__ = \
"""
TLSs are not used everywhere. Payloads from clients are secured. But transmission of many other files are not secured, which
btw. also contains cookie. 
"""

__attack__ = \
"""
Passive attack with wireshark.
"""

__mitigation__ = \
"""
Consistent usage of TLS.
"""

import logging

import requests

from __base__ import setup_log

log = logging.getLogger(__name__)


def find_unsecured_paths(response):
    import bs4
    url = response.url
    soup = bs4.BeautifulSoup(response.text, features="lxml")

    def find_by(tag, attribute):
        for link in soup.find_all(tag):
            if link.has_attr(attribute):
                href = link[attribute]
                if not href.startswith("http"):
                    href = url + href
                if not href.startswith("https"):
                    print("Unsecured links detected: ", href)
    find_by('a', 'href')
    find_by('link', 'href')
    find_by('script', 'src')


def secured_login():
    with requests.session() as session:
        session.verify = False
        response = session.get(
            "http://glocken.hacking-lab.com/12001/cookie_case2/cookie2/controller?action=showpage&page=navigate")
        find_unsecured_paths(response)
        session.post("https://glocken.hacking-lab.com/12001/cookie_case2/auth_cookie2/login",
                     data={
                         'username': 'hacker10',
                         'password': "compass",
                         'action': 'login',
                         'originalURL': 'https://glocken.hacking-lab.com/12001/cookie_case2/cookie2/controller?action=profile&pid=1',
                         'send': 'Login',
                     })
        find_unsecured_paths(response)
        response = session.get(
            "https://glocken.hacking-lab.com/12001/cookie_case2/cookie2/controller?action=profile&pid=1")
        find_unsecured_paths(response)
        response = session.get(
            "https://glocken.hacking-lab.com/12001/cookie_case2/cookie2/controller?action=pay")
        find_unsecured_paths(response)
        response = session.get(
            "http://glocken.hacking-lab.com/12001/cookie_case2/cookie2/controller?action=showpage&page=shoppingcart")
        find_unsecured_paths(response)


if __name__ == '__main__':
    setup_log(False)
    secured_login()
