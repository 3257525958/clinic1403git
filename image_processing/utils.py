# import cv2
# import dlib
# import os
#
# # مشخص کردن مسیر فایل مدل
# # BASE_DIR = os.path.dirname(os.path.abspath(_file_))  # مسیر پوشه اسکریپت
# BASE_DIR = os.getcwd()
# MODEL_PATH = os.path.join(BASE_DIR, "shape_predictor_68_face_landmarks.dat")
#
# # بارگذاری مدل شناسایی نقاط کلیدی چهره
# if not os.path.exists(MODEL_PATH):
#     raise FileNotFoundError(f"مدل یافت نشد: {MODEL_PATH}. لطفاً فایل را در مسیر درست قرار دهید.")
#
# detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor(MODEL_PATH)
#
# # خواندن تصویر
# image_path = os.path.join(BASE_DIR, "test.jpg")  # تصویر تست
# image = cv2.imread(image_path)
#
# if image is None:
#     raise FileNotFoundError(f"تصویر '{image_path}' یافت نشد.")
#
# # تبدیل به تصویر سطح خاکستری
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # شناسایی چهره‌ها
# faces = detector(gray)
#
# for face in faces:
#     landmarks = predictor(gray, face)
#
#     # رسم نقاط کلیدی روی چهره
#     for n in range(68):  # ۶۸ نقطه کلیدی
#         x, y = landmarks.part(n).x, landmarks.part(n).y
#         cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
#
# # نمایش نتیجه
# cv2.imshow("Landmarks Detection", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import cv2
import dlib
import numpy as np

# بارگذاری مدل نقاط چهره
MODEL_PATH = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(MODEL_PATH)

def process_image(image_path):
    """
    پردازش تصویر برای تشخیص چهره و نمایش نقاط کلیدی آن
    """
    # خواندن تصویر
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"تصویر '{image_path}' یافت نشد.")

    # تبدیل تصویر به سطح خاکستری
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # تشخیص چهره‌ها
    faces = detector(gray)
    if len(faces) == 0:
        raise ValueError("چهره‌ای در تصویر یافت نشد.")

    # پردازش هر چهره و نمایش نقاط کلیدی
    for face in faces:
        landmarks = predictor(gray, face)

        # رسم نقاط روی تصویر
        for i in range(68):  # 68 نقطه مشخصه چهره
            x, y = landmarks.part(i).x, landmarks.part(i).y
            cv2.circle(image, (x, y), 2, (0, 255, 0), -1)

    return image


if __name__ == "_main_":
    # اجرای تست پردازش تصویر
    test_image = "test.jpg"
    output_image = process_image(test_image)

    cv2.imshow("Processed Image", output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()