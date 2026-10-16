import mysql.connector


class Messaging:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            port=3305,
            user="root",
            password="MYSQL1234",
            database="Messaging"
        )

        self.cur = self.mydb.cursor()

    # -------------------------
    # ACCOUNT
    # -------------------------

    def create_account(self, username, password):
        sql = """
        INSERT INTO accounts (username, password)
        VALUES (%s, %s)
        """

        self.cur.execute(sql, (username, password))
        self.mydb.commit()

        return self.cur.lastrowid

    def get_user_id(self, username):
        sql = """
        SELECT user_id
        FROM accounts
        WHERE username = %s
        """

        self.cur.execute(sql, (username,))
        result = self.cur.fetchone()

        if result:
            return result[0]

        return None

    def get_username(self, user_id):
        sql = """
        SELECT username
        FROM accounts
        WHERE user_id = %s
        """

        self.cur.execute(sql, (user_id,))
        result = self.cur.fetchone()

        if result:
            return result[0]

        return None

    # -------------------------
    # CONVERSATION
    # -------------------------

    def create_conv(self, conv_name):
        sql = """
        INSERT INTO conversations (conversation_name)
        VALUES (%s)
        """

        self.cur.execute(sql, (conv_name,))
        self.mydb.commit()

        return self.cur.lastrowid

    def get_conv_name(self, conversation_id):
        sql = """
        SELECT conversation_name
        FROM conversations
        WHERE conversation_id = %s
        """

        self.cur.execute(sql, (conversation_id,))
        result = self.cur.fetchone()

        if result:
            return result[0]

        return None

    def get_conv_id(self, conv_name):
        sql = """
        SELECT conversation_id
        FROM conversations
        WHERE conversation_name = %s
        """

        self.cur.execute(sql, (conv_name,))
        result = self.cur.fetchone()

        if result:
            return result[0]

        return None

    # -------------------------
    # CONVERSATION MEMBERS
    # -------------------------

    def add_user(self, user_id, conversation_id):
        sql = """
        INSERT INTO convtable (user_id, conversation_id)
        VALUES (%s, %s)
        """

        self.cur.execute(sql, (user_id, conversation_id))
        self.mydb.commit()

    def remove_user(self, user_id, conversation_id):
        sql = """
        DELETE FROM convtable
        WHERE user_id = %s
        AND conversation_id = %s
        """

        self.cur.execute(sql, (user_id, conversation_id))
        self.mydb.commit()

    def get_users(self, conversation_id):
        sql = """
        SELECT a.username
        FROM accounts a
        JOIN convtable ct
            ON a.user_id = ct.user_id
        WHERE ct.conversation_id = %s
        """

        self.cur.execute(sql, (conversation_id,))

        return [row[0] for row in self.cur.fetchall()]

    def get_user_conversations(self, user_id):
        sql = """
        SELECT c.conversation_id
        FROM conversations c
        JOIN convtable ct
            ON c.conversation_id = ct.conversation_id
        WHERE ct.user_id = %s
        """

        self.cur.execute(sql, (user_id,))

        return [row[0] for row in self.cur.fetchall()]

    # -------------------------
    # MESSAGES
    # -------------------------

    def send_message(self, conversation_id, user_id, message_text):
        sql = """
        INSERT INTO messages
            (conversation_id, user_id, message_text)
        VALUES
            (%s, %s, %s)
        """

        self.cur.execute(
            sql,
            (conversation_id, user_id, message_text)
        )

        self.mydb.commit()

        return self.cur.lastrowid

    def get_messages(self, conversation_id):
        sql = """
        SELECT
            a.username,
            m.message_text
        FROM messages m
        JOIN accounts a
            ON m.user_id = a.user_id
        WHERE m.conversation_id = %s
        ORDER BY m.message_id
        """

        self.cur.execute(sql, (conversation_id,))

        return self.cur.fetchall()


# -------------------------
# TEST
# -------------------------

if __name__ == "__main__":

    msg = Messaging()

    print("Connected to Messaging database successfully.")

    print("User ID for kanti:",
          msg.get_user_id("kanti"))

    print("Username for user 1:",
          msg.get_username(1))

    print("Conversation 1:",
          msg.get_conv_name(1))

    print("Users in conversation 1:",
          msg.get_users(1))

    print("Messages:")
    for username, message in msg.get_messages(1):
        print(username + ":", message)