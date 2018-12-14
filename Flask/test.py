# -*- coding: utf-8 -*-
import requests

#print(requests.get('http://127.0.0.1:5555/getbase'))
print(requests.get('http://journal-flask.herokuapp.com/getbase').text)
