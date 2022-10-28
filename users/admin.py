from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin #이거 사용할 수 없다
from .models import User

admin.site.register(User)