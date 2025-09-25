import { useState } from "react";
import {User, Phone, Scissors, Calendar, Clock } from 'lucide-react';
import { appointmentService } from "../services/api";

const AppointmentForm = ({ onAppointmentCreated }) => {
    const [form, setForm ] = useState ({
        nome: '',
        telefone: '',
        servico: 'Corte de Cabelo',
        data: '',
        horario: '',
    });
    const [Loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);

        try {
            await appointmentService.create(form);
            alert('Agendamento realizado com sucesso!')
            setForm({nome: '', telefone: '', servico: 'Corte de Cabelo', data: '', horario: ''});
            onAppointmentCreated();
        } catch (error) {
            console.error('Erro ao criar agendamento:', error);
            alert('Erro ao agendar. Tente novamente.');
        } finally{
            setLoading(false);
        }
    };

    return (
        <form onSubmit={handleSubmit} className="form-card">
            <h2>Fazer Agendamento</h2>

            <div className="input-group">
                <User size={20} />
                <input
                    type='text'
                    placeholder="Seu nome"
                    value={form.nome}
                    onChange={e => setForm({...form, nome: e.target.value})}
                    required
                    />
            </div>

            <div className="input-group">
                <Phone size={20} />
                <input
                    type='tel'
                    placeholder="Seu telefone"
                    value={form.telefone}
                    onChange={e => setForm({...form, telefone: e.target.value})}
                    required
                    />
            </div>

            <div className="input-group">
                <Scissors size={20} />
                <select
                value={form.servico}
                onChange={e => setForm({...form, servico: e.target.value})}
                >
                <option>Corte de Cabelo</option>
                <option>Barba</option>
                <option>Corte + Barba</option>
                <option>Corte Degradê</option>
                <option>Corte Navalhado</option>
                </select>
            </div>
             <div className="input-row">
            <div className="input-group">
                <Calendar size={20} />
                <input
                    type="date"
                    value={form.data}
                    onChange={e => setForm({ ...form, data: e.target.value })}
                    required
            />
            </div>

            <div className="input-group">
                <Clock size={20} />
                <input
                    type="time"
                    value={form.horario}
                    onChange={e => setForm({ ...form, horario: e.target.value })}
                    required
                />
            </div>
        </div>

        <button type="submit" disabled={Loading}>
            {Loading ? 'Agendando...' : 'Confirmar Agendamento'}
        </button>

        </form>
    );
};

export default AppointmentForm;