from backend.db import get_connection

def create_transaction(islem_tipi, islem_tarihi, miktar, birim_fiyat, komisyon_miktar, toplam_tutar, ka_zarar, calisan_id, hesap_no, varlik_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        sql = """
        INSERT INTO IslemlerTablosu 
        (IslemTipi, IslemTarihi, Miktar, BirimFiyat, KomisyonMiktar, ToplamTutar, KarZarar, CalisanID, HesapNo, VarlikID)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (islem_tipi, islem_tarihi, miktar, birim_fiyat, komisyon_miktar, 
                           toplam_tutar, ka_zarar, calisan_id, hesap_no, varlik_id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def delete_transaction(islem_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        sql = "DELETE FROM IslemlerTablosu WHERE IslemID = ?"
        cursor.execute(sql, (islem_id,))
        
        if cursor.rowcount == 0:
            raise Exception(f"{islem_id} ID'li bir işlem bulunamadı.")
        
        conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        conn.close()

def update_transaction(islem_id, islem_tipi, islem_tarihi, miktar, birim_fiyat, komisyon_miktar, toplam_tutar, ka_zarar, calisan_id, hesap_no, varlik_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        sql_check = "SELECT COUNT(*) FROM IslemlerTablosu WHERE IslemID = ?"
        cursor.execute(sql_check, (islem_id,))
        if cursor.fetchone()[0] == 0:
            raise Exception(f"{islem_id} ID'li işlem bulunamadı.")
        
        sql = """
        UPDATE IslemlerTablosu
        SET IslemTipi = ?, IslemTarihi = ?, Miktar = ?, BirimFiyat = ?, 
            KomisyonMiktar = ?, ToplamTutar = ?, KarZarar = ?, CalisanID = ?, 
            HesapNo = ?, VarlikID = ?
        WHERE IslemID = ?
        """
        cursor.execute(sql, (islem_tipi, islem_tarihi, miktar, birim_fiyat, komisyon_miktar,
                           toplam_tutar, ka_zarar, calisan_id, hesap_no, varlik_id, islem_id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def fetch_all_transactions():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM IslemlerTablosu")
    islemler = cursor.fetchall()
    conn.close()
    return islemler

def fetch_transaction_by_id(islem_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM IslemlerTablosu WHERE IslemID = ?", (islem_id,))
    islem = cursor.fetchone()
    conn.close()
    return islem

def fetch_transactions_by_account(hesap_no):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM IslemlerTablosu WHERE HesapNo = ?", (hesap_no,))
    islemler = cursor.fetchall()
    conn.close()
    return islemler

def fetch_transactions_by_employee(calisan_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM IslemlerTablosu WHERE CalisanID = ?", (calisan_id,))
    islemler = cursor.fetchall()
    conn.close()
    return islemler

def fetch_transactions_by_asset(varlik_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM IslemlerTablosu WHERE VarlikID = ?", (varlik_id,))
    islemler = cursor.fetchall()
    conn.close()
    return islemler

def fetch_transactions_by_type(islem_tipi):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM IslemlerTablosu WHERE IslemTipi = ?", (islem_tipi,))
    islemler = cursor.fetchall()
    conn.close()
    return islemler

def fetch_transactions_by_date_range(baslangic_tarihi, bitis_tarihi):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM IslemlerTablosu WHERE IslemTarihi BETWEEN ? AND ?", 
                  (baslangic_tarihi, bitis_tarihi))
    islemler = cursor.fetchall()
    conn.close()
    return islemler


if __name__ == "__main__":
    print("İşlemler listesi:")
    for i in fetch_all_transactions():
        print("İşlem:", i)
    
    print("\nİşlem ekleme testi (Örnek: 100 gram altın alış işlemi):")
    print("---------------")
    try:
        create_transaction("Alış", "2024-01-15", 100, 2500.50, 50.0, 250100.0, 0, 2, 1000, 3)
        print("İşlem eklendi.")
    except Exception as e:
        print("İşlem eklenirken hata:", e)
    
    print("\nİşlem silme testi:")
    print("---------------")
    try:
        #delete_transaction(1)
        print("İşlem silindi.")
    except Exception as e:
        print("İşlem silinirken hata:", e)
    
    print("\nİşlem güncelleme testi:")
    print("---------------")
    try:
        #update_transaction(2, "Satış", "2024-01-16", 50, 2550.0, 50.0, 127550.0, 2500, 1, 1, 1)
        print("İşlem güncellendi.")
    except Exception as e:
        print("İşlem güncellenirken hata:", e)
    
    print("\nHesaba göre işlemleri getirme testi:")
    print("---------------")
    try:
        islemler = fetch_transactions_by_account(1)
        for i in islemler:
            print("Hesabın işlemi:", i)
    except Exception as e:
        print("İşlemler getirilirken hata:", e)
    
    print("\nİşlem tipine göre getirme testi (Alış işlemleri):")
    print("---------------")
    try:
        islemler = fetch_transactions_by_type("Alış")
        for i in islemler:
            print("Alış işlemi:", i)
    except Exception as e:
        print("İşlemler getirilirken hata:", e)