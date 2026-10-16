from flask import Flask
from mysql_connector import Messaging

app = Flask(__name__)


# ============================================================
# DATABASE
# ============================================================

def get_db():
    """
    Create a database connection for the current request.
    """
    return Messaging()


# ============================================================
# HOME / SERVER TEST
# ============================================================

@app.route("/")
def home():
    return "Messaging server is running."


# ============================================================
# ACCOUNT MANAGEMENT
# ============================================================

@app.route("/signup/<username>/<password>/", methods=["GET", "POST"])
def signup(username, password):

    database = get_db()

    # Check whether username already exists
    user_id = database.get_user_id(username)

    if user_id is not None:
        return "exists"

    # Create account
    new_user_id = database.create_account(
        username,
        password
    )

    return str(new_user_id)


@app.route("/login/<username>/<password>/")
def login(username, password):

    database = get_db()

    database.cur.execute(
        """
        SELECT user_id
        FROM accounts
        WHERE username = %s
        AND password = %s
        """,
        (username, password)
    )

    result = database.cur.fetchone()

    if result is None:
        return "-1"

    return str(result[0])


@app.route("/exists/<username>")
def exists(username):

    database = get_db()

    user_id = database.get_user_id(username)

    if user_id is None:
        return ""

    return username


@app.route("/getusername/<user_id>/")
def getusername(user_id):

    database = get_db()

    username = database.get_username(
        int(user_id)
    )

    if username is None:
        return ""

    return username


# ============================================================
# CONVERSATIONS
# ============================================================

@app.route("/createconv/<conversation_name>/<user_id>")
def createconv(conversation_name, user_id):

    database = get_db()

    # Create conversation
    conversation_id = database.create_conv(
        conversation_name
    )

    # The creator automatically becomes a member
    database.add_user(
        int(user_id),
        conversation_id
    )

    return str(conversation_id)


@app.route("/getconvname/<conversation_id>")
def getconvname(conversation_id):

    database = get_db()

    name = database.get_conv_name(
        int(conversation_id)
    )

    if name is None:
        return ""

    return name


@app.route("/getconvid/<conversation_name>")
def getconvid(conversation_name):

    database = get_db()

    conversation_id = database.get_conv_id(
        conversation_name
    )

    if conversation_id is None:
        return "-1"

    return str(conversation_id)


@app.route("/getallconvs/<user_id>")
def getallconvs(user_id):

    database = get_db()

    conversations = database.get_user_conversations(
        int(user_id)
    )

    return str(conversations)


# ============================================================
# CONVERSATION MEMBERS
# ============================================================

@app.route("/getusers/<conversation_id>")
def getusers(conversation_id):

    database = get_db()

    users = database.get_users(
        int(conversation_id)
    )

    return str(users)


@app.route(
    "/addtoconv/<conversation_id>/<username>",
    methods=["GET", "POST"]
)
def addtoconv(conversation_id, username):

    database = get_db()

    # Convert username to user_id
    user_id = database.get_user_id(username)

    if user_id is None:
        return "user_not_found"

    try:

        database.add_user(
            user_id,
            int(conversation_id)
        )

    except Exception:

        # User may already be in the conversation
        pass

    return "added"


@app.route(
    "/removefromconv/<conversation_id>/<username>",
    methods=["GET", "POST"]
)
def removefromconv(conversation_id, username):

    database = get_db()

    user_id = database.get_user_id(username)

    if user_id is None:
        return "user_not_found"

    database.remove_user(
        user_id,
        int(conversation_id)
    )

    return "removed"


@app.route(
    "/removefromconvid/<conversation_id>/<user_id>",
    methods=["GET", "POST"]
)
def removefromconvid(conversation_id, user_id):

    database = get_db()

    database.remove_user(
        int(user_id),
        int(conversation_id)
    )

    return "removed"


# ============================================================
# MESSAGES
# ============================================================

@app.route(
    "/putmsg/<conversation_id>/<user_id>/<message>",
    methods=["GET", "POST"]
)
def putmsg(conversation_id, user_id, message):

    database = get_db()

    # Store the message
    database.send_message(
        int(conversation_id),
        int(user_id),
        message
    )

    return message


@app.route("/getmsgs/<conversation_id>")
def getmsgs(conversation_id):

    database = get_db()

    messages = database.get_messages(
        int(conversation_id)
    )

    output = ""

    for username, message in messages:

        output += username
        output += ": "
        output += message
        output += "\n"

    return output


# ============================================================
# SERVER START
# ============================================================

if __name__ == "__main__":

    print()
    print("======================================")
    print("       MESSAGING SERVER")
    print("======================================")
    print()
    print("MySQL : 127.0.0.1:3305")
    print("Flask : 0.0.0.0:5000")
    print()
    print("Server is ready for LAN clients.")
    print("======================================")
    print()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )