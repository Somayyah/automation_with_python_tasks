#! /usr/bin/env python3

import os
import requests

reviews_dir = "/data/feedback/"
dict = { "title" : "" ,
         "name" : "" ,
         "date" : "" ,
         "feedback" : "" }

for review in os.listdir("/data/feedback"):
        if review.startswith("."):
                continue
        with open(reviews_dir + review, "r") as r:
                for element in ["title", "name", "date", "feedback"]:
                        dict[element] = r.readline()
                response = requests.post("http://34.123.27.80/feedback/", data=dict)
                print(response)
