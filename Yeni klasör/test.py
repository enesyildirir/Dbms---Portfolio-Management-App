from flask import Flask, render_template, request, redirect, session, url_for, jsonify
import pyodbc
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'cok_gizli_anahtar'

# --- MSSQL BAĞLANTISI ---
# Test dosyasından öğrendiğimiz sunucu adını buraya yaz (Muhtemelen . veya MMC)
SERVER_NAME = 'MMC' 
DATABASE_NAME = 'VTYSproje'

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
        # Alternatif sürücü denemesi (Gerekirse)
        conn_str = conn_str.replace('ODBC Driver 17 for SQL Server', 'SQL Server')
        return pyodbc.connect(conn_str)

# --- ROTALAR ---

@app.route('/')
def index():
    # Oturum kontrolü: Giriş yapılmamışsa login ekranına at
    if 'user_id' not in session:
        return render_template('test.html', page_mode='login', current_user=None, clients=[], transactions=[])
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 1. Şu anki kullanıcıyı (Broker) çek
    cursor.execute("SELECT * FROM CalisanlarTablosu WHERE CalisanID = ?", (session['user_id'],))
    user_row = cursor.fetchone()
    
    current_user = {
        "id": user_row.CalisanID,
        "name": user_row.Ad,
        "surname": user_row.Soyad,
        "role": "broker" 
    }

    # 2. SADECE BU BROKERA AİT MÜŞTERİLERİ ÇEK
    # SQL Sorgusu: HesaplarTablosu üzerinden CalisanID eşleşmesi yapıyoruz.
    clients_query = """
    SELECT DISTINCT y.YatirimciID, y.Ad, y.Soyad, y.Tel, y.Eposta, r.ProfilAdi, r.Aciklama, r.MaksIslemOrani
    FROM YatirimcilarTablosu y
    JOIN HesaplarTablosu h ON y.YatirimciID = h.YatirimciID
    LEFT JOIN RiskProfilTablosu r ON h.RiskProfilID = r.RiskProfilID
    WHERE h.CalisanID = ?
    """
    cursor.execute(clients_query, (session['user_id'],))
    clients_rows = cursor.fetchall()
    
    clients_data = []
    for row in clients_rows:
        # Bu müşterinin hesaplarını çek
        cursor.execute("SELECT * FROM HesaplarTablosu WHERE YatirimciID = ?", (row.YatirimciID,))
        accounts_rows = cursor.fetchall()
        
        accounts_data = []
        for acc in accounts_rows:
            # Komisyon bilgisini çek
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
        # --- YATIRIMCI GİRİŞİ ---
@app.route('/investor_login', methods=['POST'])
def investor_login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        print(f"--- YATIRIMCI GİRİŞ DENEMESİ: {username} ---")

        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Yatırımcıyı ara
        cursor.execute("SELECT YatirimciID, Ad, Soyad, SifreHash FROM YatirimcilarTablosu WHERE Eposta = ?", (username,))
        user_row = cursor.fetchone()
        conn.close()

        if user_row:
            print(f"   -> Yatırımcı Bulundu: ID={user_row.YatirimciID}")
            
            # Şifre Kontrolü
            if user_row.SifreHash == password:
                print("   -> ŞİFRE DOĞRU! Oturum açılıyor...")
                
                session.clear()
                session['investor_id'] = user_row.YatirimciID
                session['user_type'] = 'investor'
                session.permanent = True
                session.modified = True

                return jsonify({'success': True})
            else:
                print(f"   -> ŞİFRE YANLIŞ!")
                return jsonify({'success': False, 'message': 'Şifre hatalı!'})
        else:
            print("   -> YATIRIMCI BULUNAMADI!")
            return jsonify({'success': False, 'message': 'Bu E-posta ile kayıtlı yatırımcı yok.'})

    except Exception as e:
        print(f"   -> HATA OLUŞTU: {str(e)}")
        return jsonify({'success': False, 'message': f'Hata: {str(e)}'})

