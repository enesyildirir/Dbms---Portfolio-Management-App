import { useState } from 'react';
import { TrendingUp, Lock, User, ChevronDown } from 'lucide-react';

interface User {
  id: number;
  name: string;
  surname: string;
  email: string;
  role: 'broker' | 'investor';
}

interface LoginScreenProps {
  onLogin: (user: User) => void;
}

export function LoginScreen({ onLogin }: LoginScreenProps) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [userType, setUserType] = useState<'broker' | 'investor'>('investor');

  // Mock kullanıcılar (gerçek sistemde veritabanından gelecek)
  const mockUsers = {
    broker: {
      username: 'mehmet.yildirim',
      password: 'broker123',
      data: {
        id: 1,
        name: 'Mehmet',
        surname: 'Yıldırım',
        email: 'mehmet.yildirim@broker.com',
        role: 'broker' as const,
      },
    },
    investor: {
      username: 'ayse.kaya',
      password: 'investor123',
      data: {
        id: 1,
        name: 'Ayşe',
        surname: 'Kaya',
        email: 'ayse.kaya@email.com',
        role: 'investor' as const,
      },
    },
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    const mockUser = mockUsers[userType];
    
    if (username === mockUser.username && password === mockUser.password) {
      onLogin(mockUser.data);
    } else {
      alert('Kullanıcı adı veya şifre hatalı!');
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 flex items-center justify-center p-4">
      <div className="max-w-md w-full">
        {/* Logo & Title */}
        <div className="text-center mb-8">
          <div className="inline-flex items-center justify-center w-16 h-16 bg-gradient-to-br from-blue-600 to-indigo-600 rounded-2xl mb-4 shadow-lg">
            <TrendingUp className="w-8 h-8 text-white" />
          </div>
          <h1 className="text-gray-900 mb-2">Yatırım Takip Sistemi</h1>
          <p className="text-gray-600">Hesabınıza giriş yapın</p>
        </div>

        {/* Login Form */}
        <div className="bg-white rounded-2xl shadow-xl p-8 border border-gray-100">
          <form onSubmit={handleSubmit} className="space-y-6">
            {/* User Type Selection */}
            <div>
              <label className="block text-sm text-gray-700 mb-2">
                Giriş Tipi
              </label>
              <div className="relative">
                <select
                  value={userType}
                  onChange={(e) => setUserType(e.target.value as 'broker' | 'investor')}
                  className="w-full px-4 py-3 pr-10 bg-gray-50 border border-gray-300 rounded-xl appearance-none focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition-all"
                >
                  <option value="investor">Yatırımcı</option>
                  <option value="broker">Broker / Çalışan</option>
                </select>
                <ChevronDown className="absolute right-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400 pointer-events-none" />
              </div>
            </div>

            {/* Username */}
            <div>
              <label className="block text-sm text-gray-700 mb-2">
                Kullanıcı Adı
              </label>
              <div className="relative">
                <User className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                <input
                  type="text"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  placeholder="kullanici.adi"
                  className="w-full pl-10 pr-4 py-3 bg-gray-50 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition-all"
                  required
                />
              </div>
            </div>

            {/* Password */}
            <div>
              <label className="block text-sm text-gray-700 mb-2">
                Şifre
              </label>
              <div className="relative">
                <Lock className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                <input
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="••••••••"
                  className="w-full pl-10 pr-4 py-3 bg-gray-50 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition-all"
                  required
                />
              </div>
            </div>

            {/* Submit Button */}
            <button
              type="submit"
              className="w-full bg-gradient-to-r from-blue-600 to-indigo-600 text-white py-3 rounded-xl hover:from-blue-700 hover:to-indigo-700 transition-all shadow-lg hover:shadow-xl"
            >
              Giriş Yap
            </button>
          </form>

          {/* Demo Credentials */}
          <div className="mt-6 pt-6 border-t border-gray-200">
            <p className="text-xs text-gray-500 mb-3">Demo hesapları:</p>
            <div className="space-y-2 text-xs">
              <div className="bg-blue-50 p-3 rounded-lg">
                <p className="text-blue-900">
                  <span className="opacity-75">Yatırımcı:</span> ayse.kaya / investor123
                </p>
              </div>
              <div className="bg-indigo-50 p-3 rounded-lg">
                <p className="text-indigo-900">
                  <span className="opacity-75">Broker:</span> mehmet.yildirim / broker123
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
