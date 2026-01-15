# Jacob Spitler 2026
# Python Challenge @ L3Harris
# Lines of code: 15
from flask import Flask, render_template, request, url_for, redirect
import random
app = Flask(__name__)
snakes = [["Anaconda", "Anacondas are the world's heaviest snakes that use their power to crush prey before swallowing them whole.", []],["Racer", "Black racer snakes are common throughout their range, as are several other types of black snakes, some venomous. This creates confusion, which isn\'t helped by the fact that C. constrictor is not even a classic constricting snake as its binomial name would suggest.", []],["Black Mamba", "Black mambas are the fastest moving snakes in the world. On a smooth surface, they have been known to slither as fast as 10 to 12 mph. To put that in perspective, a black mamba can move faster than a Komodo dragon. Since mambas are also able to swim, they can move smoothly and easily in the water, too. ", []],["Copperhead", "Copperhead snakes are some of the most commonly encountered venomous snakes in North America. They are responsible for more bites in the U.S. than any other snake species, but bites are rarely fatal.", []],["Cottonmouth", "These snakes are nocturnal, preferring to hunt at night. When catching frogs and fish, the cottonmouth holds its prey in its jaws until the venom takes effect. However, when capturing mammals, the cottonmouth bites, then releases the prey immediately because mammals are more likely to bite back. While the cottonmouth is capable of inflicting great damage through its bite, it rarely causes death in humans.", []]]
@app.route("/")
def index() -> None: return render_template("index.html", compare=False)
@app.route("/snake/<int:id>")
def snake(id: int) -> None:
    while (len := random.randint(4, 1000)) in snakes[id][2]: continue # := is the "walrus operator". Allows you to capture a value and use it in the loop's conditional test simultaneously. 
    snakes[id][2].append(len)
    return render_template("snake.html", len=len, name=snakes[id][0], fact=snakes[id][1])
@app.route("/compare")
def compare() -> None:
    for i in snakes: i[2].sort(reverse=True)
    return render_template("index.html", snakes=sorted(snakes), compare=True)