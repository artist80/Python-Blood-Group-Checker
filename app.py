from flask import Flask, render_template, request, send_file
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

app = Flask(__name__)

blood_group_table = {
    ("A", "A"): ["A", "O"],
    ("A", "B"): ["A", "B", "AB", "O"],
    ("A", "AB"): ["A", "B", "AB"],
    ("A", "O"): ["A", "O"],
    ("B", "B"): ["B", "O"],
    ("B", "AB"): ["A", "B", "AB"],
    ("B", "O"): ["B", "O"],
    ("AB", "AB"): ["A", "B", "AB"],
    ("AB", "O"): ["A", "B"],
    ("O", "O"): ["O"],
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    mother = request.form['mother']
    father = request.form['father']
    possible_blood_groups = blood_group_table.get((mother, father)) or blood_group_table.get((father, mother))
    
    return render_template('result.html', mother=mother, father=father, possible_blood_groups=possible_blood_groups)

@app.route('/download', methods=['POST'])
def download_pdf():
    mother = request.form['mother']
    father = request.form['father']
    possible_blood_groups = blood_group_table.get((mother, father)) or blood_group_table.get((father, mother))

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    p.drawString(100, height - 100, f"Blood Group Prediction Result")
    p.drawString(100, height - 120, f"Mother's Blood Group: {mother}")
    p.drawString(100, height - 140, f"Father's Blood Group: {father}")
    p.drawString(100, height - 160, "Possible Blood Groups of the Child:")

    y_position = height - 180
    for bg in possible_blood_groups:
        p.drawString(120, y_position, f"- {bg}")
        y_position -= 20

    p.showPage()
    p.save()

    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="blood_group_prediction.pdf", mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
