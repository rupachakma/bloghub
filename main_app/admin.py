from django.contrib import admin

from main_app.models import Blogpost, CustomUser, Profile

# Register your models here.
class BlogpostAdmin(admin.ModelAdmin):
    list_display=['id','title','description','image']

admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Blogpost,BlogpostAdmin)