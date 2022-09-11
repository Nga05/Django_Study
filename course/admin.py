from django.contrib import admin
from .models import Course

# Register your models here.
admin.site.register(Course)  # register model ở đây để dễ dàng inser data vào bằng giao diện trên admin


# sau khi register cần chạy lệnh: python manage.py createsuperuser
# đang nhập vào admin để chỉnh sửa bằng username và passworld

