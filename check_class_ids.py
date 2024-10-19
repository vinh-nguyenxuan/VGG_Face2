import pandas as pd
import csv

def get_id_label_map(meta_file):
    # Hàm tạo ánh xạ từ tệp identity_meta.csv
    df = pd.read_csv(meta_file, sep=',\s+', quoting=csv.QUOTE_ALL, encoding="utf-8", engine='python')
    df['Class_ID'] = df['Class_ID'].str.replace('n', '')  # Loại bỏ ký tự 'n' nếu có
    id_label_dict = dict(zip(df["Class_ID"].values, df["class"].values))
    return id_label_dict

def check_class_ids(train_list_file, meta_file):
    # Đọc file identity_meta.csv để tạo id_label_dict
    print("Reading identity_meta.csv...")
    id_label_dict = get_id_label_map(meta_file)
    print(f"Total number of IDs in id_label_dict: {len(id_label_dict)}")

    # Mở và đọc file danh sách ảnh
    print(f"Reading train list file: {train_list_file}...")
    with open(train_list_file, 'r') as f:
        count = 0
        for line in f:
            img_path = line.strip()  # Lấy đường dẫn hình ảnh, ví dụ: n000002/0001_01.jpg hoặc 000002/0001_01.jpg
            class_id = img_path.split('/')[0]  # Tách lấy Class_ID (ví dụ: n000002 hoặc 000002)
            
            # In ra thông tin đang xử lý
            print(f"Processing class_id: {class_id}")
            if class_id not in id_label_dict:
                print(f"Class ID {class_id} not found in id_label_dict.")
            else:
                print(f"Class ID {class_id} found in id_label_dict.")
            
            count += 1
            if count > 10:  # Dừng sau khi kiểm tra 10 dòng để tránh in quá nhiều
                break

# Đường dẫn đến file danh sách ảnh và file identity_meta.csv
train_list_file = "D:/Users/TUF/Downloads/VGG-Face2/data/train_list.txt"
meta_file = "D:/Users/TUF/Downloads/VGG-Face2/meta/identity_meta.csv"

# Gọi hàm kiểm tra
check_class_ids(train_list_file, meta_file)
