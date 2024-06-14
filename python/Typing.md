

# Type hints : drill


## Write a function with annotations that changes an int into a str.


To write a function with annotations that converts an integer to a string, you can use Python's type hinting to indicate the expected input type (`int`) and the output type (`str`).
**Implementation**

```python
def int_to_str(value: int) -> str:
    """
    Convert an integer to a string.

    Args:
    value (int): The integer to convert.

    Returns:
    str: The string representation of the integer.
    """
    return str(value)

# Example usage
result = int_to_str(123)
print(result)  # Output: "123"
print(type(result))  # Output: <class 'str'>
```
**Explanation**

1. **Function Definition**: `def int_to_str(value: int) -> str:`
   - `value: int`: This annotation indicates that the function expects an integer as its input.
   - `-> str`: This annotation indicates that the function will return a string.

2. **Docstring**: The function includes a docstring explaining the arguments and the return value.

3. **Return Statement**: `return str(value)` converts the integer `value` to its string representation using the `str()` function.

4. **Example Usage**: The example shows how to call the function and print the result. It also demonstrates checking the type of the result to ensure it is a string.

By running this script, you can see how the function converts an integer to a string and confirms the type of the returned value.

     
## Now one that divides an int by another.

To write a function with annotations that divides one integer by another and returns the result as a float, use Python's type hinting to indicate the expected input types (`int`) and the output type (`float`). 

**Implementation**

```python
def divide(x: int, y: int) -> float:
    """
    Divide one integer by another.

    Args:
    x (int): The dividend.
    y (int): The divisor.

    Returns:
    float: The result of the division.

    Raises:
    ValueError: If the divisor is zero.
    """
    if y == 0:
        raise ValueError("The divisor (y) cannot be zero.")
    return x / y

# Example usage
result = divide(10, 2)
print(result)  # Output: 5.0

try:
    result = divide(10, 0)
except ValueError as e:
    print(e)  # Output: The divisor (y) cannot be zero.
```

**Explanation**

1. **Function Definition**: `def divide(x: int, y: int) -> float:`
   - `x: int`: This annotation indicates that the function expects an integer as the dividend.
   - `y: int`: This annotation indicates that the function expects an integer as the divisor.
   - `-> float`: This annotation indicates that the function will return a float.

2. **Docstring**: The function includes a docstring explaining the arguments, the return value, and the potential exception.

3. **Zero Division Check**: The function checks if the divisor (`y`) is zero and raises a `ValueError` if it is, to prevent division by zero.

4. **Return Statement**: `return x / y` performs the division and returns the result as a float.

5. **Example Usage**: The example shows how to call the function and print the result. It also demonstrates handling the `ValueError` exception when attempting to divide by zero.

By running this script, you can see how the function handles division and ensures proper error handling for division by zero.

     
## Annotate the function declaration below.


def send_email(address,
               sender,
               cc,
               cci,
               subject='',
               body = None
               ):
     
Given the next strings :

suits = "♠ ♡ ♢ ♣".split()
ranks = "2 3 4 5 6 7 8 9 10 J Q K A".split()
Define Card, Deck and Players. Use type aliases.


Card =
Deck =
Players = 
     
Write a program that will create and shuffle the deck. Then distribute the cards to 4 players. Using annotations.

To create a program that shuffles a deck of cards and distributes them to 4 players, we need to follow these steps:

1. Define the `Card`, `Deck`, and `Players` type aliases.
2. Create and shuffle the deck.
3. Distribute the shuffled cards to 4 players.

**Implementation**

```python
import random
from typing import List, Tuple

# Type Aliases
Card = Tuple[str, str]
Deck = List[Card]
Players = List[List[Card]]

# Suits and Ranks
suits = "♠ ♡ ♢ ♣".split()
ranks = "2 3 4 5 6 7 8 9 10 J Q K A".split()

def create_deck() -> Deck:
    """Create a standard deck of 52 cards."""
    return [(suit, rank) for suit in suits for rank in ranks]

def shuffle_deck(deck: Deck) -> None:
    """Shuffle the deck of cards in place."""
    random.shuffle(deck)

def distribute_cards(deck: Deck, num_players: int = 4) -> Players:
    """Distribute the cards to the given number of players."""
    players: Players = [[] for _ in range(num_players)]
    for i, card in enumerate(deck):
        players[i % num_players].append(card)
    return players

def main() -> None:
    # Create and shuffle the deck
    deck: Deck = create_deck()
    shuffle_deck(deck)
    
    # Distribute the cards to 4 players
    players: Players = distribute_cards(deck)
    
    # Print the players' hands
    for i, player_hand in enumerate(players):
        print(f"Player {i + 1}'s hand: {player_hand}")

if __name__ == "__main__":
    main()
```

**Explanation**

1. **Type Aliases**:
   - `Card = Tuple[str, str]`: Each card is represented as a tuple of a suit and a rank.
   - `Deck = List[Card]`: A deck is a list of cards.
   - `Players = List[List[Card]]`: Players' hands are represented as a list of lists of cards.

2. **Suits and Ranks**:
   - `suits` and `ranks` define the suits and ranks of the cards.

3. **Functions**:
   - `create_deck() -> Deck`: Creates a standard deck of 52 cards.
   - `shuffle_deck(deck: Deck) -> None`: Shuffles the deck of cards in place.
   - `distribute_cards(deck: Deck, num_players: int = 4) -> Players`: Distributes the shuffled cards to the given number of players.

4. **Main Function**:
   - `main() -> None`: The main function that creates and shuffles the deck, distributes the cards to 4 players, and prints each player's hand.

5. **Execution**:
   - The `main` function is called if the script is executed directly.

By running this script, you will see the shuffled deck distributed among 4 players, and each player's hand will be printed.



     