# --- YATIRIMCI HESAPLARI ---
@app.route('/get_investor_accounts', methods=['GET'])
def get_investor_accounts():
    if 'investor_id' not in session:
        return jsonify([])
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = """
    SELECT h.HesapNo, h.Bakiye, h.HesapAcilisTarihi, h.HesapDurumu,
           c.Ad + ' ' + c.Soyad as BrokerAdi,
           k.PlanAdi, k.MinimumKomisyon, k.KomisyonOrani
    FROM HesaplarTablosu h
    LEFT JOIN CalisanlarTablosu c ON h.CalisanID = c.CalisanID
    LEFT JOIN KomisyonlarTablosu k ON h.KomisyonID = k.KomisyonID
    WHERE h.YatirimciID = ?
    """
    
    cursor.execute(query, (session['investor_id'],))
    rows = cursor.fetchall()
    
    accounts = []
    for row in rows:
        accounts.append({
            "accountId": row.HesapNo,
            "balance": float(row.Bakiye),
            "openDate": row.HesapAcilisTarihi.strftime('%Y-%m-%d') if row.HesapAcilisTarihi else '',
            "status": row.HesapDurumu,
            "brokerName": row.BrokerAdi or 'N/A',
            "commissionPlan": {
                "name": row.PlanAdi or 'Standart',
                "minCommission": float(row.MinimumKomisyon) if row.MinimumKomisyon else 50,
                "rate": float(row.KomisyonOrani) if row.KomisyonOrani else 1.0
            }
        })
    
    conn.close()
    return jsonify(accounts)

# --- YATIRIMCI İŞLEM GEÇMİŞİ ---
@app.route('/get_investor_transactions', methods=['GET'])
def get_investor_transactions():
    if 'investor_id' not in session:
        return jsonify([])
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = """
    SELECT i.IslemID, i.IslemTarihi, i.IslemTipi, i.Miktar, i.BirimFiyat, 
           i.ToplamTutar, i.KomisyonMiktar, v.VarlikAdi, v.VarlikID, h.HesapNo
    FROM IslemlerTablosu i
    JOIN HesaplarTablosu h ON i.HesapNo = h.HesapNo
    JOIN VarliklarTablosu v ON i.VarlikID = v.VarlikID
    WHERE h.YatirimciID = ?
    ORDER BY i.IslemTarihi DESC
    """
    
    cursor.execute(query, (session['investor_id'],))
    rows = cursor.fetchall()
    
    transactions = []
    for row in rows:
        net_total = float(row.ToplamTutar)
        if row.IslemTipi == 'ALIS':
            net_total += float(row.KomisyonMiktar)
        else:
            net_total -= float(row.KomisyonMiktar)
            
        transactions.append({
            "id": row.IslemID,
            "date": row.IslemTarihi.strftime('%Y-%m-%d %H:%M:%S'),
            "accountId": row.HesapNo,
            "asset": row.VarlikID,
            "assetName": row.VarlikAdi,
            "type": row.IslemTipi,
            "amount": float(row.Miktar),
            "unitPrice": float(row.BirimFiyat),
            "total": float(row.ToplamTutar),
            "commission": float(row.KomisyonMiktar),
            "netTotal": net_total
        })
    
    conn.close()
    return jsonify(transactions)

