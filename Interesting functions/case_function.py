#without case

def get_price(food: str):
    if food == "apple" or food == "peach":
        return 4
    elif food == "orange":
        return 3
    elif food == "grape":
        return 5
    else:
        return "Unknown"

get_price("peach")  # Output: 4

#using case
def get_price(food: str):
    match food:
        case "apple" | "peach":
            return 4
        case "orange":
            return 3
        case "grape":
            return 5
        case _:
            return "Unknown"

get_price("peach")  # Output: 4

# The `match` statement offers better readability, especially for longer series of conditions.
# It is more concise than multiple `if` or `elif` statements, reducing code complexity.
# The `match` statement also enables complex pattern matching, which is not possible with `if-elif`.