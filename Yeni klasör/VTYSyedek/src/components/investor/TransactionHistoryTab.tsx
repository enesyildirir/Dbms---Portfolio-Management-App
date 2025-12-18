import { useState } from 'react';
import { Calendar, Filter, TrendingUp, TrendingDown, Download } from 'lucide-react';

interface TransactionHistoryTabProps {
  investorId: number;
}

export function TransactionHistoryTab({ investorId }: TransactionHistoryTabProps) {
  const [selectedAccount, setSelectedAccount] = useState('all');
  const [selectedType, setSelectedType] = useState('all');
  const [dateFrom, setDateFrom] = useState('');
  const [dateTo, setDateTo] = useState('');

  // Mock data - gerçek sistemde veritabanından gelecek
  const accounts = [
    { id: 'HSP-2022-001', name: 'Yatırım Hesabı 1' },
  ];

  const transactions = [
    {
      id: 1,
      date: '2025-12-05 14:30:00',
      accountId: 'HSP-2022-001',
      asset: 'THYAO',
      assetName: 'Türk Hava Yolları',
      type: 'ALIS',
      amount: 1000,
      unitPrice: 245.50,
      total: 245500,
      commission: 2455,
      netTotal: 247955,
    },
    {
      id: 2,
      date: '2025-12-03 11:20:00',
      accountId: 'HSP-2022-001',
      asset: 'GARAN',
      assetName: 'Garanti Bankası',
      type: 'SATIS',
      amount: 500,
      unitPrice: 38.75,
      total: 19375,
      commission: 193.75,
      netTotal: 19181.25,
    },
    {
      id: 3,
      date: '2025-12-01 09:15:00',
      accountId: 'HSP-2022-001',
      asset: 'AKBNK',
      assetName: 'Akbank',
      type: 'ALIS',
      amount: 2000,
      unitPrice: 52.30,
      total: 104600,
      commission: 1046,
      netTotal: 105646,
    },
    {
      id: 4,
      date: '2025-11-28 16:45:00',
      accountId: 'HSP-2022-001',
      asset: 'EREGL',
      assetName: 'Ereğli Demir Çelik',
      type: 'ALIS',
      amount: 1500,
      unitPrice: 48.90,
      total: 73350,
      commission: 733.50,
      netTotal: 74083.50,
    },
    {
      id: 5,
      date: '2025-11-25 10:30:00',
      accountId: 'HSP-2022-001',
      asset: 'KCHOL',
      assetName: 'Koç Holding',
      type: 'SATIS',
      amount: 300,
      unitPrice: 156.20,
      total: 46860,
      commission: 468.60,
      netTotal: 46391.40,
    },
    {
      id: 6,
      date: '2025-11-20 14:00:00',
      accountId: 'HSP-2022-001',
      asset: 'SAHOL',
      assetName: 'Sabancı Holding',
      type: 'ALIS',
      amount: 1200,
      unitPrice: 78.40,
      total: 94080,
      commission: 940.80,
      netTotal: 95020.80,
    },
  ];

  const filteredTransactions = transactions.filter(t => {
    if (selectedAccount !== 'all' && t.accountId !== selectedAccount) return false;
    if (selectedType !== 'all' && t.type !== selectedType) return false;
    if (dateFrom && new Date(t.date) < new Date(dateFrom)) return false;
    if (dateTo && new Date(t.date) > new Date(dateTo)) return false;
    return true;
  });

  const totalBuy = filteredTransactions
    .filter(t => t.type === 'ALIS')
    .reduce((sum, t) => sum + t.netTotal, 0);

  const totalSell = filteredTransactions
    .filter(t => t.type === 'SATIS')
    .reduce((sum, t) => sum + t.netTotal, 0);

  const totalCommission = filteredTransactions.reduce((sum, t) => sum + t.commission, 0);

  return (
    <div className="space-y-6">
      {/* Summary Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center gap-3 mb-2">
            <div className="w-10 h-10 bg-green-100 rounded-lg flex items-center justify-center">
              <TrendingUp className="w-5 h-5 text-green-600" />
            </div>
            <div>
              <p className="text-sm text-gray-600">Toplam Alış</p>
              <p className="text-gray-900">₺{totalBuy.toLocaleString('tr-TR', { minimumFractionDigits: 2 })}</p>
            </div>
          </div>
        </div>

        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center gap-3 mb-2">
            <div className="w-10 h-10 bg-red-100 rounded-lg flex items-center justify-center">
              <TrendingDown className="w-5 h-5 text-red-600" />
            </div>
            <div>
              <p className="text-sm text-gray-600">Toplam Satış</p>
              <p className="text-gray-900">₺{totalSell.toLocaleString('tr-TR', { minimumFractionDigits: 2 })}</p>
            </div>
          </div>
        </div>

        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center gap-3 mb-2">
            <div className="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center">
              <Calendar className="w-5 h-5 text-blue-600" />
            </div>
            <div>
              <p className="text-sm text-gray-600">Toplam Komisyon</p>
              <p className="text-gray-900">₺{totalCommission.toLocaleString('tr-TR', { minimumFractionDigits: 2 })}</p>
            </div>
          </div>
        </div>
      </div>

      {/* Filters */}
      <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
        <div className="flex items-center gap-2 mb-4">
          <Filter className="w-5 h-5 text-gray-700" />
          <h3 className="text-gray-900">Filtrele</h3>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
          <div>
            <label className="block text-sm text-gray-700 mb-2">Hesap</label>
            <select
              value={selectedAccount}
              onChange={(e) => setSelectedAccount(e.target.value)}
              className="w-full px-3 py-2 bg-gray-50 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none"
            >
              <option value="all">Tüm Hesaplar</option>
              {accounts.map(acc => (
                <option key={acc.id} value={acc.id}>{acc.id}</option>
              ))}
            </select>
          </div>

          <div>
            <label className="block text-sm text-gray-700 mb-2">İşlem Tipi</label>
            <select
              value={selectedType}
              onChange={(e) => setSelectedType(e.target.value)}
              className="w-full px-3 py-2 bg-gray-50 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none"
            >
              <option value="all">Tümü</option>
              <option value="ALIS">Alış</option>
              <option value="SATIS">Satış</option>
            </select>
          </div>

          <div>
            <label className="block text-sm text-gray-700 mb-2">Başlangıç</label>
            <input
              type="date"
              value={dateFrom}
              onChange={(e) => setDateFrom(e.target.value)}
              className="w-full px-3 py-2 bg-gray-50 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none"
            />
          </div>

          <div>
            <label className="block text-sm text-gray-700 mb-2">Bitiş</label>
            <input
              type="date"
              value={dateTo}
              onChange={(e) => setDateTo(e.target.value)}
              className="w-full px-3 py-2 bg-gray-50 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none"
            />
          </div>
        </div>
      </div>

      {/* Transactions Table */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
        <div className="px-6 py-4 border-b border-gray-200 flex items-center justify-between">
          <h3 className="text-gray-900">İşlem Geçmişi ({filteredTransactions.length} kayıt)</h3>
          <button className="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors text-sm">
            <Download className="w-4 h-4" />
            <span>Dışa Aktar</span>
          </button>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full">
            <thead className="bg-gray-50">
              <tr>
                <th className="px-6 py-3 text-left text-xs text-gray-600">Tarih & Saat</th>
                <th className="px-6 py-3 text-left text-xs text-gray-600">Varlık</th>
                <th className="px-6 py-3 text-center text-xs text-gray-600">İşlem</th>
                <th className="px-6 py-3 text-right text-xs text-gray-600">Miktar</th>
                <th className="px-6 py-3 text-right text-xs text-gray-600">Birim Fiyat</th>
                <th className="px-6 py-3 text-right text-xs text-gray-600">Tutar</th>
                <th className="px-6 py-3 text-right text-xs text-gray-600">Komisyon</th>
                <th className="px-6 py-3 text-right text-xs text-gray-600">Net Tutar</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200">
              {filteredTransactions.map((transaction) => (
                <tr key={transaction.id} className="hover:bg-gray-50 transition-colors">
                  <td className="px-6 py-4 text-sm text-gray-600 whitespace-nowrap">
                    {new Date(transaction.date).toLocaleString('tr-TR')}
                  </td>
                  <td className="px-6 py-4">
                    <div>
                      <p className="text-sm text-gray-900">{transaction.asset}</p>
                      <p className="text-xs text-gray-500">{transaction.assetName}</p>
                    </div>
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
                  <td className="px-6 py-4 text-right text-sm text-gray-900">
                    {transaction.amount.toLocaleString('tr-TR')}
                  </td>
                  <td className="px-6 py-4 text-right text-sm text-gray-900">
                    ₺{transaction.unitPrice.toFixed(2)}
                  </td>
                  <td className="px-6 py-4 text-right text-sm text-gray-900">
                    ₺{transaction.total.toLocaleString('tr-TR', { minimumFractionDigits: 2 })}
                  </td>
                  <td className="px-6 py-4 text-right text-sm text-gray-600">
                    ₺{transaction.commission.toLocaleString('tr-TR', { minimumFractionDigits: 2 })}
                  </td>
                  <td className="px-6 py-4 text-right text-sm text-gray-900">
                    ₺{transaction.netTotal.toLocaleString('tr-TR', { minimumFractionDigits: 2 })}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {filteredTransactions.length === 0 && (
          <div className="p-12 text-center">
            <Calendar className="w-12 h-12 text-gray-400 mx-auto mb-3" />
            <p className="text-gray-600">İşlem kaydı bulunamadı</p>
          </div>
        )}
      </div>
    </div>
  );
}
