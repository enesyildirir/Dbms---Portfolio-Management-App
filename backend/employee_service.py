from backend.db import get_connection

def create_employee(ad, soyad, tel, tc_no, eposta, ise_giris_tarihi, sifre_hash, durum, pozisyon_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        sql_check = "SELECT COUNT(*) FROM CalisanlarTablosu WHERE TC_no = ?"
        cursor.execute(sql_check, (tc_no,))
        if cursor.fetchone()[0] > 0:
            raise Exception("Bu TC kimlik numarası ile kayıtlı bir çalışan zaten var.")
        
        sql = """
        INSERT INTO CalisanlarTablosu 
        (Ad, Soyad, Tel, TC_no, Eposta, IseGirisTarihi, SifreHash, Durum, PozisyonID)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (ad, soyad, tel, tc_no, eposta, ise_giris_tarihi, sifre_hash, durum, pozisyon_id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def delete_employee(calisan_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        sql = "DELETE FROM CalisanlarTablosu WHERE CalisanID = ?"
        cursor.execute(sql, (calisan_id,))
        
        if cursor.rowcount == 0:
            raise Exception(f"{calisan_id} ID'li bir çalışan bulunamadı.")
        
        conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        conn.close()

def update_employee(calisan_id, ad, soyad, tel, tc_no, eposta, ise_giris_tarihi, sifre_hash, durum, pozisyon_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        sql_check = "SELECT COUNT(*) FROM CalisanlarTablosu WHERE CalisanID = ?"
        cursor.execute(sql_check, (calisan_id,))
        if cursor.fetchone()[0] == 0:
            raise Exception(f"{calisan_id} ID'li çalışan bulunamadı.")
        
        sql = """
        UPDATE CalisanlarTablosu
        SET Ad = ?, Soyad = ?, Tel = ?, TC_no = ?, Eposta = ?, 
            IseGirisTarihi = ?, SifreHash = ?, Durum = ?, PozisyonID = ?
        WHERE CalisanID = ?
        """
        cursor.execute(sql, (ad, soyad, tel, tc_no, eposta, ise_giris_tarihi, 
                           sifre_hash, durum, pozisyon_id, calisan_id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def fetch_all_employees():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CalisanlarTablosu")
    calisanlar = cursor.fetchall()
    conn.close()
    return calisanlar

def fetch_employee_by_id(calisan_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CalisanlarTablosu WHERE CalisanID = ?", (calisan_id,))
    calisan = cursor.fetchone()
    conn.close()
    return calisan

def fetch_employee_by_tc(tc_no):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CalisanlarTablosu WHERE TC_no = ?", (tc_no,))
    calisan = cursor.fetchone()
    conn.close()
    return calisan

def fetch_employee_by_email(eposta):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CalisanlarTablosu WHERE Eposta = ?", (eposta,))
    calisan = cursor.fetchone()
    conn.close()
    return calisan


if __name__ == "__main__":
    print("Çalışanlar listesi:")
    for c in fetch_all_employees():
        print("Çalışan:", c)
    
    print("\nÇalışan ekleme testi:")
    print("---------------")
    try:
        create_employee("Ahmet", "Yılmaz", "5551234567", "12345678901", "ahmet@example.com", 
                       "2024-01-01", "hashed_password", 1, 1)
        print("Çalışan eklendi.")
    except Exception as e:
        print("Çalışan eklenirken hata:", e)
    
    print("\nÇalışan silme testi:")
    print("---------------")
    try:
        delete_employee(1)
        print("Çalışan silindi.")
    except Exception as e:
        print("Çalışan silinirken hata:", e)
    
    print("\nÇalışan güncelleme testi:")
    print("---------------")
    try:
        update_employee(2, "Mehmet", "Demir", "5559876543", "98765432109", "mehmet@example.com",
                       "2024-01-15", "new_hashed_password", 1, 1)
        print("Çalışan güncellendi.")
    except Exception as e:
        print("Çalışan güncellenirken hata:", e)