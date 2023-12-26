from django import forms

class UserInfoForm(forms.Form):
    name = forms.CharField(max_length=100, required=True,
    widget=forms.TextInput(attrs={'class': 'contact__input', 'placeholder': 'Your full name'}))
    email = forms.EmailField(required=True,
    widget=forms.EmailInput(attrs={'class': 'contact__input', 'placeholder': 'example@gmail.com'}))
    message = forms.CharField(required=True,
    widget=forms.Textarea(attrs={'class': 'contact__input', 'placeholder': 'Message', 'cols': 30, 'rows': 10}))
