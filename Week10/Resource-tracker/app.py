from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from helpers import login_required

# Configure the app
app = Flask(__name__)

# Configure the session
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Run the CS50 library to use SQLITE3 database
db = SQL("sqlite:///track.db")


@app.route("/add", methods=["POST"])
@login_required
def add_item():
    # Fetch the data of the item to add from the form
    name = request.form.get("newTxt")
    qty = request.form.get("newQty")
    duration = request.form.get("newDur")

    if name:
        # Add the item to the database and refresh the page
        db.execute(
            "INSERT INTO food (name, duration, qty) VALUES (:name, :duration, :qty)",
            name=name,
            duration=duration,
            qty=qty,
        )
        return redirect("/")
    else:
        return redirect("/")


@app.route("/delete", methods=["POST"])
@login_required
def delete_item():
    # Get the name of the item from the page
    name = request.form.get("item")

    # Pick the item from the database and delete it
    db.execute("DELETE FROM food WHERE name=:name", name=name)
    return redirect("/")


@app.route("/onemore", methods=["POST"])
@login_required
def onemore():
    # Get the name of the item to add one quantity
    name = request.form.get("item")

    # Fetch it from the database
    qty = db.execute("SELECT qty FROM food WHERE name=:name", name=name)[0]["qty"]

    # Add one unit
    qty += 1

    # Pick the item from the database and add one unit
    db.execute("UPDATE food SET qty=:qty WHERE name=:name", qty=qty, name=name)
    return redirect("/")


@app.route("/oneless", methods=["POST"])
@login_required
def oneless():
    # Get the name of the item to add one quantity
    name = request.form.get("item")

    # Fetch it from the database
    qty = db.execute("SELECT qty FROM food WHERE name=:name", name=name)[0]["qty"]
    
    # Add one unit
    qty -= 1

    # Pick the item from the database and add one unit
    db.execute("UPDATE food SET qty=:qty WHERE name=:name", qty=qty, name=name)
    return redirect("/")


@app.route("/coin", methods=["POST"])
@login_required
def coin():
    # Get the amount, value and action of the transaction
    coinAmount = int(request.form.get("coinsQty"))
    coinValue = request.form.get("coinsValue")
    coinAction = request.form.get("coinsAct")
    # Test with print
    # print(f"Cantidad: {coinAmount}, valor: {coinValue}, accion: {coinAction}")
    # Check the validity of the values
    if coinAmount < 1:
        return redirect("/")
    if coinValue not in ["c", "p", "g", "p"]:
        return redirect("/")
    if coinAction not in ["earn", "spend"]:
        return redirect("/")

    # Check if the transaction is valid
    # - First gather the data from the database
    coins = db.execute("SELECT c, s, g, p FROM money ORDER BY trans_id DESC LIMIT 1")[0]

    # - Check that the amount is not 0 or less when transaction is spend
    if coins[coinValue] - coinAmount < 0:
        return redirect("/")

    # If everything is correct, update de dictionary
    if coinAction == "spend":
        coins[coinValue] -= coinAmount
    elif coinAction == "earn":
        coins[coinValue] += coinAmount

    # Create a new database entry with the updated purse
    db.execute(
        "INSERT INTO money (c, s, g, p) VALUES (:c, :s, :g, :p)",
        c=coins["c"],
        s=coins["s"],
        g=coins["g"],
        p=coins["p"],
    )
    return redirect("/")


@app.route("/additem", methods=["POST"])
@login_required
def additem():
    # Catch the elements of the submit button
    name = request.form.get("itemName")
    qty = request.form.get("itemQty")
    tag = request.form.get("itemType")
    desc = request.form.get("itemDesc")

    # Check if the elements are correct
    if not name:
        return "/"
    if int(qty) < 0:
        return "/"
    if tag not in ["weapon", "potion", "ring", "armor", "scroll", "misc"]:
        return "/"

    # If the check succeeds, add the item to the database
    db.execute(
        "INSERT INTO items (qty, name, type, desc) VALUES (:qty, :name, :type, :desc)",
        qty=qty,
        name=name,
        type=tag,
        desc=desc,
    )

    # And refresh the page
    return redirect("/")


@app.route("/delitem", methods=["POST"])
@login_required
def delitem():
    # Fetch the ID of the object
    item = request.form.get("item")

    # Find the element and delete it
    print(db.execute("DELETE FROM items WHERE id=:id", id=item))
    return "/"


@app.route("/moditem", methods=["POST"])
@login_required
def moditem():
    # Fetch the ID of the object
    id = request.form.get("id")
    desc = request.form.get("desc")
    qty = request.form.get("qty")

    # Find the element and delete it
    db.execute(
        "UPDATE items SET desc=:desc, qty=:qty WHERE id=:id", desc=desc, qty=qty, id=id
    )
    return "/"


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    # Check if it's updating or just displaying
    # Request the food list from the database
    food = db.execute(
        "SELECT name, duration, qty FROM food WHERE duration!=0 AND qty!=0 ORDER BY duration"
    )
    coins = db.execute("SELECT c, s, g, p FROM money ORDER BY trans_id DESC LIMIT 1")[
        0
    ].items()
    items = db.execute(
        "SELECT qty, name, type, desc, id FROM items WHERE qty!=0 ORDER BY type"
    )

    # Group the items by type
    dbGroups = db.execute("SELECT type, COUNT(*) FROM items WHERE qty!=0 GROUP BY type")

    # Render the page with the necesary data
    return render_template(
        "index.html", rows=food, coins=coins, items=items, groups=dbGroups
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    # Forgets sessions
    session.clear()

    # If the user submits the log in form
    if request.method == "POST":
        # Gather the variables
        name = request.form.get("username")
        hash = request.form.get("password")

        # Retrieve the username from db
        results = db.execute("SELECT * FROM users WHERE name=:name", name=name)

        if not name:
            return render_template("/login.html")
        if not hash:
            return render_template("/login.html")

        # Check the nº or usernames and the pass
        if len(results) != 1 or results[0]["pass"] != hash:
            # Refresh the page if there's no match
            return redirect("/")
        else:
            # Assign session number to Flask
            session["user_id"] = results[0]["id"]
            # Go to index otherwise
            print("ACCESS GRANTED")
            return redirect("/")

    # Render the login on page load
    else:
        return render_template("login.html")
