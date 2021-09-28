from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from specials import views

urlpatterns = [
    path('specials/', views.special_list),
    path('specials/<int:pk>/', views.special_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)