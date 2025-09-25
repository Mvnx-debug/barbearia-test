# ✂️ Barbearia MVP - Sistema de Agendamento
#(atenção, projeto não está 100% finalizado.)



Um sistema moderno para barbearia desenvolvido com React no frontend e FastAPI no backend, facilitando o agendamento de horários e gestão de serviços.

### ✅ Implementadas
- **Backend FastAPI** com estrutura básica
- **Autenticação JWT** para usuários
- **Modelagem de dados** para agendamentos
- **API REST** para serviços de barbearia
- **Frontend React** com estrutura inicial

### 🚧 Em Desenvolvimento
- Interface completa do usuário
- Sistema de agendamento online
- Painel administrativo
- Integração frontend-backend
- Sistema de pagamento

## 🛠️ Tecnologias Utilizadas

### Frontend
- **React** 18.x
- **React Router DOM** - Navegação
- **Axios** - Consumo de API
- **CSS3** - Estilização

### Backend
- **FastAPI** - Framework web moderno
- **SQLite** - Banco de dados (desenvolvimento)
- **JWT** - Autenticação
- **Python 3.12** - Linguagem backend
- **SQLAlchemy** - ORM
- **Pydantic** - Validação de dados

## 📁 Estrutura do Projeto
barbearia-test/
├── backend/ # API FastAPI
│ ├── app/
│ │ ├── models/ # Modelos de dados
│ │ ├── routes/ # Rotas da API
│ │ ├── schemas/ # Schemas Pydantic
│ │ └── database.py # Configuração do banco
│ ├── requirements.txt # Dependências Python
│ └── main.py # Aplicação principal
├── frontend/ # Aplicação React
│ ├── public/
│ ├── src/
│ │ ├── components/ # Componentes React
│ │ ├── pages/ # Páginas da aplicação
│ │ ├── services/ # Serviços API
│ │ └── App.js # Componente principal
│ ├── package.json # Dependências Node
