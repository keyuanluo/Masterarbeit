import os
import shutil

# 定义源和目标基础目录
src_base_dir = "/media/robert/4TB-SSD/watchped_dataset - 副本/Excel_Box"
dst_base_dir = "/media/robert/4TB-SSD/watchped_dataset - 副本/Excel_bbox坐标"

# 遍历源目录下的所有文件和文件夹
for root, dirs, files in os.walk(src_base_dir):
    # 检查当前目录是否包含 "detections_最终.xlsx"
    if "detections_最终.xlsx" in files:
        # 获取源文件的完整路径
        src_file_path = os.path.join(root, "detections_最终.xlsx")
        
        # 获取子子文件夹的名称（当前文件夹名称）
        sub_sub_folder_name = os.path.basename(root)
        
        # 获取父文件夹的名称（子文件夹名称）
        parent_folder = os.path.basename(os.path.dirname(root))
        
        # 构建目标目录路径
        dst_dir = os.path.join(dst_base_dir, parent_folder)
        
        # 如果目标目录不存在，则创建
        os.makedirs(dst_dir, exist_ok=True)
        
        # 构建目标文件的完整路径，文件名为子子文件夹名称加上 ".xlsx"
        dst_file_name = sub_sub_folder_name + ".xlsx"
        dst_file_path = os.path.join(dst_dir, dst_file_name)
        
        # 复制并重命名文件到目标目录
        shutil.copyfile(src_file_path, dst_file_path)
        
        print(f"已将 {src_file_path} 复制到 {dst_file_path}")
