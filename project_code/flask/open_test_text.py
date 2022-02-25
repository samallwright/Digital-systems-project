
with open("project_code\\flask\\test_text.txt", "r",  encoding="utf-8") as test_text:
    text = test_text.read()
    
def get_text():
    return text
    