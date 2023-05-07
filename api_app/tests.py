from django.test import TestCase,Client
from django.urls import reverse
import random, json

from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

ok_response = status.HTTP_200_OK
bad_request = status.HTTP_400_BAD_REQUEST
created     = status.HTTP_201_CREATED
not_found   = status.HTTP_404_NOT_FOUND
no_content  = status.HTTP_204_NO_CONTENT

get_or_post = 'get_post_api'
update_delete_get = 'student_update_api'

# client creation
client = Client()

base_url = 'http://127.0.0.1:8000/api/student/'

class SetUpStudentTestAPI(TestCase):

    def setUp(self):
        """Basic SetUp for testing api"""
        
        # content type
        self.content_type = {
            'application/json'
        }

        
        # valid payload
        self.valid_payload = {
            "name": "Sivani",
            "email": 'sivani@gmail.com',
            "age": 24,
            "course": "Web Security"
        }

        #invalid payload1 
        self.invalid_payload1 = {
            "name": "Sivani",
            "email": 'sivani@gmail.com',
            "age": 24,
            "course": "Web Security"
        }

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
     
class GetAllStudentTest(SetUpStudentTestAPI):
    """Testing all student means get request to get all students data"""

    def test_get_all_stus(self):

        response = client.get(reverse(get_or_post))

        # check status code
        self.assertEqual(response.status_code, ok_response)

        
        # get data from db
        studs = Student.objects.all()

        # serializer them
        serializer = StudentSerializer(studs, many=True)

        # print(response.data)
        # print(serializer.data)


        # chekcing response body content here
        self.assertEqual(response.data, serializer.data)

class GetSingleStudentTest(SetUpStudentTestAPI):
    """Test Student Details Page valid and invalid as well"""

    def test_valid_single_stu(self, pk=None):
        if not pk:
            # pk = 1
            pk = random.choice(self.stu_ids)

        # print(f'\nprimary key is: {pk}')

         # making request to endpoints
        response = client.get(reverse(update_delete_get, kwargs={
                                                            'id': pk
                                                            }))
        # status check
        self.assertEqual(response.status_code, ok_response)

        # getting stu from db
        try: 
            stus = Student.objects.get(pk=pk)
        except:
            pass
        else:
            
            serializer = StudentSerializer(stus)

            serializer_data = {
                'student-details': serializer.data
            }

            # checking response data
            self.assertEqual(response.data, serializer_data)

    def test_invalid_single_stu(self):
        """Invalid Student Details test here"""
        pk = 100

        response = client.get(reverse(update_delete_get, kwargs={
            'id': pk
        }))

        try:
            stus = Student.objects.get(pk=pk)
        except:
            # there must be StudentDoesNot Exists Exception Occurs
            not_exists = not_found
        else:
            not_exists = False
        
        finally:
            self.assertEqual(response.status_code, not_exists)

            # self.assertEqual(response.status_code, not_found)
        
class TestUpdateStudentAPI(SetUpStudentTestAPI):

    def test_valid_stu_update(self):
        valid_id = random.choice(self.stu_ids)
        
        
        # here update request is going
        response = client.patch(reverse(update_delete_get, kwargs={
            'id': valid_id # update student age
        }))

        # check status
        self.assertEqual(response.status_code, ok_response)


        try:
            student = Student.objects.get(pk=valid_id)
        except:
            pass
        else:
            # student not be none
            self.assertIsNotNone(student) 
            
            # serialization
            serializer = StudentSerializer(student)

class PostStudentTest(SetUpStudentTestAPI):

    def test_valid_insertion(self):
        stu_data = {
            "name" :"Sivani Singh",
            "email": "sivani123@gmail.com",
            "age": 24,
            "course" :"Django"
        }

        data = json.dumps(stu_data)

        response = client.post(reverse(get_or_post), data=data, content_type='application/json')

        # check status
        self.assertEqual(response.status_code, created)

        # getting inserted student id so that we can check inserted data is inserted accuratly
        inserted_pk = response.data['data']['id']
        
        # checking that its exists in
        GetSingleStudentTest().test_valid_single_stu(pk=inserted_pk)

        # checking db data is same as provided data for insertion

        all_data = response.data['data']
        del  all_data['id']

        
        # for stu in all_data:
        #     # self.assertEqual(stu_data['name'], )
        #     # print(all_data[stu], type(stu), stu_data[stu])
        #     self.assertEqual(all_data[stu], stu_data[stu])

        all_data_same = [
                        self.assertEquals(all_data[stu], stu_data[stu]) 
                        for stu in all_data
                        ]



      


        



        
       

