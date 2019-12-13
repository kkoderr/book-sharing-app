from django.contrib.auth.views import LoginView,

class LogInUser(LoginView):
    #template_name = registration/login.html
    redirect_field_name = home
