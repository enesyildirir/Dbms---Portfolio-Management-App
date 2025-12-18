import { DollarSign, Calendar, Shield, User, CreditCard } from 'lucide-react';

interface AccountsTabProps {
  investorId: number;
}

export function AccountsTab({ investorId }: AccountsTabProps) {
  // Mock data - gerçek sistemde veritabanından gelecek
  const investorData = {
    name: 'Ayşe Kaya',
    email: 'ayse.kaya@email.com',
    phone: '+90 532 111 22 33',
    riskProfile: {
      name: 'Dengeli',
      description: 'Orta düzey risk toleransı ile dengeli portföy yapısı',
      maxStockRatio: 60,
    },
    broker: {
      name: 'Mehmet Yıldırım',
      phone: '+90 532 987 65 43',
      email: 'mehmet.yildirim@broker.com',
    },
  };

  const accounts = [
    {
      accountId: 'HSP-2022-001',
      balance: 850000,
      openDate: '2022-03-15',
      commissionPlan: {
        name: 'Standart Plan',
        minCommission: 50,
        rate: 1.0,
      },
    },
  ];

  const getRiskColor = (riskName: string) => {
    switch (riskName) {
      case 'Agresif':
        return 'bg-red-100 text-red-800 border-red-200';
      case 'Dengeli':
        return 'bg-yellow-100 text-yellow-800 border-yellow-200';
      case 'Muhafazakar':
        return 'bg-green-100 text-green-800 border-green-200';
      default:
        return 'bg-gray-100 text-gray-800 border-gray-200';
    }
  };

  const totalBalance = accounts.reduce((sum, acc) => sum + acc.balance, 0);

  return (
    <div className="space-y-6">
      {/* Total Balance Card */}
      <div className="bg-gradient-to-br from-blue-600 to-indigo-600 rounded-2xl p-8 text-white shadow-xl">
        <p className="text-blue-100 mb-2">Toplam Bakiye</p>
        <h2 className="text-white mb-6">₺{totalBalance.toLocaleString('tr-TR')}</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="bg-white/10 backdrop-blur-sm rounded-lg p-4">
            <p className="text-blue-100 text-sm mb-1">Hesap Sayısı</p>
            <p className="text-white text-xl">{accounts.length}</p>
          </div>
          <div className="bg-white/10 backdrop-blur-sm rounded-lg p-4">
            <p className="text-blue-100 text-sm mb-1">Risk Profili</p>
            <p className="text-white text-xl">{investorData.riskProfile.name}</p>
          </div>
          <div className="bg-white/10 backdrop-blur-sm rounded-lg p-4">
            <p className="text-blue-100 text-sm mb-1">Sorumlu Broker</p>
            <p className="text-white text-xl">{investorData.broker.name.split(' ')[0]}</p>
          </div>
        </div>
      </div>

      {/* Accounts List */}
      <div>
        <h3 className="text-gray-900 mb-4">Hesaplarım</h3>
        <div className="space-y-4">
          {accounts.map((account) => (
            <div key={account.accountId} className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
              <div className="flex items-start justify-between mb-6">
                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center">
                    <CreditCard className="w-6 h-6 text-blue-600" />
                  </div>
                  <div>
                    <h4 className="text-gray-900 mb-1">Hesap No: {account.accountId}</h4>
                    <p className="text-sm text-gray-600">Yatırım Hesabı</p>
                  </div>
                </div>
                <div className="text-right">
                  <p className="text-sm text-gray-600 mb-1">Bakiye</p>
                  <p className="text-gray-900">₺{account.balance.toLocaleString('tr-TR')}</p>
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div className="bg-gray-50 rounded-lg p-4">
                  <div className="flex items-center gap-2 mb-2">
                    <Calendar className="w-4 h-4 text-gray-600" />
                    <p className="text-sm text-gray-600">Açılış Tarihi</p>
                  </div>
                  <p className="text-gray-900">{account.openDate}</p>
                </div>

                <div className="bg-gray-50 rounded-lg p-4">
                  <div className="flex items-center gap-2 mb-2">
                    <DollarSign className="w-4 h-4 text-gray-600" />
                    <p className="text-sm text-gray-600">Komisyon Planı</p>
                  </div>
                  <p className="text-gray-900">{account.commissionPlan.name}</p>
                  <p className="text-xs text-gray-500">Min: ₺{account.commissionPlan.minCommission} - %{account.commissionPlan.rate}</p>
                </div>

                <div className="bg-gray-50 rounded-lg p-4">
                  <div className="flex items-center gap-2 mb-2">
                    <Shield className="w-4 h-4 text-gray-600" />
                    <p className="text-sm text-gray-600">Durum</p>
                  </div>
                  <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs bg-green-100 text-green-800">
                    Aktif
                  </span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Risk Profile */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
        <div className="flex items-center gap-2 mb-4">
          <Shield className="w-5 h-5 text-gray-700" />
          <h3 className="text-gray-900">Risk Profili</h3>
        </div>
        <div className="bg-gray-50 rounded-lg p-6 border border-gray-200">
          <div className="flex items-center justify-between mb-4">
            <span className={`inline-flex items-center px-4 py-2 rounded-full border ${getRiskColor(investorData.riskProfile.name)}`}>
              {investorData.riskProfile.name}
            </span>
            <div className="text-right">
              <p className="text-sm text-gray-600">Maksimum Hisse Oranı</p>
              <p className="text-gray-900">%{investorData.riskProfile.maxStockRatio}</p>
            </div>
          </div>
          <p className="text-gray-700">{investorData.riskProfile.description}</p>
        </div>
      </div>

      {/* Broker Info */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
        <div className="flex items-center gap-2 mb-4">
          <User className="w-5 h-5 text-gray-700" />
          <h3 className="text-gray-900">Sorumlu Broker</h3>
        </div>
        <div className="flex items-start gap-4">
          <div className="w-14 h-14 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-xl flex items-center justify-center text-white flex-shrink-0">
            <span className="text-xl">{investorData.broker.name.charAt(0)}</span>
          </div>
          <div className="flex-1">
            <h4 className="text-gray-900 mb-3">{investorData.broker.name}</h4>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              <div className="bg-gray-50 rounded-lg p-3">
                <p className="text-xs text-gray-600 mb-1">Telefon</p>
                <p className="text-sm text-gray-900">{investorData.broker.phone}</p>
              </div>
              <div className="bg-gray-50 rounded-lg p-3">
                <p className="text-xs text-gray-600 mb-1">E-posta</p>
                <p className="text-sm text-gray-900">{investorData.broker.email}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
