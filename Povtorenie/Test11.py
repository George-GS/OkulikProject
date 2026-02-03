

class APIClient:
    base_url = "https://api.test-server.com"
    default_timeout = 10

    def __init__(self, api_key, timeout=None):
        self.api_key = api_key
        self.timeout = timeout if timeout is not None else self.default_timeout

    def get_status(self):
        return 'Active' if self.timeout < 15 else 'Slow'

    def make_url(self, endpoint):
        return self.base_url + endpoint

    def validate_key(self):
        return len(self.api_key) > 5

class AuthAPIClient(APIClient):

    def __init__(self, api_key, username, password, timeout=None):
        super().__init__(api_key, timeout)
        self.username = username
        self.password = password

    def login(self):
        return self.username == 'admin' and self.password == 'secret'

    def get_auth_header(self):
        return {'Authorization' : f'Bearer {self.api_key}'}

    def make_url(self, endpoint):
        return super().make_url('/v2' + endpoint)


client = APIClient("my-secret-key-123", timeout=5)

print(client.get_status())      # "Active" (5 < 15)
print(client.make_url("/users")) # "https://api.test-server.com/users"
print(client.validate_key())    # True (длина > 5)


client2 = APIClient("12345")    # timeout не указан → должен быть 10
print(client2.get_status())     # "Active" (10 < 15)
print(client2.validate_key())   # False (длина = 5)

client3 = APIClient('my-god', 7)

print()
print(client2.timeout)
print(client3.timeout)

auth_client = AuthAPIClient(
    api_key = "super-secret-key",
    username = "admin",
    password = "secret",
    timeout = 20
)

print(auth_client.login())           # True (правильные данные)
print(auth_client.get_status())      # "Slow" (timeout=20 >= 15)
print(auth_client.make_url("/profile"))  # "https://api.test-server.com/v2/profile"
print(auth_client.get_auth_header()) # {"Authorization": "Bearer super-secret-key"}

# Также сохранилась вся функциональность родителя:
print(auth_client.validate_key())    # True (длина > 5)