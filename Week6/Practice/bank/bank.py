from cs50 import get_string


answer = get_string("Greeting: ")

if answer.strip()[:5].lower() == "hello":
    print("$0")

elif answer[0] in ["H", "h"]:
    print("$20")

else:
    print("$100")
