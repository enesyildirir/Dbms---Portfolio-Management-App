from backend.db import get_connection

def create_position(departman, pozisyon):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Pozisyonun zaten var olup olmadığını kontrol et
        sql_check = "SELECT COUNT(*) FROM PozisyonlarTablosu WHERE departman = ? AND pozisyon = ?"
        cursor.execute(sql_check, (departman, pozisyon))
        count = cursor.fetchone()[0]
        if count > 0:
            raise Exception("Bu pozisyon zaten var.")
    except Exception as e:
        conn.close()
        raise e

    sql = """
    Insert into PozisyonlarTablosu (departman, pozisyon)
    values (?, ?)
    """
    
    cursor.execute(sql, (departman, pozisyon)) # frontendten gelen verilerle
    conn.commit()
    conn.close()

def delete_position(pozisyon_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        sql = "DELETE FROM PozisyonlarTablosu WHERE PozisyonID = ?"
        cursor.execute(sql, (pozisyon_id,))

        # Hiç satır silinmediyse, o id'ye ait pozisyon yok demektir
        if cursor.rowcount == 0:
            raise Exception(f"{pozisyon_id} ID'li bir pozisyon bulunamadı.")

        conn.commit()

    except:
        conn.rollback()
        raise
    finally:
        conn.close()


def update_position(pozisyon_id, departman, pozisyon):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Pozisyonun zaten var olup olmadığını kontrol et
        sql_check = "SELECT * FROM PozisyonlarTablosu WHERE PozisyonID = ?"
        cursor.execute(sql_check, (pozisyon_id,))
        if cursor.rowcount == 0:
            raise Exception(f"{pozisyon_id} Bu pozisyon yok.")
    except Exception as e:
        conn.close()
        raise e
    sql = """
    UPDATE PozisyonlarTablosu
    SET departman = ?, pozisyon = ?
    WHERE PozisyonID = ?
    """
    cursor.execute(sql, (departman, pozisyon, pozisyon_id))
    conn.commit()
    conn.close()


def fetch_positions():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PozisyonlarTablosu")
    positions = cursor.fetchall()
    conn.close()
    return positions



## Servisi doğrudan çalıştırmak için
## python -m backend.pozisyon_service    Bu komutu kullanabilirsiniz

if __name__ == "__main__":
    # küçük bir test
    for p in fetch_positions():
        print("Pozisyon:", p)

    print("\nPozisyon ekleme testi:")
    print("---------------")    
    try:
        create_position("IT", "Yazılım Geliştirici")
        print("Pozisyon eklendi.")
    except Exception as e:
        print("Pozisyon eklenirken hata oluştu:", e)
    
    print("\nPozisyon silme testi:")
    print("---------------")
    try:
        pozisyon_id = 3 
        delete_position(pozisyon_id)
        
        print("Pozisyon silindi.")
    
    except Exception as e:
        print("Pozisyon silinirken hata oluştu:", e)


    for p in fetch_positions():
        print("Pozisyon:", p)

    print("\nPozisyon güncelleme testi:")
    print("---------------")
    try:
        pozisyon_id = 3 
        update_position(pozisyon_id, "IT", "Teknik Destek Uzmanı")
        print("Pozisyon güncellendi.")
    except Exception as e:
        print("Pozisyon güncellenirken hata oluştu:", e)
    for p in fetch_positions():
        print("Pozisyon:", p)