from flask import Flask, render_template, request, jsonify
import pyodbc
import random
from datetime import datetime
import yfinance as yf
import math
import os
import json
import time

app = Flask(__name__)

# Veritabanı Bağlantı Ayarları
# Server: MMC, Database: VTYSproje
def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=MMC;'              # Senin server ismin
        'DATABASE=VTYSproje;'      # Veritabanı ismin
        'Trusted_Connection=yes;'  # Windows Authentication kullanıyorsan bu kalsın
        # Eğer kullanıcı adı/şifre varsa üstteki satırı silip şunları aç:
        # 'UID=kullanici_adi;'
        # 'PWD=sifre;'
    )
    return conn

@app.route('/')
def index():
    # templates klasöründeki index.html'i çalıştırır
    return render_template('index.html')

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        user_type = data.get('userType')

        print(f"Gelen İstek: {user_type} - {username}")

        conn = get_db_connection()
        cursor = conn.cursor()
        user_data = None

        if user_type == 'investor':
            # DÜZELTME BURADA: RiskProfilID sorgudan çıkarıldı
            query = """
                SELECT YatirimciID, Ad, Soyad, Eposta 
                FROM YatirimcilarTablosu 
                WHERE Eposta = ? AND SifreHash = ?
            """
            cursor.execute(query, (username, password))
            row = cursor.fetchone()
            
            if row:
                user_data = {
                    'id': row.YatirimciID,
                    'name': row.Ad,
                    'surname': row.Soyad,
                    'email': row.Eposta,
                    'role': 'investor',
                    'riskProfileId': 1 # Şimdilik varsayılan bir değer veriyoruz, giriş bozulmasın diye.
                }

        elif user_type == 'broker':
            # Broker sorgusu aynı kalabilir (Tabii PozisyonID varsa)
            query = """
                SELECT CalisanID, Ad, Soyad, Eposta, PozisyonID 
                FROM CalisanlarTablosu 
                WHERE Eposta = ? AND SifreHash = ?
            """
            cursor.execute(query, (username, password))
            row = cursor.fetchone()

            if row:
                user_data = {
                    'id': row.CalisanID,
                    'name': row.Ad,
                    'surname': row.Soyad,
                    'email': row.Eposta,
                    'role': 'broker',
                    'positionId': row.PozisyonID
                }
        
        conn.close()

        if user_data:
            print("Kullanıcı bulundu, giriş yapılıyor.")
            return jsonify({'success': True, 'user': user_data})
        else:
            print("Kullanıcı bulunamadı.")
            return jsonify({'success': False, 'message': 'E-posta veya şifre hatalı!'}), 401

    except pyodbc.Error as db_err:
        print("--------------------------------------------------")
        print("VERİTABANI HATASI (SQL/Bağlantı):")
        print(db_err)
        print("--------------------------------------------------")
        return jsonify({'success': False, 'message': 'Veritabanı bağlantı hatası.'}), 500

    except Exception as e:
        print("--------------------------------------------------")
        print("PYTHON KOD HATASI:")
        print(e)
        import traceback
        traceback.print_exc()
        print("--------------------------------------------------")
        return jsonify({'success': False, 'message': f'Sunucu hatası: {str(e)}'}), 500
# ... login fonksiyonundan sonra ...





 #--------------------------------------------   
