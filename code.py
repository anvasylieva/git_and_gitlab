def pretty_print(name):
    print("*" * 80)
    print(f"Hello, {name}")
    print("*" * 80)


def pretty_pretty_print(name):
    print("-" * 80)
    pretty_print(name)


if __name__ == "__main__":
    name = "Mary"
    pretty_pretty_print(name)
