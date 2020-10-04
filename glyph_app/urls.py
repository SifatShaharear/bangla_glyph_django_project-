from django.urls import path
from . import views

urlpatterns = [
    # path('ln/<letter>/', views.HomeView.as_view(), name='home'),
    path('ln/<str:inletter>/',views.letter_detail_view),
]
