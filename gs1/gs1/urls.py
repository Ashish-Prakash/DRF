from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentinfo/<int:pk>/', views.students_detail),
    path('studentinfo/', views.student_list),
]
