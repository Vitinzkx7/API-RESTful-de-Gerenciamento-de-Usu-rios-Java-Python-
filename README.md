# API de Gerenciamento de Usuários (Java + Python)

Sistema que permite o gerenciamento de usuários via API REST (Java + Spring Boot) e geração de relatórios estatísticos em Python com Pandas.

## Tecnologias Utilizadas
- Java + Spring Boot
- Python + Pandas
- PostgreSQL (ou outro banco relacional)
- Docker (recomendado)

## Como Usar

### Backend Java
```bash
cd java_backend
./mvnw spring-boot:run
```

### Python Reports
```bash
cd python_reports
python3 generate_report.py
```

## Funcionalidades
- CRUD de usuários via API
- Autenticação (JWT recomendada)
- Geração de relatórios de usuários com Python
