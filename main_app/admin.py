from django.contrib import admin

from main_app.models import Blogger_Profile, Blogpost, CustomUser, Viewer_Profile

# Register your models here.
class BlogpostAdmin(admin.ModelAdmin):
    list_display=['id','title','description','image']

admin.site.register(CustomUser)
admin.site.register(Blogger_Profile)
admin.site.register(Viewer_Profile)
admin.site.register(Blogpost,BlogpostAdmin)