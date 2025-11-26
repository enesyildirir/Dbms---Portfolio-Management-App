- MsSql de veritabanı oluşturuyoruz.
- Aşağıdaki sorgularla tabloları oluşturuyoruz. 
- db.py içerisine oluşturduğumuz "Database = vtys_ornek;" şeklinde giriyoruz.
- servisleri doğrudan denemek için __init__.py oluşturup servis içine uygun kodu yazıyoruz.


### Tablolar ###

CREATE TABLE PozisyonlarTablosu (
    PozisyonID INT IDENTITY(1,1) PRIMARY KEY,
    Pozisyon NVARCHAR(50) NOT NULL,
    Departman NVARCHAR(50) NOT NULL
);

CREATE TABLE CalisanlarTablosu (
    CalisanID INT IDENTITY(1,1) PRIMARY KEY,
    Ad NVARCHAR(50) NOT NULL,
    Soyad NVARCHAR(50) NOT NULL,
    PozisyonID INT NOT NULL,
    IseGirisTarihi DATE NOT NULL,
    KullaniciAdi NVARCHAR(50) NOT NULL,
    SifreHash NVARCHAR(256) NOT NULL,
    Durum NVARCHAR(20) NOT NULL,
    Tel NVARCHAR(15) NULL,

    FOREIGN KEY (PozisyonID)
        REFERENCES PozisyonlarTablosu(PozisyonID)
);

CREATE TABLE RiskProfilTablosu (
    RiskProfilID INT IDENTITY(1,1) PRIMARY KEY,
    ProfilAdi NVARCHAR(50),
    Aciklama NVARCHAR(255),
    TavsiyeEdilenVarlikDagilimi NVARCHAR(255),
    MaksHisseOrani DECIMAL(5,2)
);

CREATE TABLE YatirimcilarTablosu (
    YatirimciID INT IDENTITY(1,1) PRIMARY KEY,
    Ad NVARCHAR(50) NOT NULL,
    Soyad NVARCHAR(50) NOT NULL,
    TC_no NVARCHAR(11) NOT NULL UNIQUE,
    Eposta NVARCHAR(100),
    Tel NVARCHAR(20),
    CalisanID INT NOT NULL,
    RiskProfilID INT NOT NULL,

    FOREIGN KEY (CalisanID) REFERENCES CalisanlarTablosu(CalisanID),
    FOREIGN KEY (RiskProfilID) REFERENCES RiskProfilTablosu(RiskProfilID)
);

CREATE TABLE KomisyonTablosu (
    KomisyonID INT IDENTITY(1,1) PRIMARY KEY,
    KomisyonTipi NVARCHAR(50) NOT NULL,
    TemelOran DECIMAL(10,2) NOT NULL,
    MinimumKomisyon DECIMAL(18,2) NOT NULL,
    GecerlilikTarihi DATE NOT NULL
);

CREATE TABLE HesaplarTablosu (
    HesapNo INT IDENTITY(1000,1) PRIMARY KEY,
    YatirimciID INT NOT NULL,
    HesapTuru NVARCHAR(50),
    HesapAcilisTarihi DATE NOT NULL,
    Bakiye DECIMAL(18,2) NOT NULL DEFAULT 0,
    ParaBirimi NVARCHAR(10),
    HesapDurumu NVARCHAR(20),
    YetkilendirmeTuru NVARCHAR(50),
    KomisyonID INT,

    FOREIGN KEY (YatirimciID) REFERENCES YatirimcilarTablosu(YatirimciID),
    FOREIGN KEY (KomisyonID) REFERENCES KomisyonTablosu(KomisyonID)
);

CREATE TABLE VarliklarTablosu (
    VarlikSembol NVARCHAR(10) PRIMARY KEY,
    VarlikAdi NVARCHAR(50) NOT NULL,
    VarlikTuru NVARCHAR(50),
    Sektor NVARCHAR(50),
    Piyasa NVARCHAR(50),
    MaksimumFiyat DECIMAL(18,2)
);

CREATE TABLE IslemlerTablosu (
    IslemID INT IDENTITY(1,1) PRIMARY KEY,
    HesapNo INT NOT NULL,
    VarlikSembol NVARCHAR(10) NOT NULL,
    IslemTipi NVARCHAR(20),
    IslemTarihi DATETIME NOT NULL,
    Miktar INT NOT NULL,
    BirimFiyat DECIMAL(18,2) NOT NULL,
    CalisanID INT NOT NULL,
    Komisyon DECIMAL(18,2),
    ToplamTutar DECIMAL(18,2),
    KarZarar DECIMAL(18,2),
    IslemGerceklestiren NVARCHAR(50),

    FOREIGN KEY (HesapNo) REFERENCES HesaplarTablosu(HesapNo),
    FOREIGN KEY (VarlikSembol) REFERENCES VarliklarTablosu(VarlikSembol),
    FOREIGN KEY (CalisanID) REFERENCES CalisanlarTablosu(CalisanID)
);
