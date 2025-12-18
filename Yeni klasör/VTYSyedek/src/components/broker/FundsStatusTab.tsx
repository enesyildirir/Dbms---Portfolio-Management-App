import { TrendingUp, TrendingDown, PieChart, BarChart3, Activity } from 'lucide-react';
import { useState } from 'react';

export function FundsStatusTab() {
  const [selectedFund, setSelectedFund] = useState<number | null>(null);

  const funds = [
    {
      id: 1,
      name: 'Teknoloji Büyüme Fonu',
      code: 'TBF-001',
      totalValue: 145000000,
      clientCount: 3420,
      yourClients: 24,
      performance1M: 5.2,
      performance3M: 12.8,
      performance1Y: 28.5,
      status: 'Aktif',
      allocation: 32,
    },
    {
      id: 2,
      name: 'Dengeli Karma Fon',
      code: 'DKF-002',
      totalValue: 98000000,
      clientCount: 5680,
      yourClients: 38,
      performance1M: 2.8,
      performance3M: 7.5,
      performance1Y: 15.2,
      status: 'Aktif',
      allocation: 28,
    },
    {
      id: 3,
      name: 'Gayrimenkul Gelir Fonu',
      code: 'GGF-003',
      totalValue: 210000000,
      clientCount: 2150,
      yourClients: 15,
      performance1M: 1.5,
      performance3M: 4.2,
      performance1Y: 10.8,
      status: 'Aktif',
      allocation: 18,
    },
    {
      id: 4,
      name: 'Enerji Sektör Fonu',
      code: 'ESF-004',
      totalValue: 72000000,
      clientCount: 1890,
      yourClients: 12,
      performance1M: -1.2,
      performance3M: 8.9,
      performance1Y: 22.3,
      status: 'Volatil',
      allocation: 12,
    },
    {
      id: 5,
      name: 'Altın Koruma Fonu',
      code: 'AKF-005',
      totalValue: 56000000,
      clientCount: 4320,
      yourClients: 31,
      performance1M: 0.8,
      performance3M: 3.1,
      performance1Y: 8.5,
      status: 'Aktif',
      allocation: 10,
    },
  ];

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'Aktif':
        return 'bg-green-100 text-green-800';
      case 'Volatil':
        return 'bg-yellow-100 text-yellow-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  const totalYourClients = funds.reduce((sum, fund) => sum + fund.yourClients, 0);
  const avgPerformance1M = funds.reduce((sum, fund) => sum + fund.performance1M, 0) / funds.length;

  return (
    <div className="space-y-6">
      {/* Summary Cards */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center justify-between mb-2">
            <span className="text-gray-600">Toplam Fon</span>
            <PieChart className="w-5 h-5 text-indigo-600" />
          </div>
          <p className="text-gray-900">{funds.length}</p>
        </div>

        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center justify-between mb-2">
            <span className="text-gray-600">Müşterileriniz</span>
            <BarChart3 className="w-5 h-5 text-indigo-600" />
          </div>
          <p className="text-gray-900">{totalYourClients} Yatırımcı</p>
        </div>

        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center justify-between mb-2">
            <span className="text-gray-600">Ort. Performans</span>
            <Activity className="w-5 h-5 text-green-600" />
          </div>
          <p className="text-green-600">+%{avgPerformance1M.toFixed(2)}</p>
          <p className="text-xs text-gray-500">Son 1 Ay</p>
        </div>

        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center justify-between mb-2">
            <span className="text-gray-600">Aktif Fonlar</span>
            <TrendingUp className="w-5 h-5 text-indigo-600" />
          </div>
          <p className="text-gray-900">{funds.filter(f => f.status === 'Aktif').length}/{funds.length}</p>
        </div>
      </div>

      {/* Funds List */}
      <div className="space-y-6">
        {funds.map((fund) => (
          <div key={fund.id} className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
            <div className="p-6">
              {/* Fund Header */}
              <div className="flex flex-col lg:flex-row lg:items-start lg:justify-between gap-4 mb-6">
                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-xl flex items-center justify-center text-white flex-shrink-0">
                    <PieChart className="w-6 h-6" />
                  </div>
                  <div>
                    <h3 className="text-gray-900 mb-1">{fund.name}</h3>
                    <div className="flex items-center gap-3 flex-wrap">
                      <span className="text-sm text-gray-600">{fund.code}</span>
                      <span className="text-sm text-gray-400">•</span>
                      <span className="text-sm text-gray-600">₺{(fund.totalValue / 1000000).toFixed(1)}M Büyüklük</span>
                    </div>
                  </div>
                </div>
                <span className={`inline-flex items-center px-3 py-1 rounded-full text-sm ${getStatusColor(fund.status)}`}>
                  {fund.status}
                </span>
              </div>

              {/* Stats Grid */}
              <div className="grid grid-cols-2 lg:grid-cols-6 gap-4 mb-4">
                <div>
                  <p className="text-sm text-gray-600 mb-1">Toplam Yatırımcı</p>
                  <p className="text-gray-900">{fund.clientCount.toLocaleString('tr-TR')}</p>
                </div>
                <div>
                  <p className="text-sm text-gray-600 mb-1">Müşterileriniz</p>
                  <p className="text-indigo-600">{fund.yourClients}</p>
                </div>
                <div>
                  <p className="text-sm text-gray-600 mb-1">1 Aylık</p>
                  <div className="flex items-center gap-1">
                    {fund.performance1M >= 0 ? (
                      <>
                        <TrendingUp className="w-4 h-4 text-green-600" />
                        <span className="text-green-600">+%{fund.performance1M}</span>
                      </>
                    ) : (
                      <>
                        <TrendingDown className="w-4 h-4 text-red-600" />
                        <span className="text-red-600">%{fund.performance1M}</span>
                      </>
                    )}
                  </div>
                </div>
                <div>
                  <p className="text-sm text-gray-600 mb-1">3 Aylık</p>
                  <div className="flex items-center gap-1">
                    <TrendingUp className="w-4 h-4 text-green-600" />
                    <span className="text-green-600">+%{fund.performance3M}</span>
                  </div>
                </div>
                <div>
                  <p className="text-sm text-gray-600 mb-1">Yıllık</p>
                  <div className="flex items-center gap-1">
                    <TrendingUp className="w-4 h-4 text-green-600" />
                    <span className="text-green-600">+%{fund.performance1Y}</span>
                  </div>
                </div>
                <div>
                  <p className="text-sm text-gray-600 mb-1">Dağılım</p>
                  <p className="text-gray-900">%{fund.allocation}</p>
                </div>
              </div>

              {/* Progress Bar */}
              <div className="mb-4">
                <div className="flex items-center justify-between text-sm mb-2">
                  <span className="text-gray-600">Portföy Dağılımı</span>
                  <span className="text-gray-900">%{fund.allocation}</span>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-2">
                  <div
                    className="bg-gradient-to-r from-indigo-500 to-purple-600 h-2 rounded-full transition-all"
                    style={{ width: `${fund.allocation}%` }}
                  />
                </div>
              </div>

              {/* Action */}
              <div className="pt-4 border-t border-gray-100">
                <button 
                  onClick={() => setSelectedFund(selectedFund === fund.id ? null : fund.id)}
                  className="w-full lg:w-auto bg-indigo-600 text-white px-6 py-2 rounded-lg hover:bg-indigo-700 transition-colors"
                >
                  {selectedFund === fund.id ? 'Detayları Gizle' : 'Müşteri Detaylarını Görüntüle'}
                </button>
              </div>

              {/* Client Details */}
              {selectedFund === fund.id && (
                <div className="mt-6 pt-6 border-t border-gray-200">
                  <h4 className="text-gray-900 mb-4">Bu Fonda Yatırımı Olan Müşterileriniz ({fund.yourClients})</h4>
                  <div className="bg-gray-50 rounded-lg p-4">
                    <div className="space-y-3">
                      {/* Mock client data for this fund */}
                      {[
                        { name: 'Ayşe Kaya', amount: 125000, percentage: 15 },
                        { name: 'Mehmet Özkan', amount: 98000, percentage: 12 },
                        { name: 'Zeynep Demir', amount: 67000, percentage: 8 },
                        { name: 'Ali Yılmaz', amount: 54000, percentage: 7 },
                        { name: 'Fatma Aydın', amount: 45000, percentage: 5 },
                      ].slice(0, Math.min(5, fund.yourClients)).map((client, idx) => (
                        <div key={idx} className="flex items-center justify-between bg-white p-3 rounded-lg">
                          <div className="flex items-center gap-3">
                            <div className="w-8 h-8 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-lg flex items-center justify-center text-white text-sm">
                              {client.name.charAt(0)}
                            </div>
                            <div>
                              <p className="text-sm text-gray-900">{client.name}</p>
                              <p className="text-xs text-gray-500">Yatırım: ₺{client.amount.toLocaleString('tr-TR')}</p>
                            </div>
                          </div>
                          <div className="text-right">
                            <p className="text-sm text-gray-900">%{client.percentage}</p>
                            <p className="text-xs text-gray-500">portföy</p>
                          </div>
                        </div>
                      ))}
                      {fund.yourClients > 5 && (
                        <div className="text-center pt-2">
                          <button className="text-sm text-indigo-600 hover:text-indigo-700">
                            +{fund.yourClients - 5} müşteri daha göster
                          </button>
                        </div>
                      )}
                    </div>
                  </div>
                </div>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}