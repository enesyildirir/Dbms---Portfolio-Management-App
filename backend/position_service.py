from backend.db import get_connection

def create_position(departmant, position):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    Insert into PozisyonlarTablosu (departman, pozisyon)
    values (?, ?)
    """
    
    cursor.execute(sql, (departmant, position)) # frontendten gelen verilerle
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
if __name__ == "__main__":
    # küçük bir test
    create_position("IT", "Stajyer")
    print("Pozisyon eklendi.")

    for p in fetch_positions():
        print("Pozisyon:", p)
# servisi çalıştırmak için python -m backend.position_service
"""
Pozisyon eklendi.
Pozisyon: (1, 'Stajyer', 'IT')
Pozisyon: (2, 'Stajyer', 'IT')
çiktisi verir.
"""