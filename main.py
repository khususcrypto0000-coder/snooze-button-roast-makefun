import os

ENTRY_TEXT = "Your alarm clock is the only employee who clocks in early on Saturday at 6 a.m. \u2014 and cashes its overtime in the one morning you actually earned."


def main():
    text = ENTRY_TEXT.strip()
    assert text and not text.isspace()
    assert "\n" not in text and "\r" not in text
    assert 1 <= len(text) <= 200
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
