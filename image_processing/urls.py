
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_page, name='upload_page'),  # صفحه آپلود
    path('upload/image/process/', views.upload_image, name='upload_image'),  # پردازش تصویر
    path('change_lip_size/', views.change_lip_size_view, name='change_lip_size'),
]

