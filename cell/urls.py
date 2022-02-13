from django.urls import path
from cell import views

# create your urls path here
urlpatterns=[
    path('',views.index,name='index_cell'),
    path('register/',views.register,name='register_cell'),
    path('login/',views.login,name='login_cell'),
    path('logout/',views.logout,name='logout_cell'),
    path('home/',views.home,name='home_cell'),
    path('post/',views.post,name='post_cell'),
    path('profile/',views.profile,name='profile_cell'),
]