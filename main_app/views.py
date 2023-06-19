import json
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.decorators.csrf import csrf_exempt

from .EmailBackend import EmailBackend


def login_page(request):
    if request.user.is_authenticated:
        if request.user.user_type == '1':
            return redirect(reverse("admin_home"))
        elif request.user.user_type == '2':
            return redirect(reverse("staff_home"))
        elif request.user.user_type == '3':
            if request.user.has_paid_fees():  # Assuming 'has_paid_fees' method is implemented in your User or Student model
                return redirect(reverse("student_home"))
            else:
                return redirect(reverse("payment_required"))  # Redirect to a payment page or an error page
    return render(request, 'main_app/login.html')


def doLogin(request, **kwargs):
    if request.method != 'POST':
        return HttpResponse("<h4>Denied</h4>")
    else:
        # Authenticate
        user = EmailBackend.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            if user.user_type == '1':
                return redirect(reverse("admin_home"))
            elif user.user_type == '2':
                return redirect(reverse("staff_home"))
            elif user.user_type == '3':
                if user.has_paid_fees():  # Assuming 'has_paid_fees' method is implemented in your User or Student model
                    return redirect(reverse("student_home"))
                else:
                    return redirect(reverse("payment_required"))  # Redirect to a payment page or an error page
        else:
            messages.error(request, "Invalid details")
            return redirect("/")

def payment_required(request):
    return HttpResponse("payment Required")


def logout_user(request):
    if request.user is not None:
        logout(request)
    return redirect("/")