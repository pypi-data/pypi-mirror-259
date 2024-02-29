from komodo.framework.komodo_user import KomodoUser
from komodo.store.user_store import UserStore


class UserLoader:

    @classmethod
    def load(cls, email) -> KomodoUser:
        user = UserStore().retrieve_user(email)
        print(user)
        return KomodoUser(name=user.name, email=user.email)
