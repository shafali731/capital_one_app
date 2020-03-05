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
def start():
    return render_template('new_welcome.html')
@app.route('/result/<term>/<place>')
def welcome(term,place):
    ret = sample.query_api(term,place)
    y = json.loads(ret)
    t = list(y.values())
    amount = t[-1]
    lats = ["" for p in range(int(amount))]
    longs = ["" for p in range(int(amount))]
    resturs_urls = ["" for x in range(int(amount))]
    resturs_names = ["" for x in range(int(amount))]
    # locations = []
    # print(locations)
    for k in range(int(amount)):
        lats[k]= y[str(k)]["coordinates"]["latitude"]
        longs[k] = y[str(k)]["coordinates"]["longitude"]
        # resturs[k]= y[str(k)]['name']
        # print(locations[k])
    # print(t[0])
    amount_double = (int(amount))
    u =0
    while(u <amount_double):
        resturs_urls[u]= y[str(u)]['url']
        u+=1
    # print("u:  ")
    # print(u)
    # print(amount_double*2)
    for k in range(int(amount)):
        resturs_names[k]= y[str(k)]['name']
    # while(u<(amount_double*2)):
    #     resturs[u]= y[str(u)]['name']
    #     u+=1
        # resturs[u+1]=y[str(u)]
        # u+=2
    # print(locations)
    # print(lats)
    # print(y)
    # print(y["1"]['name'])
    # print(resturs)
    # print(amount)
    return render_template('index.html', resturs_urls=resturs_urls, resturs_names=resturs_names,ret =y, lats=lats, longs= longs, amount = int(amount))
@app.route('/res/<term>/<place>')
def search_result(term,place):
    ret = sample.query_api(term, place)
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
# def search_result():
#     ret = sample.query_api("turkish","New York")
#     y = json.loads(ret)
#     t = list(y.values())
#     # amount = y.slice(-1);
#     # amount = sorted(y.keys())[-4]
#     # amount = sorted(y.keys())
#     amount = t[-1]
#     # for p in range(int(amount)):
#     #     lats[p] = ""
#     #     longs[p] = ""
#     lats =["" for p in range(int(amount))]
#     longs =["" for p in range(int(amount))]
#     for a in range(int(amount)):
#         lats[a] = y[str(a)]["coordinates"]['latitude']
#         longs[a] = y[str(a)]["coordinates"]['longitude']
#     a = y['2']["coordinates"]['latitude']
#     b = y['2']['coordinates']['longitude']
#
#     return render_template('index.html',amount = amount,ret = ret, a= a, b= b, lats= lats,longs=longs)

    # return render_template('index.html', ret = ret)


@app.route('/search', methods=["GET"])
def search():
    term = request.args.get('term')
    loc = request.args.get('place')
    if(loc == ""):
        loc = "new york"
    if(term == ""):
        term = "indian"
    return redirect(url_for('welcome',term=term,place=loc))

# @app.route('/search', methods=["GET"])
# def search():
#     '''If search query is for books, then redirects to book_search.
#     If search query is for books, then redirects to movie_search.'''
#     place = request.args.get("h")
#     query =request.args.get("query").replace(" " , "+")
#     if(query==""):
#         return redirect(url_for('index'))
#     # if(type == "Books"):
#     #     return redirect(url_for('book_search', query=query))
#     # else:
#     #     return redirect(url_for('movie_search', query=query))


if __name__ == '__main__':
    app.debug = True  # Set to `False` before release
    app.run()
