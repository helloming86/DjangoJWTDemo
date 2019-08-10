from django.contrib.auth.models import User
from users.models import Profile


class MobileAuthBackend:
    """
    手机号码验证登录
    """
    def authenticate(self, request, username=None, password=None):
        try:
            user = Profile.objects.get(mobile=username).user
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
