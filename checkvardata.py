import os

# Đường dẫn đến thư mục chứa các thư mục theo tên nhân vật
data_dir = "C:/Users/TUF/Downloads/faces_emore/lfw"

# Lấy danh sách các thư mục (tên nhân vật)
folders = os.listdir(data_dir)

# Sắp xếp các thư mục theo thứ tự bảng chữ cái để gán số thứ tự
folders.sort()

# Duyệt qua danh sách các thư mục và đổi tên chúng thành số thứ tự
for idx, folder_name in enumerate(folders):
    old_path = os.path.join(data_dir, folder_name)
    new_folder_name = str(idx)  # Số thứ tự từ 0 trở đi
    new_path = os.path.join(data_dir, new_folder_name)
    
    # Kiểm tra nếu old_path là một thư mục thì tiến hành đổi tên
    if os.path.isdir(old_path):
        print(f"Rename {old_path} to {new_path}")
        os.rename(old_path, new_path)
