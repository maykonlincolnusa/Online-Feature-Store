# Guia de Contribuição

Obrigado por considerar contribuir com o Feature Store! Este documento fornece diretrizes para contribuir com o projeto.

## Código de Conduta

Ao participar deste projeto, você concorda em seguir nosso código de conduta. Seja respeitoso, inclusivo e profissional em todas as interações.

## Como Contribuir

### Reportar Bugs

Se você encontrou um bug:

1. **Verifique** se o bug já foi reportado em [Issues](https://github.com/seu-usuario/feature-store-project/issues)
2. Se não foi reportado, **crie uma nova issue** com:
   - Título claro e descritivo
   - Passos para reproduzir o problema
   - Comportamento esperado vs. comportamento atual
   - Versão do Python, OS, e outras informações relevantes
   - Logs de erro (se aplicável)

### Sugerir Melhorias

Para sugerir novas features ou melhorias:

1. **Verifique** se já existe uma issue relacionada
2. **Crie uma nova issue** descrevendo:
   - Motivação: Por que essa feature é útil?
   - Proposta: Como deveria funcionar?
   - Alternativas: Outras abordagens consideradas?

### Pull Requests

#### Processo

1. **Fork** o repositório
2. **Crie um branch** para sua feature:
   ```bash
   git checkout -b feature/minha-feature
   ```

3. **Faça suas alterações** seguindo as diretrizes de código

4. **Adicione testes** para suas mudanças

5. **Execute os testes**:
   ```bash
   pytest tests/
   ```

6. **Verifique o code style**:
   ```bash
   black src/
   flake8 src/
   mypy src/
   ```

7. **Commit** suas mudanças:
   ```bash
   git commit -m "feat: adiciona nova feature X"
   ```

8. **Push** para o branch:
   ```bash
   git push origin feature/minha-feature
   ```

9. **Abra um Pull Request** no GitHub

#### Diretrizes para PRs

- **Um PR = Uma feature/fix**: Mantenha PRs focados em uma única mudança
- **Testes**: Toda nova funcionalidade deve ter testes
- **Documentação**: Atualize a documentação se necessário
- **Descrição clara**: Explique o que foi mudado e por quê
- **Commits semânticos**: Use [Conventional Commits](https://www.conventionalcommits.org/)

## Diretrizes de Desenvolvimento

### Configuração do Ambiente

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/feature-store-project.git
cd feature-store-project

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instale dependências
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Instale em modo de desenvolvimento
pip install -e .
```

### Estrutura de Código

```
src/
├── features/          # Definições e transformações
├── ingestion/         # Ingestão de dados
├── serving/           # API de serving
├── versioning/        # Sistema de versionamento
└── utils/            # Utilitários
```

### Style Guide

#### Python

Seguimos o [PEP 8](https://pep8.org/) com algumas exceções:

- **Line length**: 100 caracteres (não 79)
- **Imports**: Use `isort` para ordenar
- **Formatting**: Use `black` para formatação automática
- **Type hints**: Sempre use type hints

Exemplo:

```python
from typing import List, Dict, Optional
from datetime import datetime


def calculate_feature(
    data: Dict[str, Any],
    window_size: int = 7,
    normalize: bool = True
) -> Optional[float]:
    """
    Calcula feature com janela de tempo.
    
    Args:
        data: Dicionário com dados de entrada
        window_size: Tamanho da janela em dias
        normalize: Se deve normalizar o resultado
        
    Returns:
        Valor da feature ou None se dados inválidos
    """
    if not data:
        return None
    
    # Implementação...
    result = 0.0
    
    return result if not normalize else result / window_size
```

#### Docstrings

Use Google-style docstrings:

```python
def function_name(param1: int, param2: str) -> bool:
    """
    Breve descrição da função.
    
    Descrição mais longa se necessário, explicando
    detalhes de implementação.
    
    Args:
        param1: Descrição do primeiro parâmetro
        param2: Descrição do segundo parâmetro
        
    Returns:
        Descrição do retorno
        
    Raises:
        ValueError: Quando param1 é negativo
        
    Examples:
        >>> function_name(10, "test")
        True
    """
    pass
```

#### Testes

- **Cobertura**: Mínimo de 80% de cobertura
- **Organização**: Um arquivo de teste por módulo
- **Naming**: `test_<function_name>_<scenario>`

Exemplo:

```python
import pytest
from src.features.transformations import calculate_age


def test_calculate_age_valid_date():
    """Testa cálculo de idade com data válida"""
    record = {"birth_date": datetime(1990, 1, 1)}
    age = calculate_age(record)
    assert age > 0


def test_calculate_age_missing_data():
    """Testa comportamento com dados faltantes"""
    record = {}
    with pytest.raises(ValueError):
        calculate_age(record)


@pytest.mark.parametrize("birth_year,expected_age", [
    (1990, 34),
    (2000, 24),
    (1980, 44),
])
def test_calculate_age_multiple_years(birth_year, expected_age):
    """Testa múltiplos anos de nascimento"""
    record = {"birth_date": datetime(birth_year, 1, 1)}
    age = calculate_age(record)
    assert age == expected_age
```

### Commit Messages

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**:
- `feat`: Nova feature
- `fix`: Bug fix
- `docs`: Documentação
- `style`: Formatação (não afeta código)
- `refactor`: Refatoração
- `test`: Adiciona/modifica testes
- `chore`: Manutenção

**Exemplos**:

```
feat(features): adiciona transformação de embedding

Implementa transformação para gerar embeddings de texto
usando modelo BERT pré-treinado.

Closes #123
```

```
fix(api): corrige race condition no cache

Race condition ocorria quando múltiplas requisições
simultâneas tentavam popular o cache.

Fixes #456
```

### Versionamento

Seguimos [Semantic Versioning](https://semver.org/):

- **MAJOR**: Mudanças incompatíveis na API
- **MINOR**: Novas funcionalidades compatíveis
- **PATCH**: Correções de bugs compatíveis

## Review Process

1. **Automated checks**: CI deve passar
2. **Code review**: Pelo menos 1 aprovação
3. **Discussion**: Responda a comentários
4. **Updates**: Faça mudanças solicitadas
5. **Merge**: Mantenedor fará o merge

## Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a mesma licença do projeto (MIT License).

## Dúvidas?

- Abra uma [Discussion](https://github.com/seu-usuario/feature-store-project/discussions)
- Entre em contato: team@example.com

---

**Obrigado por contribuir! 🎉**