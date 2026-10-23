# Beton Dekor

Aplicação web em Django desenvolvida e entregue para uma empresa do setor de construção civil. O sistema publica o catálogo de produtos, organiza categorias e subcategorias, recebe contatos e permite que a equipe atualize o conteúdo por uma área administrativa.

Aplicação em produção: https://betondekor.com.br/

## Funcionalidades

- Catálogo público com categorias, subcategorias e páginas individuais por produto.
- Cadastro de descrição, dimensões, cores, unidade de venda e especificações.
- Até três imagens por produto, armazenadas no Cloudinary.
- Área autenticada para criar, editar, duplicar, ordenar e remover produtos.
- Gestão de categorias e subcategorias.
- Formulário de contato com mensagens persistidas para acompanhamento.
- Interface responsiva baseada no layout aprovado pelo cliente.

## Stack

- Python e Django 6.
- Django Templates e htmx.
- PostgreSQL em produção e SQLite como alternativa local.
- Cloudinary para mídia.
- Docker Compose, Gunicorn e Nginx.
- WhiteNoise para arquivos estáticos.

## Arquitetura

```text
Navegador
   |
Nginx
   |
Gunicorn + Django
   |-------- PostgreSQL
   |-------- Cloudinary
```

O domínio principal fica no app `core`. Os modelos `CategoriaPrincipal`, `Subcategoria`, `Produto` e `MensagemContato` sustentam o catálogo e o contato. O deploy em containers separa banco, aplicação e proxy reverso.

## Execução local com Docker

1. Copie `.env.example` para `.env` e preencha as variáveis.
2. Inicie os serviços:

```bash
docker compose up --build
```

3. Aplique as migrações e crie um usuário administrativo:

```bash
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

A aplicação fica disponível em `http://localhost`.

## Execução local com Python

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Estado

O site público está em produção. Este repositório contém a aplicação Django e os arquivos usados no deploy; credenciais reais são fornecidas por variáveis de ambiente e não devem ser versionadas.
