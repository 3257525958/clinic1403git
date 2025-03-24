# import cv2
import numpy as np
import os
from django.conf import settings
import subprocess
subprocess.run(['git', 'clone', 'https://github.com/CoinCheung/BiSeNet.git'])

# تعریف مسیر مدل BiSeNet
BISENET_MODEL_PATH = os.path.join(settings.BASE_DIR, 'models', 'bisenet.pth')


def analyze_face_bisenet(image_path):
    if 1 == 2 :
        import torch
        # from PIL import Image
        # from torchvision import transforms
        #
        # # اطمینان از تعریف متغیر BISENET_MODEL_PATH (مثلاً به صورت global)
        # # BISENET_MODEL_PATH = os.path.join(settings.BASE_DIR, 'models', 'bisenet.pth')
        #
        # # بارگذاری مدل (بر روی CPU)
        # model = torch.load(BISENET_MODEL_PATH, map_location=torch.device('cpu'))
        # model.eval()
        #
        # # بارگذاری و آماده‌سازی تصویر با PIL
        # image_pil = Image.open(image_path).convert('RGB')
        # transform = transforms.Compose([
        #     transforms.Resize((512, 512)),  # تغییر اندازه به 512x512
        #     transforms.ToTensor(),
        #     transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
        # ])
        # input_image = transform(image_pil).unsqueeze(0)
        #
        # # پردازش تصویر توسط مدل BiSeNet
        # with torch.no_grad():
        #     seg_output = model(input_image)[0]  # فرض می‌کنیم خروجی مدل یک tensor است
        #     seg_map = seg_output.argmax(0).byte().cpu().numpy()
        #
        # # تبدیل تصویر اصلی به آرایه numpy (برای رسم نقاط)
        # image_np = np.array(image_pil.resize((512, 512)))
        #
        # # لیست کلاس‌هایی که می‌خواهیم مرزهایشان را مشخص کنیم
        # # (بر اساس آموزش مدل؛ شما می‌توانید این لیست را مطابق با نیاز تغییر دهید)
        # labels_of_interest = [1, 2, 3, 4, 5, 6]
        #
        # # برای هر کلاس، ماسک بگیرید و مرزها (contours) را پیدا کنید
        # for label in labels_of_interest:
        #     mask = np.uint8((seg_map == label) * 255)
        #     contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #     # رسم نقاط (دایره‌های کوچک) سبز بر روی نقاط مرز
        #     for cnt in contours:
        #         for point in cnt:
        #             x, y = point[0]
        #             cv2.circle(image_np, (x, y), radius=1, color=(0, 255, 0), thickness=-1)
        #
        # # ذخیره تصویر نهایی با نقاط مرزی
        # output_path = image_path.replace('.jpg', '_bisenet_annotated.jpg')
        # cv2.imwrite(output_path, cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR))

    return output_path



def upload_page(request):
    """ نمایش صفحه آپلود تصویر """
    return render(request, 'upload.html')



def preprocess_image(image_path, target_size=(512, 512)):
    # خواندن تصویر
    image = cv2.imread(image_path)

    # تبدیل به فضای رنگی RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # تغییر اندازه تصویر
    image = cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)

    # کاهش نویز و افزایش وضوح
    image = cv2.GaussianBlur(image, (3, 3), 0)

    # ذخیره تصویر پردازش‌شده موقت
    temp_image_path = image_path.replace('.jpg', '_preprocessed.jpg')
    cv2.imwrite(temp_image_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

    return temp_image_path


import os
import requests
import hashlib

def download_file(url, save_path, chunk_size=1024):
    response = requests.get(url, stream=True)
    response.raise_for_status()  # در صورت بروز خطا، exception ایجاد می‌کند
    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:  # اگر chunk خالی نباشد
                file.write(chunk)
    print(f"11111111111111 '{save_path}'")


def calculate_sha256(file_path, chunk_size=4096):
    hash_sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()


if 1 == 2:
    print("kkkkkkkkkkkkkkkkkkkkkkkkkkkk")
    url = "https://huggingface.co/maze/faceX/resolve/main/bisenet.pth"
    save_dir = "models"
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, "bisenet.pth")

    # دانلود فایل
    download_file(url, save_path)

    # محاسبه هش SHA256
    sha256_hash = calculate_sha256(save_path)
    print("SHA256 222222222222222:", sha256_hash)

    # مقایسه با هش معتبر
    valid_sha256 = "468e13ca13a9b43cc0881a9f99083a430e9c0a38abd935431d1c28ee94b26567"
    if sha256_hash == valid_sha256:
        print("valid")
    else:
        print("invalid")


from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import os

# def change_lip_size_view(request):
#     if request.method == 'POST':
#         try:
#             # دریافت مسیر عکس
#             image_url = request.POST.get('image_path')
#             fs = FileSystemStorage()
#             image_path = os.path.join(fs.location, os.path.basename(image_url))
#
#             # تغییر حجم لب‌ها
#             resized_image_path = change_lip_size(image_path)
#             resized_image_url = fs.url(os.path.basename(resized_image_path))
#
#             # نمایش نتیجه به کاربر
#             return render(request, 'result.html', {'annotated_image_url': resized_image_url})
#
#         except Exception as e:
#             return render(request, 'error.html', {'error_message': f"خطا در تغییر حجم لب: {str(e)}"})
#
#     return redirect('upload_page')

