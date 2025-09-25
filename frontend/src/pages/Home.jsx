import { useState } from 'react';
import Header from '../components/Header';
import AppointmentForm from '../components/AppointmentForm';
import AppointmentList from '../components/AppointmentList';

const Home = () => {
  const [refreshList, setRefreshList] = useState(0);

  const handleAppointmentCreated = () => {
    setRefreshList(prev => prev + 1);
  };

  return (
    <div className="app">
      <Header />
      <main className="main-content">
        <AppointmentForm onAppointmentCreated={handleAppointmentCreated} />
        <AppointmentList key={refreshList} />
      </main>
    </div>
  );
};

export default Home;