from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from .forms import ContactForm
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, "index.html")

def services(request):
    return render(request, "services.html")

def about(request):
    return render(request, "about.html")

def faq(request):
    return render(request, "faq.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save()
            subject = f"New Contact Message: {contact.subject}"
            body = f"""
Name: {contact.name}
Email: {contact.email}

Message:
{contact.message}
"""

            email = EmailMessage(
                subject=subject,
                body=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.ADMIN_EMAIL],
                reply_to=[contact.email],
            )

            try:
                email.send(fail_silently=False)
                messages.success(request, "Your message has been sent successfully!")
                return redirect("contact")

            except Exception:
                messages.error(request, "Email sending failed. Please try again later.")

    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            if user.groups.filter(name='Hospital').exists():
                return redirect('hospital:dashboard')

            # elif user.groups.filter(name='Laundry').exists():
            #     return redirect('laundary:dashboard')

            # elif user.groups.filter(name='Delivery').exists():
            #     return redirect('delivery:dashboard')

            else:
                messages.error(request, "No role assigned to this user")
                logout(request)

        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')




