""" เขียน function ชื่อ create_user_profile ที่มีคุณสมบัติดังนี้:

รับ parameters: username (จำเป็น), age (ค่าเริ่มต้น 18), premium (ค่าเริ่มต้น False)
return string ที่จัดรูปแบบข้อมูลผู้ใช้
รูปแบบ: "[username] (age: [age]) - [Premium User / Standard User]"

print(create_user_profile("Issra", 20))
print(create_user_profile("Teerapat"))
print(create_user_profile("Ponlawat", 21, True))
"""

def create_user_profile(username, age=18, premium=False):
    # Your Problem 3 solution
    user_type = "Standard"

    if premium == True:
        user_type = "Premium" 
    return f"{username} (age: {age}) - {user_type}"
