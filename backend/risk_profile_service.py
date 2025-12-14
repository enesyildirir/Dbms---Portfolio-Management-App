from backend.db import get_connection

def create_risk_profile(profil_adi, aciklama, maksimum_orani):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        sql_check = "SELECT COUNT(*) FROM RiskProfilTablosu WHERE ProfilAdi = ?"
        cursor.execute(sql_check, (profil_adi,))
        if cursor.fetchone()[0] > 0:
            raise Exception("Bu profil adı ile bir risk profili zaten var.")
        
        sql = """
        INSERT INTO RiskProfilTablosu (ProfilAdi, Aciklama, MaksIslemOrani)
        VALUES (?, ?, ?)
        """
        cursor.execute(sql, (profil_adi, aciklama, maksimum_orani))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def delete_risk_profile(risk_profil_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        sql = "DELETE FROM RiskProfilTablosu WHERE RiskProfilID = ?"
        cursor.execute(sql, (risk_profil_id,))
        
        if cursor.rowcount == 0:
            raise Exception(f"{risk_profil_id} ID'li bir risk profili bulunamadı.")
        
        conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        conn.close()

def update_risk_profile(risk_profil_id, profil_adi, aciklama, maksimum_orani):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        sql_check = "SELECT COUNT(*) FROM RiskProfilTablosu WHERE RiskProfilID = ?"
        cursor.execute(sql_check, (risk_profil_id,))
        if cursor.fetchone()[0] == 0:
            raise Exception(f"{risk_profil_id} ID'li risk profili bulunamadı.")
        
        sql = """
        UPDATE RiskProfilTablosu
        SET ProfilAdi = ?, Aciklama = ?, MaksIslemOrani = ?
        WHERE RiskProfilID = ?
        """
        cursor.execute(sql, (profil_adi, aciklama, maksimum_orani, risk_profil_id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def fetch_all_risk_profiles():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM RiskProfilTablosu")
    profiller = cursor.fetchall()
    conn.close()
    return profiller

def fetch_risk_profile_by_id(risk_profil_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM RiskProfilTablosu WHERE RiskProfilID = ?", (risk_profil_id,))
    profil = cursor.fetchone()
    conn.close()
    return profil

if __name__ == "__main__":
    print("Risk Profilleri listesi:")
    for rp in fetch_all_risk_profiles():
        print("Risk Profili:", rp)
    
    print("\nRisk Profili ekleme testi:")
    print("---------------")
    try:
        create_risk_profile("Muhafazakar", "Düşük riskli yatırımlar", 20.0)
        print("Risk Profili eklendi.")
    except Exception as e:
        print("Risk Profili eklenirken hata:", e)