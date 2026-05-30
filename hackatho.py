import json
import os

# Tên file lưu trữ dữ liệu
FILE_NAME = "data.json"

# Nạp dữ liệu từ file JSON vào danh sách ngay khi khởi động chương trình
danh_sach_sv = []
if os.path.exists(FILE_NAME):
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            danh_sach_sv = json.load(f)
    except Exception:
        danh_sach_sv = []

# ==========================================
# VÒNG LẶP MENU ĐIỀU KHIỂN CHÍNH
# ==========================================
while True:
    print("\n" + "="*20 + " MENU QUẢN LÝ SINH VIÊN " + "="*20)
    print("1. Hiển thị danh sách sinh viên")
    print("2. Thêm mới sinh viên")
    print("3. Cập nhật thông tin sinh viên")
    print("4. Xoá sinh viên")
    print("5. Tìm kiếm sinh viên")
    print("6. Sắp xếp danh sách sinh viên")
    print("7. Thống kê điểm TB")
    print("8. Liệt kê sinh viên có điểm TB cao nhất / thấp nhất")
    print("9. Phân loại học lực sinh viên (Tự động tích hợp)")
    print("10. Thoát")
    print("=" * 64)
    
    luon_chon = input(" Mới bạn chọn chức năng (1-10): ").strip()
    
    match luon_chon:
        case '1':
            print("\n--- [1] DANH SÁCH SINH VIÊN ---")
            if not danh_sach_sv:
                print("Danh sách trống.")
            else:
                print("-" * 95)
                print(f"{'Mã SV':<10} | {'Họ và Tên':<25} | {'Toán':<6} | {'Lý':<6} | {'Hóa':<6} | {'Điểm TB':<8} | {'Xếp Loại':<12}")
                print("-" * 95)
                for sv in danh_sach_sv:
                    print(f"{sv['ma_sv']:<10} | {sv['ho_ten']:<25} | {sv['toan']:<6.2f} | {sv['ly']:<6.2f} | {sv['hoa']:<6.2f} | {sv['diem_tb']:<8.2f} | {sv['xep_loai']:<12}")
                print("-" * 95)
                
        case '2':
            print("\n--- [2] THÊM MỚI SINH VIÊN ---")
            # Nhập và kiểm tra trùng mã SV
            while True:
                ma_sv = input("Nhập Mã SV: ").strip().upper()
                if not ma_sv:
                    print(" Mã SV không được để trống!")
                    continue
                trung_ma = any(sv['ma_sv'] == ma_sv for sv in danh_sach_sv)
                if trung_ma:
                    print(" Mã SV đã tồn tại! Vui lòng nhập mã khác.")
                else:
                    break
                    
            ho_ten = input("Nhập Họ Tên: ").strip().title()
            
            # Nhập điểm Toán kèm bắt lỗi khoảng [0 - 10]
            while True:
                try:
                    toan = float(input("Nhập điểm Toán: "))
                    if 0 <= toan <= 10: break
                    print(" Điểm phải nằm trong khoảng từ 0 đến 10!")
                except ValueError:
                    print(" Vui lòng nhập số hợp lệ!")
                    
            # Nhập điểm Lý kèm bắt lỗi khoảng [0 - 10]
            while True:
                try:
                    ly = float(input("Nhập điểm Lý: "))
                    if 0 <= ly <= 10: break
                    print(" Điểm phải nằm trong khoảng từ 0 đến 10!")
                except ValueError:
                    print(" Vui lòng nhập số hợp lệ!")
                    
            # Nhập điểm Hóa kèm bắt lỗi khoảng [0 - 10]
            while True:
                try:
                    hoa = float(input("Nhập điểm Hóa: "))
                    if 0 <= hoa <= 10: break
                    print(" Điểm phải nằm trong khoảng từ 0 đến 10!")
                except ValueError:
                    print(" Vui lòng nhập số hợp lệ!")
            
            # Tính toán Điểm TB và Phân loại học lực (Chức năng 9)
            diem_tb = round((toan + ly + hoa) / 3, 2)
            
            if diem_tb < 5.0:
                xep_loai = "Yeu"
            elif diem_tb < 7.0:
                xep_loai = "Trung Binh"
            elif diem_tb < 8.0:
                xep_loai = "Kha"
            else:
                xep_loai = "Gioi"
            
            # Lưu vào danh sách
            sv_moi = {
                "ma_sv": ma_sv, "ho_ten": ho_ten, "toan": round(toan, 2), 
                "ly": round(ly, 2), "hoa": round(hoa, 2), 
                "diem_tb": diem_tb, "xep_loai": xep_loai
            }
            danh_sach_sv.append(sv_moi)
            
            # Ghi file lưu trữ dữ liệu tự động
            try:
                with open(FILE_NAME, "w", encoding="utf-8") as f:
                    json.dump(danh_sach_sv, f, ensure_ascii=False, indent=4)
            except Exception as e:
                print(f"Lỗi lưu file: {e}")
            print("Thêm sinh viên thành công!")
            
        case '3':
            print("\n--- [3] CẬP NHẬT THÔNG TIN ---")
            ma_sv = input("Nhập Mã SV cần sửa: ").strip().upper()
            found = False
            
            for sv in danh_sach_sv:
                if sv['ma_sv'] == ma_sv:
                    print(f"Tìm thấy SV: {sv['ho_ten']}. Tiến hành nhập điểm mới:")
                    
                    while True:
                        try:
                            sv['toan'] = float(input("Nhập điểm Toán mới: "))
                            if 0 <= sv['toan'] <= 10: break
                            print(" Điểm phải nằm trong khoảng từ 0 đến 10!")
                        except ValueError:
                            print(" Vui lòng nhập số hợp lệ!")
                            
                    while True:
                        try:
                            sv['ly'] = float(input("Nhập điểm Lý mới: "))
                            if 0 <= sv['ly'] <= 10: break
                            print(" Điểm phải nằm trong khoảng từ 0 đến 10!")
                        except ValueError:
                            print(" Vui lòng nhập số hợp lệ!")
                            
                    while True:
                        try:
                            sv['hoa'] = float(input("Nhập điểm Hóa mới: "))
                            if 0 <= sv['hoa'] <= 10: break
                            print("❌ Điểm phải nằm trong khoảng từ 0 đến 10!")
                        except ValueError:
                            print("❌ Vui lòng nhập số hợp lệ!")
                    
                    # Làm tròn và tính toán lại điểm TB & học lực
                    sv['toan'] = round(sv['toan'], 2)
                    sv['ly'] = round(sv['ly'], 2)
                    sv['hoa'] = round(sv['hoa'], 2)
                    sv['diem_tb'] = round((sv['toan'] + sv['ly'] + sv['hoa']) / 3, 2)
                    
                    if sv['diem_tb'] < 5.0:
                        sv['xep_loai'] = "Yeu"
                    elif sv['diem_tb'] < 7.0:
                        sv['xep_loai'] = "Trung Binh"
                    elif sv['diem_tb'] < 8.0:
                        sv['xep_loai'] = "Kha"
                    else:
                        sv['xep_loai'] = "Gioi"
                        
                    # Ghi đè cập nhật vào file
                    with open(FILE_NAME, "w", encoding="utf-8") as f:
                        json.dump(danh_sach_sv, f, ensure_ascii=False, indent=4)
                    print("Cập nhật thông tin thành công!")
                    found = True
                    break
            if not found:
                print(" Không tìm thấy sinh viên có mã này.")
                
        case '4':
            print("\n--- [4] XÓA SINH VIÊN ---")
            ma_sv = input("Nhập Mã SV cần xóa: ").strip().upper()
            found = False
            
            for sv in danh_sach_sv:
                if sv['ma_sv'] == ma_sv:
                    xac_nhan = input(f"Bạn có chắc muốn xóa SV '{sv['ho_ten']}' không? (Y/N): ").strip().upper()
                    if xac_nhan == 'Y':
                        danh_sach_sv.remove(sv)
                        with open(FILE_NAME, "w", encoding="utf-8") as f:
                            json.dump(danh_sach_sv, f, ensure_ascii=False, indent=4)
                        print(" Đã xóa sinh viên.")
                    else:
                        print(" Hủy bỏ thao tác xóa.")
                    found = True
                    break
            if not found:
                print("Không tìm thấy sinh viên có mã này.")
                
        case '5':
            print("\n--- [5] TÌM KIẾM SINH VIÊN ---")
            tu_khoa = input("Nhập Mã SV hoặc Tên cần tìm (gần đúng): ").strip().lower()
            ket_qua = [sv for sv in danh_sach_sv if tu_khoa in sv['ma_sv'].lower() or tu_khoa in sv['ho_ten'].lower()]
            
            if ket_qua:
                print(f"\n Tìm thấy {len(ket_qua)} kết quả ")
                print("-" * 95)
                print(f"{'Mã SV':<10} | {'Họ và Tên':<25} | {'Toán':<6} | {'Lý':<6} | {'Hóa':<6} | {'Điểm TB':<8} | {'Xếp Loại':<12}")
                print("-" * 95)
                for sv in ket_qua:
                    print(f"{sv['ma_sv']:<10} | {sv['ho_ten']:<25} | {sv['toan']:<6.2f} | {sv['ly']:<6.2f} | {sv['hoa']:<6.2f} | {sv['diem_tb']:<8.2f} | {sv['xep_loai']:<12}")
                print("-" * 95)
            else:
                print(" Không tìm thấy sinh viên nào khớp với từ khóa.")
                
        case '6':
            print("\n--- [6] SẮP XẾP DANH SÁCH ---")
            print("1. Sắp xếp theo Điểm TB giảm dần")
            print("2. Sắp xếp theo Tên tăng dần (A-Z)")
            luon_chon_sx = input("Chọn kiểu sắp xếp (1 hoặc 2): ").strip()
            
            match luon_chon_sx:
                case '1':
                    danh_sach_sv.sort(key=lambda x: x['diem_tb'], reverse=True)
                    print("Đã sắp xếp theo Điểm TB giảm dần! ")
                case '2':
                    danh_sach_sv.sort(key=lambda x: x['ho_ten'].split()[-1] if x['ho_ten'] else "")
                    print(" Đã sắp xếp theo Tên tăng dần (A-Z)! ")
                case _:
                    print("Lựa chọn sắp xếp không hợp lệ.")
                    
        case '7':
            print("\n--- [7] THỐNG KÊ HỌC LỰC ---")
            tk = {"Gioi": 0, "Kha": 0, "Trung Binh": 0, "Yeu": 0}
            for sv in danh_sach_sv:
                if sv['xep_loai'] in tk:
                    tk[sv['xep_loai']] += 1
            print(f"Số lượng sinh viên loại Giỏi     : {tk['Gioi']}")
            print(f" Số lượng sinh viên loại Khá      : {tk['Kha']}")
            print(f" Số lượng sinh viên loại Trung Bình: {tk['Trung Binh']}")
            print(f" Số lượng sinh viên loại Yếu      : {tk['Yeu']}")
            
        case '8':
            print("\n--- [8] SV ĐIỂM TB CAO NHẤT / THẤP NHẤT ---")
            if not danh_sach_sv:
                print("Danh sách trống.")
            else:
                max_diem = max(sv['diem_tb'] for sv in danh_sach_sv)
                min_diem = min(sv['diem_tb'] for sv in danh_sach_sv)
                
                sv_max = [sv for sv in danh_sach_sv if sv['diem_tb'] == max_diem]
                sv_min = [sv for sv in danh_sach_sv if sv['diem_tb'] == min_diem]
                
                print(f"\n ĐIỂM TB CAO NHẤT ({max_diem}):")
                for sv in sv_max:
                    print(f" -> Mã: {sv['ma_sv']} | Tên: {sv['ho_ten']} | Điểm TB: {sv['diem_tb']} ({sv['xep_loai']})")
                
                print(f"\n ĐIỂM TB THẤP NHẤT ({min_diem}):")
                for sv in sv_min:
                    print(f" -> Mã: {sv['ma_sv']} | Tên: {sv['ho_ten']} | Điểm TB: {sv['diem_tb']} ({sv['xep_loai']})")
                    
        case '9':
            print("\n Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break
            
        case _:
            print(" Lựa chọn không hợp lệ, vui lòng nhập lại từ 1 đến 10.")