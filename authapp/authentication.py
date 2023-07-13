from django.contrib.auth.backends import ModelBackend
from authapp.models import CustomUser

class CustomModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        user = CustomUser.objects.filter(username__iexact=username).values()
        if user:
            username = user[0].get('username')
        return super().authenticate(request, username, password)
