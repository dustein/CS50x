import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

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
        
    return render_template("index.html")

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if (request.method == "POST"):
        search_symbol = request.form.get("symbol")
        found_symbol = lookup(search_symbol)
        symbol = str(found_symbol["symbol"])
        shares = int(request.form.get("shares"))
        current_price = found_symbol["price"]
        total_cost = shares * current_price
        user_id = session["user_id"]
        get_user_cash = db.execute("SELECT cash FROM users WHERE id=?", user_id)
        user_cash = get_user_cash[0]["cash"]

        if (not search_symbol):
            return apology("You need to inform the Stock Symbol to Search.")

        if (not found_symbol):
            return apology("That Stock Symbol dos not exist.")

        if(shares < 1):
            return apology("Invalid number.")

        if (current_price * shares > user_cash):
            return apology("You don't have enought money.")

        print(user_id)
        print(symbol)
        print(shares)
        print(current_price)
        print(total_cost)

        db.execute("INSERT INTO buyshare (user_id, symbol, shares, share_cost, total_cost) VALUES (?, ?, ?, ?, ?)", user_id, symbol, shares, current_price, total_cost)

        return render_template("bought.html", symbol=symbol, shares=shares, current_price=current_price, total_cost=total_cost)

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


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
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
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
    """Get stock quote."""
    if (request.method == "POST"):
        search_symbol = request.form.get("symbol")
        found_symbol = lookup(search_symbol)
        return render_template("/quoted.html", result=found_symbol)

    else:
        return render_template("/quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if (request.method == "POST"):

        username = request.form.get("username")
        registered_user = db.execute("SELECT * FROM users WHERE username = ?", username)
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # Testar se existe o username
        if (not username):
            return apology("You must inform an Username.")
        elif (registered_user):
            return apology("This Username is already taken.")

        # Comparar se as senhas inseridas são iguais
        elif (password != confirm_password):
            return apology("The Password and Password Confirmation didin't match.")

        # Quando tudo der certo...

        else:
            # gerar o hash pro password informado
            hash_password = generate_password_hash(password, method='scrypt', salt_length=16)

            #gravar o novo usuario
            db.execute("INSERT INTO users (username, hash) VALUES (?,?)", username, hash_password)

            return render_template("/login.html")

    # Se o metodo for GET
    else:
        return render_template("/register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")