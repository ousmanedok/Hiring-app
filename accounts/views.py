from django.contrib import auth
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import FormView

from .forms import UserLoginForm


# Create your views here.
class LoginView(FormView):
    """
    Provides the ability to login as a user with an email and password
    """

    success_url = "/"
    form_class = UserLoginForm
    template_name = "registration/login.html"

    def get_context_data(self, **kwargs):
        ctx = super(LoginView, self).get_context_data(**kwargs)
        ctx["page_title"] = "Login"
        ctx["meta_description"] = ""
        return ctx

    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def get_form_class(self):
        return self.form_class        

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))
