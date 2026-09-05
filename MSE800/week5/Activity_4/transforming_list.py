def create_squares_dict(numbers: list[int]) -> dict[str, int]:
    """Build a dictionary that maps each number (as a string key) to its square."""
    return {str(n): n**2 for n in numbers}


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    squares = create_squares_dict(numbers)
    print(squares)