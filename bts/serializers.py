from rest_framework import serializers


class AuthParamsSerializer(serializers.Serializer):

    username = serializers.EmailField(max_length=75)
    password = serializers.CharField()
