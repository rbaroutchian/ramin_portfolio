from .models import User



def UserSetting(request):
    user_setting = User.objects.filter(is_main_setting=True).first()
    return {'user_setting': user_setting}
