from rest_framework import serializers
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="accounts:user-detail")
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'email',
        'bio','birth_date','avatar']