@app.route('/api/broker/dashboard/<int:broker_id>', methods=['GET'])
def get_broker_dashboard(broker_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # 1. TEMEL İSTATİSTİKLER (Veritabanından Hesapla)
        # Toplam Komisyon
        cursor.execute("SELECT SUM(KomisyonMiktar) FROM IslemlerTablosu WHERE CalisanID = ?", (broker_id,))
        row_total = cursor.fetchone()
        total_commission = float(row_total[0]) if row_total[0] else 0

        # Bu Ayki Komisyon (SQL Server Syntax: MONTH(IslemTarihi))
        import datetime
        current_month = datetime.datetime.now().month
        current_year = datetime.datetime.now().year
        
        cursor.execute("""
            SELECT SUM(KomisyonMiktar) FROM IslemlerTablosu 
            WHERE CalisanID = ? AND MONTH(IslemTarihi) = ? AND YEAR(IslemTarihi) = ?
        """, (broker_id, current_month, current_year))
        row_month = cursor.fetchone()
        monthly_commission = float(row_month[0]) if row_month[0] else 0

        # Aktif Müşteri Sayısı (İşlem yapmış benzersiz müşteri sayısı)
        cursor.execute("SELECT COUNT(DISTINCT HesapNo) FROM IslemlerTablosu WHERE CalisanID = ?", (broker_id,))
        row_active = cursor.fetchone()
        active_clients_count = row_active[0] if row_active[0] else 0

        broker_stats = {
            'totalCommission': total_commission,
            'monthlyCommission': monthly_commission,
            'activeClients': active_clients_count
        }

        # 2. GRAFİK İÇİN AYLIK PERFORMANS VERİLERİ (Son 6 Ay)
        # Tarihe göre gruplayıp ay ay toplam komisyonu çekiyoruz
        query_performance = """
            SELECT 
                FORMAT(IslemTarihi, 'yyyy-MM') as Donem,
                SUM(KomisyonMiktar) as ToplamKomisyon,
                COUNT(IslemID) as IslemSayisi
            FROM IslemlerTablosu
            WHERE CalisanID = ?
            GROUP BY FORMAT(IslemTarihi, 'yyyy-MM')
            ORDER BY Donem
        """
        cursor.execute(query_performance, (broker_id,))
        perf_rows = cursor.fetchall()

        monthly_performance = []
        for row in perf_rows:
            monthly_performance.append({
                'month': row.Donem,           # Örn: "2023-12"
                'commission': float(row.ToplamKomisyon),
                'count': row.IslemSayisi
            })
        # --- 2.1 : SON 5 İŞLEM ---
        # Müşteri Adı (Yatirimcilar) ve Varlık Adı (Varliklar) tablolarıyla birleştiriyoruz
        query_recent = """
            SELECT TOP 5
                I.IslemTarihi, 
                Y.Ad + ' ' + Y.Soyad as MusteriAdi,
                V.VarlikAdi,
                I.IslemTipi,
                I.Miktar,
                I.BirimFiyat,
                I.KomisyonMiktar
            FROM IslemlerTablosu I
            JOIN HesaplarTablosu H ON I.HesapNo = H.HesapNo
            JOIN YatirimcilarTablosu Y ON H.YatirimciID = Y.YatirimciID
            JOIN VarliklarTablosu V ON I.VarlikID = V.VarlikID
            WHERE I.CalisanID = ?
            ORDER BY I.IslemTarihi DESC
        """
        cursor.execute(query_recent, (broker_id,))
        recent_rows = cursor.fetchall()
        
        recent_transactions = []
        for row in recent_rows:
            recent_transactions.append({
                'date': str(row.IslemTarihi)[0:16], # Saniye kısmını kırpıyoruz
                'client': row.MusteriAdi,
                'asset': row.VarlikAdi,
                'type': row.IslemTipi,
                'amount': float(row.Miktar),
                'price': float(row.BirimFiyat),
                'commission': float(row.KomisyonMiktar)
            })

        # 3. MÜŞTERİ LİSTESİ VE PORTFÖYLERİ (Önceki kodun aynısı)
        # 4. MÜŞTERİ LİSTESİ VE PORTFÖYLERİ (GÜNCELLENMİŞ VERSİYON)
        query = """
            SELECT 
                Y.YatirimciID, Y.Ad, Y.Soyad, Y.Tel, Y.Eposta, 
                H.HesapNo, H.Bakiye, H.HesapAcilisTarihi, H.HesapDurumu
            FROM HesaplarTablosu H
            JOIN YatirimcilarTablosu Y ON H.YatirimciID = Y.YatirimciID
            WHERE H.CalisanID = ?
        """
        cursor.execute(query, (broker_id,))
        rows = cursor.fetchall()
        
        clients_map = {}
        all_rows = [row for row in rows] 

        for row in all_rows:
            y_id = row.YatirimciID
            acc_no = row.HesapNo

            # Portföyü Çek
            portfolio_query = """
                SELECT V.VarlikID, V.VarlikAdi,
                       SUM(CASE WHEN I.IslemTipi = 'ALIS' THEN I.Miktar ELSE 0 END) - 
                       SUM(CASE WHEN I.IslemTipi = 'SATIS' THEN I.Miktar ELSE 0 END) as Adet
                FROM IslemlerTablosu I
                JOIN VarliklarTablosu V ON I.VarlikID = V.VarlikID
                WHERE I.HesapNo = ?
                GROUP BY V.VarlikID, V.VarlikAdi
                HAVING (SUM(CASE WHEN I.IslemTipi = 'ALIS' THEN I.Miktar ELSE 0 END) - 
                        SUM(CASE WHEN I.IslemTipi = 'SATIS' THEN I.Miktar ELSE 0 END)) > 0
            """
            cursor.execute(portfolio_query, (acc_no,))
            portfolio_rows = cursor.fetchall()

            holdings = []
            for p_row in portfolio_rows:
                holdings.append({
                    'assetId': p_row.VarlikID,
                    'assetName': p_row.VarlikAdi,
                    'quantity': float(p_row.Adet)
                })

            if y_id not in clients_map:
                # Risk Profilini Rastgele veya Sabit Belirle (DB'de yoksa)
                # Burayı daha zeki hale getiriyoruz:
                risk_profile = {'name': 'Genel', 'maxStockRatio': 50, 'description': 'Standart yatırımcı profili.'}
                
                # Örnek mantık: ID'si tek olanlar Agresif, çift olanlar Dengeli olsun (Demo amaçlı)
                if y_id % 3 == 0:
                    risk_profile = {'name': 'Agresif', 'maxStockRatio': 80, 'description': 'Yüksek getiri hedefli, yüksek risk toleransı.'}
                elif y_id % 3 == 1:
                    risk_profile = {'name': 'Dengeli', 'maxStockRatio': 60, 'description': 'Orta düzey risk ve getiri dengesi.'}
                else:
                    risk_profile = {'name': 'Muhafazakar', 'maxStockRatio': 30, 'description': 'Düşük risk, sermaye koruma öncelikli.'}

                clients_map[y_id] = {
                    'id': y_id,
                    'name': f"{row.Ad} {row.Soyad}",
                    'phone': row.Tel,
                    'email': row.Eposta,
                    'riskProfile': risk_profile,
                    'accounts': []
                }
            
            # --- İŞTE EKSİK OLAN KISIM BURASIYDI ---
            # Hesap detaylarına commissionPlan ve minCommission ekliyoruz
            clients_map[y_id]['accounts'].append({
                'accountId': row.HesapNo,
                'balance': float(row.Bakiye),
                'openDate': str(row.HesapAcilisTarihi),
                'status': row.HesapDurumu,
                'commissionPlan': 'Standart Plan',  # <-- ARTIK UNDEFINED OLMAYACAK
                'minCommission': 50,                # <-- ARTIK UNDEFINED OLMAYACAK
                'holdings': holdings
            })

        clients_list = list(clients_map.values())

        return jsonify({
            'success': True,
            'stats': broker_stats,
            'monthlyPerformance': monthly_performance,
            'recentTransactions': recent_transactions,
            'clients': clients_list
        })

    except Exception as e:
        print(f"Broker Dashboard hatası: {e}")
        return jsonify({'success': False, 'message': str(e)}), 500
    finally:
        conn.close()
# İŞLEM OLUŞTURMA API'Sİ
#********************************
#--------------------------------------------
@app.route('/api/transaction/create', methods=['POST'])
def create_transaction():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        data = request.json
        account_id = data.get('accountId')
        asset_code = data.get('assetId')
        trans_type = data.get('type')        
        amount = float(data.get('amount'))
        unit_price = float(data.get('price'))
        
        # --- 1. GÜVENLİK KONTROLÜ: HESAP AKTİF Mİ? ---
        cursor.execute("SELECT HesapDurumu FROM HesaplarTablosu WHERE HesapNo = ?", (account_id,))
        status_row = cursor.fetchone()
        
        if not status_row:
             return jsonify({'success': False, 'message': 'Hesap bulunamadı!'}), 404
             
        # Eğer Durum 'Aktif' değilse işlemi reddet
        if status_row[0] != 'Aktif':
             return jsonify({'success': False, 'message': 'HATA: Bu hesap PASİF durumdadır. İşlem yapmak için önce hesabı aktifleştirin.'}), 400
        print(f"--- İŞLEM TALEBİ: {trans_type} - {asset_code} ---")

        # 1. VARLIK ID BULMA (Gelişmiş Eşleştirme)
        varlik_id = None
        
        # Manuel Harita (Veritabanındaki ID'lerini buraya göre güncellemelisin)
        # Örn: Senin veritabanında SASA'nın ID'si 9 ise buraya 9 yaz.
        asset_map = {
            'THYAO.IS': 1,  'THYAO': 1,
            'USDTRY': 2,    'USD/TRY': 2,
            'GARAN.IS': 6,  'GARAN': 6,
            'AKBNK.IS': 7,  'AKBNK': 7,
            'EREGL.IS': 11, 'EREGL': 11,
            # Diğer hisselerinin ID'lerini SQL tablonla eşleşecek şekilde buraya ekleyebilirsin
        }
        
        if asset_code in asset_map:
            varlik_id = asset_map[asset_code]
            print(f"Haritadan bulundu: ID {varlik_id}")
        else:
            # Haritada yoksa Veritabanında Ara
            # ÖNCE TEMİZLİK YAP: 'SASA.IS' -> 'SASA'
            clean_name = asset_code.replace('.IS', '').replace('TRY=X', 'Dolar')
            
            print(f"Veritabanında aranıyor: {clean_name}")
            
            # Veritabanında VarlikAdi içinde arıyoruz (Örn: 'Sasa' kelimesi geçiyor mu?)
            cursor.execute("SELECT TOP 1 VarlikID FROM VarliklarTablosu WHERE VarlikAdi LIKE ?", (f"%{clean_name}%",))
            row = cursor.fetchone()
            
            if row:
                varlik_id = row[0]
                print(f"Veritabanından bulundu: ID {varlik_id}")
            else:
                # KRİTİK DEĞİŞİKLİK: Bulamazsa hata ver, THY (1) yapma!
                return jsonify({'success': False, 'message': f"HATA: '{asset_code}' veritabanında bulunamadı! Lütfen önce VarliklarTablosu'na ekleyin."}), 400

        # 2. HESAP BİLGİLERİNİ ÇEK
        cursor.execute("SELECT Bakiye, YatirimciID, CalisanID FROM HesaplarTablosu WHERE HesapNo = ?", (account_id,))
        acc_row = cursor.fetchone()
        
        if not acc_row:
            return jsonify({'success': False, 'message': 'Hesap bulunamadı!'}), 404
            
        current_balance = float(acc_row[0])
        investor_id = acc_row[1]
        broker_id = acc_row[2]

        total_amount = amount * unit_price
        commission = total_amount * 0.01 
        
        # 3. KONTROLLER
        if trans_type == 'ALIS':
            cost = total_amount + commission
            if current_balance < cost:
                 return jsonify({'success': False, 'message': f'Yetersiz Bakiye! Gereken: {cost:.2f}, Mevcut: {current_balance:.2f}'}), 400
            net_impact = -cost 

        elif trans_type == 'SATIS':
            # Stok Kontrolü
            query_stock = """
                SELECT 
                    SUM(CASE WHEN IslemTipi = 'ALIS' THEN Miktar ELSE 0 END) - 
                    SUM(CASE WHEN IslemTipi = 'SATIS' THEN Miktar ELSE 0 END) as Adet
                FROM IslemlerTablosu 
                WHERE HesapNo = ? AND VarlikID = ?
            """
            cursor.execute(query_stock, (account_id, varlik_id))
            stock_row = cursor.fetchone()
            current_stock = stock_row[0] if stock_row[0] is not None else 0
            
            if current_stock < amount:
                return jsonify({'success': False, 'message': f'Yetersiz Hisse! Elinizde {current_stock} adet var.'}), 400

            net_impact = total_amount - commission 

        # 4. KAYDET VE GÜNCELLE
        query_insert = """
            INSERT INTO IslemlerTablosu 
            (IslemTarihi, IslemTipi, Miktar, BirimFiyat, ToplamTutar, KomisyonMiktar, KarZarar, CalisanID, HesapNo, VarlikID)
            VALUES (GETDATE(), ?, ?, ?, ?, ?, 0, ?, ?, ?)
        """
        cursor.execute(query_insert, (trans_type, amount, unit_price, total_amount, commission, broker_id, account_id, varlik_id))
        
        query_update = "UPDATE HesaplarTablosu SET Bakiye = Bakiye + ? WHERE HesapNo = ?"
        cursor.execute(query_update, (net_impact, account_id))
        
        conn.commit()
        return jsonify({'success': True, 'message': 'İşlem başarıyla gerçekleşti.'})

    except Exception as e:
        conn.rollback()
        print(f"HATA: {e}")
        return jsonify({'success': False, 'message': str(e)}), 500
    finally:
        conn.close()
#********************************************

# PİYASA VERİLERİ ALMA API'Sİ
# ---------------------------------------------
@app.route('/api/market/assets', methods=['GET'])
def get_market_assets():
    # AYARLAR
    CACHE_FILE = 'market_cache.json' # Verilerin saklanacağı dosya
    CACHE_DURATION = 3600  # Kaç saniye geçerli olsun? (3600 sn = 1 Saat)

    # 1. VARSAYILAN LİSTE (Fallback ve İskelet)
    assets_map = {
        'THYAO.IS': {'id': 'THYAO', 'name': 'Türk Hava Yolları', 'type': 'Hisse', 'default_price': 245.50},
        'GARAN.IS': {'id': 'GARAN', 'name': 'Garanti Bankası', 'type': 'Hisse', 'default_price': 38.75},
        'AKBNK.IS': {'id': 'AKBNK', 'name': 'Akbank', 'type': 'Hisse', 'default_price': 52.30},
        'EREGL.IS': {'id': 'EREGL', 'name': 'Ereğli Demir Çelik', 'type': 'Hisse', 'default_price': 48.90},
        'KCHOL.IS': {'id': 'KCHOL', 'name': 'Koç Holding', 'type': 'Hisse', 'default_price': 156.20},
        'SAHOL.IS': {'id': 'SAHOL', 'name': 'Sabancı Holding', 'type': 'Hisse', 'default_price': 78.40},
        'PETKM.IS': {'id': 'PETKM', 'name': 'Petkim', 'type': 'Hisse', 'default_price': 34.60},
        'TUPRS.IS': {'id': 'TUPRS', 'name': 'Tüpraş', 'type': 'Hisse', 'default_price': 189.30},
        'ASELS.IS': {'id': 'ASELS', 'name': 'Aselsan', 'type': 'Hisse', 'default_price': 65.40},
        'BIMAS.IS': {'id': 'BIMAS', 'name': 'BİM Mağazalar', 'type': 'Hisse', 'default_price': 485.00},
        'SASA.IS':  {'id': 'SASA',  'name': 'Sasa Polyester', 'type': 'Hisse', 'default_price': 42.10},
        'TRY=X':    {'id': 'USDTRY', 'name': 'Dolar/TL', 'type': 'Döviz', 'default_price': 34.50}
    }

    # 2. ÖNBELLEK KONTROLÜ
    # Eğer dosya varsa ve süresi dolmamışsa dosyadan oku
    if os.path.exists(CACHE_FILE):
        file_age = time.time() - os.path.getmtime(CACHE_FILE)
        if file_age < CACHE_DURATION:
            print(f"Veriler önbellekten okunuyor... ({int(file_age/60)} dk önce güncellendi)")
            try:
                with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                    cached_data = json.load(f)
                return jsonify({'success': True, 'assets': cached_data})
            except:
                print("Önbellek dosyası bozuk, yeniden çekilecek.")

    # 3. İNTERNETTEN VERİ ÇEKME (Cache yoksa veya süresi dolduysa)
    assets_list = []
    
    try:
        tickers_list = list(assets_map.keys())
        print("Yahoo Finance'den GÜNCEL veri çekiliyor...")
        
        data = yf.download(tickers_list, period="1d", interval="1m", progress=False, auto_adjust=True, threads=False)['Close']
        
        if data.empty:
            raise Exception("Boş veri döndü")

        for ticker, info in assets_map.items():
            price = info['default_price']
            
            try:
                if ticker in data.columns:
                    val = data[ticker].iloc[-1]
                    if val is not None and not math.isnan(float(val)):
                        price = round(float(val), 2)
            except:
                pass

            assets_list.append({
                'id': info['id'],
                'name': info['name'],
                'type': info['type'],
                'currentPrice': price
            })

        # 4. YENİ VERİYİ DOSYAYA KAYDET
        try:
            with open(CACHE_FILE, 'w', encoding='utf-8') as f:
                json.dump(assets_list, f, ensure_ascii=False, indent=4)
            print("Yeni veriler önbelleğe kaydedildi.")
        except Exception as cache_error:
            # Dosya yazılamazsa bile sunucu çökmesin, sadece ekrana hata bassın
            print(f"UYARI: Önbellek dosyası yazılamadı ({cache_error}). Ancak program çalışmaya devam ediyor.")

    except Exception as e:
        print(f"PİYASA VERİ HATASI: {e}")
        # Hata durumunda varsayılanları yükle
        for ticker, info in assets_map.items():
            assets_list.append({
                'id': info['id'],
                'name': info['name'],
                'type': info['type'],
                'currentPrice': info['default_price']
            })

    return jsonify({'success': True, 'assets': assets_list})
#****************************************************************************    

#--------------------------------------------
@app.route('/api/account/toggle-status', methods=['POST'])
def toggle_account_status():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        data = request.json
        account_id = data.get('accountId')
        
        # 1. Mevcut durumu bul
        cursor.execute("SELECT HesapDurumu FROM HesaplarTablosu WHERE HesapNo = ?", (account_id,))
        row = cursor.fetchone()
        
        if not row:
            return jsonify({'success': False, 'message': 'Hesap bulunamadı'}), 404
            
        current_status = row[0]
        
        # 2. Durumu tersine çevir
        new_status = 'Aktif' if current_status == 'Pasif' else 'Pasif'
        
        # 3. Güncelle
        cursor.execute("UPDATE HesaplarTablosu SET HesapDurumu = ? WHERE HesapNo = ?", (new_status, account_id))
        conn.commit()
        
        return jsonify({'success': True, 'newStatus': new_status, 'message': f'Hesap durumu {new_status} olarak güncellendi.'})

    except Exception as e:
        conn.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500
    finally:
        conn.close()

#********************************************
#--------------------------------------------
# app.py içindeki get_investor_dashboard fonksiyonu:

@app.route('/api/investor/dashboard/<int:investor_id>', methods=['GET'])
def get_investor_dashboard(investor_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # 1. YATIRIMCI BİLGİLERİ
        cursor.execute("SELECT YatirimciID, Ad, Soyad, Eposta FROM YatirimcilarTablosu WHERE YatirimciID = ?", (investor_id,))
        inv = cursor.fetchone()
        
        if not inv:
            return jsonify({'success': False, 'message': 'Yatırımcı bulunamadı'}), 404

        investor_data = {
            'id': inv.YatirimciID,
            'name': inv.Ad,
            'surname': inv.Soyad,
            'email': inv.Eposta
        }

        # 2. RİSK PROFİLİ (ID'ye göre dinamik atama)
        risk_types = [
            {'name': 'Agresif', 'maxStock': 80, 'desc': 'Yüksek getiri hedefli, yüksek risk toleransı.'},
            {'name': 'Dengeli', 'maxStock': 60, 'desc': 'Orta düzey risk toleransı ile dengeli portföy yapısı.'},
            {'name': 'Muhafazakar', 'maxStock': 30, 'desc': 'Düşük risk, sermaye koruma öncelikli.'}
        ]
        # ID'ye göre sabit bir profil belirle (Her seferinde değişmemesi için)
        user_risk = risk_types[investor_id % 3]

        # 3. SORUMLU BROKER
        cursor.execute("""
            SELECT TOP 1 C.Ad, C.Soyad, C.Eposta, C.Tel
            FROM HesaplarTablosu H
            JOIN CalisanlarTablosu C ON H.CalisanID = C.CalisanID
            WHERE H.YatirimciID = ?
        """, (investor_id,))
        broker_row = cursor.fetchone()

        broker_data = None
        if broker_row:
            broker_data = {
                'name': f"{broker_row.Ad} {broker_row.Soyad}",
                'email': broker_row.Eposta,
                'phone': broker_row.Tel or 'Belirtilmemiş',
                'initial': broker_row.Ad[0] if broker_row.Ad else 'B'
            }
        else:
            broker_data = {'name': 'Atanmamış', 'email': '-', 'phone': '-', 'initial': '?'}

        # 4. HESAPLAR
        cursor.execute("""
            SELECT HesapNo, Bakiye, HesapDurumu, HesapAcilisTarihi
            FROM HesaplarTablosu 
            WHERE YatirimciID = ?
        """, (investor_id,))
        
        accounts_list = []
        for row in cursor.fetchall():
            accounts_list.append({
                'accountNumber': row.HesapNo,
                'balance': float(row.Bakiye),
                'status': row.HesapDurumu,
                'openDate': str(row.HesapAcilisTarihi)[0:10],
                'commissionPlan': 'Standart Plan',
                'minCommission': 50
            })

        # 5. İŞLEM GEÇMİŞİ (HEPSİ) - DÜZELTİLMİŞ SORGUSU
        # VarlikKodu sütunu olmadığı için onu kaldırdık.
        cursor.execute("""
            SELECT I.IslemTarihi, V.VarlikAdi, I.IslemTipi, I.Miktar, I.BirimFiyat, I.ToplamTutar, I.KomisyonMiktar, I.HesapNo
            FROM IslemlerTablosu I
            JOIN HesaplarTablosu H ON I.HesapNo = H.HesapNo
            JOIN VarliklarTablosu V ON I.VarlikID = V.VarlikID
            WHERE H.YatirimciID = ?
            ORDER BY I.IslemTarihi DESC
        """, (investor_id,))
        
        transactions_list = []
        for t in cursor.fetchall():
            raw_total = float(t.ToplamTutar)
            commission = float(t.KomisyonMiktar) if t.KomisyonMiktar else 0
            
            # Net Tutar: Alışta Maliyet = Tutar + Komisyon, Satışta Gelir = Tutar - Komisyon
            net_total = raw_total + commission if t.IslemTipi == 'ALIS' else raw_total - commission

            transactions_list.append({
                'date': str(t.IslemTarihi)[0:19],
                'asset': t.VarlikAdi,        # VarlikKodu yerine VarlikAdi kullanıyoruz
                'assetName': t.VarlikAdi,
                'accountId': t.HesapNo,
                'type': t.IslemTipi,
                'amount': float(t.Miktar),
                'unitPrice': float(t.BirimFiyat),
                'total': raw_total,
                'commission': commission,
                'netTotal': net_total
            })

        return jsonify({
            'success': True,
            'investor': investor_data,
            'riskProfile': user_risk,
            'broker': broker_data,
            'accounts': accounts_list,
            'transactions': transactions_list
        })

    except Exception as e:
        print(f"Hata: {e}")
        return jsonify({'success': False, 'message': str(e)}), 500
    finally:
        conn.close()
#********************************************
#--------------------------------------------
# --- BROKER LİSTESİ (Dropdown için) ---
@app.route('/api/brokers', methods=['GET'])
def get_brokers():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Tüm çalışanları (Brokerları) çek
        cursor.execute("SELECT CalisanID, Ad, Soyad FROM CalisanlarTablosu")
        brokers = [{'id': row.CalisanID, 'name': f"{row.Ad} {row.Soyad}"} for row in cursor.fetchall()]
        return jsonify({'success': True, 'brokers': brokers})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
    finally:
        conn.close()

# --- YENİ HESAP AÇMA ---
# --- YENİ HESAP AÇMA (DÜZELTİLMİŞ VERSİYON) ---
# --- YENİ HESAP AÇMA (GARANTİ YÖNTEM - OUTPUT KULLANIMI) ---
@app.route('/api/account/create', methods=['POST'])
def create_account():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        data = request.json
        investor_id = data.get('investorId')
        broker_id = data.get('brokerId')
        initial_deposit = data.get('initialDeposit')
        
        from datetime import datetime
        today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # DÜZELTME: 'OUTPUT INSERTED.HesapNo' komutunu ekledik.
        # Bu komut, ekleme yaparken oluşan ID'yi anında bize geri fırlatır.
        # Böylece Python bunu normal bir SELECT sorgusu sanar ve hatasız okur.
        query = """
            INSERT INTO HesaplarTablosu (YatirimciID, CalisanID, Bakiye, HesapAcilisTarihi, HesapDurumu)
            OUTPUT INSERTED.HesapNo
            VALUES (?, ?, ?, ?, 'Aktif')
        """
        
        cursor.execute(query, (investor_id, broker_id, initial_deposit, today))
        
        # Artık veriyi güvenle alabiliriz
        row = cursor.fetchone()
        
        if row:
            new_acc_id = row[0] # Yeni oluşan Hesap No
        else:
            new_acc_id = "Bilinmiyor"
            
        conn.commit()
        
        return jsonify({'success': True, 'accountId': new_acc_id, 'message': 'Hesap başarıyla oluşturuldu.'})

    except Exception as e:
        conn.rollback()
        print(f"Hesap Açma Hatası: {e}")
        return jsonify({'success': False, 'message': str(e)}), 500
    finally:
        conn.close()
#********************************************
#--------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)