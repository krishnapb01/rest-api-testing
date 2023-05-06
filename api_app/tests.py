from django.test import TestCase,Client
from django.urls import reverse

from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

ok_response = status.HTTP_200_OK
bad_request = status.HTTP_400_BAD_REQUEST
created     = status.HTTP_201_CREATED
not_found   = status.HTTP_404_NOT_FOUND
no_content  = status.HTTP_204_NO_CONTENT

get_or_post = 'get_post_api'

# client creation
client = Client()

base_url = 'http://127.0.0.1:8000/api/student/'

class StudentAPITest(TestCase):

    def setUp(self):
        names = ('krishna', 'aman', 'ankit', 'rohan')
        courses = ('Python', 'Django', 'React JS', 'AWS')
        ages    = (21,23,32,24)

        # creating/setup models instance to test them
        self.stu_ids = []

        for i in range(4):
            name = names[i]     # getting name
            course = courses[i] # getting course
            age    = ages[i]    # getting age
            email  = name+'@gmail.com' # getting email

            obj = Student.objects.create(name=name, course=course, email=email, age=age)
            
            # storing their pk for testing purpose
            self.stu_ids.append(obj.pk)
    
    def test_get_request(self):
        response = client.get(reverse(get_or_post))

        print(response.content)