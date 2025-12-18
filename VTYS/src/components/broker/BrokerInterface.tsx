import { useState } from 'react';
import { Briefcase, BarChart3, Users, Plus, LogOut } from 'lucide-react';
import { PerformanceTab } from './PerformanceTab';
import { ClientManagementTab } from './ClientManagementTab';
import { NewTransactionTab } from './NewTransactionTab';

interface User {
  id: number;
  name: string;
  surname: string;
  email: string;
  role: 'broker' | 'investor';
}

interface BrokerInterfaceProps {
  user: User;
  onLogout: () => void;
}

type TabType = 'performance' | 'clients' | 'transaction';

export function BrokerInterface({ user, onLogout }: BrokerInterfaceProps) {
  const [activeTab, setActiveTab] = useState<TabType>('performance');

  const tabs = [
    { id: 'performance' as TabType, label: 'Genel Bakış / Performans', icon: BarChart3 },
    { id: 'clients' as TabType, label: 'Müşteri Yönetimi', icon: Users },
    { id: 'transaction' as TabType, label: 'Yeni İşlem Girişi', icon: Plus },
  ];

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white border-b border-gray-200 sticky top-0 z-10 shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-gradient-to-br from-indigo-600 to-purple-600 rounded-xl flex items-center justify-center">
                <Briefcase className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className="text-gray-900">Broker Paneli</h1>
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
        {activeTab === 'performance' && <PerformanceTab brokerId={user.id} />}
        {activeTab === 'clients' && <ClientManagementTab brokerId={user.id} />}
        {activeTab === 'transaction' && <NewTransactionTab brokerId={user.id} />}
      </main>
    </div>
  );
}
