
from django import forms

class PreRegistroForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={"id": "email", "placeholder": "Informe o seu endereço de e-mail"}
    ))
