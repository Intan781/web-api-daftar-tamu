from flask import Flask, request, jsonify
from models import db, Tamu

app = Flask(__name__)

# Konfigurasi SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Endpoint untuk menerima data tamu dari aplikasi Android
@app.route("/api/tamu", methods=["POST"])
def tambah_tamu():
    data = request.get_json()
    try:
        tamu = Tamu(
            nama=data.get("nama"),
            no_hp=data.get("no_hp"),
            no_polis=data.get("no_polis"),
            keperluan=data.get("keperluan"),
            alamat=data.get("alamat"),
            email=data.get("email")
        )
        db.session.add(tamu)
        db.session.commit()
        return jsonify({"status": "success", "message": "Data berhasil disimpan"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Endpoint untuk menampilkan semua data tamu
@app.route("/api/tamu", methods=["GET"])
def lihat_tamu():
    semua_tamu = Tamu.query.all()
    hasil = []
    for tamu in semua_tamu:
        hasil.append({
            "id": tamu.id,
            "nama": tamu.nama,
            "no_hp": tamu.no_hp,
            "no_polis": tamu.no_polis,
            "keperluan": tamu.keperluan,
            "alamat": tamu.alamat,
            "email": tamu.email
        })
    return jsonify(hasil)

# Jalankan aplikasi Flask
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
