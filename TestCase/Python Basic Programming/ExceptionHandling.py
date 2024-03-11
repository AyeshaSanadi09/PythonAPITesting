try:
    a = int(input())
    b = int(input())
    print(a+b)
except Exception:
    print(Exception)
finally:
    print("This is finally block")