from __future__ import print_function
import os
from flask import Flask, request, render_template, session, redirect, flash, url_for
from util import sample
from urllib.parse import quote

import argparse
import json
import pprint
import requests
import sys
import urllib


app=Flask(__name__)

@app.route('/')
def index():
    ret = sample.query_api("turkish","New York")
    y = json.loads(ret)
    t = list(y.values())
    # amount = y.slice(-1);
    # amount = sorted(y.keys())[-4]
    # amount = sorted(y.keys())
    amount = t[-1]
    # for p in range(int(amount)):
    #     lats[p] = ""
    #     longs[p] = ""
    lats =["" for p in range(int(amount))]
    longs =["" for p in range(int(amount))]
    for a in range(int(amount)):
        lats[a] = y[str(a)]["coordinates"]['latitude']
        longs[a] = y[str(a)]["coordinates"]['longitude']
    a = y['2']["coordinates"]['latitude']
    b = y['2']['coordinates']['longitude']

    return render_template('index.html',amount = amount,ret = ret, a= a, b= b, lats= lats,longs=longs)
    # return render_template('index.html', ret = ret)

@app.route('/search', methods=["GET"])
def search():
    '''If search query is for books, then redirects to book_search.
    If search query is for books, then redirects to movie_search.'''
    place = request.args.get("h")
    query =request.args.get("query").replace(" " , "+")
    if(query==""):
        return redirect(url_for('index'))
    # if(type == "Books"):
    #     return redirect(url_for('book_search', query=query))
    # else:
    #     return redirect(url_for('movie_search', query=query))


if __name__ == '__main__':
    app.debug = True  # Set to `False` before release
    app.run()
