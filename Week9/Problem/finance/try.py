from cs50 import SQL
import collections

db = SQL("sqlite:///finance.db")

stocks = db.execute("SELECT symbol, qty, action, price FROM track WHERE user=4")
diff = db.execute("SELECT DISTINCT symbol FROM track WHERE user=4")
for i in diff:
    i["qty"] = 0


for i in range(len(diff)):
    for j in range(len(stocks)):
        if diff[i]["symbol"] == stocks[j]["symbol"]:
            if stocks[j]["action"] == "BUY":
                diff[i]["qty"] += stocks[j]["qty"]
            elif stocks[j]["action"] == "SELL":
                diff[i]["qty"] -= stocks[j]["qty"]


print(diff)