import { Users, TrendingUp, DollarSign, ArrowUpRight, Search } from 'lucide-react';
import { useState } from 'react';

export function ClientAssetsTab() {
  const [searchQuery, setSearchQuery] = useState('');

  const clients = [
    {
      id: 1,
      name: 'Mehmet Özkan',
      portfolioValue: 850000,
      monthlyChange: 12.5,
      investmentCount: 8,
      riskProfile: 'Dengeli',
      lastActivity: '2 saat önce',
    },
    {
      id: 2,
      name: 'Zeynep Kara',
      portfolioValue: 1250000,
      monthlyChange: 18.2,
      investmentCount: 12,
      riskProfile: 'Agresif',
      lastActivity: '1 gün önce',
    },
    {
      id: 3,
      name: 'Ali Yıldız',
      portfolioValue: 450000,
      monthlyChange: 8.7,
      investmentCount: 5,
      riskProfile: 'Muhafazakar',
      lastActivity: '3 saat önce',
    },
    {
      id: 4,
      name: 'Ayşe Demir',
      portfolioValue: 650000,
      monthlyChange: 15.3,
      investmentCount: 9,
      riskProfile: 'Dengeli',
      lastActivity: '5 saat önce',
    },
    {
      id: 5,
      name: 'Can Aydın',
      portfolioValue: 950000,
      monthlyChange: -2.1,
      investmentCount: 7,
      riskProfile: 'Agresif',
      lastActivity: '1 saat önce',
    },
    {
      id: 6,
      name: 'Selin Çelik',
      portfolioValue: 380000,
      monthlyChange: 6.8,
      investmentCount: 6,
      riskProfile: 'Muhafazakar',
      lastActivity: '4 saat önce',
    },
  ];

  const totalStats = {
    totalClients: clients.length,
    totalAssets: clients.reduce((sum, client) => sum + client.portfolioValue, 0),
    averageReturn: clients.reduce((sum, client) => sum + client.monthlyChange, 0) / clients.length,
  };

  const filteredClients = clients.filter(client =>
    client.name.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const getRiskColor = (risk: string) => {
    switch (risk) {
      case 'Agresif':
        return 'bg-red-100 text-red-800';
      case 'Dengeli':
        return 'bg-yellow-100 text-yellow-800';
      case 'Muhafazakar':
        return 'bg-green-100 text-green-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <div className="space-y-6">
      {/* Summary Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center justify-between mb-2">
            <span className="text-gray-600">Toplam Müşteri</span>
            <Users className="w-5 h-5 text-indigo-600" />
          </div>
          <p className="text-gray-900">{totalStats.totalClients}</p>
        </div>

        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center justify-between mb-2">
            <span className="text-gray-600">Toplam Varlık</span>
            <DollarSign className="w-5 h-5 text-indigo-600" />
          </div>
          <p className="text-gray-900">₺{totalStats.totalAssets.toLocaleString('tr-TR')}</p>
        </div>

        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center justify-between mb-2">
            <span className="text-gray-600">Ort. Getiri</span>
            <TrendingUp className="w-5 h-5 text-green-600" />
          </div>
          <p className="text-green-600">+%{totalStats.averageReturn.toFixed(2)}</p>
        </div>
      </div>

      {/* Search */}
      <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
        <div className="relative">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
          <input
            type="text"
            placeholder="Müşteri ara..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full pl-10 pr-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent outline-none"
          />
        </div>
      </div>

      {/* Clients List */}
      <div className="grid grid-cols-1 gap-6">
        {filteredClients.map((client) => (
          <div key={client.id} className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-md transition-shadow">
            <div className="p-6">
              <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
                {/* Client Info */}
                <div className="flex items-start gap-4 flex-1">
                  <div className="w-14 h-14 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-xl flex items-center justify-center text-white flex-shrink-0">
                    <span className="text-xl">{client.name.charAt(0)}</span>
                  </div>
                  <div>
                    <h3 className="text-gray-900 mb-1">{client.name}</h3>
                    <div className="flex items-center gap-3 flex-wrap">
                      <span className="text-sm text-gray-600">{client.investmentCount} Yatırım</span>
                      <span className="text-sm text-gray-400">•</span>
                      <span className={`inline-flex items-center px-2 py-0.5 rounded-full text-xs ${getRiskColor(client.riskProfile)}`}>
                        {client.riskProfile}
                      </span>
                    </div>
                  </div>
                </div>

                {/* Stats */}
                <div className="grid grid-cols-2 lg:grid-cols-3 gap-4 lg:gap-8">
                  <div>
                    <p className="text-sm text-gray-600 mb-1">Portföy Değeri</p>
                    <p className="text-gray-900">₺{client.portfolioValue.toLocaleString('tr-TR')}</p>
                  </div>
                  <div>
                    <p className="text-sm text-gray-600 mb-1">Aylık Değişim</p>
                    <div className="flex items-center gap-1">
                      {client.monthlyChange >= 0 ? (
                        <>
                          <ArrowUpRight className="w-4 h-4 text-green-600" />
                          <span className="text-green-600">+%{client.monthlyChange}</span>
                        </>
                      ) : (
                        <>
                          <TrendingUp className="w-4 h-4 text-red-600" />
                          <span className="text-red-600">%{client.monthlyChange}</span>
                        </>
                      )}
                    </div>
                  </div>
                  <div>
                    <p className="text-sm text-gray-600 mb-1">Son Aktivite</p>
                    <p className="text-gray-900">{client.lastActivity}</p>
                  </div>
                </div>

                {/* Action */}
                <button className="bg-indigo-600 text-white px-6 py-2 rounded-lg hover:bg-indigo-700 transition-colors whitespace-nowrap">
                  Detayları Gör
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