def upload_image(request):
    """ دریافت و تحلیل تصویر آپلود شده """
    if request.method == 'POST' and request.FILES.get('image') and (1 == 2):
        try:
            # دریافت فایل آپلود شده
            uploaded_file = request.FILES['image']
            # ذخیره تصویر در پوشه media
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_path = os.path.join(fs.location, filename)

            # پیش‌پردازش تصویر (بهینه‌سازی سایز و کیفیت)
            preprocessed_image_path = preprocess_image(file_path)

            # تحلیل تصویر و مشخص کردن نقاط چهره با BiSeNet
            annotated_image_path = analyze_face_bisenet(preprocessed_image_path)
            # # تحلیل تصویر و مشخص کردن نقاط چهره
            # annotated_image_path = analyze_face(preprocessed_image_path)
            annotated_image_url = fs.url(os.path.basename(annotated_image_path))

            # نمایش نتیجه به کاربر
            return render(request, 'result.html', {'annotated_image_url': annotated_image_url})

        except Exception as e:
            return render(request, 'error.html', {'error_message': f"خطا در تحلیل تصویر: {str(e)}"})

    return render(request, 'error.html', {'error_message': "درخواست نامعتبر"})

# def analyze_face_bisenet(image_path):
#     import torch
#
#     model = torch.load(BISENET_MODEL_PATH, map_location=torch.device('cpu'))
#     # model = load_bisenet_model()
#
#     # بارگذاری تصویر و تبدیل به فرمت مناسب
#     image = Image.open(image_path).convert('RGB')
#     transform = transforms.Compose([
#         transforms.Resize((512, 512)),  # تغییر اندازه تصویر
#         transforms.ToTensor(),
#         transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
#     ])
#     input_image = transform(image).unsqueeze(0)
#
#     # پردازش تصویر با مدل
#     with torch.no_grad():
#         output = model(input_image)[0].argmax(0).byte().cpu().numpy()
#
#     # تبدیل خروجی مدل به تصویر
#     segmented_image = np.zeros_like(output, dtype=np.uint8)
#
#     # اختصاص رنگ‌های مشخص به بخش‌های مختلف چهره
#     colors = {
#         1: (0, 255, 0),   # پوست صورت
#         2: (255, 0, 0),   # ابرو
#         3: (0, 0, 255),   # چشم‌ها
#         4: (255, 255, 0), # لب
#         5: (255, 0, 255), # بینی
#         6: (0, 255, 255)  # گونه‌ها و چانه
#     }
#
#     for label, color in colors.items():
#         segmented_image[output == label] = color
#
#     # ترکیب تصویر اصلی با بخش‌های تشخیص داده شده
#     image = np.array(image.resize((512, 512)))
#     result = cv2.addWeighted(image, 0.6, segmented_image, 0.4, 0)
#
#     # ذخیره تصویر پردازش‌شده
#     output_path = image_path.replace('.jpg', '_bisenet.jpg')
#     cv2.imwrite(output_path, cv2.cvtColor(result, cv2.COLOR_RGB2BGR))
#
#     return output_path


# def change_lip_size(image_path, scale=1.3):
#     # بارگذاری عکس از مسیر
#     image = cv2.imread(image_path)
#     if image is None:
#         raise ValueError("تصویر در مسیر داده شده یافت نشد!")
#     h, w = image.shape[:2]
#
#     # استفاده از Mediapipe Face Mesh
#     mp_face_mesh = mp.solutions.face_mesh
#     face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, refine_landmarks=True)
#
#     # پردازش تصویر
#     results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#
#     if results.multi_face_landmarks:
#         for face_landmarks in results.multi_face_landmarks:
#             # تشخیص نقاط لب
#             lip_points = [
#                 61, 291, 185, 40, 39, 37, 267, 269, 270, 409,
#                 146, 91, 181, 84, 17, 314, 405, 321, 375
#             ]
#
#             # تبدیل نقاط به مختصات تصویر
#             landmarks = [(int(lm.x * w), int(lm.y * h)) for idx, lm in enumerate(face_landmarks.landmark) if idx in lip_points]
#
#             # ایجاد ماسک دقیق با Convex Hull
#             hull = cv2.convexHull(np.array(landmarks))
#             mask = np.zeros((h, w), dtype=np.uint8)
#             cv2.fillConvexPoly(mask, hull, 255)
#
#             # استخراج ناحیه لب با ماسک
#             lips = cv2.bitwise_and(image, image, mask=mask)
#
#             # پیدا کردن محدوده لب
#             x, y, w_lip, h_lip = cv2.boundingRect(hull)
#
#             # تغییر اندازه لب
#             new_w = int(w_lip * scale)
#             new_h = int(h_lip * scale)
#             lips_resized = cv2.resize(lips[y:y + h_lip, x:x + w_lip], (new_w, new_h))
#
#             # محاسبه موقعیت جدید
#             center_x = x + w_lip // 2
#             center_y = y + h_lip // 2
#             new_x = max(0, center_x - new_w // 2)
#             new_y = max(0, center_y - new_h // 2)
#
#             # ایجاد ماسک ترکیبی
#             mask_blur = cv2.GaussianBlur(mask, (51, 51), 0)
#             mask_blur = cv2.cvtColor(mask_blur, cv2.COLOR_GRAY2BGR)
#             mask_blur = mask_blur.astype(np.float32) / 255
#
#             # ترکیب طبیعی با تصویر اصلی
#             try:
#                 image[new_y:new_y + new_h, new_x:new_x + new_w] = (
#                         image[new_y:new_y + new_h, new_x:new_x + new_w] * (1 - mask_blur) +
#                         lips_resized * mask_blur
#                 ).astype(np.uint8)
#             except Exception as e:
#                 print(f"خطا در ترکیب تصویر: {str(e)}")
#
#     # ذخیره تصویر نهایی و بازگرداندن مسیر
#     output_path = "result.jpg"
#     cv2.imwrite(output_path, image)
#     return output_path  # بازگرداندن مسیر فایل به جای آرایه

