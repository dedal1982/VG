from django.urls import path

from city_app import views


urlpatterns = [
    path("catalog/", views.catalog_view, name="home"),
    path("", views.choose_city_view, name="city"),
    path("portfolio/", views.get_portfolio, name="portfolio"),
    path("portfolio/vmware-vsphere/", views.get_portfolio1, name="portfolio1"),
    path("portfolio/hunter-3d/", views.get_portfolio2, name="portfolio2"),
]
