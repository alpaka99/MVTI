from rest_framework import serializers
from django.contrib.auth import get_user_model

User= get_user_model()

class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # 쓰기전용이다
    class Meta:
        model = User
        fields = ('username', 'password', )

