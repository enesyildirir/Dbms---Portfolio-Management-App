import { User, Mail, Phone, Award, Calendar, TrendingUp, Users, Target } from 'lucide-react';
import { useState } from 'react';

export function BrokerProfileTab() {
  const [isEditing, setIsEditing] = useState(false);
  const [formData, setFormData] = useState({
    name: 'Mehmet Yıldırım',
    email: 'mehmet.yildirim@broker.com',
    phone: '+90 532 987 65 43',
  });

  const handleSave = () => {
    // Mock save - gerçek sistemde API'ye gönderilecek
    alert('Profil bilgileri güncellendi!');
    setIsEditing(false);
  };

  const handleCancel = () => {
    setFormData({
      name: 'Mehmet Yıldırım',
      email: 'mehmet.yildirim@broker.com',
      phone: '+90 532 987 65 43',
    });
    setIsEditing(false);
  };

  const profile = {
    name: 'Mehmet Yıldırım',
    email: 'mehmet.yildirim@broker.com',
    phone: '+90 532 987 65 43',
    license: 'BRK-2018-12345',
    company: 'Premium Yatırım A.Ş.',
    experience: 8,
    joinDate: '10 Ocak 2018',
    specializations: ['Teknoloji', 'Enerji', 'Finans'],
  };

  const stats = {
    totalClients: 89,
    activeInvestments: 245,
    avgReturn: 16.8,
    customerSatisfaction: 4.8,
    totalAssetsManaged: 54500000,
  };

  return (
    <div className="space-y-6">
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Profile Card */}
        <div className="lg:col-span-2 bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <div className="flex items-start gap-6 mb-6">
            <div className="w-24 h-24 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-xl flex items-center justify-center text-white flex-shrink-0">
              <span className="text-4xl">{profile.name.charAt(0)}</span>
            </div>
            <div className="flex-1">
              <h2 className="text-gray-900 mb-2">{profile.name}</h2>
              <p className="text-gray-600 mb-1">{profile.company}</p>
              <p className="text-sm text-gray-500">Lisans No: {profile.license}</p>
            </div>
          </div>

          <div className="space-y-4 mb-6">
            <div className="flex items-start gap-4 p-4 bg-gray-50 rounded-lg">
              <Mail className="w-5 h-5 text-gray-600 mt-0.5" />
              <div className="flex-1">
                <p className="text-sm text-gray-600 mb-1">E-posta</p>
                {isEditing ? (
                  <input
                    type="email"
                    value={formData.email}
                    onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none"
                  />
                ) : (
                  <p className="text-gray-900">{formData.email}</p>
                )}
              </div>
            </div>

            <div className="flex items-start gap-4 p-4 bg-gray-50 rounded-lg">
              <Phone className="w-5 h-5 text-gray-600 mt-0.5" />
              <div className="flex-1">
                <p className="text-sm text-gray-600 mb-1">Telefon</p>
                {isEditing ? (
                  <input
                    type="tel"
                    value={formData.phone}
                    onChange={(e) => setFormData({ ...formData, phone: e.target.value })}
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none"
                  />
                ) : (
                  <p className="text-gray-900">{formData.phone}</p>
                )}
              </div>
            </div>

            <div className="flex items-start gap-4 p-4 bg-gray-50 rounded-lg">
              <Award className="w-5 h-5 text-gray-600 mt-0.5" />
              <div>
                <p className="text-sm text-gray-600 mb-1">Deneyim</p>
                <p className="text-gray-900">{profile.experience} Yıl</p>
              </div>
            </div>

            <div className="flex items-start gap-4 p-4 bg-gray-50 rounded-lg">
              <Calendar className="w-5 h-5 text-gray-600 mt-0.5" />
              <div>
                <p className="text-sm text-gray-600 mb-1">Başlangıç Tarihi</p>
                <p className="text-gray-900">{profile.joinDate}</p>
              </div>
            </div>
          </div>

          {/* Specializations */}
          <div className="mb-6">
            <p className="text-sm text-gray-600 mb-3">Uzmanlık Alanları</p>
            <div className="flex flex-wrap gap-2">
              {profile.specializations.map((spec, index) => (
                <span
                  key={index}
                  className="inline-flex items-center px-3 py-1 rounded-full text-sm bg-indigo-100 text-indigo-800"
                >
                  {spec}
                </span>
              ))}
            </div>
          </div>

          {isEditing ? (
            <div className="flex gap-3">
              <button
                onClick={handleSave}
                className="flex-1 bg-indigo-600 text-white px-6 py-3 rounded-lg hover:bg-indigo-700 transition-colors"
              >
                Değişiklikleri Kaydet
              </button>
              <button
                onClick={handleCancel}
                className="px-6 py-3 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
              >
                İptal
              </button>
            </div>
          ) : (
            <button
              onClick={() => setIsEditing(true)}
              className="w-full bg-indigo-600 text-white px-6 py-3 rounded-lg hover:bg-indigo-700 transition-colors"
            >
              Profili Düzenle
            </button>
          )}
        </div>

        {/* Stats Cards */}
        <div className="space-y-6">
          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 bg-indigo-100 rounded-lg flex items-center justify-center">
                <Users className="w-5 h-5 text-indigo-600" />
              </div>
              <div>
                <p className="text-sm text-gray-600">Toplam Müşteri</p>
                <p className="text-gray-900">{stats.totalClients}</p>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center">
                <Target className="w-5 h-5 text-blue-600" />
              </div>
              <div>
                <p className="text-sm text-gray-600">Aktif Yatırım</p>
                <p className="text-gray-900">{stats.activeInvestments}</p>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 bg-green-100 rounded-lg flex items-center justify-center">
                <TrendingUp className="w-5 h-5 text-green-600" />
              </div>
              <div>
                <p className="text-sm text-gray-600">Ortalama Getiri</p>
                <p className="text-green-600">+%{stats.avgReturn}</p>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 bg-yellow-100 rounded-lg flex items-center justify-center">
                <Award className="w-5 h-5 text-yellow-600" />
              </div>
              <div>
                <p className="text-sm text-gray-600">Müşteri Memnuniyeti</p>
                <div className="flex items-center gap-1">
                  <p className="text-gray-900">{stats.customerSatisfaction}</p>
                  <span className="text-sm text-gray-500">/5.0</span>
                </div>
              </div>
            </div>
          </div>

          <div className="bg-gradient-to-br from-indigo-500 to-purple-600 rounded-xl shadow-sm p-6 text-white">
            <p className="text-indigo-100 mb-2">Yönetilen Toplam Varlık</p>
            <p className="text-3xl">₺{(stats.totalAssetsManaged / 1000000).toFixed(1)}M</p>
          </div>
        </div>
      </div>

      {/* Performance Chart Section */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
        <h3 className="text-gray-900 mb-4">Performans Geçmişi</h3>
        <div className="h-64 flex items-center justify-center bg-gray-50 rounded-lg">
          <p className="text-gray-500">Performans grafiği burada görüntülenecek</p>
        </div>
      </div>
    </div>
  );
}