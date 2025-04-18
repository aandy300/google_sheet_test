import os
import json

# 定義 JSON 檔案名稱
output_json_file = "parsed_folders.json"

# 定義目標資料夾路徑
target_folder = r"F:\Coding\python\Google_Sheet\tmp\repo"  # 目標資料夾路徑

# 初始化資料夾名稱陣列
folder_array = []

# 掃描目標資料夾，將所有資料夾名稱存入陣列
for item in os.listdir(target_folder):
    item_path = os.path.join(target_folder, item)
    if os.path.isdir(item_path):  # 確保是資料夾
        folder_array.append(item)

# 初始化結果物件
parsed_data = {}

# 逐一解析資料夾名稱
for folder in folder_array:
    parts = folder.split("_")  # 以 "_" 分割資料夾名稱
    if len(parts) >= 3:  # 確保資料夾名稱符合解析格式
        host_name = parts[0]  # 第一部分
        adm_version_1 = parts[1]  # 第二部分
        adm_version_2 = parts[2]  # 第三部分
        repo_full_path = os.path.join(target_folder, folder)  # 資料夾的完整路徑

        # 儲存解析結果
        parsed_data[folder] = {
            "host name": host_name,
            "ADM Version 1": adm_version_1,
            "ADM Version 2": adm_version_2,
            "repo path": repo_full_path,
        }

# 將結果儲存為 JSON 檔案
with open(output_json_file, "w", encoding="utf-8") as json_file:
    json.dump(parsed_data, json_file, indent=4, ensure_ascii=False)

print(f"解析完成，結果已儲存至 {output_json_file}")