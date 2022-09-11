# thư viện (class) serializers: nơi chứa các function chuyển đổi data từ front-end(json) đến database
# hoặc data từ models thành json cho front-end/ hoặc các hệ thống khác....
# nói chùng: serialize là nơi chuyển đổi dữ liệu


from dataclasses import field
from http import server
from rest_framework import serializers
from .models import Course

class GetAllCourseSerializer(serializers.ModelSerializer): # tạo class kế thừa từ serializers

    class Meta:
        model = Course  # truyền vào model muốn đưa dữ liệu vào để trả vào cho client -> chính là model đã tạo trong models.py
        fields = '__all__' 
         # truyền vào những field muốn đầy vào cho client

class CourseSerializer(serializers.Serializer):
    title1 = serializers.CharField(max_length=255)
    content1 = serializers.CharField(max_length=255)
    price1 = serializers.IntegerField()
