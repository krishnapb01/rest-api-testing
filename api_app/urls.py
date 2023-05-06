from django.urls import path
from .views import StudentAPI, StudentUpdateAPI
# urlpatterns

urlpatterns = [
    path('student/', StudentAPI.as_view(), name='get_post_api'),
    path('student/<int:id>/', StudentUpdateAPI.as_view(), name='student_update_api'),

]