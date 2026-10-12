from django.urls import path,include  # type: ignore
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees',views.EmployeeViewset, basename='employee')

urlpatterns = [
    # function based View url pattern
    path('students/', views.studentsView),
    path('students/<int:pk>/',views.studentDetailView),

    #class based view url pattern
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
    path('',include(router.urls))
]