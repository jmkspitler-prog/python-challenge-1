from flask import Flask, render_template, request, url_for, redirect
import random

app = Flask(__name__)
all_lengths = {"Anaconda": [], "Racer": [], "Black Mamba": [], "Copperhead": [], "Cottonmouth": []}

compare = False # bool

@app.route("/")
def index():
    return render_template("index.html", dictionary=all_lengths, compare=False)

@app.route("/snake1")
def snake1():
    len = random.randint(4, 40)
    all_lengths["Anaconda"].append(len)
    return render_template("snake1.html", len=len)

@app.route("/snake2")
def snake2():
    len = random.randint(4, 40)
    all_lengths["Racer"].append(len)
    return render_template("snake2.html", len=len)

@app.route("/snake3")
def snake3():
    len = random.randint(4, 40)
    all_lengths["Black Mamba"].append(len)
    return render_template("snake3.html", len=len)

@app.route("/snake4")
def snake4():
    len = random.randint(4, 40)
    all_lengths["Copperhead"].append(len)
    return render_template("snake4.html", len=len)

@app.route("/snake5")
def snake5():
    len = random.randint(4, 40)
    all_lengths["Cottonmouth"].append(len)
    return render_template("snake5.html", len=len)

@app.route("/compare")
def compare():
    for snake in all_lengths: all_lengths[snake].sort(reverse=True)
    new_lengths = dict(sorted(all_lengths.items()))
    return render_template("index.html", dictionary=new_lengths, compare=True)