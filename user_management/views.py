import json
from allauth.account.views import SignupView
from django.http.response import HttpResponse, HttpResponseBadRequest
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


