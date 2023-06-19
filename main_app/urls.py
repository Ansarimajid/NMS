"""college_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import hod_views, staff_views, student_views, views

urlpatterns = [
     path("", views.login_page, name='login_page'),
     path("doLogin/", views.doLogin, name='user_login'),
     path("logout_user/", views.logout_user, name='user_logout'),
     path("admin/home/", hod_views.admin_home, name='admin_home'),
     path("staff/add", hod_views.add_staff, name='add_staff'),
     path("admin_view_profile", hod_views.admin_view_profile,name='admin_view_profile'),
     path("check_email_availability", hod_views.check_email_availability,name="check_email_availability"),
     path("student/add/", hod_views.add_student, name='add_student'),
     path("staff/manage/", hod_views.manage_staff, name='manage_staff'),
     path("student/manage/", hod_views.manage_student, name='manage_student'),
     path("staff/edit/<int:staff_id>", hod_views.edit_staff, name='edit_staff'),
     path("staff/delete/<int:staff_id>",hod_views.delete_staff, name='delete_staff'),
     path("student/delete/<int:student_id>",hod_views.delete_student, name='delete_student'),
     path("student/edit/<int:student_id>",hod_views.edit_student, name='edit_student'),
     path('payment-required/', views.payment_required, name='payment_required'),
     path('changestatus/<int:student_id>/', hod_views.change_payment_status, name='change_payment_status'),
          path('admin/upload_notes/', hod_views.upload_note, name='upload_note'),


     # Staff
     path("staff/home/", staff_views.staff_home, name='staff_home'),
     path("staff/view/profile/", staff_views.staff_view_profile,name='staff_view_profile'),



     # Student
     path("student/home/", student_views.student_home, name='student_home'),
     path("student/view/profile/", student_views.student_view_profile,name='student_view_profile'),
    path('student/view_notes/', student_views.view_notes, name='view_notes'),
]
