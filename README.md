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

```python
# Candidate
class Candidate(db.Model):
    # Atributos do modelo

# CandidateDetails
class CandidateDetails(db.Model):
    # Atributos do modelo

# Location
class Location(db.Model):
    # Atributos do modelo

# CandidateDocument
class CandidateDocument(db.Model):
    # Atributos do modelo

# CandidateContact
class CandidateContact(db.Model):
    # Atributos do modelo

# Experience
class Experience(db.Model):
    # Atributos do modelo

# Skill
class Skill(db.Model):
    # Atributos do modelo

# SkillItem
class SkillItem(db.Model):
    # Atributos do modelo

# CandidateSkill
class CandidateSkill(db.Model):
    # Atributos do modelo

# Employer
class Employer(db.Model):
    # Atributos do modelo

# Proposal
class Proposal(db.Model):
    # Atributos do modelo

# ProposalRequirements
class ProposalRequirements(db.Model):
    # Atributos do modelo

# Remuneration
class Remuneration(db.Model):
    # Atributos do modelo

# ProposalRemuneration
class ProposalRemuneration(db.Model):
    # Atributos do modelo

# Match
class Match(db.Model):
    # Atributos do modelo
