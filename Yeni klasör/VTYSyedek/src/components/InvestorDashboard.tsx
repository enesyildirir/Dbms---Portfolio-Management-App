import { useState } from 'react';
import { TrendingUp, Users, PieChart, User, LogOut } from 'lucide-react';
import { InvestmentsTab } from './investor/InvestmentsTab';
import { BrokersTab } from './investor/BrokersTab';
import { FundsTab } from './investor/FundsTab';
import { ProfileTab } from './investor/ProfileTab';

interface InvestorDashboardProps {
  onLogout: () => void;
}

type TabType = 'investments' | 'brokers' | 'funds' | 'profile';

export function InvestorDashboard({ onLogout }: InvestorDashboardProps) {
  const [activeTab, setActiveTab] = useState<TabType>('investments');

  const tabs = [
    { id: 'investments' as TabType, label: 'Yatırımlarım', icon: TrendingUp },
    { id: 'brokers' as TabType, label: 'Brokerlar', icon: Users },
    { id: 'funds' as TabType, label: 'Fonlar', icon: PieChart },
    { id: 'profile' as TabType, label: 'Profil', icon: User },
  ];

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white border-b border-gray-200 sticky top-0 z-10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center gap-3">
              <TrendingUp className="w-8 h-8 text-blue-600" />
              <div>
                <h1 className="text-gray-900">Portföy Yönetimi</h1>
                <p className="text-sm text-gray-500">Yatırımcı Paneli</p>
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
        {activeTab === 'investments' && <InvestmentsTab />}
        {activeTab === 'brokers' && <BrokersTab />}
        {activeTab === 'funds' && <FundsTab />}
        {activeTab === 'profile' && <ProfileTab />}
      </main>
    </div>
  );
}
