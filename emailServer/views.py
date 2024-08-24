from django.http import HttpResponse
from django.views.generic import ListView,FormView
from django.core.mail import send_mail
from .forms import MyForm
from django.template.loader import render_to_string
from playground.models import MyModel
from django.core.mail import EmailMessage

class BasicEmailView(FormView, ListView):
    template_name = "content/email.html"
    context_object_name = 'mydata'
    success_url = "/"
    form_class = MyForm
    model = MyModel

    def form_valid(self, form):
        # Send email
        send_mail(
            "Macondo test Email",
            form.cleaned_data["message"],
            "moetezmaddouri@gmail.com",
            ["devwebconsulting@gmail.com"],
            fail_silently=False,
        )

        # Save form data to the database
        form.save()

        return super().form_valid(form)
    def sendEmail(request):
        templateMessage = "content/email_template.html"
        subject = "Macondo test Email"
        from_email = "moetezmaddouri@gmail.com"
        to_email = ["machatyahya@gmail.com","haythem.madouri@gmail.com","devwebconsulting@gmail.com"]
        # Example data to pass to the template
        temperature = 32  # Replace this with your actual temperature data

        # Prepare context data for the template
        context = {
            'temperature': temperature,
        }
        # Render the HTML template with context (if needed)
        html_message = render_to_string(templateMessage,context)

        # Create the email message
        email = EmailMessage(
            subject,
            html_message,
            from_email,
            to_email
        )
        email.content_subtype = "html"  # Set the content subtype to HTML

        # Send the email
        email.send(fail_silently=False)

        return HttpResponse("Email envoyée avec succès")
