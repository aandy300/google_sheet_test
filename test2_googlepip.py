from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

# 授权服务账户
SCOPES = ["https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("放憑證JSON", scopes=SCOPES)
drive_service = build("drive", "v3", credentials=creds)

# 原文件 ID 和目标名称
source_file_id = "放要複製的表單ID"
destination_name = "Copied Google Sheet"

# 文件复制
copied_file = drive_service.files().copy(fileId=source_file_id, body={"name": destination_name}).execute()

# print(copied_file)

# print(f"Copied file URL: https://docs.google.com/spreadsheets/d/{copied_file['id']}")

# https://docs.google.com/spreadsheets/d/1MrcK1pgX8Cd4PwM5sNBrmizBX4zL6ss0gS6mKkxHV4k/edit?gid=0#gid=0
# https://docs.google.com/spreadsheets/d/1flN2W84UQ5afPL4W8BxWxCosgohTIAOVQzjHM_1tJKw/edit?gid=0#gid=0

# ---
# ID 1 - 1dfebIZ5uYxzgOMoWa5X5IOHCVnuxNpuOpW04Ht45CBU
# ID 2 - 1flN2W84UQ5afPL4W8BxWxCosgohTIAOVQzjHM_1tJKw
# 获取新文件的 ID
# copied_file = "1dfebIZ5uYxzgOMoWa5X5IOHCVnuxNpuOpW04Ht45CBU"
copied_file_id = copied_file["id"]
print(f"Copied file URL: https://docs.google.com/spreadsheets/d/{copied_file_id}")

# 添加权限（共享给特定用户）
user_email = "aandy300@gmail.com"  # 替换为您或他人的 Gmail 地址
drive_service.permissions().create(
    fileId=copied_file_id,
    body={
        "type": "user",         # 用户类型
        "role": "writer",       # 权限类型（writer 表示编辑权限）
        "emailAddress": user_email
    }
).execute()

print(f"File shared with {user_email}")