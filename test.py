def greet(name: str) -> str:
    """
    Simple greeting function
    """
    return f"Hello, {name}!"


def main():
    user = "Developer"
    message = greet(user)
    print(message)


if __name__ == "__main__":
    main()
