import { useState } from 'react';
import { Star, TrendingUp, Users, Award, DollarSign } from 'lucide-react';

export function BrokersTab() {
  const [selectedBroker, setSelectedBroker] = useState<number | null>(null);
  const [investmentAmount, setInvestmentAmount] = useState('');

  const brokers = [
    {
      id: 1,
      name: 'Ahmet Yılmaz',
      company: 'Premium Yatırım',
      rating: 4.8,
      clients: 156,
      experience: 12,
      specialty: 'Teknoloji ve Finans',
      performance: 18.5,
      minInvestment: 50000,
    },
    {
      id: 2,
      name: 'Elif Kaya',
      company: 'Global Broker',
      rating: 4.9,
      clients: 203,
      experience: 15,
      specialty: 'Enerji ve Gayrimenkul',
      performance: 22.3,
      minInvestment: 100000,
    },
    {
      id: 3,
      name: 'Mehmet Demir',
      company: 'Finans Plus',
      rating: 4.7,
      clients: 128,
      experience: 10,
      specialty: 'Sağlık ve Teknoloji',
      performance: 16.8,
      minInvestment: 75000,
    },
    {
      id: 4,
      name: 'Zeynep Arslan',
      company: 'Yatırım Merkezi',
      rating: 4.6,
      clients: 94,
      experience: 8,
      specialty: 'Gıda ve Tarım',
      performance: 15.2,
      minInvestment: 40000,
    },
  ];

  const handleInvest = (brokerId: number) => {
    alert(`${investmentAmount} TL yatırım talebiniz ${brokers.find(b => b.id === brokerId)?.name} ile başlatıldı.`);
    setSelectedBroker(null);
    setInvestmentAmount('');
  };

  return (
    <div className="space-y-6">
      {/* Info Banner */}
      <div className="bg-blue-50 border border-blue-200 rounded-xl p-6">
        <div className="flex items-start gap-3">
          <Users className="w-6 h-6 text-blue-600 flex-shrink-0 mt-1" />
          <div>
            <h3 className="text-blue-900 mb-1">Profesyonel Broker Desteği</h3>
            <p className="text-blue-700">
              Deneyimli brokerlarımız ile çalışarak yatırımlarınızı profesyonel bir şekilde yönetin.
            </p>
          </div>
        </div>
      </div>

      {/* Brokers Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {brokers.map((broker) => (
          <div key={broker.id} className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-md transition-shadow">
            <div className="p-6">
              {/* Broker Header */}
              <div className="flex items-start justify-between mb-4">
                <div className="flex items-start gap-4">
                  <div className="w-16 h-16 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-xl flex items-center justify-center text-white flex-shrink-0">
                    <span className="text-2xl">{broker.name.charAt(0)}</span>
                  </div>
                  <div>
                    <h3 className="text-gray-900 mb-1">{broker.name}</h3>
                    <p className="text-sm text-gray-600">{broker.company}</p>
                    <div className="flex items-center gap-1 mt-2">
                      <Star className="w-4 h-4 text-yellow-500 fill-yellow-500" />
                      <span className="text-gray-900">{broker.rating}</span>
                      <span className="text-gray-500 text-sm ml-1">({broker.clients} müşteri)</span>
                    </div>
                  </div>
                </div>
              </div>

              {/* Broker Stats */}
              <div className="grid grid-cols-2 gap-4 mb-4 pt-4 border-t border-gray-100">
                <div>
                  <div className="flex items-center gap-2 text-gray-600 text-sm mb-1">
                    <Award className="w-4 h-4" />
                    <span>Deneyim</span>
                  </div>
                  <p className="text-gray-900">{broker.experience} Yıl</p>
                </div>
                <div>
                  <div className="flex items-center gap-2 text-gray-600 text-sm mb-1">
                    <TrendingUp className="w-4 h-4" />
                    <span>Performans</span>
                  </div>
                  <p className="text-green-600">+%{broker.performance}</p>
                </div>
              </div>

              <div className="mb-4">
                <p className="text-sm text-gray-600 mb-1">Uzmanlık Alanı</p>
                <p className="text-gray-900">{broker.specialty}</p>
              </div>

              <div className="flex items-center gap-2 text-sm text-gray-600 mb-4">
                <DollarSign className="w-4 h-4" />
                <span>Min. Yatırım: ₺{broker.minInvestment.toLocaleString('tr-TR')}</span>
              </div>

              {/* Investment Form */}
              {selectedBroker === broker.id ? (
                <div className="space-y-3 pt-4 border-t border-gray-100">
                  <div>
                    <label className="block text-sm text-gray-600 mb-2">Yatırım Miktarı (₺)</label>
                    <input
                      type="number"
                      value={investmentAmount}
                      onChange={(e) => setInvestmentAmount(e.target.value)}
                      placeholder={`Min. ${broker.minInvestment.toLocaleString('tr-TR')}`}
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none"
                    />
                  </div>
                  <div className="flex gap-3">
                    <button
                      onClick={() => handleInvest(broker.id)}
                      className="flex-1 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors"
                    >
                      Yatırım Yap
                    </button>
                    <button
                      onClick={() => setSelectedBroker(null)}
                      className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
                    >
                      İptal
                    </button>
                  </div>
                </div>
              ) : (
                <button
                  onClick={() => setSelectedBroker(broker.id)}
                  className="w-full bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors"
                >
                  Yatırım Yap
                </button>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
