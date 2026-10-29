# Campeonato de Futsal

Projeto Django para gerenciamento de um campeonato de futsal com times, jogadores, partidas e tabela.

## Tecnologias

- Python
- Django
- SQLite

## Como executar

1. Ative o ambiente virtual:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

2. Rode o servidor:
   ```powershell
   python manage.py runserver
   ```

3. Acesse no navegador:
   ```text
   http://127.0.0.1:8000/
   ```

## Painel administrativo

Acesse:

```text
http://127.0.0.1:8000/admin/
```

Crie um superusuário com:

```powershell
python manage.py createsuperuser
```

## Estrutura principal

- `campeonato/` - app do campeonato
- `futsal_project/` - configuração do projeto Django
- `manage.py` - comando principal do Django

## Observações

Este projeto foi desenvolvido para servir como base para um campeonato de futsal com interface e cadastro de dados.
