import { DollarSign, Users, TrendingUp, Activity, Calendar, ArrowUpRight, ArrowDownRight, Download } from 'lucide-react';
import { useState } from 'react';

interface PerformanceTabProps {
  brokerId: number;
}

export function PerformanceTab({ brokerId }: PerformanceTabProps) {
  const [selectedPeriod, setSelectedPeriod] = useState<'week' | 'month' | 'year'>('month');

  const handleExportReport = () => {
    alert('Performans raporu indiriliyor...');
    // Gerçek sistemde PDF veya Excel export yapılacak
  };

  // Mock data - gerçek sistemde veritabanından gelecek
  const brokerData = {
    name: 'Mehmet Yıldırım',
    position: 'Kıdemli Yatırım Danışmanı',
    email: 'mehmet.yildirim@broker.com',
    totalCommission: 124500,
    monthlyCommission: 18750,
    accountCount: 24,
    activeClients: 21,
  };

  const recentTransactions = [
    {
      id: 1,
      date: '2025-12-05 14:30',
      client: 'Ayşe Kaya',
      asset: 'THYAO',
      type: 'ALIS',
      amount: 1000,
      price: 245.50,
      commission: 245.50,
    },
    {
      id: 2,
      date: '2025-12-05 11:15',
      client: 'Mehmet Özkan',
      asset: 'GARAN',
      type: 'SATIS',
      amount: 500,
      price: 38.75,
      commission: 193.75,
    },
    {
      id: 3,
      date: '2025-12-04 16:45',
      client: 'Zeynep Demir',
      asset: 'AKBNK',
      type: 'ALIS',
      amount: 2000,
      price: 52.30,
      commission: 523.00,
    },
    {
      id: 4,
      date: '2025-12-04 10:20',
      client: 'Ali Yılmaz',
      asset: 'EREGL',
      type: 'ALIS',
      amount: 1500,
      price: 48.90,
      commission: 366.75,
    },
    {
      id: 5,
      date: '2025-12-03 15:00',
      client: 'Fatma Aydın',
      asset: 'KCHOL',
      type: 'SATIS',
      amount: 800,
      price: 156.20,
      commission: 624.80,
    },
  ];

  const monthlyStats = [
    { month: 'Haziran', commission: 15200, clients: 18 },
    { month: 'Temmuz', commission: 18900, clients: 20 },
    { month: 'Ağustos', commission: 16500, clients: 21 },
    { month: 'Eylül', commission: 21300, clients: 22 },
    { month: 'Ekim', commission: 19800, clients: 23 },
    { month: 'Kasım', commission: 18750, clients: 24 },
  ];

  return (
    <div className="space-y-6">
      {/* Personal Info Card */}
      <div className="bg-gradient-to-br from-indigo-600 to-purple-600 rounded-2xl p-6 text-white shadow-lg">
        <div className="flex items-start justify-between">
          <div>
            <h2 className="text-white mb-2">{brokerData.name}</h2>
            <p className="text-indigo-100 mb-1">{brokerData.position}</p>
            <p className="text-indigo-200 text-sm">{brokerData.email}</p>
          </div>
          <div className="w-16 h-16 bg-white/20 backdrop-blur-sm rounded-xl flex items-center justify-center">
            <span className="text-3xl">{brokerData.name.charAt(0)}</span>
          </div>
        </div>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center justify-between mb-3">
            <div className="w-12 h-12 bg-green-100 rounded-xl flex items-center justify-center">
              <DollarSign className="w-6 h-6 text-green-600" />
            </div>
            <div className="flex items-center gap-1 text-green-600 text-sm">
              <ArrowUpRight className="w-4 h-4" />
              <span>+12.5%</span>
            </div>
          </div>
          <p className="text-sm text-gray-600 mb-1">Toplam Komisyon</p>
          <p className="text-gray-900">₺{brokerData.totalCommission.toLocaleString('tr-TR')}</p>
        </div>

        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center justify-between mb-3">
            <div className="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center">
              <Calendar className="w-6 h-6 text-blue-600" />
            </div>
            <div className="flex items-center gap-1 text-blue-600 text-sm">
              <ArrowUpRight className="w-4 h-4" />
              <span>+5.2%</span>
            </div>
          </div>
          <p className="text-sm text-gray-600 mb-1">Aylık Komisyon</p>
          <p className="text-gray-900">₺{brokerData.monthlyCommission.toLocaleString('tr-TR')}</p>
        </div>

        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center justify-between mb-3">
            <div className="w-12 h-12 bg-indigo-100 rounded-xl flex items-center justify-center">
              <Users className="w-6 h-6 text-indigo-600" />
            </div>
            <div className="flex items-center gap-1 text-indigo-600 text-sm">
              <ArrowUpRight className="w-4 h-4" />
              <span>+3</span>
            </div>
          </div>
          <p className="text-sm text-gray-600 mb-1">Toplam Müşteri</p>
          <p className="text-gray-900">{brokerData.accountCount}</p>
        </div>

        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center justify-between mb-3">
            <div className="w-12 h-12 bg-purple-100 rounded-xl flex items-center justify-center">
              <Activity className="w-6 h-6 text-purple-600" />
            </div>
          </div>
          <p className="text-sm text-gray-600 mb-1">Aktif Müşteri</p>
          <p className="text-gray-900">{brokerData.activeClients} / {brokerData.accountCount}</p>
        </div>
      </div>

      {/* Monthly Performance Chart */}
      <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
        <div className="flex items-center justify-between mb-6">
          <h3 className="text-gray-900">Aylık Performans</h3>
          <div className="flex items-center gap-2">
            <button
              onClick={() => setSelectedPeriod('week')}
              className={`px-3 py-1 rounded-lg text-sm transition-colors ${
                selectedPeriod === 'week'
                  ? 'bg-indigo-100 text-indigo-700'
                  : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
              }`}
            >
              Haftalık
            </button>
            <button
              onClick={() => setSelectedPeriod('month')}
              className={`px-3 py-1 rounded-lg text-sm transition-colors ${
                selectedPeriod === 'month'
                  ? 'bg-indigo-100 text-indigo-700'
                  : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
              }`}
            >
              Aylık
            </button>
            <button
              onClick={() => setSelectedPeriod('year')}
              className={`px-3 py-1 rounded-lg text-sm transition-colors ${
                selectedPeriod === 'year'
                  ? 'bg-indigo-100 text-indigo-700'
                  : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
              }`}
            >
              Yıllık
            </button>
          </div>
        </div>
        <div className="space-y-4">
          {monthlyStats.map((stat, index) => {
            const maxCommission = Math.max(...monthlyStats.map(s => s.commission));
            const percentage = (stat.commission / maxCommission) * 100;
            
            return (
              <div key={index}>
                <div className="flex items-center justify-between mb-2">
                  <span className="text-sm text-gray-600">{stat.month}</span>
                  <div className="flex items-center gap-4">
                    <span className="text-sm text-gray-500">{stat.clients} müşteri</span>
                    <span className="text-gray-900">₺{stat.commission.toLocaleString('tr-TR')}</span>
                  </div>
                </div>
                <div className="w-full bg-gray-100 rounded-full h-2">
                  <div
                    className="bg-gradient-to-r from-indigo-500 to-purple-600 h-2 rounded-full transition-all"
                    style={{ width: `${percentage}%` }}
                  />
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Recent Transactions */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
        <div className="px-6 py-4 border-b border-gray-200 flex items-center justify-between">
          <h3 className="text-gray-900">Son 5 İşlem</h3>
          <button
            onClick={handleExportReport}
            className="flex items-center gap-2 px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors text-sm"
          >
            <Download className="w-4 h-4" />
            <span>Rapor İndir</span>
          </button>
        </div>
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead className="bg-gray-50">
              <tr>
                <th className="px-6 py-3 text-left text-sm text-gray-600">Tarih & Saat</th>
                <th className="px-6 py-3 text-left text-sm text-gray-600">Müşteri</th>
                <th className="px-6 py-3 text-left text-sm text-gray-600">Varlık</th>
                <th className="px-6 py-3 text-center text-sm text-gray-600">İşlem Tipi</th>
                <th className="px-6 py-3 text-right text-sm text-gray-600">Miktar</th>
                <th className="px-6 py-3 text-right text-sm text-gray-600">Birim Fiyat</th>
                <th className="px-6 py-3 text-right text-sm text-gray-600">Komisyon</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200">
              {recentTransactions.map((transaction) => (
                <tr key={transaction.id} className="hover:bg-gray-50 transition-colors">
                  <td className="px-6 py-4 text-sm text-gray-600">{transaction.date}</td>
                  <td className="px-6 py-4 text-sm text-gray-900">{transaction.client}</td>
                  <td className="px-6 py-4">
                    <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs bg-blue-100 text-blue-800">
                      {transaction.asset}
                    </span>
                  </td>
                  <td className="px-6 py-4 text-center">
                    <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs ${
                      transaction.type === 'ALIS' 
                        ? 'bg-green-100 text-green-800' 
                        : 'bg-red-100 text-red-800'
                    }`}>
                      {transaction.type}
                    </span>
                  </td>
                  <td className="px-6 py-4 text-right text-sm text-gray-900">{transaction.amount.toLocaleString('tr-TR')}</td>
                  <td className="px-6 py-4 text-right text-sm text-gray-900">₺{transaction.price.toFixed(2)}</td>
                  <td className="px-6 py-4 text-right text-sm text-green-600">₺{transaction.commission.toFixed(2)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}