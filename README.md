# New Cycle

[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)

Descrição curta do projeto.

## Tecnologias Utilizadas

- Python
- Flask
- PostgreSQL
- SQLAlchemy
- Docker
- Docker Compose

## Visão Geral

O projeto New Cycle é uma aplicação web que permite a criação de uma rede social voltada para profissionais e empresas. A plataforma permite que profissionais encontrem oportunidades de emprego e empresas possam ofertar essas oportunidades. O objetivo principal é quebrar ciclos de pobreza e gerar novos caminhos melhores para todos.

## Pré-requisitos

- Python 3.x
- Docker
- Docker Compose

## Configuração do Ambiente

1. Clone o repositório para sua máquina local: `git clone https://github.com/RafaelFino/new-cycle.git`
2. Navegue até o diretório do projeto: `cd new-cycle`
3. Instale as dependências Python executando o comando: `pip3 install -r requirements.txt`
4. Inicie o ambiente Docker usando o comando: `docker-compose up -d`
5. Execute as migrações do banco de dados usando o comando: `python3 manage.py db upgrade`

## Executando a Aplicação

1. Execute o comando: `python3 app.py` para iniciar o servidor Flask.
2. Acesse a aplicação em seu navegador através do endereço: `http://localhost:5000`

## Estrutura do Projeto

A estrutura de pastas e arquivos do projeto é a seguinte:

- `/app.py`: Arquivo principal da aplicação que inicia o servidor Flask.
- `/config.py`: Arquivo de configuração com as variáveis de ambiente e configurações da aplicação.
- `/database.py`: Configuração do banco de dados e definição dos modelos SQLAlchemy.
- `/routes.py`: Arquivo com as rotas e controladores da aplicação.
- `/templates/`: Pasta contendo os templates HTML da aplicação.
- `/static/`: Pasta contendo os arquivos estáticos (CSS, JS, imagens) da aplicação.
- `/tests/`: Pasta contendo os testes unitários da aplicação.
- `/docker-compose.yml`: Arquivo de configuração do Docker Compose para executar o ambiente de desenvolvimento.
- `/requirements.txt`: Arquivo com as dependências Python do projeto.

## Modelo de Dados

A aplicação utiliza o seguinte modelo de dados:

