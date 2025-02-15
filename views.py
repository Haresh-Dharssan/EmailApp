from .forms import EmailForm
from .models import Emails
from django.contrib import messages
from django.views.generic import ListView,FormView
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.models import User

class BasicEmailView(FormView, ListView):
    template_name = "emailapp/home.html"
    context_object_name = 'mydata'
    model = Emails
    form_class = EmailForm
    success_url = "/email"

    def form_valid(self, form):
        my_subject=form.cleaned_data['subject']
        my_message=form.cleaned_data['message']
        my_recipent=form.cleaned_data['email']

        send_mail(
            subject=my_subject,
            message=my_message,
            from_email=None,
            recipient_list=[my_recipent],
            fail_silently=False
        )
        messages.success(self.request,'Successfully Sent The Message!')

        obj = Emails(
            subject=my_subject,
            message=my_message,
            email=my_recipent
        )
        obj.save()

        return super().form_valid(form)


