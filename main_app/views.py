import json
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.decorators.csrf import csrf_exempt

from .EmailBackend import EmailBackend
from functools import wraps
from django.shortcuts import redirect, reverse

from django.contrib.auth import logout
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth import logout

from django.contrib.auth import logout

from django.contrib.auth import logout

from functools import wraps
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .EmailBackend import EmailBackend

def require_fee_payment(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user = request.user

        if user.is_authenticated and user.user_type == '3':  # Assuming 'user_type' identifies a student
            if not user.has_paid_fees() and user.payment_required:
                # Reset the payment_required flag
                user.payment_required = False
                user.save()

                # Logout the user and terminate the session
                logout_user(request)

                return redirect(reverse_lazy('payment_required'))  # Redirect to a payment page or an error page

        # Check and update payment status during each request
        if user.is_authenticated and not user.has_paid_fees():
            # Logout the user and terminate the session
            logout_user(request)

            return redirect(reverse_lazy('payment_required'))  # Redirect to a payment page or an error page

        return view_func(request, *args, **kwargs)

    return wrapper



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

@require_fee_payment
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