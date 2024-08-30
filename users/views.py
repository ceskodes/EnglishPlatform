from django.shortcuts import render, redirect
from django.views import generic, View
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordChangeView

# Login modules
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

# Form modules
from .forms import SignUpForm, LogInForm
from django.views.generic.edit import FormView
from django.contrib.auth.forms import PasswordChangeForm

# Form to register new users
class SignUpFormView(generic.FormView):
    template_name = "signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy('home')  # Redirect to the home page after successful signup
    
    def form_valid(self, form):
        # Save the user and related Person instance using the form's save method
        created_user = form.save()
        
        # Log the user in
        login(self.request, created_user)
        
        # Redirect to the desired URL
        return redirect(self.success_url)
    
# Form to Log In
class LogInFormView(FormView):
    template_name = 'login.html'
    form_class = LogInForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Incorrect username or password.')
            return self.form_invalid(form)

# Form to Log Out
class LogOutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        # Log out the user
        logout(request)
        # Redirect to a specified URL after signing out
        return redirect(reverse_lazy('login'))  # Change 'home' to your desired redirect URL
    
# Profile Views
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile_personal_info.html"
    
class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'profile_change_password.html'    
    success_url = reverse_lazy('profile')
    
    def __str__(self):
        return f"{self.name} {self.last_name}"
