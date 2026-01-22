# Setup Local - Legal AI Backend v2.0

Guia completo para configurar o projeto localmente para desenvolvimento.

## Pré-requisitos

- Python 3.11+
- Node.js 18+
- PostgreSQL 15+
- Git
- Docker (opcional, mas recomendado)

## Opção 1: Setup com Docker (Recomendado)

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/legal-ai-fullstack.git
cd legal-ai-fullstack
```

### 2. Criar arquivo .env
```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
```

### 3. Editar variáveis de ambiente
```bash
# backend/.env
DATABASE_URL=postgresql://legal_ai:legal_ai_password@postgres:5432/legal_ai
OPENAI_API_KEY=sk-sua-chave-aqui
JWT_SECRET=sua-chave-secreta-aqui
ENVIRONMENT=development

# frontend/.env
VITE_API_URL=http://localhost:8000/api/v2
```

### 4. Iniciar os containers
```bash
docker-compose up -d
```

### 5. Verificar se está funcionando
```bash
# Backend
curl http://localhost:8000/api/v2/health

# Frontend
open http://localhost:3000
```

## Opção 2: Setup Local sem Docker

### Backend

#### 1. Criar ambiente virtual
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

#### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

#### 3. Configurar banco de dados
```bash
# Criar banco de dados PostgreSQL
createdb legal_ai

# Executar migrações
alembic upgrade head
```

#### 4. Iniciar servidor
```bash
uvicorn app.main:app --reload
```

O backend estará disponível em `http://localhost:8000`

### Frontend

#### 1. Instalar dependências
```bash
cd frontend
npm install
```

#### 2. Configurar variáveis de ambiente
```bash
cp .env.example .env
# Editar .env conforme necessário
```

#### 3. Iniciar servidor de desenvolvimento
```bash
npm run dev
```

O frontend estará disponível em `http://localhost:3000`

## Estrutura de Diretórios

```
legal-ai-fullstack/
├── backend/
│   ├── app/
│   │   ├── domain/          # Entidades e interfaces
│   │   ├── application/     # Casos de uso
│   │   ├── infrastructure/  # Implementações técnicas
│   │   ├── interfaces/      # Endpoints da API
│   │   └── main.py          # Aplicação FastAPI
│   ├── migrations/          # Alembic migrations
│   ├── requirements.txt     # Dependências Python
│   ├── Dockerfile
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── pages/           # Páginas da aplicação
│   │   ├── components/      # Componentes React
│   │   ├── hooks/           # Custom hooks
│   │   ├── services/        # Serviços (API, etc)
│   │   └── App.tsx
│   ├── package.json
│   ├── vite.config.ts
│   ├── Dockerfile
│   └── .env.example
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API.md
│   └── SETUP.md
├── docker-compose.yml
├── README.md
└── LICENSE.md
```

## Variáveis de Ambiente

### Backend (.env)

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| DATABASE_URL | URL de conexão PostgreSQL | postgresql://user:pass@localhost:5432/legal_ai |
| OPENAI_API_KEY | Chave da API OpenAI | sk-... |
| JWT_SECRET | Chave secreta para JWT | sua-chave-secreta-aqui |
| JWT_ALGORITHM | Algoritmo JWT | HS256 |
| JWT_EXPIRATION | Expiração do token em segundos | 3600 |
| ENVIRONMENT | Ambiente (development/production) | development |

### Frontend (.env)

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| VITE_API_URL | URL da API backend | http://localhost:8000/api/v2 |

## Testes

### Backend
```bash
cd backend
pytest
```

### Frontend
```bash
cd frontend
npm run test
```

## Troubleshooting

### Erro: "Connection refused" ao conectar ao banco de dados
- Certifique-se de que PostgreSQL está rodando
- Verifique as credenciais em DATABASE_URL
- Tente criar o banco manualmente: `createdb legal_ai`

### Erro: "ModuleNotFoundError" no backend
- Certifique-se de que o ambiente virtual está ativado
- Reinstale as dependências: `pip install -r requirements.txt`

### Erro: "Port already in use"
- Mude a porta no arquivo de configuração
- Ou mate o processo que está usando a porta

### Frontend não conecta com backend
- Verifique se VITE_API_URL está correto
- Certifique-se de que o backend está rodando
- Verifique CORS no backend

## Próximos Passos

1. Leia [ARCHITECTURE.md](ARCHITECTURE.md) para entender a estrutura
2. Leia [API.md](API.md) para conhecer os endpoints
3. Comece a desenvolver!

## Recursos Úteis

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [React Docs](https://react.dev/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)

---

Dúvidas? Abra uma issue no GitHub!