| Modelo | Campo       | Tipo      | Tamanho (bytes) | Obrigatório |
|--------|-------------|-----------|-----------------|-------------|
| Candidate | ID            | Integer   |                 | Sim         |
| Candidate | PassHash     | String    | 255             | Sim         |
| Candidate | Visible      | Boolean   |                 | Sim         |
| Candidate | CreatedAt    | Date      |                 | Sim         |
| Candidate | UpdatedAt    | Date      |                 | Sim         |
| Candidate | Valid        | Boolean   |                 | Sim         |
| CandidateDetails | CandidateID | Integer   |                 | Sim         |
| CandidateDetails | Name         | String    | 255             | Sim         |
| CandidateDetails | LocationID   | String    | 255             | Sim         |
| CandidateDetails | CreatedAt   | Date      |                 | Sim         |
| CandidateDetails | UpdatedAt   | Date      |                 | Sim         |
| CandidateDetails | Valid       | Boolean   |                 | Sim         |
| Location | ID           | Integer   |                 | Sim         |
| Location | Address      | String    | 255             | Sim         |
| Location | Number       | String    | 20              | Sim         |
| Location | Neighborhood | String    | 255             | Sim         |
| Location | Country      | String    | 255             | Sim         |
| Location | State        | String    | 255             | Sim         |
| Location | City         | String    | 255             | Sim         |
| Location | ZipCode      | String    | 20              | Sim         |
| Location | CreatedAt    | Date      |                 | Sim         |
| Location | UpdatedAt    | Date      |                 | Sim         |
| Location | Valid        | Boolean   |                 | Sim         |
| CandidateDocument | ID         | Integer   |                 | Sim         |
| CandidateDocument | CandidateID | Integer   |                 | Sim         |
| CandidateDocument | Type       | String    | 20              | Sim         |
| CandidateDocument | Value      | String    | 255             | Sim         |
| CandidateDocument | ExpireAt   | Date      |                 | Sim         |
| CandidateDocument | CreatedAt | Date      |                 | Sim         |
| CandidateDocument | UpdatedAt | Date      |                 | Sim         |
| CandidateDocument | Valid     | Boolean   |                 | Sim         |
| CandidateContact | ID          | Integer   |                 | Sim         |
| CandidateContact | CandidateID | Integer   |                 | Sim         |
| CandidateContact | Type        | String    | 20              | Sim         |
| CandidateContact | Value       | String    | 255             | Sim         |
| CandidateContact | CreatedAt  | Date      |                 | Sim         |
| CandidateContact | UpdatedAt  | Date      |                 | Sim         |
| CandidateContact | Valid      | Boolean   |                 | Sim         |
| Experience | ID           | Integer   |                 | Sim         |
| Experience | CandidateID  | Integer   |                 | Sim         |
| Experience | EmployerName | String    | 255             | Sim         |
| Experience | Description  | Text      |                 | Sim         |
| Experience | StartedAt    | Date      |                 | Sim         |
| Experience | EndedAt      | Date      |                 | Sim         |
| Experience | CreatedAt    | Date      |                 | Sim         |
| Experience | UpdatedAt    | Date      |                 | Sim         |
| Experience | Valid        | Boolean   |                 | Sim         |
| Skill | ID               | Integer   |                 | Sim         |
| Skill | Name             | String    | 255             | Sim         |
| Skill | MaxValue         | Integer   |                 | Sim         |
| Skill | Kind             | String    | 20              | Sim         |
| SkillItem | ID           | Integer   |                 | Sim         |
| SkillItem | SkillID       | Integer   |                 | Sim         |
| SkillItem | Name         | String    | 255             | Sim         |
| SkillItem | Value        | Integer   |                 | Sim         |
| SkillItem | StartedAt     | Date      |                 | Sim         |
| SkillItem | EndedAt       | Date      |                 | Sim         |
| SkillItem | CreatedAt     | Date      |                 | Sim         |
| SkillItem | UpdatedAt     | Date      |                 | Sim         |
| SkillItem | Valid         | Boolean   |                 | Sim         |
| CandidateSkill | CandidateID | Integer   |                 | Sim         |
| CandidateSkill | SkillItemID | Integer   |                 | Sim         |
| CandidateSkill | StartedAt   | Date      |                 | Sim         |
| CandidateSkill | CreatedAt   | Date      |                 | Sim         |
| CandidateSkill | UpdatedAt   | Date      |                 | Sim         |
| CandidateSkill | Valid       | Boolean   |                 | Sim         |
| Employer | ID            | Integer   |                 | Sim         |
| Employer | Name          | String    | 255             | Sim         |
| Employer | LocationID    | String    | 255             | Sim         |
| Employer | StartedAt     | Date      |                 | Sim         |
| Proposal | ID            | Integer   |                 | Sim         |
| Proposal | EmployerID    | Integer   |                 | Sim         |
| Proposal | Title         | String    | 255             | Sim         |
| Proposal | Description   | Text      |                 | Sim         |
| Proposal | ContractType  | String    | 20              | Sim         |
| Proposal | ContractDuration | String | 20              | Sim         |
| Proposal | ContractDurationTime | String | 20          | Sim         |
| Proposal | PartTime      | Boolean   |                 | Sim         |
| Proposal | Remote        | Boolean   |                 | Sim         |
| Proposal | ExpireAt      | Date      |                 | Sim         |
| Proposal | StartedAt     | Date      |                 | Sim         |
| Proposal | CreatedAt     | Date      |                 | Sim         |
| Proposal | UpdatedAt     | Date      |                 | Sim         |
| Proposal | Valid         | Boolean   |                 | Sim         |
| ProposalRequirements | ID      | Integer   |                 | Sim         |
| ProposalRequirements | ProposalID | Integer |                 | Sim         |
| ProposalRequirements | SkillID | Integer   |                 | Sim         |
| ProposalRequirements | Required | Boolean |                 | Sim         |
| ProposalRequirements | MinAcceptValue | Integer |            | Sim         |
| ProposalRequirements | MinExperience | Integer | Default 0   | Sim         |
| ProposalRequirements | Priority | Integer   |                 | Sim         |
| ProposalRequirements | StartedAt | Date      |                 | Sim         |
| ProposalRequirements | CreatedAt | Date      |                 | Sim         |
| ProposalRequirements | UpdatedAt | Date      |                 | Sim         |
| ProposalRequirements | Valid | Boolean   |                 | Sim         |
| Remuneration | ID               | Integer   |                 | Sim         |
| Remuneration | Description      | String    | 255             | Sim         |
| Remuneration | Currency         | String    | 20              | Sim         |
| Remuneration | Occurrency       | String    | 20              | Sim         |
| Remuneration | Type             | String    | 20              | Sim         |
| Remuneration | CreatedAt        | Date      |                 | Sim         |
| Remuneration | UpdatedAt        | Date      |                 | Sim         |
| Remuneration | Valid            | Boolean   |                 | Sim         |
| ProposalRemuneration | ID        | Integer   |                 | Sim         |
| ProposalRemuneration | ProposalID | Integer |                 | Sim         |
| ProposalRemuneration | RemunerationID | Integer |             | Sim         |
| ProposalRemuneration | MinValue   | Integer   |                 | Sim         |
| ProposalRemuneration | MaxValue   | Integer   |                 | Sim         |
| ProposalRemuneration | CreatedAt  | Date      |                 | Sim         |
| ProposalRemuneration | UpdatedAt  | Date      |                 | Sim         |
| ProposalRemuneration | Valid      | Boolean   |                 | Sim         |
| Match | ID                     | Integer   |                 | Sim         |
| Match | ProposalID             | Integer   |                 | Sim         |
| Match | CandidateID            | Integer   |                 | Sim         |
| Match | CandidateResult        | Boolean   |                 | Sim         |
| Match | EmployerResult         | Boolean   |                 | Sim         |
| Match | CandidateReview        | String    | 255             | Sim         |
| Match | EmployerReview         | String    | 255             | Sim         |
| Match | Status                 | String    | 20              | Sim         |
| Match | CreatedAt              | Date      |                 | Sim         |
| Match | UpdatedAt              | Date      |                 | Sim         |
| Match | Valid                  | Boolean   |                 | Sim         |

