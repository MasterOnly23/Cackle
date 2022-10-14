from django.contrib import admin
from SocialMedia.models import Post,Profile,Relationship,Country
# Register your models here.


admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Relationship)
admin.site.register(Country)