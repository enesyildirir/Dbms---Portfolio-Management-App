import { useState } from 'react';
import { Search, Phone, Mail, DollarSign, Shield, TrendingUp, User, X, ChevronRight } from 'lucide-react';

interface ClientManagementTabProps {
  brokerId: number;
}

export function ClientManagementTab({ brokerId }: ClientManagementTabProps) {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedClient, setSelectedClient] = useState<number | null>(null);
  const [detailModalClient, setDetailModalClient] = useState<number | null>(null);

  // Mock data - gerçek sistemde veritabanından gelecek
  const clients = [
    {
      id: 1,
      name: 'Ayşe Kaya',
      phone: '+90 532 111 22 33',
      email: 'ayse.kaya@email.com',
      accounts: [
        {
          accountId: 'HSP-2022-001',
          balance: 850000,
          openDate: '2022-03-15',
          commissionPlan: 'Standart Plan',
          minCommission: 50,
        },
      ],
      riskProfile: {
        name: 'Dengeli',
        maxStockRatio: 60,
        description: 'Orta düzey risk toleransı',
      },
    },
    {
      id: 2,
      name: 'Mehmet Özkan',
      phone: '+90 532 222 33 44',
      email: 'mehmet.ozkan@email.com',
      accounts: [
        {
          accountId: 'HSP-2021-045',
          balance: 1250000,
          openDate: '2021-11-20',
          commissionPlan: 'Premium Plan',
          minCommission: 100,
        },
      ],
      riskProfile: {
        name: 'Agresif',
        maxStockRatio: 90,
        description: 'Yüksek risk toleransı',
      },
    },
    {
      id: 3,
      name: 'Zeynep Demir',
      phone: '+90 532 333 44 55',
      email: 'zeynep.demir@email.com',
      accounts: [
        {
          accountId: 'HSP-2023-012',
          balance: 450000,
          openDate: '2023-01-10',
          commissionPlan: 'Standart Plan',
          minCommission: 50,
        },
        {
          accountId: 'HSP-2023-078',
          balance: 320000,
          openDate: '2023-06-22',
          commissionPlan: 'Standart Plan',
          minCommission: 50,
        },
      ],
      riskProfile: {
        name: 'Muhafazakar',
        maxStockRatio: 30,
        description: 'Düşük risk toleransı',
      },
    },
    {
      id: 4,
      name: 'Ali Yılmaz',
      phone: '+90 532 444 55 66',
      email: 'ali.yilmaz@email.com',
      accounts: [
        {
          accountId: 'HSP-2022-089',
          balance: 675000,
          openDate: '2022-08-05',
          commissionPlan: 'Premium Plan',
          minCommission: 100,
        },
      ],
      riskProfile: {
        name: 'Dengeli',
        maxStockRatio: 60,
        description: 'Orta düzey risk toleransı',
      },
    },
  ];

  const filteredClients = clients.filter(client =>
    client.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
    client.email.toLowerCase().includes(searchQuery.toLowerCase())
  );

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

  const detailClient = detailModalClient ? clients.find(c => c.id === detailModalClient) : null;

  return (
    <div className="space-y-6">
      {/* Detail Modal */}
      {detailModalClient && detailClient && (
        <div className="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl shadow-2xl max-w-3xl w-full max-h-[90vh] overflow-y-auto">
            {/* Modal Header */}
            <div className="sticky top-0 bg-gradient-to-r from-indigo-600 to-purple-600 px-6 py-4 flex items-center justify-between">
              <div className="flex items-center gap-3">
                <div className="w-12 h-12 bg-white/20 backdrop-blur-sm rounded-xl flex items-center justify-center text-white">
                  <span className="text-xl">{detailClient.name.charAt(0)}</span>
                </div>
                <div>
                  <h3 className="text-white">Müşteri Detayları</h3>
                  <p className="text-indigo-100 text-sm">{detailClient.name}</p>
                </div>
              </div>
              <button
                onClick={() => setDetailModalClient(null)}
                className="text-white hover:bg-white/20 p-2 rounded-lg transition-colors"
              >
                <X className="w-6 h-6" />
              </button>
            </div>

            {/* Modal Content */}
            <div className="p-6 space-y-6">
              {/* Contact Info */}
              <div>
                <h4 className="text-gray-900 mb-3">İletişim Bilgileri</h4>
                <div className="bg-gray-50 rounded-lg p-4 space-y-3">
                  <div className="flex items-center gap-3">
                    <Phone className="w-5 h-5 text-gray-600" />
                    <div>
                      <p className="text-xs text-gray-500">Telefon</p>
                      <p className="text-gray-900">{detailClient.phone}</p>
                    </div>
                  </div>
                  <div className="flex items-center gap-3">
                    <Mail className="w-5 h-5 text-gray-600" />
                    <div>
                      <p className="text-xs text-gray-500">E-posta</p>
                      <p className="text-gray-900">{detailClient.email}</p>
                    </div>
                  </div>
                </div>
              </div>

              {/* Risk Profile */}
              <div>
                <h4 className="text-gray-900 mb-3">Risk Profili</h4>
                <div className="bg-gray-50 rounded-lg p-4">
                  <div className="flex items-center justify-between mb-3">
                    <span className={`inline-flex items-center px-3 py-1 rounded-full text-sm border ${getRiskColor(detailClient.riskProfile.name)}`}>
                      {detailClient.riskProfile.name}
                    </span>
                    <span className="text-sm text-gray-600">
                      Max Hisse Oranı: <span className="text-gray-900">%{detailClient.riskProfile.maxStockRatio}</span>
                    </span>
                  </div>
                  <p className="text-sm text-gray-700">{detailClient.riskProfile.description}</p>
                </div>
              </div>

              {/* Accounts */}
              <div>
                <h4 className="text-gray-900 mb-3">Hesaplar ({detailClient.accounts.length})</h4>
                <div className="space-y-3">
                  {detailClient.accounts.map((account, index) => (
                    <div key={index} className="bg-gray-50 rounded-lg p-4 border border-gray-200">
                      <div className="grid grid-cols-2 gap-4 mb-3">
                        <div>
                          <p className="text-xs text-gray-500 mb-1">Hesap No</p>
                          <p className="text-sm text-gray-900">{account.accountId}</p>
                        </div>
                        <div className="text-right">
                          <p className="text-xs text-gray-500 mb-1">Bakiye</p>
                          <p className="text-sm text-gray-900">₺{account.balance.toLocaleString('tr-TR')}</p>
                        </div>
                      </div>
                      <div className="grid grid-cols-2 gap-4">
                        <div>
                          <p className="text-xs text-gray-500 mb-1">Açılış Tarihi</p>
                          <p className="text-sm text-gray-900">{account.openDate}</p>
                        </div>
                        <div>
                          <p className="text-xs text-gray-500 mb-1">Komisyon Planı</p>
                          <p className="text-sm text-gray-900">{account.commissionPlan}</p>
                          <p className="text-xs text-gray-500">Min: ₺{account.minCommission}</p>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              {/* Actions */}
              <div className="flex gap-3 pt-4 border-t border-gray-200">
                <button className="flex-1 bg-indigo-600 text-white py-3 rounded-lg hover:bg-indigo-700 transition-colors">
                  İşlem Geçmişini Gör
                </button>
                <button className="flex-1 bg-gray-100 text-gray-700 py-3 rounded-lg hover:bg-gray-200 transition-colors">
                  Portföyü Görüntüle
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Search Bar */}
      <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
        <div className="relative">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
          <input
            type="text"
            placeholder="Müşteri ara (isim veya e-posta)..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full pl-10 pr-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent outline-none"
          />
        </div>
      </div>

      {/* Stats Summary */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center gap-3">
            <div className="w-12 h-12 bg-indigo-100 rounded-xl flex items-center justify-center">
              <User className="w-6 h-6 text-indigo-600" />
            </div>
            <div>
              <p className="text-sm text-gray-600">Toplam Müşteri</p>
              <p className="text-gray-900">{clients.length}</p>
            </div>
          </div>
        </div>

        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center gap-3">
            <div className="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center">
              <DollarSign className="w-6 h-6 text-blue-600" />
            </div>
            <div>
              <p className="text-sm text-gray-600">Toplam Hesap</p>
              <p className="text-gray-900">{clients.reduce((sum, c) => sum + c.accounts.length, 0)}</p>
            </div>
          </div>
        </div>

        <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
          <div className="flex items-center gap-3">
            <div className="w-12 h-12 bg-green-100 rounded-xl flex items-center justify-center">
              <TrendingUp className="w-6 h-6 text-green-600" />
            </div>
            <div>
              <p className="text-sm text-gray-600">Toplam Varlık</p>
              <p className="text-gray-900">
                ₺{clients.reduce((sum, c) => 
                  sum + c.accounts.reduce((acc, a) => acc + a.balance, 0), 0
                ).toLocaleString('tr-TR')}
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Clients List */}
      <div className="space-y-4">
        {filteredClients.map((client) => (
          <div key={client.id} className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
            {/* Client Header */}
            <div 
              className="p-6 cursor-pointer hover:bg-gray-50 transition-colors"
              onClick={() => setSelectedClient(selectedClient === client.id ? null : client.id)}
            >
              <div className="flex items-start justify-between">
                <div className="flex items-start gap-4">
                  <div className="w-14 h-14 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-xl flex items-center justify-center text-white flex-shrink-0">
                    <span className="text-xl">{client.name.charAt(0)}</span>
                  </div>
                  <div>
                    <h3 className="text-gray-900 mb-2">{client.name}</h3>
                    <div className="flex flex-col gap-1">
                      <div className="flex items-center gap-2 text-sm text-gray-600">
                        <Phone className="w-4 h-4" />
                        <span>{client.phone}</span>
                      </div>
                      <div className="flex items-center gap-2 text-sm text-gray-600">
                        <Mail className="w-4 h-4" />
                        <span>{client.email}</span>
                      </div>
                    </div>
                  </div>
                </div>
                <div className="text-right">
                  <p className="text-sm text-gray-600 mb-1">{client.accounts.length} Hesap</p>
                  <p className="text-gray-900">
                    ₺{client.accounts.reduce((sum, acc) => sum + acc.balance, 0).toLocaleString('tr-TR')}
                  </p>
                </div>
              </div>
            </div>

            {/* Expanded Details */}
            {selectedClient === client.id && (
              <div className="border-t border-gray-200 bg-gray-50 p-6">
                {/* Risk Profile */}
                <div className="mb-6">
                  <div className="flex items-center gap-2 mb-3">
                    <Shield className="w-5 h-5 text-gray-600" />
                    <h4 className="text-gray-900">Risk Profili</h4>
                  </div>
                  <div className="bg-white rounded-lg p-4 border border-gray-200">
                    <div className="flex items-center justify-between mb-2">
                      <span className={`inline-flex items-center px-3 py-1 rounded-full text-sm border ${getRiskColor(client.riskProfile.name)}`}>
                        {client.riskProfile.name}
                      </span>
                      <span className="text-sm text-gray-600">
                        Max Hisse Oranı: <span className="text-gray-900">%{client.riskProfile.maxStockRatio}</span>
                      </span>
                    </div>
                    <p className="text-sm text-gray-600">{client.riskProfile.description}</p>
                  </div>
                </div>

                {/* Accounts */}
                <div>
                  <div className="flex items-center gap-2 mb-3">
                    <DollarSign className="w-5 h-5 text-gray-600" />
                    <h4 className="text-gray-900">Hesaplar</h4>
                  </div>
                  <div className="space-y-3">
                    {client.accounts.map((account, index) => (
                      <div key={index} className="bg-white rounded-lg p-4 border border-gray-200">
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                          <div>
                            <p className="text-xs text-gray-500 mb-1">Hesap No</p>
                            <p className="text-sm text-gray-900">{account.accountId}</p>
                          </div>
                          <div>
                            <p className="text-xs text-gray-500 mb-1">Bakiye</p>
                            <p className="text-sm text-gray-900">₺{account.balance.toLocaleString('tr-TR')}</p>
                          </div>
                          <div>
                            <p className="text-xs text-gray-500 mb-1">Komisyon Planı</p>
                            <p className="text-sm text-gray-900">{account.commissionPlan}</p>
                            <p className="text-xs text-gray-500">Min: ₺{account.minCommission}</p>
                          </div>
                          <div>
                            <p className="text-xs text-gray-500 mb-1">Açılış Tarihi</p>
                            <p className="text-sm text-gray-900">{account.openDate}</p>
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Action */}
                <div className="pt-4 border-t border-gray-100">
                  <button 
                    onClick={() => setDetailModalClient(client.id)}
                    className="w-full lg:w-auto bg-indigo-600 text-white px-6 py-2 rounded-lg hover:bg-indigo-700 transition-colors flex items-center justify-center gap-2"
                  >
                    <span>Müşteri Detaylarını Görüntüle</span>
                    <ChevronRight className="w-4 h-4" />
                  </button>
                </div>
              </div>
            )}
          </div>
        ))}
      </div>

      {filteredClients.length === 0 && (
        <div className="bg-white rounded-xl p-12 text-center shadow-sm border border-gray-200">
          <User className="w-12 h-12 text-gray-400 mx-auto mb-3" />
          <p className="text-gray-600">Müşteri bulunamadı</p>
        </div>
      )}
    </div>
  );
}