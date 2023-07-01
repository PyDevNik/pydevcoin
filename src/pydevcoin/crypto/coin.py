import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)))

from db.db import Database
from db.user import User
import random
import string

class PyDevCoin:
    def __init__(self) -> None:
        self._db = Database()
        self._string = string.ascii_letters
        self._token_length = 20
        self._fees = 0

    def transfer(self, from_user: User, to_user: User, amount: float):
        fee = 0.10
        price = amount - (amount * fee)
        self._db.add_balance(from_user, -amount)
        self._db.add_balance(to_user, +price)
        self._fees += (amount * fee)

    def register(self, username: str, password: str) -> str:
        if self._db.get_user_by_username(username):
            return
        else:
            token = "".join([random.choice(self._string) for i in range(self._token_length)])
            self._db.add_user(User(
                username = username,
                password = password,
                token = token
                ))
            return token
        
    def login(self, username: str, password: str) -> str:
        if not self._db.get_user_by_username(username):
            return
        user = self._db.get_user_by_username(username)
        if not password == user.password:
            return
        token = user.token
        return token
    