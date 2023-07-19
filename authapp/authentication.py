from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from authapp.models import CustomUser

class CustomModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        user = CustomUser.objects.filter(username__iexact=username).values()
        if user:
            username = user[0].get('username')
        return super().authenticate(request, username, password)
    
class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
