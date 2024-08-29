from django.shortcuts import render, redirect
from django.views import generic, View
from django.urls import reverse_lazy

# Login modules
from django.contrib.auth import login, logout, authenticate

# Form modules
from .forms import SignUpForm, SignInForm
from django.views.generic.edit import FormView
# Create your views here.

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
class SignInFormView(FormView):
    template_name = 'signin.html'
    form_class = SignInForm
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
class SignOutView(View):
    def get(self, request, *args, **kwargs):
        # Log out the user
        logout(request)
        # Redirect to a specified URL after signing out
        return redirect(reverse_lazy('home'))  # Change 'home' to your desired redirect URL