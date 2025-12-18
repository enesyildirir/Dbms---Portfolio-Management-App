import { useState } from 'react';
import { Plus, TrendingUp, TrendingDown, AlertCircle, CheckCircle } from 'lucide-react';

interface NewTransactionTabProps {
  brokerId: number;
}

export function NewTransactionTab({ brokerId }: NewTransactionTabProps) {
  const [selectedAccount, setSelectedAccount] = useState('');
  const [selectedAsset, setSelectedAsset] = useState('');
  const [transactionType, setTransactionType] = useState<'ALIS' | 'SATIS'>('ALIS');
  const [amount, setAmount] = useState('');
  const [unitPrice, setUnitPrice] = useState('');
  const [showSuccess, setShowSuccess] = useState(false);

  // Mock data - gerçek sistemde veritabanından gelecek
  const accounts = [
    { id: 'HSP-2022-001', clientName: 'Ayşe Kaya', balance: 850000 },
    { id: 'HSP-2021-045', clientName: 'Mehmet Özkan', balance: 1250000 },
    { id: 'HSP-2023-012', clientName: 'Zeynep Demir', balance: 450000 },
    { id: 'HSP-2023-078', clientName: 'Zeynep Demir', balance: 320000 },
    { id: 'HSP-2022-089', clientName: 'Ali Yılmaz', balance: 675000 },
  ];

  const assets = [
    { id: 'THYAO', name: 'Türk Hava Yolları', type: 'Hisse', currentPrice: 245.50 },
    { id: 'GARAN', name: 'Garanti Bankası', type: 'Hisse', currentPrice: 38.75 },
    { id: 'AKBNK', name: 'Akbank', type: 'Hisse', currentPrice: 52.30 },
    { id: 'EREGL', name: 'Ereğli Demir Çelik', type: 'Hisse', currentPrice: 48.90 },
    { id: 'KCHOL', name: 'Koç Holding', type: 'Hisse', currentPrice: 156.20 },
    { id: 'SAHOL', name: 'Sabancı Holding', type: 'Hisse', currentPrice: 78.40 },
    { id: 'PETKM', name: 'Petkim', type: 'Hisse', currentPrice: 34.60 },
    { id: 'TUPRS', name: 'Tüpraş', type: 'Hisse', currentPrice: 189.30 },
  ];

  const calculateTotal = () => {
    const qty = parseFloat(amount) || 0;
    const price = parseFloat(unitPrice) || 0;
    return qty * price;
  };

  const calculateCommission = () => {
    const total = calculateTotal();
    const commissionRate = 0.01; // %1 komisyon
    return total * commissionRate;
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (!selectedAccount || !selectedAsset || !amount || !unitPrice) {
      alert('Lütfen tüm alanları doldurun!');
      return;
    }

    // Mock submission - gerçek sistemde veritabanına kaydedilecek
    const transaction = {
      accountId: selectedAccount,
      assetId: selectedAsset,
      type: transactionType,
      amount: parseFloat(amount),
      unitPrice: parseFloat(unitPrice),
      total: calculateTotal(),
      commission: calculateCommission(),
      date: new Date().toISOString(),
      brokerId: brokerId,
    };

    console.log('Yeni İşlem:', transaction);
    
    setShowSuccess(true);
    setTimeout(() => {
      setShowSuccess(false);
      // Reset form
      setSelectedAccount('');
      setSelectedAsset('');
      setTransactionType('ALIS');
      setAmount('');
      setUnitPrice('');
    }, 2000);
  };

  const selectedAssetData = assets.find(a => a.id === selectedAsset);
  const selectedAccountData = accounts.find(a => a.id === selectedAccount);

  return (
    <div className="max-w-4xl mx-auto space-y-6">
      {/* Success Message */}
      {showSuccess && (
        <div className="bg-green-50 border border-green-200 rounded-xl p-4 flex items-center gap-3">
          <CheckCircle className="w-6 h-6 text-green-600" />
          <div>
            <p className="text-green-900">İşlem başarıyla kaydedildi!</p>
            <p className="text-sm text-green-700">İşlem detayları müşteriye bildirildi.</p>
          </div>
        </div>
      )}

      {/* Form Card */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
        <div className="bg-gradient-to-r from-indigo-600 to-purple-600 px-6 py-4">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-white/20 backdrop-blur-sm rounded-lg flex items-center justify-center">
              <Plus className="w-6 h-6 text-white" />
            </div>
            <div>
              <h2 className="text-white">Yeni İşlem Girişi</h2>
              <p className="text-indigo-100 text-sm">Müşteri adına alım veya satım işlemi kaydedin</p>
            </div>
          </div>
        </div>

        <form onSubmit={handleSubmit} className="p-6 space-y-6">
          {/* Account Selection */}
          <div>
            <label className="block text-sm text-gray-700 mb-2">
              Hesap Seçimi <span className="text-red-500">*</span>
            </label>
            <select
              value={selectedAccount}
              onChange={(e) => setSelectedAccount(e.target.value)}
              className="w-full px-4 py-3 bg-gray-50 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent outline-none"
              required
            >
              <option value="">Hesap seçiniz...</option>
              {accounts.map((account) => (
                <option key={account.id} value={account.id}>
                  {account.id} - {account.clientName} (Bakiye: ₺{account.balance.toLocaleString('tr-TR')})
                </option>
              ))}
            </select>
          </div>

          {/* Transaction Type */}
          <div>
            <label className="block text-sm text-gray-700 mb-2">
              İşlem Tipi <span className="text-red-500">*</span>
            </label>
            <div className="grid grid-cols-2 gap-4">
              <button
                type="button"
                onClick={() => setTransactionType('ALIS')}
                className={`p-4 rounded-lg border-2 transition-all ${
                  transactionType === 'ALIS'
                    ? 'border-green-500 bg-green-50'
                    : 'border-gray-200 bg-white hover:border-gray-300'
                }`}
              >
                <div className="flex items-center justify-center gap-2 mb-2">
                  <TrendingUp className={`w-5 h-5 ${transactionType === 'ALIS' ? 'text-green-600' : 'text-gray-400'}`} />
                  <span className={transactionType === 'ALIS' ? 'text-green-900' : 'text-gray-700'}>
                    Alış
                  </span>
                </div>
              </button>

              <button
                type="button"
                onClick={() => setTransactionType('SATIS')}
                className={`p-4 rounded-lg border-2 transition-all ${
                  transactionType === 'SATIS'
                    ? 'border-red-500 bg-red-50'
                    : 'border-gray-200 bg-white hover:border-gray-300'
                }`}
              >
                <div className="flex items-center justify-center gap-2 mb-2">
                  <TrendingDown className={`w-5 h-5 ${transactionType === 'SATIS' ? 'text-red-600' : 'text-gray-400'}`} />
                  <span className={transactionType === 'SATIS' ? 'text-red-900' : 'text-gray-700'}>
                    Satış
                  </span>
                </div>
              </button>
            </div>
          </div>

          {/* Asset Selection */}
          <div>
            <label className="block text-sm text-gray-700 mb-2">
              Varlık Seçimi <span className="text-red-500">*</span>
            </label>
            <select
              value={selectedAsset}
              onChange={(e) => {
                setSelectedAsset(e.target.value);
                const asset = assets.find(a => a.id === e.target.value);
                if (asset) {
                  setUnitPrice(asset.currentPrice.toString());
                }
              }}
              className="w-full px-4 py-3 bg-gray-50 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent outline-none"
              required
            >
              <option value="">Varlık seçiniz...</option>
              {assets.map((asset) => (
                <option key={asset.id} value={asset.id}>
                  {asset.id} - {asset.name} ({asset.type}) - ₺{asset.currentPrice.toFixed(2)}
                </option>
              ))}
            </select>
            {selectedAssetData && (
              <div className="mt-2 p-3 bg-blue-50 rounded-lg">
                <p className="text-sm text-blue-900">
                  Güncel Fiyat: <span className="font-medium">₺{selectedAssetData.currentPrice.toFixed(2)}</span>
                </p>
              </div>
            )}
          </div>

          {/* Amount and Price */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label className="block text-sm text-gray-700 mb-2">
                Miktar (Adet) <span className="text-red-500">*</span>
              </label>
              <input
                type="number"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                placeholder="Örn: 1000"
                min="1"
                step="1"
                className="w-full px-4 py-3 bg-gray-50 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent outline-none"
                required
              />
            </div>

            <div>
              <label className="block text-sm text-gray-700 mb-2">
                Birim Fiyat (₺) <span className="text-red-500">*</span>
              </label>
              <input
                type="number"
                value={unitPrice}
                onChange={(e) => setUnitPrice(e.target.value)}
                placeholder="Örn: 245.50"
                min="0.01"
                step="0.01"
                className="w-full px-4 py-3 bg-gray-50 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent outline-none"
                required
              />
            </div>
          </div>

          {/* Summary */}
          {amount && unitPrice && (
            <div className="bg-gray-50 rounded-lg p-6 border border-gray-200">
              <h4 className="text-gray-900 mb-4">İşlem Özeti</h4>
              <div className="space-y-3">
                <div className="flex items-center justify-between">
                  <span className="text-gray-600">Toplam Tutar:</span>
                  <span className="text-gray-900">₺{calculateTotal().toLocaleString('tr-TR', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</span>
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-gray-600">Komisyon (%1):</span>
                  <span className="text-gray-900">₺{calculateCommission().toLocaleString('tr-TR', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</span>
                </div>
                <div className="flex items-center justify-between pt-3 border-t border-gray-300">
                  <span className="text-gray-900">Net Tutar:</span>
                  <span className="text-gray-900">
                    ₺{(calculateTotal() + (transactionType === 'ALIS' ? calculateCommission() : -calculateCommission())).toLocaleString('tr-TR', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
                  </span>
                </div>
              </div>
            </div>
          )}

          {/* Warning */}
          {selectedAccountData && calculateTotal() > selectedAccountData.balance && transactionType === 'ALIS' && (
            <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4 flex items-start gap-3">
              <AlertCircle className="w-5 h-5 text-yellow-600 flex-shrink-0 mt-0.5" />
              <div>
                <p className="text-yellow-900">Yetersiz Bakiye</p>
                <p className="text-sm text-yellow-700">
                  Hesap bakiyesi (₺{selectedAccountData.balance.toLocaleString('tr-TR')}) işlem tutarından düşük.
                </p>
              </div>
            </div>
          )}

          {/* Submit Button */}
          <button
            type="submit"
            className="w-full bg-gradient-to-r from-indigo-600 to-purple-600 text-white py-4 rounded-lg hover:from-indigo-700 hover:to-purple-700 transition-all shadow-lg hover:shadow-xl"
          >
            İşlemi Kaydet
          </button>
        </form>
      </div>

      {/* Info Card */}
      <div className="bg-blue-50 border border-blue-200 rounded-xl p-6">
        <div className="flex items-start gap-3">
          <AlertCircle className="w-6 h-6 text-blue-600 flex-shrink-0 mt-1" />
          <div>
            <h4 className="text-blue-900 mb-2">Önemli Bilgiler</h4>
            <ul className="text-sm text-blue-700 space-y-1">
              <li>• İşlem kaydedildikten sonra müşteriye otomatik bildirim gönderilir.</li>
              <li>• Komisyon oranı varsayılan olarak %1 olarak hesaplanmaktadır.</li>
              <li>• Satış işlemlerinde portföyde yeterli varlık olduğundan emin olun.</li>
              <li>• Tüm işlemler sistem tarafından loglanır ve denetlenebilir.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}
