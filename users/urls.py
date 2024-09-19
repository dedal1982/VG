from users import views
from django.urls import path

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    # path("test/", views.test_form_view, name="test"),
]
