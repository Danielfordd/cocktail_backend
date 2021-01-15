from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class UserSerializerWithToken(serializers.ModelSerializer):

    # token = serializers.SerializerMethodField()
    api_key = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        api_key = validated_data.pop('api_key', None)
        instance = self.Meta.model(**validated_data)
        if api_key is not None:
            instance.set_password(api_key)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('api_key', 'email', 'first_name', 'last_name')
