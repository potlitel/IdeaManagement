from django.contrib import admin

# Register your models here.
from IdeaPublisher.models import Topico, Idea

admin.site.register(Topico)
admin.site.register(Idea)
