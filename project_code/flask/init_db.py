import sqlite3

connection = sqlite3.connect("database.db")


with open("schema.sql") as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute(
    "INSERT INTO posts (title, content, summary, rouge) VALUES (?, ?, ?, ?)",
    (
        "Example Post",
        """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
             Duis condimentum ante quis risus iaculis ultrices ac a dolor. Nullam mollis
             lacus orci, et tincidunt libero tempor sed. Etiam vitae laoreet libero.
             Nullam tincidunt nulla vel lacinia mollis. Cras id consectetur odio, in
             ismod ipsum. Vivamus augue dui, rutrum et suscipit luctus, accumsan eget
             elit. Vestibulum rhoncus sodales tortor dapibus tincidunt. Interdum et
             malesuada fames ac ante ipsum primis in faucibus. Donec ut enim sit amet
             ipsum iaculis tempus sed vel elit. Etiam velit risus, dignissim quis sodales
             quis, fermentum non velit. Proin sit amet velit posuere, facilisis magna et,
             semper justo. Nunc a nisl et erat ultricies pellentesque eu ullamcorper leo.""",
        """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
             Duis condimentum ante quis risus iaculis ultrices ac a dolor. Nullam mollis
             lacus orci, et tincidunt libero tempor sed. Etiam vitae laoreet libero.
             Nullam tincidunt nulla vel lacinia mollis. Cras id consectetur odio, in
             ismod ipsum. Vivamus augue dui, rutrum et suscipit luctus, accumsan eget
             elit. Vestibulum rhoncus sodales tortor dapibus tincidunt. Interdum et
             malesuada fames ac ante ipsum primis in faucibus. Donec ut enim sit amet
             ipsum iaculis tempus sed vel elit. Etiam velit risus, dignissim quis sodales
             quis, fermentum non velit. Proin sit amet velit posuere, facilisis magna et,
             semper justo. Nunc a nisl et erat ultricies pellentesque eu ullamcorper leo""",
        "Dummy Rouge Score",
    ),
)

connection.commit()
connection.close()


def reset():
    connection = sqlite3.connect("database.db")
    with open("schema.sql") as f:
        connection.executescript(f.read())
    cur = connection.cursor()
    cur.execute(
        "INSERT INTO posts (title, content) VALUES (?, ?)",
        (
            "Example Post",
            """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                Duis condimentum ante quis risus iaculis ultrices ac a dolor. Nullam mollis
                lacus orci, et tincidunt libero tempor sed. Etiam vitae laoreet libero.
                Nullam tincidunt nulla vel lacinia mollis. Cras id consectetur odio, in
                ismod ipsum. Vivamus augue dui, rutrum et suscipit luctus, accumsan eget
                elit. Vestibulum rhoncus sodales tortor dapibus tincidunt. Interdum et
                malesuada fames ac ante ipsum primis in faucibus. Donec ut enim sit amet
                ipsum iaculis tempus sed vel elit. Etiam velit risus, dignissim quis sodales
                quis, fermentum non velit. Proin sit amet velit posuere, facilisis magna et,
                semper justo. Nunc a nisl et erat ultricies pellentesque eu ullamcorper leo.""",
        ),
    )
    connection.commit()
    connection.close()
