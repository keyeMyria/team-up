from random import randint

from faker import Faker
import arrow

from django.db.utils import IntegrityError
from accounts.models import User
from chat.models import Room, Message
from games.models import LeagueOfLegendsAccount


def generate_user(is_superuser=False):
    fake = Faker()

    while True:
        first_name = fake.first_name()
        last_name = fake.last_name()
        simple_profile = fake.simple_profile()
        username = simple_profile['username']
        birthdate = simple_profile['birthdate']
        birthdate = arrow.get(birthdate).datetime
        email = simple_profile['mail']
        gender = simple_profile['sex']
        try:
            return User.objects.create(username=username, first_name=first_name,
                                       last_name=last_name, email=email, is_superuser=is_superuser,
                                       is_staff=is_superuser, birthdate=birthdate, gender=gender)
        except IntegrityError:
            pass


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


def generate_league_of_legends_account_data(user, credentials=None) -> dict:
    if not credentials:
        credentials = {}

    league_choices = LeagueOfLegendsAccount.LEAGUE_CHOICES
    division_choices = LeagueOfLegendsAccount.DIVISION_CHOICES
    server_choices = LeagueOfLegendsAccount.SERVER_CHOICES

    fake = Faker()
    data = {
        'username': credentials.get('username', fake.user_name()),
        'user_profile': user.userprofile,
        'league': credentials.get('league', randint(1, len(league_choices))),
        'division': credentials.get('division', randint(1, len(division_choices))),
        'server': credentials.get('server', randint(1, len(server_choices)))
    }

    return data
