# Como Exportar para GitHub

## Passo 1: Criar Repositório no GitHub

1. Acesse [github.com/new](https://github.com/new)
2. Preencha os dados:
   - **Repository name**: `legal-ai-fullstack`
   - **Description**: `Legal AI Backend v2.0 - Full Stack System`
   - **Public** (para que todos possam ver)
   - **Add a README file**: Não (já temos um)
   - **Add .gitignore**: Não (já temos um)
   - **Choose a license**: MIT License
3. Clique em "Create repository"

## Passo 2: Adicionar Remote e Push

```bash
cd /home/ubuntu/legal-ai-fullstack

# Adicionar remote (substitua SEU_USUARIO pelo seu username do GitHub)
git remote add origin https://github.com/SEU_USUARIO/legal-ai-fullstack.git

# Renomear branch para main (opcional, mas recomendado)
git branch -M main

# Push do código
git push -u origin main
```

## Passo 3: Configurar GitHub Actions (CI/CD)

Crie o arquivo `.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  backend-tests:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_USER: legal_ai
          POSTGRES_PASSWORD: legal_ai_password
          POSTGRES_DB: legal_ai
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        cd backend
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        cd backend
        pytest

  frontend-tests:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
    
    - name: Install dependencies
      run: |
        cd frontend
        npm install
    
    - name: Run tests
      run: |
        cd frontend
        npm run test
```

## Passo 4: Adicionar Secrets no GitHub

1. Vá para **Settings** → **Secrets and variables** → **Actions**
2. Clique em **New repository secret**
3. Adicione:
   - `OPENAI_API_KEY`: Sua chave da API OpenAI
   - `JWT_SECRET`: Uma chave secreta forte

## Passo 5: Configurar Proteção de Branch (Opcional)

1. Vá para **Settings** → **Branches**
2. Clique em **Add rule** para a branch `main`
3. Ative:
   - "Require a pull request before merging"
   - "Require status checks to pass before merging"
   - "Require branches to be up to date before merging"

## Passo 6: Deploy Automático (Opcional)

Para deploy automático em Heroku, Railway, ou Render, configure as credenciais correspondentes nos Secrets do GitHub.

## Resultado Final

Seu repositório estará em:
```
https://github.com/SEU_USUARIO/legal-ai-fullstack
```

## Próximos Passos

1. Compartilhe o link do repositório
2. Convide colaboradores
3. Configure CI/CD
4. Configure deploy automático
5. Comece a desenvolver!

---

Para mais informações, veja [README.md](README.md) e [docs/SETUP.md](docs/SETUP.md).
