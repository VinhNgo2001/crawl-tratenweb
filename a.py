import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://www.tratencongty.com/tinh-dong-nai/?page={}"

start_page = 12
end_page = 27

companies = []

for page in range(start_page, end_page + 1):
    url = BASE_URL.format(page)
    print(f"Đang lấy page {page} - {url}")
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    for a in soup.select("div.search-results a"):
        href = a.get("href")
        name = a.get_text(strip=True)
        if href and name:
            companies.append({
                "ten_cong_ty": name,
                "url": href
            })

# Xuất ra JSON với tên file có khoảng page
output_file = f"companies_links_page_{start_page}_{end_page}.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(companies, f, ensure_ascii=False, indent=4)

print(f"✅ Đã lưu danh sách công ty vào {output_file}")
