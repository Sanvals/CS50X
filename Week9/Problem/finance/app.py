import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from math import floor

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # --- TODO 4
    # Display a HTML table summarizing:
    # Stocks owned, shares owned, current price, total value of holding
    # Also, cash balance accompanied by a grand total

    # First we extract the db information for this user
    stock = db.execute("SELECT symbol, qty, price, action FROM track WHERE user=:user", user=int(session["user_id"]))
    balance = db.execute("SELECT cash FROM users WHERE id=:user", user=int(session["user_id"]))[0]["cash"]

    # And an extra variable for the different stocks
    diff = db.execute("SELECT DISTINCT symbol FROM track WHERE user=:user", user=int(session["user_id"]))
    # And we add a counter to it

    for i in diff:
        i["qty"] = 0
        i["price"] = lookup(i["symbol"])["price"]

    # Let's check through the transactions and sort the stocks
    # First thgouth the different stocks
    for i in range(len(diff)):
        # Second through the transactions
        for j in range(len(stock)):
            if diff[i]["symbol"] == stock[j]["symbol"]:
                if stock[j]["action"] == "BUY":
                    diff[i]["qty"] += stock[j]["qty"]
                else:
                    diff[i]["qty"] -= stock[j]["qty"]

    # We establish the total
    total = balance
    for i in diff:
        print(balance)
        total += i["price"] * i["qty"]

    # And reformat it to decimal
    total = float(total * 100) / 100

    # Return the page for the appropiate variables
    return render_template("index.html", diff=diff, balance=balance, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # --- TODO 3
    # Let's first render the page
    if request.method == "GET":
        return render_template("buy.html")
    else:
        # Require input of symbol from field whose name is symbol
        symbol = request.form.get("symbol")

        # Render an apology if the symbol does not exist
        if not lookup(symbol):
            return apology("Symbol does not exist", 400)

        # Require input of shares from field whose name is shares
        shares = request.form.get("shares")

        # Render an apology if the input is not a positive integer
        if not shares.isdigit():
            return apology("Must provide a positive integer", 400)

        if int(shares) < 0:
            return apology("Must provide a positive integer", 400)

        # Odds are you'll want to call lookup to a stock's current price
        price = float(lookup(symbol)["price"])

        # Odds are thar you'll want to select how much cash the user has
        cash = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])[0]["cash"]

        # Check that the user has cash enough
        if float(cash) < (float(shares) * float(price)):
            return apology("Not enough cash available")

        # Call the SQLITE3 function to add a new row
        db.execute("INSERT INTO track (user, qty, price, symbol, action) VALUES (:user, :qty, :price, :symbol, :action)",
                   user=session["user_id"], qty=shares, price=price, symbol=symbol, action="BUY")

        # Now, let's update the user's balance
        newBalance = float(cash) - (float(price) * int(shares))
        db.execute("UPDATE users SET cash=:cash WHERE id=:id", cash=newBalance, id=session["user_id"])

    # Upon completion redirect the user to the home page
    return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # --- TODO 5
    # For each row, make clear whether it's sell or buy, include:
    # Symbol, BUY or SELL, price, qty and date of transaction

    record = db.execute("SELECT * FROM track WHERE user=:id", id=session["user_id"])

    print(record)
    return render_template("/history.html", data=record)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    # --- TODO 2
    if request.method == "GET":
        return render_template("quote.html")
        # Require a stock's symbol input whose name is symbol
    else:
        symbol = request.form.get("symbol")
        # Submit user's input via POST to /quote
        quoted = lookup(symbol)

        # Check that there are matches on the lookup
        if not quoted:
            return apology("No matches for these symbols")
        # And return the quoted page with the results
        else:
            name = quoted["name"]
            price = quoted["price"]
            identifier = quoted["symbol"]
            return render_template("quoted.html", name=name, price=price, identifier=identifier)


@app.route("/register", methods=["GET", "POST"])
def register():
    # --- TODO 1
    if request.method == "GET":
        return render_template("register.html")
    # Complete the implementation
    # - Require username as input
    else:
        name = request.form.get("username")
        if not name:
            return apology("Must choose a name", 400)

        # Check if the user already exists
        names = db.execute("SELECT * FROM users WHERE username=:username", username=name)
        if names:
            return apology("Name already taken", 400)

        # - Require password as input
        password = request.form.get("password")
        if not password:
            return apology("Must choose a password", 400)

        # - Require confirmation as input
        confirmation = request.form.get("confirmation")
        if not confirmation:
            return apology("Must repeat the password", 400)

        # - Check  if confirmation and password match
        if password != confirmation:
            # - If not, return an apology
            return apology("Passwords do not match", 400)
        # - Submit the user's input via POST to /register
        db.execute("INSERT INTO users (username, hash) VALUES(:username,:hash)",
                   username=name, hash=generate_password_hash(password))

        # - Return to main page
        return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # --- TODO 5
    # Require the input of a symbol from a select menu
    # First we fetch all the different stocks owned
    held = db.execute("SELECT symbol, qty FROM track WHERE user=:id", id=session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])[0]["cash"]

    # We create the placeholder for the stocks and the amount
    options = {}

    # Iterate through the DB
    for i in range(len(held)):
        symbol = held[i]["symbol"]
        amount = held[i]["qty"]

        if symbol in options:
            # Check if the item exists:
            # Add the amount
            options[symbol] += amount
        else:
            # Create the item with the amount
            options[symbol] = amount

    if request.method == "GET":
        # And pass it to the options of the select menu
        return render_template("sell.html", options=options)
    else:
        # Extract the two variables
        name = request.form.get("symbol")
        sellamount = int(request.form.get("shares"))

        # Check: if sell is bigger than the owned
        print(f"WANNA SELL {sellamount} OF {name}")
        if options[name] < sellamount:
            return apology("NOT ENOUGH OWNED", 400)

        # Check: If name is not in options
        if name not in options:
            return apology("STOCK NOT OWNED", 400)

        # If it passed the checks, proceed with the sellout
        price = lookup(name)["price"]
        newBalance = cash + sellamount * price
        db.execute("UPDATE users SET cash=:cash WHERE id=:id", cash=newBalance, id=session["user_id"])

        # And call the DB to update the tracker
        db.execute("INSERT INTO track (user, qty, price, symbol, action) VALUES (:user, :qty, :price, :symbol, :action)",
                   user=session["user_id"], qty=sellamount, price=price, symbol=symbol, action="SELL")

        # Upon completion, redirect the user to the home page
        return redirect("/")
