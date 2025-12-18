import { TrendingUp, Briefcase } from 'lucide-react';

interface LoginSelectionProps {
  onLogin: (type: 'investor' | 'broker') => void;
}

export function LoginSelection({ onLogin }: LoginSelectionProps) {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center p-4">
      <div className="max-w-6xl w-full">
        <div className="text-center mb-12">
          <div className="flex items-center justify-center mb-4">
            <TrendingUp className="w-12 h-12 text-indigo-600" />
          </div>
          <h1 className="text-indigo-900 mb-2">Portföy Yönetim Sistemi</h1>
          <p className="text-gray-600">Lütfen hesap türünüzü seçin</p>
        </div>

        <div className="grid md:grid-cols-2 gap-8">
          {/* Yatırımcı Girişi */}
          <button
            onClick={() => onLogin('investor')}
            className="bg-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-1 text-left"
          >
            <div className="w-16 h-16 bg-blue-100 rounded-xl flex items-center justify-center mb-6">
              <TrendingUp className="w-8 h-8 text-blue-600" />
            </div>
            <h2 className="text-gray-900 mb-3">Yatırımcı Girişi</h2>
            <p className="text-gray-600 mb-6">
              Yatırımlarınızı görüntüleyin, brokerlar ile çalışın ve portföyünüzü yönetin.
            </p>
            <div className="flex items-center text-blue-600">
              <span>Giriş Yap</span>
              <svg className="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
              </svg>
            </div>
          </button>

          {/* Broker Girişi */}
          <button
            onClick={() => onLogin('broker')}
            className="bg-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-1 text-left"
          >
            <div className="w-16 h-16 bg-indigo-100 rounded-xl flex items-center justify-center mb-6">
              <Briefcase className="w-8 h-8 text-indigo-600" />
            </div>
            <h2 className="text-gray-900 mb-3">Broker Girişi</h2>
            <p className="text-gray-600 mb-6">
              Müşterilerinizi yönetin, danışmanlık yapın ve ekibinizle iletişim kurun.
            </p>
            <div className="flex items-center text-indigo-600">
              <span>Giriş Yap</span>
              <svg className="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
              </svg>
            </div>
          </button>
        </div>
      </div>
    </div>
  );
}
