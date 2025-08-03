# 📘 My_ebook – Thư viện tri thức số cá nhân

![Build Status](https://github.com/hoanglong8/My_ebook/actions/workflows/deploy.yml/badge.svg)

![Banner](docs/assets/banner.png)

Website này được xây dựng bằng [MkDocs](https://www.mkdocs.org/) và [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) để lưu trữ, tổ chức và xuất bản các bài viết đa lĩnh vực như triết học, khoa học, lịch sử, công nghệ, tài chính, gia đình, v.v.

## 🌐 Website online

> 👉 https://hoanglong8.github.io/My_ebook/

---

## 🚀 Cách đóng góp nội dung

Bạn có thể đóng góp thêm bài viết vào các chuyên mục có sẵn theo hướng dẫn dưới đây:

### 1. Fork & Clone repo

```bash
git clone https://github.com/hoanglong8/My_ebook.git
cd My_ebook
```

### 2. Thêm bài viết mới

- Mỗi chuyên mục nằm trong thư mục con của `docs/`, ví dụ:
  - `docs/1_Philosophy_Spirituality_Esotericism_Huyen_hoc/`
  - `docs/4_Finance_Business_Politics_Society/`

- Bạn hãy tạo file `.md` mới trong thư mục phù hợp. Tên file nên viết không dấu, dùng gạch dưới `_`.

Ví dụ:

```
docs/4_Finance_Business_Politics_Society/lich_su_dong_tien_viet_nam.md
```

### 3. Thêm metadata ở đầu file `.md`:

```markdown
---
title: Lịch sử đồng tiền Việt Nam
date: 2025-08-03
tags: [tài chính, tiền tệ, lịch sử]
summary: Bài viết tóm tắt các giai đoạn phát triển tiền tệ từ cổ đại đến hiện đại tại Việt Nam.
---
```

### 4. Commit và tạo pull request

```bash
git add .
git commit -m "Thêm bài viết về lịch sử đồng tiền"
git push origin main
```

Sau đó tạo **pull request** nếu bạn là người đóng góp bên ngoài.

---

## 📚 Cấu trúc repo

```
My_ebook/
├── docs/
│   ├── 1_Philosophy_Spirituality_Esotericism_Huyen_hoc/
│   ├── 2_STEM_Science_Tech_Engineer_Math/
│   ├── 3_BigHistory_Art_Geometry_Literature/
│   ├── 4_Finance_Business_Politics_Society/
│   ├── 5_Information_Technology/
│   ├── 6_Homeland_Lineage_Family_Self/
│   └── index.md
├── mkdocs.yml
└── .github/workflows/deploy.yml
└── Tổng hợp ebook và các khóa học hay.md
```

---

## 🧠 Mục tiêu của dự án

- Xây dựng **một thư viện tri thức cá nhân mở rộng dần theo thời gian**
- Sử dụng tư duy hệ thống và mô-đun hóa để phân loại nội dung
- Ghi lại tri thức cá nhân, gia đình, dòng họ, và ngành nghề chuyên môn

---

## 🛠️ Công nghệ sử dụng

- MkDocs + Material Theme
- GitHub Pages (tự động deploy qua GitHub Actions)
- Markdown (chuẩn đơn giản, dễ viết, dễ chia sẻ)

---

## ❤️ Góp ý & phát triển

Mọi góp ý, bổ sung xin gửi qua [Issues](https://github.com/hoanglong8/My_ebook/issues) hoặc [Pull Request](https://github.com/hoanglong8/My_ebook/pulls).

---

## 🧩 Categories Overview

| Folder | Description |
|--------|-------------|
| `1_Philosophy_Spirituality_Esotericism_Huyen_hoc` | Triết học, Tâm linh, Huyền học |
| `2_STEM_Science_Tech_Engineer_Math` | Khoa học tự nhiên, Kỹ thuật, Kiến trúc và Toán học |
| `3_BigHistory_Art_Geometry_Literature` | Khoa học xã hội, Văn học, Nghệ thuật, Lịch sử và Địa lý |
| `4_Finance_Business_Politics_Society` | Tài chính, Kinh doanh, Chính trị, Văn hóa và Xã hội |
| `5_Information_Technology` | Công nghệ thông tin |
| `6_Homeland_Lineage_Family_Self` | Quê hương, Dòng họ, Gia đình và Bản thân |

---

> ✍️ Built with purpose. Written with curiosity. Organized with love.


## Workflows tạo sách nói:

Bước 1: Upload bản scan lên các nền tảng (Archive, Google Drive, Smallpdf...) để lưu trữ và OCR => Link ebook.

Bước 2: Lấy full raw text về, dùng các công cụ (ChatGPT, Gemini, Claude...) để soát lỗi chính tả, sửa dấu câu, kiểm tra & biên tập lại nội dung/kịch bản => File .text cuốn sách.

Bước 3: Sử dụng các công cụ (text to speech như j2team, ChatGPT, elevenlabs...) để tạo các bản đọc audio => File .mp3 cuốn sách.

Bước 4: Sử dụng các công cụ (text to image như midjourney, stable diffusion, comfy IU...) để tạo các ảnh minh họa, phục chế, bắn màu, mở rộng kích thước, tăng độ phân giải... => File .png cho từng chương, từng trang sách (chú ý sự nhất quán cho nhân vật).

Bước 5: Sử dụng các công cụ (image to video như klingAI, runwayML, shakkerAI ...) để tạo các đoạn video chuyển động từ ảnh bước 4 => File .mp4 cho từng chương, từng trang sách (tùy vào mục đích - bước này có thể cần hoặc bỏ).

Bước 6: Sử dụng các công cụ edit như Capcut, Adobe premier, Canva... để tạo ra các đoạn video hoàn chỉnh => File .mp4 cuốn sách.

Bước 7: Upload video lên các nền tảng như Youtube, facebook group, Zalo group, website blog, telegram group... để chia sẻ, lưu trữ => Link video.
