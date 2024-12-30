from django.contrib import admin
from .models import Channel, Video, StorySubmission
# Register your models here.
admin.site.register(Channel)
admin.site.register(Video)
admin.site.register(StorySubmission)

admin.site.site_title = "Mic Camera Stories Admin"
admin.site.site_header = "Mic Camera Stories Admin"
admin.site.index_title = "Welcome to the Mic Camera Stories Admin Dashboard"