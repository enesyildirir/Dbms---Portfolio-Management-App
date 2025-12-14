from backend.db import get_connection

def create_asset(varlik_id, varlik_adi, varlik_turu, piyasa):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        sql_check = "SELECT COUNT(*) FROM VarliklarTablosu WHERE VarlikAdi = ?"
        cursor.execute(sql_check, (varlik_adi,))
        if cursor.fetchone()[0] > 0:
            raise Exception("Bu varlık zaten var.")
        
        sql = """
        INSERT INTO VarliklarTablosu (VarlikID,VarlikAdi, VarlikTuru, Piyasa)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(sql, (varlik_id, varlik_adi, varlik_turu, piyasa))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def delete_asset(varlik_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        sql = "DELETE FROM VarliklarTablosu WHERE VarlikID = ?"
        cursor.execute(sql, (varlik_id,))
        
        if cursor.rowcount == 0:
            raise Exception(f"{varlik_id} ID'li bir varlık bulunamadı.")
        
        conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        conn.close()

def update_asset(varlik_id, varlik_adi, varlik_turu, piyasa):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        sql_check = "SELECT COUNT(*) FROM VarliklarTablosu WHERE VarlikID = ?"
        cursor.execute(sql_check, (varlik_id,))
        if cursor.fetchone()[0] == 0:
            raise Exception(f"{varlik_id} ID'li varlık bulunamadı.")
        
        sql = """
        UPDATE VarliklarTablosu
        SET VarlikAdi = ?, VarlikTuru = ?, Piyasa = ?
        WHERE VarlikID = ?
        """
        cursor.execute(sql, (varlik_adi, varlik_turu, piyasa, varlik_id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def fetch_all_assets():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM VarliklarTablosu")
    varliklar = cursor.fetchall()
    conn.close()
    return varliklar

def fetch_asset_by_id(varlik_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM VarliklarTablosu WHERE VarlikID = ?", (varlik_id,))
    varlik = cursor.fetchone()
    conn.close()
    return varlik


if __name__ == "__main__":
    print("Varlıklar listesi:")
    for v in fetch_all_assets():
        print("Varlık:", v)
    
    print("\nVarlık ekleme testi:")
    print("---------------")
    try:
        create_asset("3", "GLD", "Altın", "NYSE")
        print("Varlık eklendi.")
    except Exception as e:
        print("Varlık eklenirken hata:", e)
    
    print("\nVarlık silme testi:")
    print("---------------")
    try:
        #delete_asset(1)
        print("Varlık silindi.")
    except Exception as e:
        print("Varlık silinirken hata:", e)
    
    print("\nVarlık güncelleme testi:")
    print("---------------")
    try:
        #update_asset(2, "Ethereum", "Kripto", "Binance")
        print("Varlık güncellendi.")
    except Exception as e:
        print("Varlık güncellenirken hata:", e)