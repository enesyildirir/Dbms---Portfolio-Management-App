import { TrendingUp, TrendingDown, DollarSign, ArrowUpRight, ArrowDownRight } from 'lucide-react';

export function InvestmentsTab() {
  const portfolioSummary = {
    totalValue: 1250000,
    dailyChange: 15750,
    dailyChangePercent: 1.28,
    monthlyReturn: 8.5,
  };

  const investments = [
    { id: 1, name: 'Teknoloji Fonu A', type: 'Fon', value: 450000, change: 5.2, shares: 1500, avgPrice: 300 },
    { id: 2, name: 'Enerji Hisse Paketi', type: 'Hisse', value: 325000, change: -2.1, shares: 5000, avgPrice: 65 },
    { id: 3, name: 'Gayrimenkul Fonu B', type: 'Fon', value: 275000, change: 3.8, shares: 2200, avgPrice: 125 },
    { id: 4, name: 'Banka Hisseleri', type: 'Hisse', value: 200000, change: 1.5, shares: 8000, avgPrice: 25 },
  ];

  return (
    <div className="space-y-6">
      {/* Portfolio Summary Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center justify-between mb-2">
            <span className="text-gray-600">Toplam Portföy Değeri</span>
            <DollarSign className="w-5 h-5 text-blue-600" />
          </div>
          <p className="text-gray-900">₺{portfolioSummary.totalValue.toLocaleString('tr-TR')}</p>
        </div>

        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center justify-between mb-2">
            <span className="text-gray-600">Günlük Değişim</span>
            {portfolioSummary.dailyChange > 0 ? (
              <ArrowUpRight className="w-5 h-5 text-green-600" />
            ) : (
              <ArrowDownRight className="w-5 h-5 text-red-600" />
            )}
          </div>
          <p className={portfolioSummary.dailyChange > 0 ? 'text-green-600' : 'text-red-600'}>
            ₺{Math.abs(portfolioSummary.dailyChange).toLocaleString('tr-TR')}
          </p>
          <p className="text-sm text-gray-500">%{portfolioSummary.dailyChangePercent}</p>
        </div>

        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center justify-between mb-2">
            <span className="text-gray-600">Aylık Getiri</span>
            <TrendingUp className="w-5 h-5 text-blue-600" />
          </div>
          <p className="text-gray-900">%{portfolioSummary.monthlyReturn}</p>
        </div>

        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center justify-between mb-2">
            <span className="text-gray-600">Toplam Varlık</span>
            <TrendingUp className="w-5 h-5 text-blue-600" />
          </div>
          <p className="text-gray-900">{investments.length} Adet</p>
        </div>
      </div>

      {/* Investments Table */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
        <div className="px-6 py-4 border-b border-gray-200">
          <h2 className="text-gray-900">Yatırım Detayları</h2>
        </div>
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead className="bg-gray-50">
              <tr>
                <th className="px-6 py-3 text-left text-gray-600">Yatırım Adı</th>
                <th className="px-6 py-3 text-left text-gray-600">Tip</th>
                <th className="px-6 py-3 text-right text-gray-600">Adet/Pay</th>
                <th className="px-6 py-3 text-right text-gray-600">Ort. Fiyat</th>
                <th className="px-6 py-3 text-right text-gray-600">Toplam Değer</th>
                <th className="px-6 py-3 text-right text-gray-600">Değişim</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200">
              {investments.map((investment) => (
                <tr key={investment.id} className="hover:bg-gray-50 transition-colors">
                  <td className="px-6 py-4 text-gray-900">{investment.name}</td>
                  <td className="px-6 py-4">
                    <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs ${
                      investment.type === 'Fon' 
                        ? 'bg-blue-100 text-blue-800' 
                        : 'bg-purple-100 text-purple-800'
                    }`}>
                      {investment.type}
                    </span>
                  </td>
                  <td className="px-6 py-4 text-right text-gray-900">{investment.shares.toLocaleString('tr-TR')}</td>
                  <td className="px-6 py-4 text-right text-gray-900">₺{investment.avgPrice.toLocaleString('tr-TR')}</td>
                  <td className="px-6 py-4 text-right text-gray-900">₺{investment.value.toLocaleString('tr-TR')}</td>
                  <td className="px-6 py-4 text-right">
                    <div className="flex items-center justify-end gap-1">
                      {investment.change > 0 ? (
                        <>
                          <TrendingUp className="w-4 h-4 text-green-600" />
                          <span className="text-green-600">+%{investment.change}</span>
                        </>
                      ) : (
                        <>
                          <TrendingDown className="w-4 h-4 text-red-600" />
                          <span className="text-red-600">%{investment.change}</span>
                        </>
                      )}
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
