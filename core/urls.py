from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_redirect, name='home'),
    path('form/', views.employee_form, name='employee_form'),
    path('dashboard/', views.grh_dashboard, name='grh_dashboard'),
    path('send-email/', views.send_email_interface, name='send_email_interface'),
    path('download-report/', views.download_report_pdf, name='download_report'),  # ✅ nouveau chemin
]
