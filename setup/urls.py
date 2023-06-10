from django.contrib import admin
from django.urls import path, include
from escola.views import StudentsViewSet, CoursesViewSet, RegistrationsViewSet, ListRegistrationsStudent, ListStudentRegistrations, ListCourseLevels, ListRegistrationPeriod, RegisterView, UserTokenObtainPairView
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView


router = routers.DefaultRouter()
router.register('Students', StudentsViewSet, basename='Students')
router.register('Courses', CoursesViewSet, basename='Courses')
router.register('Registrations', RegistrationsViewSet,
                basename='Registrations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('student/<int:pk>/matriculas/', ListRegistrationsStudent.as_view()),
    path('course/<int:pk>/matriculas/', ListStudentRegistrations.as_view()),
    path('course/levels/', ListCourseLevels.as_view()),
    path('registration/periods/', ListRegistrationPeriod.as_view()),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', UserTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh')

]
