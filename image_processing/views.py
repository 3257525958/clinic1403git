from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
import cv2
import numpy as np
import os


def upload_page(request):
    """ نمایش صفحه آپلود تصویر """
    return render(request, 'upload.html')


from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os

def upload_image(request):
    """ دریافت و تحلیل تصویر آپلود شده """
    if request.method == 'POST' and request.FILES.get('image'):
        try:
            # دریافت فایل آپلود شده
            uploaded_file = request.FILES['image']

            # ذخیره تصویر در پوشه media
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_path = os.path.join(fs.location, filename)

            # تحلیل تصویر و مشخص کردن نقاط چهره
            annotated_image_path = analyze_face(file_path)
            annotated_image_url = fs.url(os.path.basename(annotated_image_path))

            # نمایش نتیجه به کاربر
            return render(request, 'result.html', {'annotated_image_url': annotated_image_url})

        except Exception as e:
            return render(request, 'error.html', {'error_message': f"خطا در تحلیل تصویر: {str(e)}"})

    return render(request, 'error.html', {'error_message': "درخواست نامعتبر"})
import cv2
import mediapipe as mp

def analyze_face(image_path):
    # بارگذاری عکس
    image = cv2.imread(image_path)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # استفاده از Mediapipe Face Mesh
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, refine_landmarks=True)

    # پردازش عکس
    results = face_mesh.process(rgb_image)

    # اگر چهره تشخیص داده شد
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # رسم نقاط کلیدی روی عکس
            mp_drawing = mp.solutions.drawing_utils
            mp_drawing.draw_landmarks(
                image=image,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_CONTOURS,
                landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
                connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1)
            )

    # ذخیره عکس پردازش شده
    output_path = image_path.replace('.jpg', '_processed.jpg')
    cv2.imwrite(output_path, image)

    return output_path
# ********************************************************************
# import cv2
# import mediapipe as mp
#
# def analyze_face_with_more_landmarks(image_path):
#     # بارگذاری عکس
#     image = cv2.imread(image_path)
#     rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#
#     # استفاده از Mediapipe Face Mesh
#     mp_face_mesh = mp.solutions.face_mesh
#     face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, refine_landmarks=True)
#
#     # پردازش عکس
#     results = face_mesh.process(rgb_image)
#
#     # اگر چهره تشخیص داده شد
#     if results.multi_face_landmarks:
#         for face_landmarks in results.multi_face_landmarks:
#             # رسم نقاط کلیدی روی عکس
#             mp_drawing = mp.solutions.drawing_utils
#             mp_drawing.draw_landmarks(
#                 image=image,
#                 landmark_list=face_landmarks,
#                 connections=mp_face_mesh.FACEMESH_CONTOURS,  # نقاط کلیدی صورت
#                 landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
#                 connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1)
#             )
#
#     # ذخیره عکس پردازش شده
#     output_path = image_path.replace('.jpg', '_more_landmarks.jpg')
#     cv2.imwrite(output_path, image)
#
#     return output_path


#
# -------------------------------------------لب-------------------------------------------------
import cv2
import mediapipe as mp
import numpy as np

def change_lip_size(image_path, scale=1.5):
    # بارگذاری عکس
    image = cv2.imread(image_path)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # استفاده از Mediapipe Face Mesh
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, refine_landmarks=True)

    # پردازش عکس
    results = face_mesh.process(rgb_image)

    # اگر چهره تشخیص داده شد
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # تشخیص نقاط لب‌ها (لیندمارک‌های 61 تا 80 و 291 تا 308)
            lip_points = []
            for idx in range(61, 81):  # لب بالا
                lip_points.append((face_landmarks.landmark[idx].x, face_landmarks.landmark[idx].y))
            for idx in range(291, 309):  # لب پایین
                lip_points.append((face_landmarks.landmark[idx].x, face_landmarks.landmark[idx].y))

            # تبدیل نقاط به مختصات تصویر
            h, w, _ = image.shape
            lip_points = [(int(x * w), int(y * h)) for x, y in lip_points]

            # ایجاد ماسک برای لب‌ها
            mask = np.zeros((h, w), dtype=np.uint8)
            cv2.fillPoly(mask, [np.array(lip_points)], 255)

            # بزرگ‌تر کردن لب‌ها
            lip_region = cv2.bitwise_and(image, image, mask=mask)
            lip_region = cv2.resize(lip_region, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)

            # جایگزینی لب‌های بزرگ‌تر در عکس اصلی
            x, y, _ = lip_region.shape
            center_x = sum(p[0] for p in lip_points) // len(lip_points)
            center_y = sum(p[1] for p in lip_points) // len(lip_points)
            start_x = center_x - x // 2
            start_y = center_y - y // 2
            image[start_y:start_y + y, start_x:start_x + x] = lip_region

    # ذخیره عکس پردازش شده
    output_path = image_path.replace('.jpg', '_lip_resized.jpg')
    cv2.imwrite(output_path, image)

    return output_path


from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import os

def change_lip_size_view(request):
    if request.method == 'POST':
        try:
            # دریافت مسیر عکس
            image_url = request.POST.get('image_path')
            fs = FileSystemStorage()
            image_path = os.path.join(fs.location, os.path.basename(image_url))

            # تغییر حجم لب‌ها
            resized_image_path = change_lip_size(image_path)
            resized_image_url = fs.url(os.path.basename(resized_image_path))

            # نمایش نتیجه به کاربر
            return render(request, 'result.html', {'annotated_image_url': resized_image_url})

        except Exception as e:
            return render(request, 'error.html', {'error_message': f"خطا در تغییر حجم لب: {str(e)}"})

    return redirect('upload_page')