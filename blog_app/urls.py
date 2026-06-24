from django.urls import path
from . import views
from .forms import StyledAuthenticationForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('auth/', views.auth_gate, name='auth_gate'),
    path('signup/', views.signup, name='signup'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html',
            authentication_form=StyledAuthenticationForm,
            redirect_authenticated_user=True
        ),
        name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('category/<int:pk>/', views.category_posts, name='category_posts'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('like/<int:pk>/', views.add_like, name='add_like'),
    path('comment/<int:pk>/', views.add_comment, name='add_comment'),
]