# ⚖️ Legal AI Backend v2.0 - Full Stack

Um sistema backend jurídico de nível de produção com **Clean Architecture**, **DDD**, banco de dados persistente e autenticação de usuários.

## 🎯 Características

- ✅ **Frontend Moderno**: React 19 + TailwindCSS 4 + shadcn/ui
- ✅ **Backend Robusto**: FastAPI com validação Pydantic
- ✅ **Banco de Dados**: PostgreSQL com Alembic migrations
- ✅ **Autenticação**: JWT com refresh tokens
- ✅ **Clean Architecture**: Domain, Application, Infrastructure, Interfaces
- ✅ **Resiliência**: Retry exponencial, timeouts, fallback seguro
- ✅ **Auditoria**: Logging estruturado em JSON
- ✅ **Docker**: Pronto para containerização
- ✅ **CI/CD**: GitHub Actions configurado

## 📁 Estrutura do Projeto

```
legal-ai-fullstack/
├── frontend/                 # React + TailwindCSS
│   ├── src/
│   │   ├── pages/           # Páginas da aplicação
│   │   ├── components/      # Componentes reutilizáveis
│   │   ├── hooks/           # Custom hooks
│   │   ├── services/        # Integração com API
│   │   └── App.tsx
│   ├── package.json
│   └── vite.config.ts
├── backend/                  # FastAPI + SQLAlchemy
│   ├── app/
│   │   ├── domain/          # Entidades de negócio
│   │   ├── application/     # Casos de uso
│   │   ├── infrastructure/  # Implementações técnicas
│   │   ├── interfaces/      # API endpoints
│   │   └── main.py
│   ├── migrations/          # Alembic migrations
│   ├── requirements.txt
│   └── docker/Dockerfile
├── docker-compose.yml       # Orquestração de containers
├── .github/workflows/       # CI/CD
└── docs/                    # Documentação
```

## 🚀 Quick Start

### Com Docker (Recomendado)

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/legal-ai-fullstack.git
cd legal-ai-fullstack

# Inicie os containers
docker-compose up -d

# Acesse
# Frontend: http://localhost:3000
# Backend: http://localhost:8000
# Docs: http://localhost:8000/docs
```

### Desenvolvimento Local

#### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 📡 API Endpoints

### Autenticação
- `POST /api/v2/auth/register` - Registrar novo usuário
- `POST /api/v2/auth/login` - Login
- `POST /api/v2/auth/refresh` - Refresh token

### Análises
- `GET /api/v2/analyses` - Listar análises do usuário
- `POST /api/v2/analyses` - Criar nova análise
- `GET /api/v2/analyses/{id}` - Obter análise específica
- `DELETE /api/v2/analyses/{id}` - Deletar análise

### Sistema
- `GET /api/v2/health` - Status do sistema
- `GET /api/v2/docs` - Swagger UI

## 🔐 Configuração de Variáveis de Ambiente

### Backend (.env)
```
DATABASE_URL=postgresql://user:password@localhost:5432/legal_ai
OPENAI_API_KEY=sk-...
JWT_SECRET=sua-chave-secreta-aqui
JWT_ALGORITHM=HS256
JWT_EXPIRATION=3600
ENVIRONMENT=development
```

### Frontend (.env)
```
VITE_API_URL=http://localhost:8000/api/v2
```

## 🧪 Testes

```bash
# Backend
cd backend
pytest

# Frontend
cd frontend
npm run test
```

## 📊 Banco de Dados

### Schema Principal

**Users**
- id (UUID)
- email (String, unique)
- password_hash (String)
- name (String)
- created_at (DateTime)
- updated_at (DateTime)

**LegalAnalyses**
- id (UUID)
- user_id (FK)
- raw_text (Text)
- content_hash (String)
- summary (Text)
- document_type (String)
- legal_area (String)
- language (String)
- involved_parties (JSON)
- relevant_dates (JSON)
- key_points (JSON)
- metadata (JSON)
- created_at (DateTime)
- updated_at (DateTime)

**AuditLogs**
- id (UUID)
- user_id (FK)
- event_type (String)
- payload (JSON)
- status (String)
- created_at (DateTime)

## 🏗️ Arquitetura

### Clean Architecture em 4 Camadas

```
┌─────────────────────────────────────┐
│   Interfaces (API REST)             │ ← FastAPI endpoints
├─────────────────────────────────────┤
│   Application (Casos de Uso)        │ ← Lógica de orquestração
├─────────────────────────────────────┤
│   Infrastructure (Técnico)          │ ← BD, IA, Cache
├─────────────────────────────────────┤
│   Domain (Negócio)                  │ ← Entidades, interfaces
└─────────────────────────────────────┘
```

## 🔄 Pipeline de Análise

```
Texto → Validação → IA Processing → Cache → Persistência → Resposta
```

## 📈 Monitoramento

- Logs estruturados em JSON
- Rastreamento de erros
- Métricas de performance
- Auditoria de todas as operações

## 🚢 Deploy

### Heroku
```bash
git push heroku main
```

### AWS / DigitalOcean / Render
Veja `docs/DEPLOY.md` para instruções detalhadas.

## 📚 Documentação Completa

- [Arquitetura](docs/ARCHITECTURE.md)
- [API Reference](docs/API.md)
- [Setup Local](docs/SETUP.md)
- [Deploy](docs/DEPLOY.md)
- [Contribuindo](CONTRIBUTING.md)

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

MIT License - veja LICENSE.md para detalhes

## 👨‍💼 Suporte

Para dúvidas ou sugestões, abra uma issue no GitHub ou entre em contato através de support@legalai.com

---

**Legal AI Backend v2.0** | Arquitetura para o futuro do Direito | © 2026
