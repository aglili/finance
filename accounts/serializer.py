from rest_framework import serializers
from .models import CustomUser 
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



class UserSignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email', 'occupation', 'date_of_birth', 'address', 'income', 'savings', 'password']


    def validate(self, data):
        if CustomUser.objects.filter(username=data['username']).exists():
            return serializers.ValidationError({"error":"UserName Already Exists"})
        return data
    
    def create(self, validated_data):
        user = CustomUser.objects.create(first_name=validated_data['first_name'],last_name=validated_data['last_name'],
                                             username=validated_data['username'],email=validated_data['email'],occupation=validated_data['occupation'],
                                             address=validated_data['address'],income=validated_data['income'],savings=validated_data['savings'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ['username','password']

    def validate(self, data):
        if not CustomUser.objects.filter(username=data['username']).exists():
            return serializers.ValidationError({"error":"User Does Not Exist"})
        return data
    
    def get_jwt_token(self,data):

        user = authenticate(username=data['username'],password=data['password'])

        if not user:
            return serializers.ValidationError({"error":"Invalid Login Credentials","data":{}})
        
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            "message":"Login SucessFul"
        }
        


    
