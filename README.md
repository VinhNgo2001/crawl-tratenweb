# crawl tratenweb
# 🏢 Công cụ Crawl dữ liệu doanh nghiệp từ [tratencongty.com](https://www.tratencongty.com)

## 🚀 Yêu cầu môi trường
- Python **>= 3.8**
- Hệ điều hành: Windows / Linux / MacOS
- Kết nối Internet

## 📦 Cài đặt thư viện
Chạy lệnh sau để cài các thư viện cần thiết:

```bash
pip install -r requirements.txt

⚙️ Cách sử dụng
1️⃣ Bước 1: Crawl danh sách công ty (a.py)

File a.py dùng để lấy danh sách công ty theo từng tỉnh/thành phố và lưu ra file .json.

Ví dụ chạy:

python a.py


Kết quả: sinh ra file companies_links_{tinh}_{start}_{end}.json
(VD: companies_links_dong-nai_11_22.json)
Bước 2: Crawl chi tiết công ty (d.py)

File d.py đọc danh sách link trong file JSON và lấy chi tiết thông tin công ty, sau đó xuất ra file .docx .

Ví dụ chạy:

python d.py


Kết quả: sinh ra file companies_details.docx chứa các thông tin:

Tên công ty

Địa chỉ

Ngày hoạt động

Đại diện pháp luật

Số điện thoại (dưới dạng hình ảnh)

📂 Cấu trúc thư mục
project/
│── a.py                   # Crawl danh sách công ty
│── d.py                   # Crawl chi tiết công ty
│── companies_links.json    # File JSON chứa danh sách link (sinh ra sau khi chạy a.py)
│── companies_details.docx  # File Word kết quả (sinh ra sau khi chạy d.py)
│── requirements.txt
│── README.md

Bo sung co the thay doi thanh' tinh? khac de lay du~ lieu
