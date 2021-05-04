from django.contrib import admin
from .models import *

admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Person)
admin.site.register(Writer)
admin.site.register(Studio)
admin.site.register(Movie)