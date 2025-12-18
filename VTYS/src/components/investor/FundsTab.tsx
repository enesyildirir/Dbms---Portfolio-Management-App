import { TrendingUp, TrendingDown, Info } from 'lucide-react';

export function FundsTab() {
  const funds = [
    {
      id: 1,
      name: 'Teknoloji Büyüme Fonu',
      code: 'TBF-001',
      type: 'Hisse Senedi Fonu',
      riskLevel: 'Yüksek',
      return1Month: 5.2,
      return3Month: 12.8,
      return1Year: 28.5,
      minInvestment: 10000,
      totalValue: 145000000,
      investorCount: 3420,
    },
    {
      id: 2,
      name: 'Dengeli Karma Fon',
      code: 'DKF-002',
      type: 'Karma Fon',
      riskLevel: 'Orta',
      return1Month: 2.8,
      return3Month: 7.5,
      return1Year: 15.2,
      minInvestment: 5000,
      totalValue: 98000000,
      investorCount: 5680,
    },
    {
      id: 3,
      name: 'Gayrimenkul Gelir Fonu',
      code: 'GGF-003',
      type: 'Gayrimenkul Fonu',
      riskLevel: 'Düşük',
      return1Month: 1.5,
      return3Month: 4.2,
      return1Year: 10.8,
      minInvestment: 25000,
      totalValue: 210000000,
      investorCount: 2150,
    },
    {
      id: 4,
      name: 'Enerji Sektör Fonu',
      code: 'ESF-004',
      type: 'Sektör Fonu',
      riskLevel: 'Yüksek',
      return1Month: -1.2,
      return3Month: 8.9,
      return1Year: 22.3,
      minInvestment: 15000,
      totalValue: 72000000,
      investorCount: 1890,
    },
    {
      id: 5,
      name: 'Altın Koruma Fonu',
      code: 'AKF-005',
      type: 'Kıymetli Maden Fonu',
      riskLevel: 'Düşük',
      return1Month: 0.8,
      return3Month: 3.1,
      return1Year: 8.5,
      minInvestment: 5000,
      totalValue: 56000000,
      investorCount: 4320,
    },
    {
      id: 6,
      name: 'Banka Hisse Fonu',
      code: 'BHF-006',
      type: 'Hisse Senedi Fonu',
      riskLevel: 'Orta',
      return1Month: 3.5,
      return3Month: 9.2,
      return1Year: 18.7,
      minInvestment: 10000,
      totalValue: 125000000,
      investorCount: 2890,
    },
  ];

  const getRiskColor = (risk: string) => {
    switch (risk) {
      case 'Yüksek':
        return 'bg-red-100 text-red-800';
      case 'Orta':
        return 'bg-yellow-100 text-yellow-800';
      case 'Düşük':
        return 'bg-green-100 text-green-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <div className="space-y-6">
      {/* Info Banner */}
      <div className="bg-indigo-50 border border-indigo-200 rounded-xl p-6">
        <div className="flex items-start gap-3">
          <Info className="w-6 h-6 text-indigo-600 flex-shrink-0 mt-1" />
          <div>
            <h3 className="text-indigo-900 mb-1">Fon Yatırımları</h3>
            <p className="text-indigo-700">
              Profesyonel olarak yönetilen fonlarımız ile çeşitlendirilmiş portföy oluşturun. Her fonun risk seviyesini ve geçmiş performansını inceleyebilirsiniz.
            </p>
          </div>
        </div>
      </div>

      {/* Funds Grid */}
      <div className="grid grid-cols-1 gap-6">
        {funds.map((fund) => (
          <div key={fund.id} className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-md transition-shadow">
            <div className="p-6">
              {/* Fund Header */}
              <div className="flex flex-col lg:flex-row lg:items-start lg:justify-between gap-4 mb-6">
                <div className="flex-1">
                  <div className="flex items-start gap-3 mb-2">
                    <div className="w-12 h-12 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-lg flex items-center justify-center text-white flex-shrink-0">
                      <TrendingUp className="w-6 h-6" />
                    </div>
                    <div>
                      <h3 className="text-gray-900 mb-1">{fund.name}</h3>
                      <div className="flex items-center gap-3 flex-wrap">
                        <span className="text-sm text-gray-600">{fund.code}</span>
                        <span className="text-sm text-gray-400">•</span>
                        <span className="text-sm text-gray-600">{fund.type}</span>
                      </div>
                    </div>
                  </div>
                </div>
                <span className={`inline-flex items-center px-3 py-1 rounded-full text-sm ${getRiskColor(fund.riskLevel)}`}>
                  {fund.riskLevel} Risk
                </span>
              </div>

              {/* Fund Stats */}
              <div className="grid grid-cols-2 lg:grid-cols-5 gap-4 mb-6">
                <div>
                  <p className="text-sm text-gray-600 mb-1">1 Aylık</p>
                  <div className="flex items-center gap-1">
                    {fund.return1Month >= 0 ? (
                      <>
                        <TrendingUp className="w-4 h-4 text-green-600" />
                        <span className="text-green-600">+%{fund.return1Month}</span>
                      </>
                    ) : (
                      <>
                        <TrendingDown className="w-4 h-4 text-red-600" />
                        <span className="text-red-600">%{fund.return1Month}</span>
                      </>
                    )}
                  </div>
                </div>
                <div>
                  <p className="text-sm text-gray-600 mb-1">3 Aylık</p>
                  <div className="flex items-center gap-1">
                    {fund.return3Month >= 0 ? (
                      <>
                        <TrendingUp className="w-4 h-4 text-green-600" />
                        <span className="text-green-600">+%{fund.return3Month}</span>
                      </>
                    ) : (
                      <>
                        <TrendingDown className="w-4 h-4 text-red-600" />
                        <span className="text-red-600">%{fund.return3Month}</span>
                      </>
                    )}
                  </div>
                </div>
                <div>
                  <p className="text-sm text-gray-600 mb-1">Yıllık</p>
                  <div className="flex items-center gap-1">
                    {fund.return1Year >= 0 ? (
                      <>
                        <TrendingUp className="w-4 h-4 text-green-600" />
                        <span className="text-green-600">+%{fund.return1Year}</span>
                      </>
                    ) : (
                      <>
                        <TrendingDown className="w-4 h-4 text-red-600" />
                        <span className="text-red-600">%{fund.return1Year}</span>
                      </>
                    )}
                  </div>
                </div>
                <div>
                  <p className="text-sm text-gray-600 mb-1">Toplam Büyüklük</p>
                  <p className="text-gray-900">₺{(fund.totalValue / 1000000).toFixed(1)}M</p>
                </div>
                <div>
                  <p className="text-sm text-gray-600 mb-1">Yatırımcı</p>
                  <p className="text-gray-900">{fund.investorCount.toLocaleString('tr-TR')}</p>
                </div>
              </div>

              {/* Action */}
              <div className="flex items-center justify-between pt-4 border-t border-gray-100">
                <span className="text-sm text-gray-600">
                  Min. Yatırım: <span className="text-gray-900">₺{fund.minInvestment.toLocaleString('tr-TR')}</span>
                </span>
                <button className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition-colors">
                  Detaylı İncele
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
