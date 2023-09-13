# TODO
from cs50 import get_float


def main():
    imp = get_import() * 100
    coins = get_coins(imp)
    print(coins)


# Create the function to get the import
def get_import():
    # Initialize the loop
    while True:
        # Check that the import is > 0
        qty = get_float("imp owed: ")
        if qty > 0:
            return qty


def get_coins(imp):
    # Initialize the variables
    coins = 0
    # Get how many different coints there are
    value = [25, 10, 5, 1]

    # Iterate through the list of values
    for i in range(len(value)):
        # Check that the import is valid
        while (imp >= value[i]):
            # Discount the value and add a coin
            coins += 1
            imp -= value[i]

    return coins


# Initialize the program
main()