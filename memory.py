import sqlite3
import json
import os
from datetime import datetime

class ConversationMemory:
    """Manages conversation history and context for the squad debate system."""
    
    def __init__(self, memory_file=":memory:"):
        """Initialize memory system with SQLite database.
        
        Args:
            memory_file: Path to SQLite database file, or ":memory:" for in-memory database
        """
        self.conn = sqlite3.connect(memory_file)
        self.cursor = self.conn.cursor()
        self._initialize_database()
        
    def _initialize_database(self):
        """Create necessary tables if they don't exist."""
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            speaker TEXT,
            message TEXT,
            message_type TEXT
        )
        ''')
        self.conn.commit()
    
    def add_user_message(self, message):
        """Add a user message to the memory."""
        timestamp = datetime.now().isoformat()
        self.cursor.execute(
            "INSERT INTO messages (timestamp, speaker, message, message_type) VALUES (?, ?, ?, ?)",
            (timestamp, "User", message, "user_input")
        )
        self.conn.commit()
    
    def add_ai_message(self, personality_name, message):
        """Add an AI personality message to the memory."""
        timestamp = datetime.now().isoformat()
        self.cursor.execute(
            "INSERT INTO messages (timestamp, speaker, message, message_type) VALUES (?, ?, ?, ?)",
            (timestamp, personality_name, message, "ai_response")
        )
        self.conn.commit()
    
    def get_conversation_history(self, limit=20):
        """Retrieve recent conversation history.
        
        Args:
            limit: Maximum number of messages to retrieve
            
        Returns:
            List of message dictionaries
        """
        self.cursor.execute(
            "SELECT timestamp, speaker, message, message_type FROM messages ORDER BY id DESC LIMIT ?",
            (limit,)
        )
        
        history = []
        for timestamp, speaker, message, message_type in reversed(self.cursor.fetchall()):
            history.append({
                "timestamp": timestamp,
                "speaker": speaker,
                "content": message,
                "type": message_type
            })
        
        return history
    
    def get_formatted_history(self, limit=10):
        """Get formatted conversation history for LLM context.
        
        Args:
            limit: Maximum number of messages to include
            
        Returns:
            Formatted string of conversation history
        """
        history = self.get_conversation_history(limit)
        
        formatted = "Recent conversation history:\n\n"
        for msg in history:
            formatted += f"{msg['speaker']}: {msg['content']}\n\n"
        
        return formatted
    
    def clear(self):
        """Clear all conversation history."""
        self.cursor.execute("DELETE FROM messages")
        self.conn.commit()
    
    def __del__(self):
        """Close database connection when object is destroyed."""
        if hasattr(self, 'conn'):
            self.conn.close()
