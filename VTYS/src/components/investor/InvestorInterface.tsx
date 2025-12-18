import { useState } from 'react';
import { Wallet, Receipt, PieChart, LogOut } from 'lucide-react';
import { AccountsTab } from './AccountsTab';
import { TransactionHistoryTab } from './TransactionHistoryTab';
import { PortfolioTab } from './PortfolioTab';

interface User {
  id: number;
  name: string;
  surname: string;
  email: string;
  role: 'broker' | 'investor';
}

interface InvestorInterfaceProps {
  user: User;
  onLogout: () => void;
}

type TabType = 'accounts' | 'history' | 'portfolio';

export function InvestorInterface({ user, onLogout }: InvestorInterfaceProps) {
  const [activeTab, setActiveTab] = useState<TabType>('accounts');

  const tabs = [
    { id: 'accounts' as TabType, label: 'Hesaplarım ve Bakiye', icon: Wallet },
    { id: 'history' as TabType, label: 'İşlem Geçmişi', icon: Receipt },
    { id: 'portfolio' as TabType, label: 'Portföy Durumu', icon: PieChart },
  ];

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white border-b border-gray-200 sticky top-0 z-10 shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-gradient-to-br from-blue-600 to-indigo-600 rounded-xl flex items-center justify-center">
                <Wallet className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className="text-gray-900">Yatırımcı Paneli</h1>
                <p className="text-sm text-gray-500">{user.name} {user.surname}</p>
              </div>
            </div>
            <button
              onClick={onLogout}
              className="flex items-center gap-2 px-4 py-2 text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-lg transition-colors"
            >
              <LogOut className="w-5 h-5" />
              <span>Çıkış</span>
            </button>
          </div>
        </div>
      </header>

      {/* Tabs Navigation */}
      <div className="bg-white border-b border-gray-200 shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <nav className="flex gap-8 overflow-x-auto">
            {tabs.map((tab) => {
              const Icon = tab.icon;
              return (
                <button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id)}
                  className={`flex items-center gap-2 py-4 px-2 border-b-2 transition-colors whitespace-nowrap ${
                    activeTab === tab.id
                      ? 'border-blue-600 text-blue-600'
                      : 'border-transparent text-gray-500 hover:text-gray-700'
                  }`}
                >
                  <Icon className="w-5 h-5" />
                  <span>{tab.label}</span>
                </button>
              );
            })}
          </nav>
        </div>
      </div>

      {/* Tab Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {activeTab === 'accounts' && <AccountsTab investorId={user.id} />}
        {activeTab === 'history' && <TransactionHistoryTab investorId={user.id} />}
        {activeTab === 'portfolio' && <PortfolioTab investorId={user.id} />}
      </main>
    </div>
  );
}
