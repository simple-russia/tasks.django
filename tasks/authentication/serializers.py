from rest_framework import serializers



class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    id = serializers.IntegerField()

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
