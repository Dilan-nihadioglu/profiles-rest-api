from rest_framework import serializers
from profiles_api import models



class HelloSerializer(serializers.Serializer):
    """
    Serializes a name field for testing our API view
    """
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes a user profile object """
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
    def update(self, instance, validated_data):
        """Kullanıcı hesabını güncellemeyi yönetir"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Profile feed item verisini serileştirir"""

    class Meta:
        model = models.ProfileFeedItem  # Hangi model serileştirilecek
        fields = ('id', 'user_profile', 'status_text', 'created_on')  # Hangi alanlar serileştirilecek

        extra_kwargs = {
            'user_profile': {'read_only': True}  # Bu alan yalnızca okunabilir olacak
        }




        
