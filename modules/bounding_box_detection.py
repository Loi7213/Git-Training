import cv2
import dlib

def detect_face(image_path):
    # Đọc ảnh
    image = cv2.imread(image_path)
    
    # Khởi tạo face detector của dlib
    detector = dlib.get_frontal_face_detector()
    
    # Chuyển ảnh sang grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Phát hiện khuôn mặt
    faces = detector(gray)
    
    # Nếu phát hiện được khuôn mặt
    if len(faces) > 0:
        # Lấy tọa độ của khuôn mặt đầu tiên
        face = faces[0]
        x1, y1, x2, y2 = face.left(), face.top(), face.right(), face.bottom()
        return (x1, y1, x2, y2)
    else:
        return None

# Sử dụng hàm
image_path = "path_to_your_image.jpg"
result = detect_face(image_path)

if result:
    print(f"Tọa độ bounding box: {result}")
else:
    print("Không tìm thấy khuôn mặt trong ảnh!")