import { User, Mail, Phone, MapPin, Calendar, Shield, Bell, CreditCard } from 'lucide-react';

export function ProfileTab() {
  const profile = {
    name: 'Ayşe Yılmaz',
    email: 'ayse.yilmaz@email.com',
    phone: '+90 532 123 45 67',
    address: 'İstanbul, Türkiye',
    joinDate: '15 Mart 2022',
    accountType: 'Premium Yatırımcı',
    investorId: 'INV-2022-00847',
  };

  return (
    <div className="space-y-6">
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Main Profile Card */}
        <div className="lg:col-span-2 bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <div className="flex items-start gap-6 mb-6">
            <div className="w-24 h-24 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-xl flex items-center justify-center text-white flex-shrink-0">
              <span className="text-4xl">{profile.name.charAt(0)}</span>
            </div>
            <div className="flex-1">
              <h2 className="text-gray-900 mb-2">{profile.name}</h2>
              <p className="text-gray-600 mb-1">{profile.accountType}</p>
              <p className="text-sm text-gray-500">Müşteri No: {profile.investorId}</p>
            </div>
          </div>

          <div className="space-y-4">
            <div className="flex items-start gap-4 p-4 bg-gray-50 rounded-lg">
              <Mail className="w-5 h-5 text-gray-600 mt-0.5" />
              <div>
                <p className="text-sm text-gray-600 mb-1">E-posta</p>
                <p className="text-gray-900">{profile.email}</p>
              </div>
            </div>

            <div className="flex items-start gap-4 p-4 bg-gray-50 rounded-lg">
              <Phone className="w-5 h-5 text-gray-600 mt-0.5" />
              <div>
                <p className="text-sm text-gray-600 mb-1">Telefon</p>
                <p className="text-gray-900">{profile.phone}</p>
              </div>
            </div>

            <div className="flex items-start gap-4 p-4 bg-gray-50 rounded-lg">
              <MapPin className="w-5 h-5 text-gray-600 mt-0.5" />
              <div>
                <p className="text-sm text-gray-600 mb-1">Adres</p>
                <p className="text-gray-900">{profile.address}</p>
              </div>
            </div>

            <div className="flex items-start gap-4 p-4 bg-gray-50 rounded-lg">
              <Calendar className="w-5 h-5 text-gray-600 mt-0.5" />
              <div>
                <p className="text-sm text-gray-600 mb-1">Üyelik Tarihi</p>
                <p className="text-gray-900">{profile.joinDate}</p>
              </div>
            </div>
          </div>

          <button className="w-full mt-6 bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition-colors">
            Profili Düzenle
          </button>
        </div>

        {/* Settings Cards */}
        <div className="space-y-6">
          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center">
                <Shield className="w-5 h-5 text-blue-600" />
              </div>
              <h3 className="text-gray-900">Güvenlik</h3>
            </div>
            <div className="space-y-3">
              <button className="w-full text-left px-4 py-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors">
                <p className="text-gray-900">Şifre Değiştir</p>
              </button>
              <button className="w-full text-left px-4 py-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors">
                <p className="text-gray-900">İki Faktörlü Doğrulama</p>
              </button>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 bg-indigo-100 rounded-lg flex items-center justify-center">
                <Bell className="w-5 h-5 text-indigo-600" />
              </div>
              <h3 className="text-gray-900">Bildirimler</h3>
            </div>
            <div className="space-y-3">
              <label className="flex items-center justify-between cursor-pointer">
                <span className="text-gray-700">E-posta Bildirimleri</span>
                <input type="checkbox" defaultChecked className="w-5 h-5 text-blue-600 rounded" />
              </label>
              <label className="flex items-center justify-between cursor-pointer">
                <span className="text-gray-700">SMS Bildirimleri</span>
                <input type="checkbox" defaultChecked className="w-5 h-5 text-blue-600 rounded" />
              </label>
              <label className="flex items-center justify-between cursor-pointer">
                <span className="text-gray-700">Fiyat Uyarıları</span>
                <input type="checkbox" className="w-5 h-5 text-blue-600 rounded" />
              </label>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 bg-green-100 rounded-lg flex items-center justify-center">
                <CreditCard className="w-5 h-5 text-green-600" />
              </div>
              <h3 className="text-gray-900">Ödeme Yöntemleri</h3>
            </div>
            <button className="w-full px-4 py-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors">
              <p className="text-gray-900">Banka Hesaplarını Yönet</p>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
