from . import views
from django.urls import path

app_name='bankapp'


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('userhome',views.userhome,name='userhome'),
    path('application_form/',views.application_form,name='application_form'),
    # path('',views.district,name='district'),
    path('ajax/load_branch/',views.load_branch,name='ajax_load_branch'),
    path('message',views.message,name='message'),
    path('logout',views.logout,name='logout'),
]