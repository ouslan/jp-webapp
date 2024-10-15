from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='web_app:log_in_page')
def account_setting(request):
    return render(request, "registration/account_settings.html")
