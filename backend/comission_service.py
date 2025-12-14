from backend.db import get_connection

def create_commission(minimum_komisyon, varlik_id, calisan_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        sql_check = "SELECT COUNT(*) FROM KomisyonlarTablosu WHERE VarlikID = ? AND CalisanID = ?"
        cursor.execute(sql_check, (varlik_id, calisan_id))
        if cursor.fetchone()[0] > 0:
            raise Exception("Bu varlık ve çalışan için bir komisyon kaydı zaten var.")
        
        sql = """
        INSERT INTO KomisyonlarTablosu (MinimumKomisyon, VarlikID, CalisanID)
        VALUES (?, ?, ?)
        """
        cursor.execute(sql, (minimum_komisyon, varlik_id, calisan_id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def delete_commission(komisyon_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        sql = "DELETE FROM KomisyonlarTablosu WHERE KomisyonID = ?"
        cursor.execute(sql, (komisyon_id,))
        
        if cursor.rowcount == 0:
            raise Exception(f"{komisyon_id} ID'li bir komisyon kaydı bulunamadı.")
        
        conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        conn.close()

def update_commission(komisyon_id, minimum_komisyon, varlik_id, calisan_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        sql_check = "SELECT COUNT(*) FROM KomisyonlarTablosu WHERE KomisyonID = ?"
        cursor.execute(sql_check, (komisyon_id,))
        if cursor.fetchone()[0] == 0:
            raise Exception(f"{komisyon_id} ID'li komisyon kaydı bulunamadı.")
        
        sql = """
        UPDATE KomisyonlarTablosu
        SET MinimumKomisyon = ?, VarlikID = ?, CalisanID = ?
        WHERE KomisyonID = ?
        """
        cursor.execute(sql, (minimum_komisyon, varlik_id, calisan_id, komisyon_id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def fetch_all_commissions():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM KomisyonlarTablosu")
    komisyonlar = cursor.fetchall()
    conn.close()
    return komisyonlar

def fetch_commission_by_id(komisyon_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM KomisyonlarTablosu WHERE KomisyonID = ?", (komisyon_id,))
    komisyon = cursor.fetchone()
    conn.close()
    return komisyon

def fetch_commissions_by_employee(calisan_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM KomisyonlarTablosu WHERE CalisanID = ?", (calisan_id,))
    komisyonlar = cursor.fetchall()
    conn.close()
    return komisyonlar

def fetch_commissions_by_asset(varlik_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM KomisyonlarTablosu WHERE VarlikID = ?", (varlik_id,))
    komisyonlar = cursor.fetchall()
    conn.close()
    return komisyonlar


if __name__ == "__main__":
    print("Komisyonlar listesi:")
    for k in fetch_all_commissions():
        print("Komisyon:", k)
    
    print("\nKomisyon ekleme testi:")
    print("---------------")
    try:
        create_commission(10.50, 2, 2)
        print("Komisyon eklendi.")
    except Exception as e:
        print("Komisyon eklenirken hata:", e)
    
    print("\nKomisyon silme testi:")
    print("---------------")
    try:
        #delete_commission(1)
        print("Komisyon silindi.")
    except Exception as e:
        print("Komisyon silinirken hata:", e)
    
    print("\nKomisyon güncelleme testi:")
    print("---------------")
    try:
        update_commission(2, 15.75, 2, 2)
        print("Komisyon güncellendi.")
    except Exception as e:
        print("Komisyon güncellenirken hata:", e)