from pages.base import Base

class UsersId(Base):
    ENDPOINT = '/users/%s'

    # Initializer

    def __init__(self):
        self.URL = self.BASE_URL + self.ENDPOINT

    # Interaction Methods
    def get_user_data(self, id):
        response = self.get_method(self.URL % str(id))
        try:
            data = response.json()["data"]
        except:
            data = {}
        return response.status_code, data
    