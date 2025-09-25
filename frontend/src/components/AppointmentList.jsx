import { useState, useEffect } from 'react';
import { Phone, Scissors, Calendar, Clock, Trash2 } from 'lucide-react';
import { appointmentService } from "../services/api";

const AppointmentList = () => {
  const [agendamentos, setAgendamentos] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchAgendamentos = async () => {
    try {
      const response = await appointmentService.getAll();
      setAgendamentos(response.data);
    } catch (error) {
      console.error('Erro ao buscar agendamentos:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleCancel = async (id) => {
    if (window.confirm('Cancelar este agendamento?')) {
      try {
        await appointmentService.delete(id);
        fetchAgendamentos();
      } catch (error) {
        console.error('Erro ao cancelar:', error);
      }
    }
  };

  useEffect(() => {
    fetchAgendamentos();
  }, []);

  if (loading) return <div className="loading">Carregando agendamentos...</div>;

  return (
    <div className="agendamentos-list">
      <h2>Agendamentos</h2>
      {agendamentos.length === 0 ? (
        <p>Nenhum agendamento encontrado.</p>
      ) : (
        agendamentos.map(ag => (
          <div key={ag.id} className="agendamento-card">
            <div className="agendamento-info">
              <h3>{ag.nome}</h3>
              <p><Phone size={16} /> {ag.telefone}</p>
              <p><Scissors size={16} /> {ag.servico}</p>
              <p><Calendar size={16} /> {ag.data} às <Clock size={16} /> {ag.horario}</p>
            </div>
            <button
              onClick={() => handleCancel(ag.id)}
              className="cancel-btn"
            >
              <Trash2 size={18} />
            </button>
          </div>
        ))
      )}
    </div>
  );
};

export default AppointmentList;