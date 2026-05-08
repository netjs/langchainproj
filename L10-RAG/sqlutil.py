
from connector import MySQLConnection
from typing import List
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage

# This function retrieves all session IDs for a given user, along with the timestamp of 
# the last activity in each session.
def get_sessions_for_user(user_id: str):
    conn = MySQLConnection.get_connection()
    cursor = conn.cursor()
     # Step 1: Check if user_id exists in chat_history
    cursor.execute("SELECT COUNT(*) FROM chat_history WHERE user_id=%s", (user_id,))
    (count,) = cursor.fetchone()

    if count == 0:
        print(f"No chat history found for user_id: {user_id}")
        return []
    
    query = """
        SELECT session_id, MAX(created_at) AS last_activity
        FROM chat_history
        WHERE user_id=%s
        GROUP BY session_id
        ORDER BY last_activity DESC;
    """
    #params to cursor.execute should be a tuple, even if it's just one value
    cursor.execute(query, (user_id,))
    rows = cursor.fetchall()
    cursor.close()
    return rows

# This function retrieves the full chat history for a specific session ID, ordered by 
# the timestamp of each message.
def get_session_messages(session_id: str) -> List[BaseMessage]:
    history: List[BaseMessage] = []
    conn = None
    cursor = None

    try:
        conn = MySQLConnection.get_connection()
        cursor = conn.cursor()

        query = """
            SELECT role, message, created_at
            FROM chat_history
            WHERE session_id=%s
            ORDER BY created_at ASC;
        """
        cursor.execute(query, (session_id,))
        rows = cursor.fetchall()

        for role, message, created_at in rows:
            if role == "user":
                history.append(HumanMessage(content=message))
            elif role == "assistant":
                history.append(AIMessage(content=message))
            # optionally handle 'system' role if you store it

    except Exception as e:
        print(f"Error fetching session messages: {e}")

    finally:
        if cursor:
            cursor.close()
        # don’t close conn if you’re reusing singleton connection
        # if you want to close each time, uncomment:
        # if conn and conn.is_connected():
        #     conn.close()

    return history

# This function saves a single chat message into the chat_history table
def save_message(user_id, session_id, role, message):
    """
    Save a single chat message into the chat_history table.
    """
    conn = MySQLConnection.get_connection()
    cursor = conn.cursor()

    sql = """
        INSERT INTO chat_history (user_id, session_id, role, message)
        VALUES (%s, %s, %s, %s)
    """
    values = (user_id, session_id, role, message)

    cursor.execute(sql, values)
    conn.commit()
    cursor.close()