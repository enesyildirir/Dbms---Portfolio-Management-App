from backend.db import get_connection

def create_investor(ad, soyad, tel, tc_no, eposta, sifre_hash, bakiye):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        sql_check = "SELECT COUNT(*) FROM YatirimcilarTablosu WHERE TC_no = ?"
        cursor.execute(sql_check, (tc_no,))
        if cursor.fetchone()[0] > 0:
            raise Exception("Bu TC kimlik numarası ile kayıtlı bir yatırımcı zaten var.")
        
        sql = """
        INSERT INTO YatirimcilarTablosu (Ad, Soyad, Tel, TC_no, Eposta, SifreHash, Bakiye)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (ad, soyad, tel, tc_no, eposta, sifre_hash, bakiye))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def delete_investor(yatirimci_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        sql = "DELETE FROM YatirimcilarTablosu WHERE YatirimciID = ?"
        cursor.execute(sql, (yatirimci_id,))
        
        if cursor.rowcount == 0:
            raise Exception(f"{yatirimci_id} ID'li bir yatırımcı bulunamadı.")
        
        conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        conn.close()

def update_investor(yatirimci_id, ad, soyad, tel, tc_no, eposta, sifre_hash, bakiye):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        sql_check = "SELECT COUNT(*) FROM YatirimcilarTablosu WHERE YatirimciID = ?"
        cursor.execute(sql_check, (yatirimci_id,))
        if cursor.fetchone()[0] == 0:
            raise Exception(f"{yatirimci_id} ID'li yatırımcı bulunamadı.")
        
        sql = """
        UPDATE YatirimcilarTablosu
        SET Ad = ?, Soyad = ?, Tel = ?, TC_no = ?, Eposta = ?, SifreHash = ?, Bakiye = ?
        WHERE YatirimciID = ?
        """
        cursor.execute(sql, (ad, soyad, tel, tc_no, eposta, sifre_hash, bakiye, yatirimci_id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def fetch_all_investors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM YatirimcilarTablosu")
    yatirimcilar = cursor.fetchall()
    conn.close()
    return yatirimcilar

def fetch_investor_by_id(yatirimci_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM YatirimcilarTablosu WHERE YatirimciID = ?", (yatirimci_id,))
    yatirimci = cursor.fetchone()
    conn.close()
    return yatirimci

def fetch_investor_by_tc(tc_no):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM YatirimcilarTablosu WHERE TC_no = ?", (tc_no,))
    yatirimci = cursor.fetchone()
    conn.close()
    return yatirimci

def fetch_investor_by_email(eposta):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM YatirimcilarTablosu WHERE Eposta = ?", (eposta,))
    yatirimci = cursor.fetchone()
    conn.close()
    return yatirimci


if __name__ == "__main__":
    print("Yatırımcılar listesi:")
    for y in fetch_all_investors():
        print("Yatırımcı:", y)
    
    print("\nYatırımcı ekleme testi:")
    print("---------------")
    try:
        create_investor("Ali", "Kaya", "5551112233", "11122233344", "ali@example.com", 
                       "hashed_password", 50000.0)
        create_investor("Ayşe", "Yıldız", "5559998877", "99988877766", "ayse@example.com",
                       "hashed_password", 75000.0)
        print("Yatırımcı eklendi.")
        for y in fetch_all_investors():
            print("Yatırımcı:", y)
    except Exception as e:
        print("Yatırımcı eklenirken hata:", e)
    
    print("\nYatırımcı silme testi:")
    print("---------------")
    try:
        delete_investor(2)
        print("Yatırımcı silindi.")
    except Exception as e:
        print("Yatırımcı silinirken hata:", e)
    
    print("\nYatırımcı güncelleme testi:")
    print("---------------")
    try:
        #update_investor(2, "Ayşe", "Yaldız", "4559998877", "89988877766", "ayse@example.com",
         #              "new_hashed_password", 75000.0)
        print("Yatırımcı güncellendi.")
    except Exception as e:
        print("Yatırımcı güncellenirken hata:", e)