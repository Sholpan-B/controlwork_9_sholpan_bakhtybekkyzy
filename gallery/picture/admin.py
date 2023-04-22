from django.contrib import admin

from picture.models import Photo, AuthorPhotoRelation

admin.site.register(Photo)
admin.site.register(AuthorPhotoRelation)
