from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("djangoapp/get_dealers/", views.get_dealers, name="get_dealers"),
    path("djangoapp/dealer/<int:dealer_id>/", views.get_dealer_by_id, name="get_dealer_by_id"),
    path("djangoapp/get_dealers/<str:state>/", views.get_dealers_by_state, name="get_dealers_by_state"),
    path("djangoapp/dealer/<int:dealer_id>/reviews/", views.get_dealer_reviews, name="get_dealer_reviews"),
]
