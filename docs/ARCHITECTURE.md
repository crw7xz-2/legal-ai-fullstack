# Arquitetura do Legal AI Backend v2.0

## Visão Geral

O Legal AI Backend v2.0 segue os princípios de **Clean Architecture** e **Domain-Driven Design (DDD)**, garantindo que o código seja modular, testável e fácil de manter.

## Camadas da Arquitetura

### 1. Domain (Domínio)
O núcleo do negócio. Contém as entidades e interfaces que definem o comportamento esperado.

**Responsabilidades:**
- Definir entidades de negócio (User, LegalAnalysis, AuditLog)
- Definir interfaces abstratas (AIProvider, CacheService, AuditLogger)
- Implementar regras de negócio puras

**Exemplo:**
```python
# domain/entities/legal_analysis.py
class LegalAnalysis:
    id: UUID
    user_id: UUID
    raw_text: str
    summary: str
    document_type: str
    legal_area: str
    language: str
    involved_parties: List[str]
    relevant_dates: List[datetime]
    key_points: List[str]
```

### 2. Application (Aplicação)
Orquestra o fluxo entre domínio e infraestrutura.

**Responsabilidades:**
- Implementar casos de uso (AnalyzeDocumentUseCase)
- Orquestrar o pipeline de processamento
- Validar entrada e saída

**Exemplo:**
```python
# application/use_cases/analyze_document.py
class AnalyzeDocumentUseCase:
    def execute(self, text: str, user_id: UUID) -> LegalAnalysis:
        # Validar texto
        # Chamar pipeline
        # Persistir resultado
        # Retornar análise
```

### 3. Infrastructure (Infraestrutura)
Implementações técnicas das interfaces de domínio.

**Responsabilidades:**
- Implementar AIProvider (OpenAI, Anthropic, etc.)
- Implementar CacheService (Redis, Memcached, etc.)
- Implementar AuditLogger (Database, ELK, etc.)
- Gerenciar conexões com banco de dados

**Exemplo:**
```python
# infrastructure/ai_providers/openai_provider.py
class OpenAIProvider(AIProvider):
    def analyze(self, text: str, prompt: str) -> Dict:
        # Chamar API OpenAI
        # Tratar erros
        # Retornar resultado
```

### 4. Interfaces (API)
A camada mais externa que lida com o mundo exterior.

**Responsabilidades:**
- Definir endpoints REST
- Validar requisições
- Serializar respostas
- Tratar erros HTTP

**Exemplo:**
```python
# interfaces/api/endpoints/analyses.py
@router.post("/analyses")
async def create_analysis(
    request: CreateAnalysisRequest,
    user: User = Depends(get_current_user)
) -> AnalysisResponse:
    # Validar requisição
    # Chamar use case
    # Retornar resposta
```

## Fluxo de Dados

```
Request HTTP
    ↓
Interfaces (Validação)
    ↓
Application (Orquestração)
    ↓
Domain (Lógica de Negócio)
    ↓
Infrastructure (Implementação Técnica)
    ↓
Database / External APIs
    ↓
Response HTTP
```

## Pipeline de Análise

```
1. Validação
   - Verificar se texto não está vazio
   - Verificar tamanho máximo

2. Pré-processamento
   - Limpeza de texto
   - Detecção de idioma

3. Processamento de IA
   - Enviar para OpenAI
   - Retry em caso de falha
   - Timeout controlado

4. Pós-processamento
   - Validar resposta
   - Enriquecer dados

5. Persistência
   - Salvar no banco de dados
   - Atualizar cache
   - Registrar auditoria

6. Retorno
   - Serializar resultado
   - Retornar ao cliente
```

## Dependências e Injeção

O projeto utiliza injeção de dependência para desacoplar componentes:

```python
# Exemplo de injeção de dependência
def get_analyze_use_case(
    ai_provider: AIProvider = Depends(get_ai_provider),
    cache: CacheService = Depends(get_cache),
    db: Database = Depends(get_database)
) -> AnalyzeDocumentUseCase:
    return AnalyzeDocumentUseCase(ai_provider, cache, db)
```

## Tratamento de Erros

Todos os erros são tratados graciosamente:

```python
try:
    result = ai_provider.analyze(text)
except AIProviderError as e:
    logger.error(f"Erro na IA: {e}")
    return fallback_response()
except Exception as e:
    logger.error(f"Erro inesperado: {e}")
    return error_response(500)
```

## Segurança

- **Autenticação**: JWT com refresh tokens
- **Autorização**: Verificação de propriedade de recursos
- **Validação**: Pydantic para validação de entrada
- **Secrets**: Variáveis de ambiente para dados sensíveis
- **CORS**: Configurado para produção

## Performance

- **Cache**: Evita reprocessamento de textos idênticos
- **Async/Await**: Processamento não-bloqueante
- **Connection Pooling**: Reutilização de conexões de BD
- **Indexação**: Índices no banco de dados para queries frequentes

## Monitoramento

- **Logging Estruturado**: JSON para fácil parsing
- **Auditoria**: Rastreamento de todas as operações
- **Métricas**: Contadores de requisições e erros
- **Health Checks**: Verificação de saúde do sistema

---

Para mais informações, veja [API.md](API.md) e [SETUP.md](SETUP.md).
