import { useState } from 'react';
import { Briefcase, Wallet, PieChart, User, MessageSquare, LogOut } from 'lucide-react';
import { ClientAssetsTab } from './broker/ClientAssetsTab';
import { FundsStatusTab } from './broker/FundsStatusTab';
import { BrokerProfileTab } from './broker/BrokerProfileTab';
import { TeamChatTab } from './broker/TeamChatTab';

interface BrokerDashboardProps {
  onLogout: () => void;
}

type TabType = 'clients' | 'funds' | 'profile' | 'team';

export function BrokerDashboard({ onLogout }: BrokerDashboardProps) {
  const [activeTab, setActiveTab] = useState<TabType>('clients');

  const tabs = [
    { id: 'clients' as TabType, label: 'Müşteri Varlıkları', icon: Wallet },
    { id: 'funds' as TabType, label: 'Fonlar', icon: PieChart },
    { id: 'profile' as TabType, label: 'Profil', icon: User },
    { id: 'team' as TabType, label: 'Ekip Mesajları', icon: MessageSquare },
  ];

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white border-b border-gray-200 sticky top-0 z-10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center gap-3">
              <Briefcase className="w-8 h-8 text-indigo-600" />
              <div>
                <h1 className="text-gray-900">Portföy Yönetimi</h1>
                <p className="text-sm text-gray-500">Broker Paneli</p>
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
      <div className="bg-white border-b border-gray-200">
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
                      ? 'border-indigo-600 text-indigo-600'
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
        {activeTab === 'clients' && <ClientAssetsTab />}
        {activeTab === 'funds' && <FundsStatusTab />}
        {activeTab === 'profile' && <BrokerProfileTab />}
        {activeTab === 'team' && <TeamChatTab />}
      </main>
    </div>
  );
}
