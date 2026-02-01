# Feature Store - Real-time & Batch Processing

Sistema completo de Feature Store com suporte a processamento em tempo real e batch, garantindo consistência entre ambos os ambientes e versionamento robusto.

## 🎯 Visão Geral

Este projeto implementa uma Feature Store completa com:

- **Features em Tempo Real**: Servindo features com latência <10ms
- **Consistência Batch/Stream**: Mesma lógica de transformação em ambos ambientes
- **Versionamento**: Controle completo de versões de features e modelos

## 🏗️ Arquitetura

```
┌─────────────────┐
│  Data Sources   │
│ (Kafka, DBs)    │
└────────┬────────┘
         │
    ┌────▼─────┐
    │ Ingestion│
    └────┬─────┘
         │
    ┌────▼──────────────┐
    │  Feature Pipeline │
    │  (Batch/Stream)   │
    └────┬──────────────┘
         │
    ┌────▼─────────┐
    │ Feature Store│
    │  (Online/    │
    │   Offline)   │
    └──────────────┘
```

## 📁 Estrutura do Projeto

```
.
├── src/
│   ├── ingestion/          # Ingestão de dados
│   ├── features/           # Definições de features
│   ├── transformations/    # Transformações batch/stream
│   ├── serving/            # API de serving
│   └── versioning/         # Controle de versões
├── config/                 # Configurações
├── tests/                  # Testes
├── docs/                   # Documentação
├── infrastructure/         # IaC (Terraform, Docker)
└── examples/              # Exemplos de uso
```

## 🚀 Quick Start

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/feature-store-project.git
cd feature-store-project

# Instale dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env

# Inicie os serviços
docker-compose up -d
```

## 📊 Componentes Principais

### 1. Feature Pipeline
- Transformações unificadas para batch e stream
- Validação de dados
- Monitoramento de qualidade

### 2. Feature Store
- **Online Store**: Redis/DynamoDB para baixa latência
- **Offline Store**: S3/Delta Lake para treinamento
- **Feature Registry**: Metadados e lineage

### 3. Serving Layer
- API REST/gRPC para serving
- Cache inteligente
- Feature materialization

## 🔧 Tecnologias

- **Stream Processing**: Apache Kafka, Flink
- **Batch Processing**: Apache Spark
- **Storage**: Redis, PostgreSQL, S3
- **Orquestração**: Airflow
- **Versionamento**: DVC, MLflow

## 📖 Documentação

Veja a [documentação completa](./docs/README.md) para mais detalhes sobre:
- [Arquitetura detalhada](./docs/architecture.md)
- [Guia de features](./docs/features-guide.md)
- [Versionamento](./docs/versioning.md)
- [Deploy](./docs/deployment.md)

## 🤝 Contribuindo

Contribuições são bem-vindas! Veja [CONTRIBUTING.md](./CONTRIBUTING.md) para detalhes.

## 📝 Licença

Este projeto está sob a licença MIT - veja [LICENSE](./LICENSE) para detalhes.