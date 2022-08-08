from django.contrib import admin
from catalog.models import *
# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(bookInstance)
admin.site.register(language)
