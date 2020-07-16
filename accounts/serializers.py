from djoser.serializers import UserCreateSerializer
from .models import *
class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = AuthUser
        fields = ('id', 'email', 'username','password', 'first_name', 'last_name')
