import { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import './index.css';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem('access_token');
    setIsAuthenticated(!!token);
    setLoading(false);
  }, []);

  // Função para atualizar o estado de autenticação
  const handleLogin = () => {
    setIsAuthenticated(true);
  };

  const handleLogout = () => {
    setIsAuthenticated(false);
    localStorage.removeItem('access_token');
    localStorage.removeItem('user');
  };

  if (loading) {
    return <div className="loading">Carregando...</div>;
  }

  return (
    <Router>
      <Routes>
        {/* Rota raiz - redireciona para home ou login */}
        <Route 
          path="/" 
          element={
            isAuthenticated ? 
            <Navigate to="/home" replace /> : 
            <Navigate to="/login" replace />
          } 
        />
        
        <Route 
          path="/login" 
          element={
            !isAuthenticated ? 
            <Login onLoginSuccess={handleLogin} /> : 
            <Navigate to="/home" replace />
          } 
        />
        
        <Route 
          path="/register" 
          element={
            !isAuthenticated ? 
            <Register /> : 
            <Navigate to="/home" replace />
          } 
        />
        
        <Route 
          path="/home" 
          element={
            isAuthenticated ? 
            <Home onLogout={handleLogout} /> : 
            <Navigate to="/login" replace />
          } 
        />
        
        {/* Rota fallback para páginas não encontradas */}
        <Route 
          path="*" 
          element={<Navigate to="/" replace />} 
        />
      </Routes>
    </Router>
  );
}

export default App;