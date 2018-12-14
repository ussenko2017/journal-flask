# -*- coding: utf-8 -*-
from Flask.Flask import myFunc
import json
with open("/media/doc/System x641/Users/DoctorWho-2/source/repos/Flask/Flask/bd.json", "r", encoding="utf-8") as opened_file:
    base = json.load(opened_file)
for i in base['base'][0]['balls']:
    print(i.values[0])