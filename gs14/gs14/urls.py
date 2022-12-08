from django.contrib import admin
from django.urls import path
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.LCStudent.as_view()),
    path('studentapi/<int:pk>', views.RUDStudent.as_view()),
]
