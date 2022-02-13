from django.urls import path
from company import views
# create your urls path here
urlpatterns = [
    path('',views.index_landing,name='index'),
    path('company/',views.index,name='index_company'),
    path('register/',views.register,name='register_company'),
    path('login/',views.login,name='login_company'),
    path('logout/',views.logout,name='logout_company'),
    path('home/',views.home,name='home_company'),
    path('post/',views.post,name='post_company'),
    path('profile/',views.profile,name='profile_company'),
    path('search/',views.search,name='search'),
]