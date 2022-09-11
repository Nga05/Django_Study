from os import stat
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response   # Response tar3 về dữ liệu, dữ liệu dc đưa vào Serialize để parse
from rest_framework import status
from .models import Course
from .serializers import GetAllCourseSerializer , CourseSerializer
# Create your views here.

class GetAllCoursesAPIView(APIView):

    def get(self, request):  # hàm get data từ dabase và hiển thị lên front-end theo request từ phía client
        list_course = Course.objects.all()
        mydata = GetAllCourseSerializer(list_course, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK) # response trả vè dữ liệu và status của response

    def post(self, request):  # hàm bắt dữ liệu từ phía client và post vào database
        mydata = CourseSerializer(data=request.data)
        if not mydata.is_valid():
            return Response('Dữ liệu sai rồi', status=status.HTTP_400_BAD_REQUEST)  # gọi hàm để lấy dữ liệu từ client gửi tới
        title = mydata.data['title1']
        price = mydata.data['price1']
        content = mydata.data['content1']
        cs = Course.objects.create(title=title, price=price, content=content)
        return Response(data=cs.id, status=status.HTTP_200_OK)


# đường đi của dữ liệu khi có request từ phía client
# lấy từ models -> serialize -> response