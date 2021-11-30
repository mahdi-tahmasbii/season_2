from django.shortcuts import render, redirect
from .forms import CreateContactForm
from .models import ContactUs, ContactInfo, AboutUs


# Create your views here.


def contact_us(request):
    contact_form = CreateContactForm(request.POST or None)
    if contact_form.is_valid():
        full_name = contact_form.cleaned_data['full_name']
        email = contact_form.cleaned_data['email']
        subject = contact_form.cleaned_data['subject']
        text = contact_form.cleaned_data['text']
        ContactUs.objects.create(full_name=full_name, email=email, subject=subject, text=text, is_read=False)
        contact_form = CreateContactForm()
        return redirect('/')

    contact_info = ContactInfo.objects.first()

    context = {
        'contact_form': contact_form,
        'contact_info': contact_info
    }

    return render(request, 'contact_us/contact_us.html', context)


def about_us(request):
    about = AboutUs.objects.first()
    context = {
        'about': about
    }
    return render(request, 'about_us/about_us.html', context)