# --- ANA SAYFAYI GÜNCELLE (Yatırımcı Desteği İçin) ---
@app.route('/')
def index():
    print("--- ANA SAYFA İSTEĞİ GELDİ ---")
    print(f"Mevcut Session İçeriği: {session}")

    # Broker kontrolü
    if 'user_id' in session:
        print(f"✅ Broker girişi tespit edildi: {session['user_id']}")
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM CalisanlarTablosu WHERE CalisanID = ?", (session['user_id'],))
        user_row = cursor.fetchone()
        
        current_user = {
            "id": user_row.CalisanID,
            "name": user_row.Ad,
            "surname": user_row.Soyad,
            "role": "broker"
        }

        # Müşterileri çek
        clients_query = """
        SELECT DISTINCT y.YatirimciID, y.Ad, y.Soyad, y.Tel, y.Eposta, r.ProfilAdi, r.Aciklama, r.MaksIslemOrani
        FROM YatirimcilarTablosu y
        JOIN HesaplarTablosu h ON y.YatirimciID = h.YatirimciID
        LEFT JOIN RiskProfilTablosu r ON h.RiskProfilID = r.RiskProfilID
        WHERE h.CalisanID = ?
        """
        cursor.execute(clients_query, (session['user_id'],))
        clients_rows = cursor.fetchall()
        
        clients_data = []
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

        # İşlemleri çek
        transactions_query = """
        SELECT TOP 10 
            i.IslemID, i.IslemTarihi, i.IslemTipi, i.Miktar, i.BirimFiyat, i.KomisyonMiktar, i.ToplamTutar,
            y.Ad + ' ' + y.Soyad as MusteriAdi,
            v.VarlikAdi
        FROM IslemlerTablosu i
        JOIN HesaplarTablosu h ON i.HesapNo = h.HesapNo
        JOIN YatirimcilarTablosu y ON h.YatirimciID = y.YatirimciID
        JOIN VarliklarTablosu v ON i.VarlikID = v.VarlikID
        WHERE i.CalisanID = ?
        ORDER BY i.IslemTarihi DESC
        """
        cursor.execute(transactions_query, (session['user_id'],))
        trans_rows = cursor.fetchall()
        
        transactions_data = []
        for t in trans_rows:
            transactions_data.append({
                "id": t.IslemID,
                "date": t.IslemTarihi.strftime('%Y-%m-%d %H:%M'),
                "client": t.MusteriAdi,
                "asset": t.VarlikAdi,
                "type": t.IslemTipi,
                "amount": float(t.Miktar),
                "price": float(t.BirimFiyat),
                "commission": float(t.KomisyonMiktar)
            })

        conn.close()
        
        return render_template('index.html', 
                               page_mode='dashboard',
                               current_user=current_user,
                               clients=clients_data,
                               transactions=transactions_data)
    
    # Yatırımcı kontrolü
    elif 'investor_id' in session:
        print(f"✅ Yatırımcı girişi tespit edildi: {session['investor_id']}")
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM YatirimcilarTablosu WHERE YatirimciID = ?", (session['investor_id'],))
        investor_row = cursor.fetchone()
        
        current_user = {
            "id": investor_row.YatirimciID,
            "name": investor_row.Ad,
            "surname": investor_row.Soyad,
            "role": "investor"
        }
        
        conn.close()
        
        return render_template('index.html',
                               page_mode='dashboard',
                               current_user=current_user,
                               clients=[],
                               transactions=[])
    
    # Giriş yapılmamış
    else:
        print("❌ Oturum yok! Login sayfası gösteriliyor...")
        return render_template('index.html', page_mode='login', current_user=None, clients=[], transactions=[])

    # 3. BU BROKERIN YAPTIĞI SON İŞLEMLERİ ÇEK
    transactions_query = """
    SELECT TOP 10 
        i.IslemID, i.IslemTarihi, i.IslemTipi, i.Miktar, i.BirimFiyat, i.KomisyonMiktar, i.ToplamTutar,
        y.Ad + ' ' + y.Soyad as MusteriAdi,
        v.VarlikAdi
    FROM IslemlerTablosu i
    JOIN HesaplarTablosu h ON i.HesapNo = h.HesapNo
    JOIN YatirimcilarTablosu y ON h.YatirimciID = y.YatirimciID
    JOIN VarliklarTablosu v ON i.VarlikID = v.VarlikID
    WHERE i.CalisanID = ?
    ORDER BY i.IslemTarihi DESC
    """
    cursor.execute(transactions_query, (session['user_id'],))
    trans_rows = cursor.fetchall()
    
    transactions_data = []
    for t in trans_rows:
        transactions_data.append({
            "id": t.IslemID,
            "date": t.IslemTarihi.strftime('%Y-%m-%d %H:%M'),
            "client": t.MusteriAdi,
            "asset": t.VarlikAdi,
            "type": t.IslemTipi,
            "amount": float(t.Miktar),
            "price": float(t.BirimFiyat),
            "commission": float(t.KomisyonMiktar)
        })

    conn.close()
    
    return render_template('index.html', 
                           page_mode='dashboard',
                           current_user=current_user,
                           clients=clients_data,
                           transactions=transactions_data)

