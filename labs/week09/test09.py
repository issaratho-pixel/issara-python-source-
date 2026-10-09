try:
    num1 = float(input("ตัวเลขตัวที่ 1 : "))
    num2 = float(input("ตัวเลขตัวที่ 2 : "))
    operator = input("เครื่องหมาย (+, -, *, /) : ")
    
    if operator == "+":
          result = num1 + num2
    elif operator == "-":
            result = num1 - num2
    elif operator == "*":
            result = num1 * num2
    elif operator == "/":
            result = num1 / num2
    else:
           raise ValueError("เตรื่องหมายต้องเป็น + - * / เท่านั้น")
    
    print(f"{num1} {operator} {num2} = {result}")
    
except ValueError:
       print("เขียนเครื่องหมายให้ถูกต้องค้าบเฮียน")

except ZeroDivisionError:
       print("ไม่สามารถใส่ 0 ได้ค้าบเฮียน")

except Exception:
       print("ทำไรค้าบเฮียน")

else:
    print("ถูกต้องค้าบเฮียนน")

finally:
       print("จบแล้วค้าบเฮียน")