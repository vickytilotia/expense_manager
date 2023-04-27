from django.shortcuts import render, redirect
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
# from .utils import account_activation_token
from django.urls import reverse
from django.contrib import auth
# Create your views here.

# why used json? can we used api here?

class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'}, status=400)
        # if User.objects.filter(email=email).exists():
        #     return JsonResponse({'email_error': 'sorry Email already exists'}, status=409)
        return JsonResponse({'email_valid': True})

class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({'error':'username should only contain alphanumeric chracters'},status = 400)
        # if User.objects.filter(username = username).exists:
        #     print(username)
        #     return JsonResponse({"error":"Sorry, Username already exists"},status = 409)
        return JsonResponse({'Username_valid':True})

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('login')