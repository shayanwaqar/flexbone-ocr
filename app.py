from flask import Flask, render_template, request
from PIL import Image
import pytesseract
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    extracted_text = None
    error = None

    if request.method == "POST":
        file = request.files.get("image")

        if not file or file.filename == "":
            error = "Please upload an image file."
        else:
            try:
                # Read file into memory
                image_bytes = file.read()

                # Open as PIL image
                image = Image.open(io.BytesIO(image_bytes))

                # Run Tesseract OCR
                extracted_text = pytesseract.image_to_string(image)

                # Optional: strip trailing whitespace
                extracted_text = extracted_text.strip()

                # If Tesseract returns nothing
                if not extracted_text:
                    error = "No text detected. Try a clearer image."
            except Exception as e:
                # Catch errors like unsupported file, Tesseract issues, etc.
                error = f"Error processing image: {e}"

    return render_template("index.html", text=extracted_text, error=error)

if __name__ == "__main__":
    # Port 8080 so it matches Cloud Run later
    app.run(host="0.0.0.0", port=8080, debug=True)
