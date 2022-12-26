from django.contrib import admin

from users.models import User
from reviews.models import (
    Category, Genre,
    Title
)


admin.site.register(User)
admin.site.register(Title)
admin.site.register(Category)
admin.site.register(Genre)
