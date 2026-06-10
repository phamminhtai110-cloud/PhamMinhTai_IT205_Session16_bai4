from datetime import datetime

patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi",
    "BN002-Tran Thi B-1990-Sot Xuat Huyet",
    "BN003-Le Van C-2015-Viem Phe Quan"
]

def find_patient_index(records, patient_id):
    for i, r in enumerate(records):
        if r.split("-")[0] == patient_id:
            return i
    return -1


def display_records(records):
    if not records:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        return

    print("--- DANH SÁCH BỆNH NHÂN --------------------------------------------------")
    for i, r in enumerate(records, 1):
        pid, name, year, diag = r.split("-")
        print(f"{i}. [{pid}] {name:<20} | Năm sinh: {year} | Chẩn đoán: {diag}")
    print("--------------------------------------------------------------------------")


def add_patient(records):
    print("\n--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")

    pid = input("Nhập mã bệnh nhân: ").strip().upper()
    name = input("Nhập tên bệnh nhân: ").strip()
    year = input("Nhập năm sinh: ").strip()
    diag = input("Nhập chẩn đoán: ").strip()

    if find_patient_index(records, pid) != -1:
        print("Mã bệnh nhân đã tồn tại!")
        return

    if not year.isdigit():
        print("Năm sinh không hợp lệ, vui lòng nhập lại!")
        return

    year = int(year)
    current_year = datetime.now().year

    if year < 1900 or year > current_year:
        print("Năm sinh không hợp lệ, vui lòng nhập lại!")
        return

    name = name.replace("-", " ").title()
    diag = diag.replace("-", " ").capitalize()

    new_record = f"{pid}-{name}-{year}-{diag}"
    records.append(new_record)

    print("\nThêm hồ sơ bệnh nhân thành công!")
    print("Dữ liệu được lưu là:")
    print(new_record)


def update_diagnosis(records):
    print("\n--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")

    pid = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()
    idx = find_patient_index(records, pid)

    if idx == -1:
        print(f"Không tìm thấy bệnh nhân mang mã {pid}!")
        return

    parts = records[idx].split("-")

    print(f"Tìm thấy bệnh nhân: {parts[1]}")
    print(f"Chẩn đoán hiện tại: {parts[3]}")

    new_diag = input("Nhập chẩn đoán mới: ").strip()
    new_diag = new_diag.replace("-", " ").capitalize()

    parts[3] = new_diag
    records[idx] = "-".join(parts)

    print("\nCập nhật chẩn đoán thành công!")
    print("Dữ liệu mới được lưu:")
    print(records[idx])


def generate_age_report(records):
    print("\n--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")

    child = adult = elderly = 0
    current_year = datetime.now().year

    for r in records:
        year = int(r.split("-")[2])
        age = current_year - year

        if age < 16:
            child += 1
        elif age <= 60:
            adult += 1
        else:
            elderly += 1

    print(f"Trẻ em: {child} bệnh nhân")
    print(f"Trưởng thành: {adult} bệnh nhân")
    print(f"Người cao tuổi: {elderly} bệnh nhân")
    print("--------------------------------------")


def main():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====")
        print("1. Xem danh sách hồ sơ bệnh án")
        print("2. Thêm hồ sơ bệnh nhân mới")
        print("3. Cập nhật chẩn đoán theo Mã BN")
        print("4. Báo cáo phân loại theo độ tuổi")
        print("5. Thoát chương trình")
        print("==================================================")

        choice = input("Chọn chức năng (1-5): ").strip()

        if choice == "1":
            display_records(patient_records)
        elif choice == "2":
            add_patient(patient_records)
        elif choice == "3":
            update_diagnosis(patient_records)
        elif choice == "4":
            generate_age_report(patient_records)
        elif choice == "5":
            print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
            break
        else:
            print("Lựa chọn không hợp lệ!")


main()