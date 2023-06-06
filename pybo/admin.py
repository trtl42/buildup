from django.contrib import admin
from .models import Person, Position, Team, Pots

# Register your models here.
admin.site.register(Person)
admin.site.register(Position)
admin.site.register(Team)
admin.site.register(Pots)
