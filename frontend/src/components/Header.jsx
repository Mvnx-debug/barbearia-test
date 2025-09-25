import { useNavigate } from 'react-router-dom';

const Header = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    navigate('/login');
  };

  return (
    <header className="header">
      <div className="header-content">
        <h1>Jonatthan Barber</h1>
        <nav className="nav">
          <button onClick={handleLogout} className="nav-button">
            Sair
          </button>
        </nav>
      </div>
    </header>
  );
};

export default Header;