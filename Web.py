# app.py
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Rute untuk menyajikan halaman HTML utama
@app.route('/')
def home():
    """
    Menyajikan file HTML utama untuk antarmuka web.
    Pastikan file 'index.html' berada di dalam folder 'templates'
    di direktori yang sama dengan 'app.py'.
    """
    return render_template('index.html')

# Rute untuk menyajikan file statis (misalnya CSS, JS, jika ada di masa depan)
# Meskipun saat ini CSS/JS ada di index.html, ini adalah praktik baik.
@app.route('/static/<path:filename>')
def static_files(filename):
    """
    Menyajikan file statis dari folder 'static'.
    """
    return send_from_directory('static', filename)

if __name__ == '__main__':
    # Jalankan aplikasi Flask.
    # host='0.0.0.0': Membuat server dapat diakses dari IP lain di jaringan lokal.
    # port=5000: Menjalankan server pada port 5000.
    app.run(debug=True, host='0.0.0.0', port=5000)
