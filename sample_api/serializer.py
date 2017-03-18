# coding: utf-8

from rest_framework import serializers
from .models import User, Entry, Affi


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('title', 'body', 'created_at', 'status', 'author')


class AffiSerializer(serializers.ModelSerializer):
    """
    シリアライズの定義
    serializer.ModelSerializer を継承
    filed = API
    """
    class Meta:
        model = Affi
        fields = '__all__'