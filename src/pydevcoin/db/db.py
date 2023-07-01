from .user import User
from typing import List
import pymongo

class Database:
    def __init__(self) -> None:
        self.__mongo_client = pymongo.MongoClient()
        self._db = self.__mongo_client.get_database("pydevcoin")
        self._users_collection = self._db.get_collection("users")
        print("Connect Success!")

    def add_user(self, user: User) -> None:
        if not self.get_user_by_username(user.username):
            self._users_collection.insert_one(user.dict())

    def get_all_users(self) -> List[User]: 
        return [User(**user_dict) for user_dict in list(self._users_collection.find({}))]

    def get_user_by_token(self, token: str) -> User: 
        user_dict = self._users_collection.find_one({"token": token})
        return User(**user_dict) if user_dict is not None else None
    
    def get_user_by_username(self, username: str) -> User: 
        user_dict = self._users_collection.find_one({"username": username})
        return User(**user_dict) if user_dict is not None else None

    def get_balance(self, user: User) -> float: 
        return user.balance 
       
    def add_balance(self, user: User, amount: float) -> None: 
        balance = self.get_balance(user)
        user.balance += amount
        self._users_collection.update_one(
            {"username": user.username},
            {"$set": user.dict()}
        )
