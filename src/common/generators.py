from faker import Faker
import arrow

from accounts.models import User
from chat.models import Room, Message


def generate_user(is_superuser=False):
    fake = Faker()

    first_name = fake.first_name()
    last_name = fake.last_name()
    simple_profile = fake.simple_profile()
    username = simple_profile['username']
    birthdate = simple_profile['birthdate']
    birthdate = arrow.get(birthdate).datetime
    email = simple_profile['mail']
    gender = simple_profile['sex']

    return User(username=username, first_name=first_name, last_name=last_name, email=email,
                is_superuser=is_superuser, is_staff=is_superuser, birthdate=birthdate,
                gender=gender)


def generate_room():
    return Room(name=Faker().word())


def generate_message(user=None, room=None):
    if user is None:
        user = generate_user()
    if room is None:
        room = generate_room()
    room.save()
    user.save()
    room.users.add(user)
    content = Faker().text(max_nb_chars=100)
    return Message(room=room, sender=user, content=content)
