from flask import Flask, render_template, request, redirect, session, url_for, jsonify
import pyodbc
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'cok_gizli_anahtar'

# Oturum Ayarları
app.config.update(
    SESSION_COOKIE_NAME='yatirim_oturum',
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SECURE=False,
    SESSION_PERMANENT=True
)

# --- MSSQL BAĞLANTISI ---
SERVER_NAME = '.'  # Buraya kendi server adını yaz (MMC veya .)
DATABASE_NAME = 'YatirimProjesiDB'

def get_db_connection():
    conn_str = (
        'DRIVER={ODBC Driver 17 for SQL Server};'
        f'SERVER={SERVER_NAME};'
        f'DATABASE={DATABASE_NAME};'
        'Trusted_Connection=yes;'
    )
    try:
        conn = pyodbc.connect(conn_str)
        return conn
    except pyodbc.Error as ex:
        print(f"Bağlantı Hatası: {ex}")
        conn_str = conn_str.replace('ODBC Driver 17 for SQL Server', 'SQL Server')
        return pyodbc.connect(conn_str)

# --- ROTALAR ---

@app.route('/')
def index():
    if 'user_id' not in session:
        return render_template('index.html', page_mode='login', current_user=None, clients=[], transactions=[])
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    role = session.get('role')
    user_id = session.get('user_id')
    
    current_user = {}
    clients_data = []
    transactions_data = []
    
    # --- BROKER GİRİŞİ YAPILDIYSA ---
    if role == 'broker':
        cursor.execute("SELECT * FROM CalisanlarTablosu WHERE CalisanID = ?", (user_id,))
        user_row = cursor.fetchone()
        current_user = {"id": user_row.CalisanID, "name": user_row.Ad, "surname": user_row.Soyad, "role": "broker", "email": user_row.Eposta}
        
        # Broker'a bağlı müşterileri çek
        clients_query = """
        SELECT DISTINCT y.YatirimciID, y.Ad, y.Soyad, y.Tel, y.Eposta, r.ProfilAdi, r.Aciklama, r.MaksIslemOrani
        FROM YatirimcilarTablosu y
        JOIN HesaplarTablosu h ON y.YatirimciID = h.YatirimciID
        LEFT JOIN RiskProfilTablosu r ON h.RiskProfilID = r.RiskProfilID
        WHERE h.CalisanID = ?
        """
        cursor.execute(clients_query, (user_id,))
        clients_rows = cursor.fetchall()
        
        for row in clients_rows:
            cursor.execute("SELECT * FROM HesaplarTablosu WHERE YatirimciID = ?", (row.YatirimciID,))
            accounts_rows = cursor.fetchall()
            accounts_data = []
            for acc in accounts_rows:
                cursor.execute("SELECT * FROM KomisyonlarTablosu WHERE KomisyonID = ?", (acc.KomisyonID,))
                comm = cursor.fetchone()
                accounts_data.append({
                    "accountId": str(acc.HesapNo),
                    "balance": float(acc.Bakiye),
                    "openDate": acc.HesapAcilisTarihi.strftime('%Y-%m-%d') if acc.HesapAcilisTarihi else '',
                    "commissionPlan": "Standart Plan",
                    "minCommission": float(comm.MinimumKomisyon) if comm else 0
                })
            
            clients_data.append({
                "id": row.YatirimciID,
                "name": f"{row.Ad} {row.Soyad}",
                "phone": row.Tel,
                "email": row.Eposta,
                "riskProfile": {
                    "name": row.ProfilAdi or 'Belirsiz',
                    "description": row.Aciklama or '',
                    "maxStockRatio": float(row.MaksIslemOrani) if row.MaksIslemOrani else 0
                },
                "accounts": accounts_data
            })

        # Broker İşlemleri
        transactions_query = """
        SELECT TOP 10 i.IslemID, i.IslemTarihi, i.IslemTipi, i.Miktar, i.BirimFiyat, i.KomisyonMiktar, i.ToplamTutar,
        y.Ad + ' ' + y.Soyad as MusteriAdi, v.VarlikAdi
        FROM IslemlerTablosu i
        JOIN HesaplarTablosu h ON i.HesapNo = h.HesapNo
        JOIN YatirimcilarTablosu y ON h.YatirimciID = y.YatirimciID
        JOIN VarliklarTablosu v ON i.VarlikID = v.VarlikID
        WHERE i.CalisanID = ? ORDER BY i.IslemTarihi DESC
        """
        cursor.execute(transactions_query, (user_id,))
        
    # --- YATIRIMCI GİRİŞİ YAPILDIYSA ---
    elif role == 'investor':
        cursor.execute("SELECT * FROM YatirimcilarTablosu WHERE YatirimciID = ?", (user_id,))
        user_row = cursor.fetchone()
        current_user = {"id": user_row.YatirimciID, "name": user_row.Ad, "surname": user_row.Soyad, "role": "investor", "email": user_row.Eposta}
        
        # Yatırımcının Kendi Hesapları
        cursor.execute("""
            SELECT h.*, k.MinimumKomisyon, c.Ad + ' ' + c.Soyad as BrokerAdi, c.Eposta as BrokerEmail, c.Tel as BrokerTel
            FROM HesaplarTablosu h
            LEFT JOIN KomisyonlarTablosu k ON h.KomisyonID = k.KomisyonID
            LEFT JOIN CalisanlarTablosu c ON h.CalisanID = c.CalisanID
            WHERE h.YatirimciID = ?
        """, (user_id,))
        accounts_rows = cursor.fetchall()
        
        my_accounts = []
        broker_info = None
        
        for acc in accounts_rows:
            if not broker_info and acc.BrokerAdi:
                broker_info = {"name": acc.BrokerAdi, "email": acc.BrokerEmail, "phone": acc.BrokerTel}
                
            my_accounts.append({
                "accountId": str(acc.HesapNo),
                "balance": float(acc.Bakiye),
                "openDate": acc.HesapAcilisTarihi.strftime('%Y-%m-%d') if acc.HesapAcilisTarihi else '',
                "status": acc.HesapDurumu,
                "commissionPlan": {"name": "Standart", "minCommission": float(acc.MinimumKomisyon) if acc.MinimumKomisyon else 0, "rate": 1.0},
                "brokerId": acc.CalisanID
            })
            
        # Yatırımcının Kendi Verisi (clients dizisi içinde tek eleman olarak gönderiyoruz ki frontend yapısı bozulmasın)
        clients_data = [{
            "id": user_row.YatirimciID,
            "name": f"{user_row.Ad} {user_row.Soyad}",
            "email": user_row.Eposta,
            "phone": user_row.Tel,
            "accounts": my_accounts,
            "broker": broker_info,
            "riskProfile": {"name": "Dengeli", "maxStockRatio": 60, "description": "Standart Profil"} # Şimdilik sabit
        }]

        # Yatırımcı İşlemleri
        transactions_query = """
        SELECT TOP 10 i.IslemID, i.IslemTarihi, i.IslemTipi, i.Miktar, i.BirimFiyat, i.KomisyonMiktar, i.ToplamTutar, v.VarlikAdi
        FROM IslemlerTablosu i
        JOIN HesaplarTablosu h ON i.HesapNo = h.HesapNo
        JOIN VarliklarTablosu v ON i.VarlikID = v.VarlikID
        WHERE h.YatirimciID = ? ORDER BY i.IslemTarihi DESC
        """
        cursor.execute(transactions_query, (user_id,))

    # İşlem Verilerini Çekme (Ortak)
    trans_rows = cursor.fetchall()
    for t in trans_rows:
        transactions_data.append({
            "id": t.IslemID,
            "date": t.IslemTarihi.strftime('%Y-%m-%d %H:%M'),
            "client": t.MusteriAdi if role == 'broker' else 'Ben',
            "asset": t.VarlikAdi,
            "type": t.IslemTipi,
            "amount": float(t.Miktar),
            "price": float(t.BirimFiyat),
            "commission": float(t.KomisyonMiktar),
            "total": float(t.ToplamTutar),
            "netTotal": float(t.ToplamTutar) # Basitlik için
        })

    conn.close()
    
    return render_template('index.html', 
                           page_mode='dashboard',
                           current_user=current_user,
                           clients=clients_data,
                           transactions=transactions_data)

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        role = data.get('role') # Frontend'den gelen rol (broker/investor)

        conn = get_db_connection()
        cursor = conn.cursor()
        
        user_row = None
        
        if role == 'broker':
            cursor.execute("SELECT CalisanID as ID, Ad, Soyad, SifreHash FROM CalisanlarTablosu WHERE Eposta = ?", (username,))
            user_row = cursor.fetchone()
        elif role == 'investor':
            cursor.execute("SELECT YatirimciID as ID, Ad, Soyad, SifreHash FROM YatirimcilarTablosu WHERE Eposta = ?", (username,))
            user_row = cursor.fetchone()
            
        conn.close()

        if user_row:
            if str(user_row.SifreHash) == str(password):
                session.clear()
                session['user_id'] = user_row.ID
                session['role'] = role
                session.permanent = True
                return jsonify({'success': True})
            else:
                return jsonify({'success': False, 'message': 'Şifre hatalı!'})
        else:
            return jsonify({'success': False, 'message': 'Kullanıcı bulunamadı.'})

    except Exception as e:
        return jsonify({'success': False, 'message': f'Hata: {str(e)}'})

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    if 'user_id' not in session: return jsonify({'success': False})
    # ... (Buradaki kod aynı kalabilir, yukarıdakiyle aynı mantık) ...
    return jsonify({'success': True, 'message': 'İşlem eklendi'}) 
    # Not: Yer kaplamaması için burayı kısalttım, önceki kodunun aynısını kullanabilirsin veya basitçe true dön

@app.route('/create_account', methods=['POST'])
def create_account():
    # ... (Önceki kodun aynısı) ...
    return jsonify({'success': True, 'message': 'Hesap açıldı'})

if __name__ == '__main__':
    app.run(debug=True)