# --- LOGIN ROTASI ---
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        print(f"--- GİRİŞ DENEMESİ: {username} ---") # Terminale YAZ

        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Kullanıcıyı ara
        cursor.execute("SELECT CalisanID, Ad, Soyad, SifreHash FROM CalisanlarTablosu WHERE Eposta = ?", (username,))
        user_row = cursor.fetchone()
        conn.close()

        if user_row:
            print(f"   -> Kullanıcı Bulundu: ID={user_row.CalisanID}, DB Şifre={user_row.SifreHash}")
            
            # Şifre Kontrolü (Düz metin karşılaştırması yapıyoruz)
            if user_row.SifreHash == password:
                print("   -> ŞİFRE DOĞRU! Oturum açılıyor...")
                session.clear()
                session['user_id'] = user_row.CalisanID
                session.modified = True
                return jsonify({'success': True})
            else:
                print(f"   -> ŞİFRE YANLIŞ! Beklenen: '{user_row.SifreHash}', Gelen: '{password}'")
                return jsonify({'success': False, 'message': 'Şifre hatalı!'})
        else:
            print("   -> KULLANICI BULUNAMADI!")
            return jsonify({'success': False, 'message': 'Bu E-posta ile kayıtlı broker yok.'})

    except Exception as e:
        print(f"   -> HATA OLUŞTU: {str(e)}")
        return jsonify({'success': False, 'message': f'Hata: {str(e)}'})
    

# --- LOGOUT ROTASI ---
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

# --- YENİ İŞLEM EKLEME ---
@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Oturum açmanız gerekiyor'})

    data = request.get_json()
    
    hesap_no = data.get('accountId')
    varlik_id = data.get('assetId')
    islem_tipi = data.get('type')
    miktar = float(data.get('amount'))
    fiyat = float(data.get('price'))
    
    toplam_tutar = miktar * fiyat
    komisyon = toplam_tutar * 0.01 
    net_tutar = toplam_tutar + komisyon if islem_tipi == 'ALIS' else toplam_tutar - komisyon

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # İşlemi Kaydet
        cursor.execute("""
            INSERT INTO IslemlerTablosu (IslemTipi, IslemTarihi, Miktar, BirimFiyat, KomisyonMiktar, ToplamTutar, KarZarar, CalisanID, HesapNo, VarlikID)
            VALUES (?, GETDATE(), ?, ?, ?, ?, 0, ?, ?, ?)
        """, (islem_tipi, miktar, fiyat, komisyon, toplam_tutar, session['user_id'], hesap_no, varlik_id))

        # Bakiyeyi Güncelle
        if islem_tipi == 'ALIS':
            cursor.execute("UPDATE HesaplarTablosu SET Bakiye = Bakiye - ? WHERE HesapNo = ?", (net_tutar, hesap_no))
        else:
            cursor.execute("UPDATE HesaplarTablosu SET Bakiye = Bakiye + ? WHERE HesapNo = ?", (net_tutar, hesap_no))

        conn.commit()
        return jsonify({'success': True, 'message': 'İşlem kaydedildi.'})
    except Exception as e:
        conn.rollback()
        return jsonify({'success': False, 'message': str(e)})
    finally:
        conn.close()

# --- YENİ HESAP AÇMA ---
@app.route('/create_account', methods=['POST'])
def create_account():
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Yetkisiz işlem'})

    data = request.get_json()
    broker_id = data.get('brokerId')
    yatirimci_id = data.get('investorId')
    baslangic_bakiye = float(data.get('initialDeposit'))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO HesaplarTablosu (HesapAcilisTarihi, Bakiye, HesapDurumu, VarlikID, KomisyonID, YatirimciID, CalisanID, RiskProfilID)
            VALUES (GETDATE(), ?, 'Aktif', 1, 1, ?, ?, 2)
        """, (baslangic_bakiye, yatirimci_id, broker_id))
        
        conn.commit()
        return jsonify({'success': True, 'message': 'Yeni hesap açıldı.'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)