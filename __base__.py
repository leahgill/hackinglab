import http.client as http_client
import logging

import requests

log = logging.getLogger(__name__)


def get_ip_address(interface="tun0"):
    import os
    mine = os.popen(f'ifconfig {interface} | grep "inet 10."')
    ip = mine.read()[13:25]
    if not ip:
        raise Exception("Please turn VPN on!")
    return ip.replace(" ", "")


def extract_user_info(response: requests.Response) -> str:
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    script = soup.find("script")
    lines = str(script).split("\n")
    user_info = []
    for line in lines:
        if line.replace(" ", "").startswith("document"):
            user_info.append(line)
    return "\n".join(user_info)


def setup_log(verbose=True):
    if verbose:
        http_client.HTTPConnection.debuglevel = 1
        logging.basicConfig(level=logging.DEBUG)
        logging.basicConfig()
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = False


def encode_url(string):
    import urllib.parse
    return urllib.parse.quote(string)


def decode_url(string):
    import urllib.parse
    return urllib.parse.unquote(string)


if __name__ == '__main__':
    print(
        decode_url("https%3A%2F%2Fglocken.hacking-lab.com%2F12001%2Furl_case4%2Furl4%2Fcontroller%3Faction%3Dprofile%26AValue%3DBuqvV44Y8xtGpY5CWOpTBg%3D%3D")
    )
