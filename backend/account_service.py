from backend.db import get_connection

def create_account(hesap_acilis_tarihi, bakiye, hesap_durumu, varlik_id, komisyon_id, yatirimci_id, calisan_id, risk_profil_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        sql = """
        INSERT INTO HesaplarTablosu 
        (HesapAcilisTarihi, Bakiye, HesapDurumu, VarlikID, KomisyonID, YatirimciID, CalisanID, RiskProfilID)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (hesap_acilis_tarihi, bakiye, hesap_durumu, varlik_id, 
                           komisyon_id, yatirimci_id, calisan_id, risk_profil_id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def delete_account(hesap_no):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        sql = "DELETE FROM HesaplarTablosu WHERE HesapNo = ?"
        cursor.execute(sql, (hesap_no,))
        
        if cursor.rowcount == 0:
            raise Exception(f"{hesap_no} numaralı bir hesap bulunamadı.")
        
        conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        conn.close()

def update_account(hesap_no, hesap_acilis_tarihi, bakiye, hesap_durumu, varlik_id, komisyon_id, yatirimci_id, calisan_id, risk_profil_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        sql_check = "SELECT COUNT(*) FROM HesaplarTablosu WHERE HesapNo = ?"
        cursor.execute(sql_check, (hesap_no,))
        if cursor.fetchone()[0] == 0:
            raise Exception(f"{hesap_no} numaralı hesap bulunamadı.")
        
        sql = """
        UPDATE HesaplarTablosu
        SET HesapAcilisTarihi = ?, Bakiye = ?, HesapDurumu = ?, VarlikID = ?, 
            KomisyonID = ?, YatirimciID = ?, CalisanID = ?, RiskProfilID = ?
        WHERE HesapNo = ?
        """
        cursor.execute(sql, (hesap_acilis_tarihi, bakiye, hesap_durumu, varlik_id,
                           komisyon_id, yatirimci_id, calisan_id, risk_profil_id, hesap_no))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def fetch_all_accounts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM HesaplarTablosu")
    hesaplar = cursor.fetchall()
    conn.close()
    return hesaplar

def fetch_account_by_number(hesap_no):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM HesaplarTablosu WHERE HesapNo = ?", (hesap_no,))
    hesap = cursor.fetchone()
    conn.close()
    return hesap

def fetch_accounts_by_investor(yatirimci_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM HesaplarTablosu WHERE YatirimciID = ?", (yatirimci_id,))
    hesaplar = cursor.fetchall()
    conn.close()
    return hesaplar

def fetch_accounts_by_employee(calisan_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM HesaplarTablosu WHERE CalisanID = ?", (calisan_id,))
    hesaplar = cursor.fetchall()
    conn.close()
    return hesaplar

def fetch_accounts_by_asset(varlik_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM HesaplarTablosu WHERE VarlikID = ?", (varlik_id,))
    hesaplar = cursor.fetchall()
    conn.close()
    return hesaplar

def fetch_accounts_by_risk_profile(risk_profil_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM HesaplarTablosu WHERE RiskProfilID = ?", (risk_profil_id,))
    hesaplar = cursor.fetchall()
    conn.close()
    return hesaplar


if __name__ == "__main__":
    print("Hesaplar listesi:")
    for h in fetch_all_accounts():
        print("Hesap:", h)
    
    print("\nHesap ekleme testi (Örnek: Yatırımcı 1, Broker 1 ile Altın hesabı açıyor):")
    print("---------------")
    try:
        create_account("2024-01-01", 10000.0, 1, 2, 2, 3, 2, 1)
        print("Hesap eklendi.")
    except Exception as e:
        print("Hesap eklenirken hata:", e)
    
    print("\nHesap silme testi:")
    print("---------------")
    try:
        #delete_account(1)
        print("Hesap silindi.")
    except Exception as e:
        print("Hesap silinirken hata:", e)
    
    print("\nHesap güncelleme testi:")
    print("---------------")
    try:
        #update_account(2, "2024-01-15", 15000.0, 1, 2, 2, 3, 2, 1)
        print("Hesap güncellendi.")
    except Exception as e:
        print("Hesap güncellenirken hata:", e)

    print("\nYatırımcıya göre hesapları güncelleme testi:")
    print("---------------")
    try:
        hesaplar = fetch_accounts_by_investor(3)
        for h in hesaplar:
            print("Yatırımcının hesabı:", h)
    except Exception as e:
        print("Hesaplar getirilirken hata:", e)