"""# 1. รับค่า text จากผู้ใช้
# 2. รับค่าอักขระที่ต้องการค้นหาจากผู้ใช้
# 3. แสดงผลจำนวณของอักขระในข้อความ text 

# ตัวอย่างหน้าจอ
# Insert your text: Issara Thong-in
# Character to find: o
# 5 letters 'o' found in 'Issara Thong-in'

print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("Insert your text : ")
char = input("Character to find : ")

for letter in text:
    if letter == char:
        count += 1
print(f"{count} letters {char} found in '{text}'")
"""

"""
password = "Issara@123"
lenght = len(password)
word = password.split('@')

if len(word) > 1 and password.count('@') == 1:
 left = word[0].isalnum()
 right = word[1].isalnum()
else:
   left = False;
   right = False;

if lenght >= 8 and len(word) == 2 and left and right == True:
    print("Your password is strong!")
else:
   print("Your password is not strong!")
"""

print("\n=== ORD() AND CHR() FUNCTIONS ===")
ch = 'R'
print(f"ord('{ch}') = {ord(ch)}")
print(f"chr(82) = {chr(82)}")




