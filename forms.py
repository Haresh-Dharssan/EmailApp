from django import forms
from django.forms import ModelForm, DateInput
from django.contrib.auth.models import User
from .models import Emails

class EmailForm(ModelForm):
    email = forms.EmailField(label="Email", required=True)
    subject = forms.CharField(label='Subject',max_length=500,required=True)
    message = forms.CharField(label='Message',max_length=1000,required=True)
   
    class Meta:
      model = Emails
      exclude = ['created_at','edited_at','message','subject']