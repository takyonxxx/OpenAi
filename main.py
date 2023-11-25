# main.py
import os

from conversation_handler import ConversationHandler

# Redirect ALSA logs to /dev/null
os.system("export ALSA_DEBUG=0")
os.system("2>/dev/null")

if __name__ == "__main__":
    conversation_handler = ConversationHandler()
    conversation_handler.start_conversation(3)
