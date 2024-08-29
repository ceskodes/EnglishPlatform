from .models import Person
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django import forms

class SignUpForm(UserCreationForm):
    """ Form to create new user """
    usable_password = None
    
    name = forms.CharField(max_length=15, label="Your name", widget= forms.TextInput(attrs={'placeholder':'Enter your name', 'class': 'w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm'}))
    last_name = forms.CharField(max_length=15, label="Your last name", widget= forms.TextInput(attrs={'placeholder':'Enter your last name', 'class': 'w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm'}))
    email = forms.EmailField(max_length=30, required=True, label="Your email", widget= forms.TextInput(attrs={'placeholder':'Enter your email', 'class': 'w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm'}))
    phone_number = forms.CharField(max_length=20, label="Your phone number", required=False, widget= forms.TextInput(attrs={'placeholder':'Enter your phone number','class': 'w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm'}))
    country = forms.CharField(max_length=15, label="Country of residence", required=False, widget= forms.TextInput(attrs={'placeholder':'Enter your country name', 'class': 'w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm'}))
    
    # Customizing the username field
    username = forms.CharField(
        max_length=20, 
        label="Username", 
        help_text="Required. 20 characters or fewer. Letters, digits, and @/./+/-/_ only.", 
        widget=forms.TextInput(attrs={'placeholder': 'Enter a username', 'class': 'w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm'})
    )
    
    # Customizing password fields
    password1 = forms.CharField(
        label="Create a password", 
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter a password', 'class': 'w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm'}),
        help_text="Your password must contain at least 8 characters."
    )
    
    password2 = forms.CharField(
        label="Confirm your password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password', 'class': 'w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm'}),
        help_text="Enter the same password as above, for verification."
    )
    
    class Meta:
        model = User
        fields = ('name', 'last_name', 'username', 'email', 'country', 'phone_number', 'password1', 'password2')
        
    
    def save(self, commit=True):
        # Create the user
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password1'],
            email=self.cleaned_data['email'],
            last_name=self.cleaned_data['last_name']
        )
        
        if commit:
            # Save the User instance
            user.save()
            
            # Create the Person instance
            Person.objects.create(
                user=user,
                name=self.cleaned_data['name'],
                last_name=self.cleaned_data['last_name'],
                email=self.cleaned_data['email'],
                phone_number=self.cleaned_data['phone_number'],
                country=self.cleaned_data['country'],
                english_level='',  # Provide a default value or handle this field as needed
                plan_subscribed='',  # Provide a default value or handle this field as needed
                plan_status=False  # Provide a default value or handle this field as needed
            )
        
        return user
    
class SignInForm(AuthenticationForm):
    """ Form to sign in """
    
    username = forms.CharField(
        max_length=20,
        label="Username",
        widget=forms.TextInput(attrs={'placeholder': 'Enter your user name', 
                                      'class': 'w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm'})
    )
    
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'type':'password', 'placeholder': 'Enter your password', 
                                          'class': 'w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm'})
    )
    
    class Meta:
        fields = ('username', 'password')