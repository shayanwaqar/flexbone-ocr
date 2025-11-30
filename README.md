# 📄 OCR Web App (Flask + Tesseract OCR) — Deployed on Google Cloud Run

A lightweight OCR (Optical Character Recognition) web application built with  **Flask** , powered by  **Tesseract OCR** , and deployed serverlessly using  **Google Cloud Run** .

Users can upload an image and instantly extract text directly from the browser.

---

## 🚀 Live Demo

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

## ▶️ Running Locally

### **1. Clone the Repo**

<pre class="overflow-visible!" data-start="1619" data-end="1667"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>git </span><span>clone</span><span> <your_repo_url>
</span><span>cd</span><span> ocr-app
</span></span></code></div></div></pre>

### **2. Install dependencies**

<pre class="overflow-visible!" data-start="1702" data-end="1745"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pip install -r requirements.txt
</span></span></code></div></div></pre>

### **3. Ensure Tesseract is installed locally**

**macOS:**

<pre class="overflow-visible!" data-start="1809" data-end="1843"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>brew install tesseract
</span></span></code></div></div></pre>

**Ubuntu:**

<pre class="overflow-visible!" data-start="1858" data-end="1904"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>sudo apt-get install tesseract-ocr
</span></span></code></div></div></pre>

### **4. Run the app**

<pre class="overflow-visible!" data-start="1930" data-end="1955"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python app.py
</span></span></code></div></div></pre>

Go to:

**[http://localhost:8080]()**

---

## 🐳 Docker Build (Optional)

To run locally using Docker:

<pre class="overflow-visible!" data-start="2059" data-end="2128"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>docker build -t ocr-app .
docker run -p 8080:8080 ocr-app
</span></span></code></div></div></pre>

---

## 🚀 Deployment Instructions (Cloud Run)

### **1. Build the image on Google Cloud Build**

<pre class="overflow-visible!" data-start="2228" data-end="2294"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>gcloud builds submit --tag gcr.io/<project-id>/ocr-app
</span></span></code></div></div></pre>

### **2. Deploy to Cloud Run**

<pre class="overflow-visible!" data-start="2328" data-end="2481"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>gcloud run deploy ocr-app \
  --image gcr.io/<project-id>/ocr-app \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
</span></span></code></div></div></pre>

Cloud Run will return a public URL where your OCR app is live.

---

## 💡 Notes & Limitations

OCR accuracy depends heavily on image quality and lighting.

This demo is intended as a lightweight proof-of-concept.

Tesseract may potentially misread stylized fonts or handwriting.

---

## 📬 Author

**Shayan Waqar**

---
