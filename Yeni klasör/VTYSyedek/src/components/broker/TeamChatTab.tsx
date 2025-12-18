import { useState } from 'react';
import { Send, Users, Search, MoreVertical, Paperclip, Smile } from 'lucide-react';

export function TeamChatTab() {
  const [selectedChat, setSelectedChat] = useState(1);
  const [message, setMessage] = useState('');
  const [searchQuery, setSearchQuery] = useState('');

  const teamMembers = [
    {
      id: 1,
      name: 'Ahmet Kaya',
      role: 'Kıdemli Broker',
      lastMessage: 'Enerji fonları hakkında konuşabilir miyiz?',
      time: '10:30',
      unread: 2,
      online: true,
    },
    {
      id: 2,
      name: 'Elif Yılmaz',
      role: 'Portföy Yöneticisi',
      lastMessage: 'Rapor hazır, inceleyebilirsin',
      time: 'Dün',
      unread: 0,
      online: true,
    },
    {
      id: 3,
      name: 'Can Demir',
      role: 'Analist',
      lastMessage: 'Teşekkürler, güzel çalışma olmuş',
      time: 'Pzt',
      unread: 0,
      online: false,
    },
    {
      id: 4,
      name: 'Zeynep Arslan',
      role: 'Müşteri İlişkileri',
      lastMessage: 'Yeni müşteri listesini gönderdim',
      time: 'Cum',
      unread: 1,
      online: true,
    },
  ];

  const messages = [
    {
      id: 1,
      sender: 'Ahmet Kaya',
      content: 'Merhaba, bugün müsait misin?',
      time: '10:15',
      isOwn: false,
    },
    {
      id: 2,
      sender: 'Sen',
      content: 'Evet, müsaitim. Nasıl yardımcı olabilirim?',
      time: '10:18',
      isOwn: true,
    },
    {
      id: 3,
      sender: 'Ahmet Kaya',
      content: 'Enerji fonları hakkında konuşabilir miyiz? Birkaç müşterim bu konuda bilgi istiyor.',
      time: '10:20',
      isOwn: false,
    },
    {
      id: 4,
      sender: 'Sen',
      content: 'Tabii ki, öğleden sonra 14:00\'da toplantı yapalım mı?',
      time: '10:25',
      isOwn: true,
    },
    {
      id: 5,
      sender: 'Ahmet Kaya',
      content: 'Harika, 14:00 benim için uygun. Görüşmek üzere!',
      time: '10:30',
      isOwn: false,
    },
  ];

  const handleSendMessage = () => {
    if (message.trim()) {
      // Mesaj gönderme işlemi
      alert(`Mesaj gönderildi: ${message}`);
      setMessage('');
    }
  };

  const filteredMembers = teamMembers.filter(member =>
    member.name.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <div className="h-[calc(100vh-280px)] flex gap-6">
      {/* Sidebar - Team Members */}
      <div className="w-80 bg-white rounded-xl shadow-sm border border-gray-200 flex flex-col">
        {/* Header */}
        <div className="p-4 border-b border-gray-200">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-gray-900">Ekip Üyeleri</h3>
            <Users className="w-5 h-5 text-gray-600" />
          </div>
          <div className="relative">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
            <input
              type="text"
              placeholder="Ara..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full pl-9 pr-3 py-2 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-indigo-500 focus:border-transparent outline-none"
            />
          </div>
        </div>

        {/* Members List */}
        <div className="flex-1 overflow-y-auto">
          {filteredMembers.map((member) => (
            <button
              key={member.id}
              onClick={() => setSelectedChat(member.id)}
              className={`w-full p-4 flex items-start gap-3 hover:bg-gray-50 transition-colors border-b border-gray-100 ${
                selectedChat === member.id ? 'bg-indigo-50' : ''
              }`}
            >
              <div className="relative flex-shrink-0">
                <div className="w-12 h-12 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-full flex items-center justify-center text-white">
                  <span>{member.name.charAt(0)}</span>
                </div>
                {member.online && (
                  <div className="absolute bottom-0 right-0 w-3 h-3 bg-green-500 border-2 border-white rounded-full" />
                )}
              </div>
              <div className="flex-1 text-left min-w-0">
                <div className="flex items-center justify-between mb-1">
                  <span className="text-gray-900 truncate">{member.name}</span>
                  <span className="text-xs text-gray-500">{member.time}</span>
                </div>
                <p className="text-sm text-gray-600 truncate">{member.role}</p>
                <p className="text-sm text-gray-500 truncate">{member.lastMessage}</p>
              </div>
              {member.unread > 0 && (
                <div className="w-5 h-5 bg-indigo-600 text-white rounded-full flex items-center justify-center text-xs flex-shrink-0">
                  {member.unread}
                </div>
              )}
            </button>
          ))}
        </div>
      </div>

      {/* Chat Area */}
      <div className="flex-1 bg-white rounded-xl shadow-sm border border-gray-200 flex flex-col">
        {/* Chat Header */}
        <div className="p-4 border-b border-gray-200 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="relative">
              <div className="w-10 h-10 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-full flex items-center justify-center text-white">
                <span>{teamMembers.find(m => m.id === selectedChat)?.name.charAt(0)}</span>
              </div>
              {teamMembers.find(m => m.id === selectedChat)?.online && (
                <div className="absolute bottom-0 right-0 w-3 h-3 bg-green-500 border-2 border-white rounded-full" />
              )}
            </div>
            <div>
              <h3 className="text-gray-900">{teamMembers.find(m => m.id === selectedChat)?.name}</h3>
              <p className="text-sm text-gray-600">{teamMembers.find(m => m.id === selectedChat)?.role}</p>
            </div>
          </div>
          <button className="p-2 hover:bg-gray-100 rounded-lg transition-colors">
            <MoreVertical className="w-5 h-5 text-gray-600" />
          </button>
        </div>

        {/* Messages */}
        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {messages.map((msg) => (
            <div key={msg.id} className={`flex ${msg.isOwn ? 'justify-end' : 'justify-start'}`}>
              <div className={`max-w-md ${msg.isOwn ? 'order-2' : 'order-1'}`}>
                {!msg.isOwn && (
                  <p className="text-sm text-gray-600 mb-1 ml-2">{msg.sender}</p>
                )}
                <div
                  className={`px-4 py-2 rounded-2xl ${
                    msg.isOwn
                      ? 'bg-indigo-600 text-white'
                      : 'bg-gray-100 text-gray-900'
                  }`}
                >
                  <p>{msg.content}</p>
                </div>
                <p className={`text-xs text-gray-500 mt-1 ${msg.isOwn ? 'text-right mr-2' : 'ml-2'}`}>
                  {msg.time}
                </p>
              </div>
            </div>
          ))}
        </div>

        {/* Message Input */}
        <div className="p-4 border-t border-gray-200">
          <div className="flex items-end gap-3">
            <button className="p-2 hover:bg-gray-100 rounded-lg transition-colors">
              <Paperclip className="w-5 h-5 text-gray-600" />
            </button>
            <button className="p-2 hover:bg-gray-100 rounded-lg transition-colors">
              <Smile className="w-5 h-5 text-gray-600" />
            </button>
            <div className="flex-1">
              <textarea
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                onKeyPress={(e) => {
                  if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    handleSendMessage();
                  }
                }}
                placeholder="Mesajınızı yazın..."
                rows={1}
                className="w-full px-4 py-2 border border-gray-300 rounded-lg resize-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent outline-none"
              />
            </div>
            <button
              onClick={handleSendMessage}
              className="bg-indigo-600 text-white p-3 rounded-lg hover:bg-indigo-700 transition-colors"
            >
              <Send className="w-5 h-5" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
