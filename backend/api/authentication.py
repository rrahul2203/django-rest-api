from lib2to3.pytree import Base
from rest_framework.authentication import TokenAuthentication as BaseTokenAuthentication

class TokenAuthentication(BaseTokenAuthentication):
    keyword = 'Bearer'