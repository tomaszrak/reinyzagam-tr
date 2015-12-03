from User.models import User
from rest_framework import serializers, viewsets

class UserSerializer(serializers.Serializer):
    '''
    Klasa tworząca serializator dla modelu User
    Wybieramy pola oraz właściwości, jakie ma przyjmować nasze api
    Wymgania mogą się różnić od modelu, jednak nie mogą przekraczać ustalonych tam wartości
    '''
    id = serializers.HyperlinkedIdentityField(view_name='user_detail', read_only=True)
    username = serializers.CharField(max_length=50, required=True)
    password = serializers.CharField(max_length=50, required=True)
    firstname = serializers.CharField(max_length=50, required=True)
    surname = serializers.CharField(max_length=50, required=True)
    email = serializers.EmailField(allow_blank=True)

    def create(self, validated_data):
        '''
        Metoda wywoływana przy tworzeniu nowego obieku
        '''
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        '''
        Metoda wywoływana przy aktualizowaniu obiektu
        '''
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance