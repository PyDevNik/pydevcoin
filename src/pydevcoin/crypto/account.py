import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)))

from crypto.coin import PyDevCoin
from db.user import User

class Account:
    def __init__(self) -> None:
        self._coin = PyDevCoin()

    def transfer(self, from_user: User, to_user: User, amount: float) -> None:
        self._coin.transfer(from_user,  to_user, amount)
        
    def register(self, username: str, password: str) -> str:
        token = self._coin.register(username, password)
        return token
    
    def login(self, username: str, password: str) -> str:
        token = self._coin.login(username, password)
        return token
    
if __name__ == "__main__":
    account = Account()
    token1 = account.login("privet", "dimas")
    print(token1)
    user1 = account._coin._db.get_user_by_token(token1)
    print(user1.balance)
    
    token2 = account.login("defalt", "gitler")
    print(token2)
    user2 = account._coin._db.get_user_by_token(token2)
    print(user2.balance)

    account.transfer(user2, user1, 100)