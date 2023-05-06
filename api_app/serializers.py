from .models import Student
from rest_framework import serializers

# Student Serializer
class StudentSerializer(serializers.Serializer):
    """Student Serializer: it provides functionality serialization for:
        read operation, 
        create/insert data into db,
        update/alter existing data.
     
    """
    
    id   = serializers.IntegerField(required=False)   # id f    ields serializer
    name =  serializers.CharField(max_length=255)     # name    field serializer
    email =  serializers.EmailField()                 # email   fields serializer
    age   = serializers.IntegerField()                # age     fields serializer
    course =  serializers.CharField(max_length=255)   # course  fields serializer
    
    def validate(self, attrs):
        """Validate method to perform validation to validate fields."""
        keys = attrs.keys() # getting all dict keys here

        # validating name
        if 'name' in keys:
            name = str(attrs['name'])

            if len(name) < 7:
                raise serializers.ValidationError('Name must contains at least 7 characters')
        
        # validating email
        if 'email' in keys:
            email = str(attrs.get('email', None))

            if len(email) <11:
                raise serializers.ValidationError('Email must contains at least 11 characters')
        
        # validate age
        if 'age' in keys:

            age  = attrs.get('age', 0)

            if age<18:
                raise serializers.ValidationError('Student age must be greater or equal to 18')
        
        if 'course' in keys:
            course = str(attrs.get('course', None))

            if len(course) <3:
                raise serializers.ValidationError('Course name is invalid')
        
        return attrs

    def create(self, validated_data):
        """Create method to allow insertion/creation"""

        # creating model instance 
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """Update method to update models instance/data"""

        # self represent the current instance
        # instance represent the old data
        # validated_data: containing new data which coming for updation

        instance.name   =  validated_data.get('name', instance.name)
        instance.email  =  validated_data.get('email', instance.email)
        instance.age    =  validated_data.get('age', instance.age)
        instance.course =  validated_data.get('course', instance.course)
        
        # saving model instance here
        instance.save()
        return instance