from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'age', 'gender', 'birthdate', 'first_name',
                  'last_name',)
        write_only_fields = ('password',)
        read_only_fields = ('id', 'social_set', 'age', 'email')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        gender = validated_data.get('gender', None)
        birthday = validated_data.get('birthday', None)

        user = User.objects.create(username=username, email=email, gender=gender, birthday=birthday)
        user.set_password(password)
        user.save()

        return user
