# TODO
from cs50 import get_int


def main():
    # Get the height of the pyramid
    H = get_height()
    # Loop through the height
    for height in range(H):
        # Create variables for both sections
        spaces = (H - height - 1) * " "
        hashes = (height + 1) * "#"
        # Finally print the level
        print(spaces + hashes)


# Create the function to get the height
def get_height():
    # Check an infinte loop
    while True:
        # Force a correct answer
        height = get_int("Height: ")
        if height > 0 and height < 9:
            # Escape the loop
            return height


# Call the main function
main()