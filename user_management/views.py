import json
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress
from django.db.models import Q
from allauth.account.views import SignupView, ConfirmEmailView, PasswordResetView, LoginView
from allauth.account.forms import LoginForm
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.http import Http404
from jess import settings as app_settings

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from allauth.account.utils import send_email_confirmation



@method_decorator(csrf_exempt, name='dispatch')
class CustomSignupView(SignupView):

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            self.form_valid(form)
            http_response = HttpResponse(json.dumps(
                {'message': 'Sign Up Successful'}), content_type='application/json')
        else:
            http_response = HttpResponseBadRequest(json.dumps(
                {'message': 'Error Sign Up', 'error': form.errors}), content_type='application/json')

        return http_response

    def form_valid(self, form):
        self.user = form.save(self.request)
        send_email_confirmation(self.request, self.user, signup=True)


class CustomConfirmEmailView(ConfirmEmailView):

    def get(self, *args, **kwargs):
        try:
            self.object = self.get_object()
            if app_settings.ACCOUNT_CONFIRM_EMAIL_ON_GET:
                return self.post(*args, **kwargs)
        except Http404:
            self.object = None
        ctx = self.get_context_data()
        return self.render_to_response(ctx)

    def post(self, *args, **kwargs):
        self.object = confirmation = self.get_object()
        confirmation.confirm(self.request)

        http_response = HttpResponse(json.dumps(
            {'message': 'Confirmation Success'}), content_type='application/json')

        return http_response


@method_decorator(csrf_exempt, name='dispatch')
class CustomPasswordResetView(PasswordResetView):

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            self.form_valid(form)
            http_response = HttpResponse(json.dumps(
                {'message': 'Sent an email to reset Password'}), content_type='application/json')
        else:
            http_response = HttpResponseBadRequest(json.dumps(
                {'message': 'Error Reset Password', 'error': form.errors}), content_type='application/json')

        return http_response
    

class CustomLoginView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        username = request._data.get('username')
        user_obj = User.objects.get(Q(username=username) | Q(email=username))
        is_verified = EmailAddress.objects.get(user=user_obj).verified 

        if not is_verified:
            response = HttpResponseBadRequest(json.dumps({
                'message': 'Error Login', 'error': 'Please verify user in email'
            }), content_type='application/json')


        return response

