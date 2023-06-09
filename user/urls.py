
from django.urls import path
from . import views
from .views import *
app_name='userurl'
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signupView, name='signup'),
    path('login/', views.loginView, name='login'),
 
    path('logout/', views.logout_view, name='logout'),

    path('Error/', views.myinvest, name='bad'),
   
    path('gain/<id>/', views.gain, name='gain'),
    path('upgrade/', views.plan, name='plan'),
    path('starts/', views.star, name='star'),
    path('superverse/', views.super, name='super'),
    path('trade/', views.trade, name='trade'),
    path('trade-log/', views.tralog, name='trade-log'),
    path('withdraw/', views.withdraw, name='with'),
    path('otp/', views.reotp, name='otp'),
    path('explore/', views.exp, name='exp'),
  
    path('deposit/', views.fund, name='depo'),
    path('payments/<slug>/', views.myfund, name='payment'),
    path('activate-user/<uidb64>/<token>', views.activate_user, name='activate'),
    path('change_password/', views.change_password, name='change_password'),
	path('change_password_confirm/', views.change_password_confirm, name='change_password_confirm'),
	path('<slug:pk>', views.change_password_code, name='change_password_code'),
	path('change_password_success/', views.change_password_success, name='change_password_success'),
   

    
]