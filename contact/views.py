from django.shortcuts import render
from .forms import ContactForm


# Create your views here.
def contact(request):
    """ A view to show the contact page form """

    contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'contact/contact.html', context)
