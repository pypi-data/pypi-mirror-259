import os
from datetime import datetime

class ChatParser():
    def __init__(self, path):
        path = os.path.expanduser(path)
        with open(path, "r", encoding="utf-8") as f:
            data = f.read().split("\n")
        data = [line for line in data if len(line.split(":")) == 3]
        data = [line for line in data if ", " in line.split(":")[-2]]
        chats = []
        members = []
        for chat in data:
            chat = chat.split(":")
            chat_dict = {}
            member = "".join(chat[-2].split()[1:])
            message = chat[-1]
            date = "".join(chat[0].split()[0:3])
            date = datetime.strptime(date, "%Y.%m.%d.")
            chat_dict['member'] = member
            chat_dict['message'] = message
            chat_dict['date'] = date
            members.append(member)
            chats.append(chat_dict)
        self.__chats__ = chats
        self.__members__ = list(set(members))

    def get_chat(self):
        return self.__chats__

    def get_members(self):
        return self.__members__