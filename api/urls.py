from django.urls import path  # type: ignore
from . import views

urlpatterns = [
    # function based View url pattern
    path('students/', views.studentsView),
    path('students/<int:pk>/',views.studentDetailView),

    #class based view url pattern
    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
]