def echo(text: str, repetitions: int=3) -> str:
    """Imitate a real-world echo."""
    output = "\n".join(text[-i:] for i in range(repetitions, 0, -1))
    return output + "\n"


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))