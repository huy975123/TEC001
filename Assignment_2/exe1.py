def check_zander():
    # Ép kiểu float vì chiều dài cá có thể là số lẻ (ví dụ 41.5)
    length = float(input("Enter the length of the zander (cm): "))
    
    limit = 42
    
    if length >= limit:
        print("The zander meets the size limit.")
    else:
        # Tính xem thiếu bao nhiêu cm
        diff = limit - length
        print("Release the fish back into the lake.")
        # Dùng f-string để in biến vào chuỗi cho gọn, hoặc dùng dấu phẩy cũng được
        print(f"The fish was {diff} cm below the size limit.")

# Gọi hàm để chạy thử
check_zander()