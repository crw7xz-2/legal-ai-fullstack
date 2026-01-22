# API Reference - Legal AI Backend v2.0

## Base URL

```
http://localhost:8000/api/v2
```

## Autenticação

A API utiliza JWT (JSON Web Tokens) para autenticação. Inclua o token no header:

```
Authorization: Bearer {token}
```

## Endpoints

### 1. Autenticação

#### Registrar Novo Usuário
```http
POST /auth/register
Content-Type: application/json

{
  "email": "usuario@example.com",
  "password": "senha_segura",
  "name": "Nome do Usuário"
}
```

**Response (201 Created):**
```json
{
  "id": "uuid",
  "email": "usuario@example.com",
  "name": "Nome do Usuário",
  "created_at": "2026-01-22T10:00:00Z"
}
```

#### Login
```http
POST /auth/login
Content-Type: application/json

{
  "email": "usuario@example.com",
  "password": "senha_segura"
}
```

**Response (200 OK):**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer",
  "expires_in": 3600
}
```

#### Refresh Token
```http
POST /auth/refresh
Content-Type: application/json

{
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Response (200 OK):**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer",
  "expires_in": 3600
}
```

### 2. Análises Jurídicas

#### Listar Análises do Usuário
```http
GET /analyses
Authorization: Bearer {token}
```

**Query Parameters:**
- `skip` (int, default: 0) - Número de registros a pular
- `limit` (int, default: 10) - Número de registros a retornar
- `document_type` (string, optional) - Filtrar por tipo de documento
- `legal_area` (string, optional) - Filtrar por área do direito

**Response (200 OK):**
```json
{
  "total": 42,
  "items": [
    {
      "id": "uuid",
      "user_id": "uuid",
      "raw_text": "SENTENÇA...",
      "content_hash": "86daafda818cc1dd...",
      "summary": "Sentença que julga procedente...",
      "document_type": "Sentença",
      "legal_area": "Cível",
      "language": "Português",
      "involved_parties": ["João da Silva", "Maria Santos"],
      "relevant_dates": ["2026-01-22"],
      "key_points": ["Ponto 1", "Ponto 2"],
      "metadata": {"provider": "OpenAI"},
      "created_at": "2026-01-22T10:00:00Z",
      "updated_at": "2026-01-22T10:00:00Z"
    }
  ]
}
```

#### Criar Nova Análise
```http
POST /analyses
Authorization: Bearer {token}
Content-Type: application/json

{
  "texto": "SENTENÇA. Vistos, examinados..."
}
```

**Response (201 Created):**
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "raw_text": "SENTENÇA...",
  "content_hash": "86daafda818cc1dd...",
  "summary": "Sentença que julga procedente...",
  "document_type": "Sentença",
  "legal_area": "Cível",
  "language": "Português",
  "involved_parties": ["João da Silva", "Maria Santos"],
  "relevant_dates": ["2026-01-22"],
  "key_points": ["Ponto 1", "Ponto 2"],
  "metadata": {"provider": "OpenAI"},
  "created_at": "2026-01-22T10:00:00Z",
  "updated_at": "2026-01-22T10:00:00Z"
}
```

#### Obter Análise Específica
```http
GET /analyses/{id}
Authorization: Bearer {token}
```

**Response (200 OK):**
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "raw_text": "SENTENÇA...",
  "content_hash": "86daafda818cc1dd...",
  "summary": "Sentença que julga procedente...",
  "document_type": "Sentença",
  "legal_area": "Cível",
  "language": "Português",
  "involved_parties": ["João da Silva", "Maria Santos"],
  "relevant_dates": ["2026-01-22"],
  "key_points": ["Ponto 1", "Ponto 2"],
  "metadata": {"provider": "OpenAI"},
  "created_at": "2026-01-22T10:00:00Z",
  "updated_at": "2026-01-22T10:00:00Z"
}
```

#### Deletar Análise
```http
DELETE /analyses/{id}
Authorization: Bearer {token}
```

**Response (204 No Content)**

### 3. Sistema

#### Health Check
```http
GET /health
```

**Response (200 OK):**
```json
{
  "status": "healthy",
  "version": "2.0.0",
  "service": "Legal AI Backend"
}
```

#### Documentação Interativa
```
GET /docs
```

Abre a documentação Swagger UI interativa.

## Códigos de Status HTTP

| Código | Descrição |
|--------|-----------|
| 200 | OK - Requisição bem-sucedida |
| 201 | Created - Recurso criado com sucesso |
| 204 | No Content - Sucesso sem conteúdo |
| 400 | Bad Request - Requisição inválida |
| 401 | Unauthorized - Autenticação necessária |
| 403 | Forbidden - Acesso negado |
| 404 | Not Found - Recurso não encontrado |
| 500 | Internal Server Error - Erro no servidor |

## Tratamento de Erros

Todas as respostas de erro seguem este formato:

```json
{
  "error": "Tipo de erro",
  "detail": "Descrição detalhada do erro",
  "status_code": 400
}
```

## Exemplos de Uso

### Com cURL

#### Registrar usuário
```bash
curl -X POST http://localhost:8000/api/v2/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "usuario@example.com",
    "password": "senha_segura",
    "name": "Nome do Usuário"
  }'
```

#### Login
```bash
curl -X POST http://localhost:8000/api/v2/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "usuario@example.com",
    "password": "senha_segura"
  }'
```

#### Criar análise
```bash
curl -X POST http://localhost:8000/api/v2/analyses \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -d '{
    "texto": "SENTENÇA. Vistos, examinados..."
  }'
```

### Com Python

```python
import requests

BASE_URL = "http://localhost:8000/api/v2"

# Login
response = requests.post(f"{BASE_URL}/auth/login", json={
    "email": "usuario@example.com",
    "password": "senha_segura"
})
token = response.json()["access_token"]

# Criar análise
headers = {"Authorization": f"Bearer {token}"}
response = requests.post(f"{BASE_URL}/analyses", 
    headers=headers,
    json={"texto": "SENTENÇA..."}
)
analysis = response.json()
print(analysis)
```

### Com JavaScript

```javascript
const BASE_URL = "http://localhost:8000/api/v2";

// Login
const loginResponse = await fetch(`${BASE_URL}/auth/login`, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    email: "usuario@example.com",
    password: "senha_segura"
  })
});
const { access_token } = await loginResponse.json();

// Criar análise
const analysisResponse = await fetch(`${BASE_URL}/analyses`, {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${access_token}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    texto: "SENTENÇA..."
  })
});
const analysis = await analysisResponse.json();
console.log(analysis);
```

## Rate Limiting

Atualmente não há rate limiting implementado. Será adicionado em versões futuras.

## Versionamento

A API utiliza versionamento na URL (`/api/v2`). Versões antigas serão mantidas por compatibilidade.

---

Para mais informações, consulte [ARCHITECTURE.md](ARCHITECTURE.md).
