import kagglehub
import shutil
import os

dataset_handle = "rascanudragos/bpi-challenge-2017"

print("Đang tải dữ liệu từ Kaggle...")
tmp_path = kagglehub.dataset_download(dataset_handle)

target_path = os.path.join(os.getcwd(), "bpi-challenge-2017")

# 4. Di chuyển dữ liệu từ cache về thư mục đích
if not os.path.exists(target_path):
    shutil.copytree(tmp_path, target_path)
    print(f"Xong! Dữ liệu đã được lưu tại: {target_path}")
else:
    print(f"Thư mục '{target_path}' đã tồn tại, không cần tải lại.")
    