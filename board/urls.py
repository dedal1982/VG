from django.urls import path

from board import views


urlpatterns = [
    path("", views.ListingList.as_view(), name="listings"),
    path("detail/<int:year>/<int:month>/<int:day>/<slug:slug>/", views.get_detail, name="listing_detail"),
]