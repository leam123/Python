from django.urls import path
from . import views

app_name = 'pharmacy'
urlpatterns = [

    path('dashboard', views.DashboardView.as_view(), name="dashboard_view"),
    path('medicine_registration', views.MedicineRegistration.as_view(), name="medicine_registration_view"),
    path('index', views.LandingIndexView.as_view(), name="landing_index_view"),
    path('registration', views.CustomerRegistrationView.as_view(), name="customer_registration_view"),
    
]