from tinydb import TinyDB
from tinydb.queries import Query

class DB:
    def __init__(self) -> None:
        self.db = TinyDB('db.json', indent=4)
    
    def add_user(self, chat_id: str, username: str) -> int:
        user = {
            'chat_id': chat_id,
            'username': username,
            'like': 0,
            'dislike': 0
        }
        return self.db.insert(user)

    def is_user(self, chat_id: str) -> bool:
        user = Query()
        return self.db.contains(user.chat_id == chat_id)
    
    def inc_like(self, chat_id: str) -> None:
        pass
    
    def inc_dislike(self, chat_id: str) -> None:
        pass

    def get_data(self, chat_id: str) -> dict:
        pass

db = DB()
db.add_user('3241234123', 'jumanovdiyorbek')
# print(db.is_user('3241234123'))