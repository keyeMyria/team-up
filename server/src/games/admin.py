from django.contrib import admin

from games.models import LeagueOfLegendsAccount

# class LeagueOfLegendsAdmin(admin.ModelAdmin):
#     pass

admin.site.register(LeagueOfLegendsAccount)
