# FastAPI Project

Este é um projeto de exemplo desenvolvido com **FastAPI**. Ele utiliza ferramentas modernas para gerenciamento de dependências e automação, como **Poetry**, **Taskipy**, **pytest**, **pipx**, **Ruff** e **Uvicorn**.

## Tecnologias Usadas

- **FastAPI**: Framework moderno para criação de APIs web.
- **Poetry**: Gerenciador de dependências e build system para Python.
- **Taskipy**: Ferramenta para automação de tarefas no ambiente de desenvolvimento.
- **pytest**: Framework de testes para Python.
- **pipx**: Ferramenta para executar pacotes Python em ambientes isolados.
- **Ruff**: Linter de código Python.
- **Uvicorn**: Servidor ASGI para execução da aplicação FastAPI.

## Pré-requisitos

Antes de começar, você precisará ter as seguintes ferramentas instaladas:

- **Python 3.7 ou superior**
- **Poetry** (Gerenciador de dependências)
- **pipx** (para isolar execução de pacotes)

### Instalação do Poetry

Caso não tenha o Poetry instalado, execute o seguinte comando:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Instalação do pipx

Se o pipx não estiver instalado, use:

```bash
python -m pip install --user pipx
python -m pipx ensurepath
```

## Instalação e Configuração do Projeto

### 1. Instalar as dependências

Para instalar as dependências do projeto, execute o comando:

```bash
poetry install
```

Isso irá instalar todas as dependências do projeto, incluindo as de desenvolvimento.

### 2. Rodar o Servidor com Uvicorn

Para rodar a aplicação FastAPI em modo de desenvolvimento, use o comando:

```bash
poetry run uvicorn app.main:app --reload
```

A aplicação estará disponível em `http://127.0.0.1:8000`.

## Automatizando Tarefas com Taskipy

**Taskipy** é utilizado para definir tarefas personalizadas no projeto. Para rodar as tarefas definidas, utilize:

```bash
poetry run task <nome-da-tarefa>
```

Você pode verificar todas as tarefas disponíveis no arquivo `pyproject.toml`.

### Exemplo de Tarefas Definidas

Se no seu `pyproject.toml` houver tarefas como rodar testes ou linters, elas podem ser executadas assim:

```bash
poetry run task lint
poetry run task tests
```

## Executando Testes com pytest

Para rodar os testes com **pytest**, utilize o seguinte comando:

```bash
poetry run pytest
```

O **pytest** irá procurar por arquivos de teste no diretório `tests/` e executar todos os testes encontrados.

## Analisando Código com Ruff

**Ruff** é utilizado como linter para garantir a qualidade do código. Para rodá-lo, use o comando:

```bash
poetry run ruff check .
```

Isso irá verificar o código do projeto em busca de erros, padrões de estilo e possíveis melhorias.

## Executando a Aplicação com pipx

Se preferir usar o **pipx** para rodar pacotes como o **Uvicorn** em um ambiente isolado, siga os seguintes passos:

### Instalar Uvicorn com pipx

Primeiro, instale o **Uvicorn** com pipx:

```bash
pipx install uvicorn
```

### Rodar a aplicação

Depois de instalado, você pode rodar o servidor com o seguinte comando:

```bash
pipx run uvicorn app.main:app --reload
```

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

```
.
├── app/
│   ├── main.py          # Arquivo principal da aplicação FastAPI
│   └── ...              # Outros arquivos de implementação da API
├── pyproject.toml       # Arquivo de configuração do Poetry
├── poetry.lock          # Arquivo gerado pelo Poetry com as dependências exatas
├── tests/               # Diretório contendo os testes
│   ├── test_main.py     # Exemplo de teste
│   └── ...              # Outros arquivos de testes
├── taskipy.ini          # Arquivo de configuração das tarefas do Taskipy
└── README.md            # Este arquivo
```

### Descrição dos principais arquivos:

- **app/main.py**: Arquivo principal contendo a definição da aplicação FastAPI.
- **pyproject.toml**: Arquivo de configuração do Poetry, onde são definidas as dependências e configurações do projeto.
- **taskipy.ini**: Arquivo de configuração do Taskipy, onde você pode definir tarefas automatizadas, como lint, testes, entre outros.
- **tests/**: Diretório onde os testes são armazenados.

## Contribuições

Contribuições são bem-vindas! Caso queira contribuir para o projeto, basta seguir os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma branch para a sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas alterações (`git commit -am 'Adiciona nova feature'`).
4. Envie para o repositório remoto (`git push origin feature/nova-feature`).
5. Abra um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
