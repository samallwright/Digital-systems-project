def get_text() -> str:
    with open("project_code\\flask\\test_text.txt", "r", encoding="utf-8") as test_text:
        text = test_text.read()
    return text


def format_for_frontend(input) -> str:
    return str("".join(input))
