import { PieChart, TrendingUp, DollarSign, Package, AlertCircle } from 'lucide-react';

interface PortfolioTabProps {
  investorId: number;
}

export function PortfolioTab({ investorId }: PortfolioTabProps) {
  // Mock data - gerçek sistemde işlemler tablosundan hesaplanacak
  const portfolioPositions = [
    {
      assetId: 'THYAO',
      assetName: 'Türk Hava Yolları',
      type: 'Hisse',
      totalBought: 1000,
      totalSold: 0,
      currentAmount: 1000,
      avgBuyPrice: 245.50,
      totalCost: 245500,
      currentPrice: 248.30, // Gerçek sistemde API'den gelecek
      currentValue: 248300,
      profitLoss: 2800,
      profitLossPercent: 1.14,
    },
    {
      assetId: 'AKBNK',
      assetName: 'Akbank',
      type: 'Hisse',
      totalBought: 2000,
      totalSold: 0,
      currentAmount: 2000,
      avgBuyPrice: 52.30,
      totalCost: 104600,
      currentPrice: 54.10,
      currentValue: 108200,
      profitLoss: 3600,
      profitLossPercent: 3.44,
    },
    {
      assetId: 'EREGL',
      assetName: 'Ereğli Demir Çelik',
      type: 'Hisse',
      totalBought: 1500,
      totalSold: 0,
      currentAmount: 1500,
      avgBuyPrice: 48.90,
      totalCost: 73350,
      currentPrice: 47.20,
      currentValue: 70800,
      profitLoss: -2550,
      profitLossPercent: -3.48,
    },
    {
      assetId: 'SAHOL',
      assetName: 'Sabancı Holding',
      type: 'Hisse',
      totalBought: 1200,
      totalSold: 0,
      currentAmount: 1200,
      avgBuyPrice: 78.40,
      totalCost: 94080,
      currentPrice: 80.50,
      currentValue: 96600,
      profitLoss: 2520,
      profitLossPercent: 2.68,
    },
  ];

  const totalCost = portfolioPositions.reduce((sum, p) => sum + p.totalCost, 0);
  const totalCurrentValue = portfolioPositions.reduce((sum, p) => sum + p.currentValue, 0);
  const totalProfitLoss = totalCurrentValue - totalCost;
  const totalProfitLossPercent = (totalProfitLoss / totalCost) * 100;

  return (
    <div className="space-y-6">
      {/* Portfolio Summary */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center gap-3 mb-2">
            <div className="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center">
              <Package className="w-5 h-5 text-blue-600" />
            </div>
            <div>
              <p className="text-sm text-gray-600">Pozisyon Sayısı</p>
              <p className="text-gray-900">{portfolioPositions.length}</p>
            </div>
          </div>
        </div>

        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center gap-3 mb-2">
            <div className="w-10 h-10 bg-indigo-100 rounded-lg flex items-center justify-center">
              <DollarSign className="w-5 h-5 text-indigo-600" />
            </div>
            <div>
              <p className="text-sm text-gray-600">Toplam Maliyet</p>
              <p className="text-gray-900">₺{totalCost.toLocaleString('tr-TR')}</p>
            </div>
          </div>
        </div>

        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center gap-3 mb-2">
            <div className="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center">
              <PieChart className="w-5 h-5 text-purple-600" />
            </div>
            <div>
              <p className="text-sm text-gray-600">Güncel Değer</p>
              <p className="text-gray-900">₺{totalCurrentValue.toLocaleString('tr-TR')}</p>
            </div>
          </div>
        </div>

        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center gap-3 mb-2">
            <div className={`w-10 h-10 rounded-lg flex items-center justify-center ${
              totalProfitLoss >= 0 ? 'bg-green-100' : 'bg-red-100'
            }`}>
              <TrendingUp className={`w-5 h-5 ${
                totalProfitLoss >= 0 ? 'text-green-600' : 'text-red-600'
              }`} />
            </div>
            <div>
              <p className="text-sm text-gray-600">Kar/Zarar</p>
              <p className={totalProfitLoss >= 0 ? 'text-green-600' : 'text-red-600'}>
                {totalProfitLoss >= 0 ? '+' : ''}₺{totalProfitLoss.toLocaleString('tr-TR')}
              </p>
              <p className={`text-xs ${totalProfitLoss >= 0 ? 'text-green-600' : 'text-red-600'}`}>
                {totalProfitLoss >= 0 ? '+' : ''}%{totalProfitLossPercent.toFixed(2)}
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Info Banner */}
      <div className="bg-blue-50 border border-blue-200 rounded-xl p-6">
        <div className="flex items-start gap-3">
          <AlertCircle className="w-6 h-6 text-blue-600 flex-shrink-0 mt-1" />
          <div>
            <h4 className="text-blue-900 mb-2">Portföy Hesaplama Bilgisi</h4>
            <p className="text-sm text-blue-700">
              Portföy pozisyonları, işlem geçmişinizdeki alış ve satış işlemlerinin netleştirilmesiyle hesaplanır. 
              Güncel piyasa fiyatları canlı veri kaynağından alınır (demo modda simüle edilmektedir).
            </p>
          </div>
        </div>
      </div>

      {/* Positions Table */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
        <div className="px-6 py-4 border-b border-gray-200">
          <h3 className="text-gray-900">Portföy Pozisyonları</h3>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full">
            <thead className="bg-gray-50">
              <tr>
                <th className="px-6 py-3 text-left text-xs text-gray-600">Varlık</th>
                <th className="px-6 py-3 text-right text-xs text-gray-600">Miktar</th>
                <th className="px-6 py-3 text-right text-xs text-gray-600">Ort. Maliyet</th>
                <th className="px-6 py-3 text-right text-xs text-gray-600">Toplam Maliyet</th>
                <th className="px-6 py-3 text-right text-xs text-gray-600">Güncel Fiyat</th>
                <th className="px-6 py-3 text-right text-xs text-gray-600">Güncel Değer</th>
                <th className="px-6 py-3 text-right text-xs text-gray-600">Kar/Zarar</th>
                <th className="px-6 py-3 text-right text-xs text-gray-600">%</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200">
              {portfolioPositions.map((position) => (
                <tr key={position.assetId} className="hover:bg-gray-50 transition-colors">
                  <td className="px-6 py-4">
                    <div>
                      <p className="text-sm text-gray-900">{position.assetId}</p>
                      <p className="text-xs text-gray-500">{position.assetName}</p>
                    </div>
                  </td>
                  <td className="px-6 py-4 text-right text-sm text-gray-900">
                    {position.currentAmount.toLocaleString('tr-TR')}
                  </td>
                  <td className="px-6 py-4 text-right text-sm text-gray-900">
                    ₺{position.avgBuyPrice.toFixed(2)}
                  </td>
                  <td className="px-6 py-4 text-right text-sm text-gray-900">
                    ₺{position.totalCost.toLocaleString('tr-TR')}
                  </td>
                  <td className="px-6 py-4 text-right text-sm text-gray-900">
                    ₺{position.currentPrice.toFixed(2)}
                  </td>
                  <td className="px-6 py-4 text-right text-sm text-gray-900">
                    ₺{position.currentValue.toLocaleString('tr-TR')}
                  </td>
                  <td className={`px-6 py-4 text-right text-sm ${
                    position.profitLoss >= 0 ? 'text-green-600' : 'text-red-600'
                  }`}>
                    {position.profitLoss >= 0 ? '+' : ''}₺{position.profitLoss.toLocaleString('tr-TR')}
                  </td>
                  <td className={`px-6 py-4 text-right text-sm ${
                    position.profitLoss >= 0 ? 'text-green-600' : 'text-red-600'
                  }`}>
                    {position.profitLoss >= 0 ? '+' : ''}%{position.profitLossPercent.toFixed(2)}
                  </td>
                </tr>
              ))}
            </tbody>
            <tfoot className="bg-gray-50 border-t-2 border-gray-300">
              <tr>
                <td className="px-6 py-4 text-sm text-gray-900">Toplam</td>
                <td className="px-6 py-4"></td>
                <td className="px-6 py-4"></td>
                <td className="px-6 py-4 text-right text-sm text-gray-900">
                  ₺{totalCost.toLocaleString('tr-TR')}
                </td>
                <td className="px-6 py-4"></td>
                <td className="px-6 py-4 text-right text-sm text-gray-900">
                  ₺{totalCurrentValue.toLocaleString('tr-TR')}
                </td>
                <td className={`px-6 py-4 text-right text-sm ${
                  totalProfitLoss >= 0 ? 'text-green-600' : 'text-red-600'
                }`}>
                  {totalProfitLoss >= 0 ? '+' : ''}₺{totalProfitLoss.toLocaleString('tr-TR')}
                </td>
                <td className={`px-6 py-4 text-right text-sm ${
                  totalProfitLoss >= 0 ? 'text-green-600' : 'text-red-600'
                }`}>
                  {totalProfitLoss >= 0 ? '+' : ''}%{totalProfitLossPercent.toFixed(2)}
                </td>
              </tr>
            </tfoot>
          </table>
        </div>
      </div>

      {/* Portfolio Distribution Chart */}
      <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
        <h3 className="text-gray-900 mb-6">Portföy Dağılımı</h3>
        <div className="space-y-4">
          {portfolioPositions.map((position) => {
            const percentage = (position.currentValue / totalCurrentValue) * 100;
            
            return (
              <div key={position.assetId}>
                <div className="flex items-center justify-between mb-2">
                  <div className="flex items-center gap-3">
                    <span className="text-sm text-gray-900">{position.assetId}</span>
                    <span className="text-xs text-gray-500">{position.assetName}</span>
                  </div>
                  <div className="text-right">
                    <span className="text-sm text-gray-900">%{percentage.toFixed(2)}</span>
                    <span className="text-xs text-gray-500 ml-2">
                      ₺{position.currentValue.toLocaleString('tr-TR')}
                    </span>
                  </div>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-2">
                  <div
                    className="bg-gradient-to-r from-blue-500 to-indigo-600 h-2 rounded-full transition-all"
                    style={{ width: `${percentage}%` }}
                  />
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}
