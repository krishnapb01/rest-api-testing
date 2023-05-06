from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer

# Student API to handle get and post request without any url parameters
class StudentAPI(APIView):
    
    def get(self, request, format=None):
        all_students = Student.objects.all() # 
        serializer = StudentSerializer(all_students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {
                'msg': 'Student data successfuly inserted',
                'data': serializer.data
            }
            return Response(res, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Student API to handle [get, patch, put, delete] request with id  parameter is required
class StudentUpdateAPI(APIView):

    def get(self, request, id):

        try:
            student = Student.objects.get(pk=id)

        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        except Student.MultipleObjectsReturned:
            return Response(status=status.HTTP_207_MULTI_STATUS)

        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        else:
            serializer = StudentSerializer(student)
            res ={
                'student-details': serializer.data
            }
            return Response(res, status=status.HTTP_200_OK)
    
    def patch(self, request, id):
        """patch request for partially updation"""

        try:
            student = Student.objects.get(pk=id)

        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        except Student.MultipleObjectsReturned:
            return Response(status=status.HTTP_207_MULTI_STATUS)

        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        else:
            serializer = StudentSerializer(student, data = request.data, partial=True)

            if serializer.is_valid():
                serializer.save()

                res = {
                    'msg': 'Congrats! data successfuly updated',
                    'data': serializer.data
                }
                return Response(res, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        """PUT request for Complete updation"""

        try:
            student = Student.objects.get(pk=id)

        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        except Student.MultipleObjectsReturned:
            return Response(status=status.HTTP_207_MULTI_STATUS)

        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        else:
            serializer = StudentSerializer(student, data = request.data)

            if serializer.is_valid():
                serializer.save()

                res = {
                    'msg': 'Congrats! data successfuly updated',
                    'data': serializer.data
                }
                return Response(res, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """delete request for objects  deletion"""

        try:
            student = Student.objects.get(pk=id)

        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        except Student.MultipleObjectsReturned:
            return Response(status=status.HTTP_207_MULTI_STATUS)

        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        else:
            student.delete()


            res = {
                'msg': 'Deleted! data successfuly delete',
            }
            return Response(res, status=status.HTTP_204_NO_CONTENT)
            
