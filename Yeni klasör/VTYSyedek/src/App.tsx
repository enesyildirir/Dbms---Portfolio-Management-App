import { useState } from 'react';
import { LoginScreen } from './components/LoginScreen';
import { BrokerInterface } from './components/broker/BrokerInterface';
import { InvestorInterface } from './components/investor/InvestorInterface';

type UserRole = 'broker' | 'investor' | null;

interface User {
  id: number;
  name: string;
  surname: string;
  email: string;
  role: 'broker' | 'investor';
}

export default function App() {
  const [user, setUser] = useState<User | null>(null);

  const handleLogin = (userData: User) => {
    setUser(userData);
  };

  const handleLogout = () => {
    setUser(null);
  };

  if (!user) {
    return <LoginScreen onLogin={handleLogin} />;
  }

  return (
    <>
      {user.role === 'broker' && <BrokerInterface user={user} onLogout={handleLogout} />}
      {user.role === 'investor' && <InvestorInterface user={user} onLogout={handleLogout} />}
    </>
  );
}
