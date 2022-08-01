#!/usr/bin/env python3

# coding=utf-8
import os
import re
import sys
import json
import time
import random
import requests
import threading
from urllib3 import *
from bs4 import BeautifulSoup

resp = requests.get('https://gxhy1688.com/market/web/detailIndex?marketCode=gz&code=646342979',
			headers={"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML], like Gecko) Chrome/35.0.1916.153 Safari/537.36"},
			verify=False
		)
soup = BeautifulSoup(resp.text, 'lxml')
print(soup)