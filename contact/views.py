from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm


# Create your views here.
def contact(request):
    """ A view to show the contact page form """

    if request.method == 'POST':
        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        }
        contact_form = ContactForm(form_data)

        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Message sent successfully!')
            return redirect(reverse('contact'))
        else:
            messages.error(request, 'Message failed to send. Check if form is valid.')
    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'contact/contact.html', context)
