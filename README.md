# 📄 OCR Web App (Flask + Tesseract OCR) — Deployed on Google Cloud Run

A lightweight OCR (Optical Character Recognition) web application built with  **Flask** , powered by  **Tesseract OCR** , and deployed serverlessly using  **Google Cloud Run** .

Users can upload an image and instantly extract text directly from the browser.

---

* 🚀 Live Demo

🔗 **Public App URL:**

👉 [https://ocr-app-432954338470.us-central1.run.app](https://ocr-app-432954338470.us-central1.run.app)

---

## 📌 Features

* Simple HTML upload form (`.png`, `.jpg`, `.jpeg`)
* Extracts text using **pytesseract** (Tesseract OCR)
* Displays output on the same page
* Fully containerized using Docker
* Deployed to **Google Cloud Run** (serverless, autoscaling, HTTPS enabled)

---

## 🛠️ Tech Stack

| Component      | Technology                      |
| -------------- | ------------------------------- |
| Backend        | Flask                           |
| OCR Engine     | Tesseract OCR (via pytesseract) |
| Image Handling | Pillow (PIL)                    |
| Server         | Gunicorn                        |
| Container      | Docker                          |
| Deployment     | Google Cloud Run                |

---

## 📁 Project Structure

<pre class="overflow-visible!" data-start="1130" data-end="1229"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>ocr-app/
│── app.py
│── requirements.txt
│── Dockerfile
│── templates/
│     └── </span><span>index</span><span>.html
</span></span></code></div></div></pre>

---

## 🧠 How It Works

1. The user uploads an image via the simple HTML form.
2. Flask receives the file and processes it with  **Pillow** .
3. The processed image is sent to  **pytesseract** , which extracts text.
4. The extracted text is displayed below the form.
5. Everything runs inside a Docker container deployed on Cloud Run.

---

## 💡 Notes & Limitations

* OCR accuracy depends heavily on image quality and lighting.
* This demo is intended as a lightweight proof-of-concept.
* Tesseract MIGHT misread stylized fonts or handwriting.

---

## 📬 Author

**Shayan Waqar**
