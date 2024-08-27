from django.shortcuts import render, redirect
from django.views import generic
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth import login

# Create your views here.
def home(request):
    return render(request, 'home.html')

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