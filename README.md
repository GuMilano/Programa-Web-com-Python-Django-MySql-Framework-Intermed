# Programa Web com Python + Django + MySQL (Intermediário)

Projeto **Django** com integração ao **MySQL**, cadastro e listagem de **produtos com imagens**, uso de **slug** para páginas de detalhe e uma função de **envio de e-mail**. (Evolução registrada nos commits do repositório.) :contentReference[oaicite:0]{index=0}

---

## Funcionalidades implementadas

Com base no histórico de commits, este projeto evoluiu para incluir: :contentReference[oaicite:1]{index=1}

- Cadastro de produtos (primeira versão “sem DB”, depois persistindo no banco)
- Produtos com **imagens** (pasta de mídia dedicada)
- Listagem/visualização de produtos e imagens
- Página de detalhe de produto com **slug**
- Página de produtos com acesso “privado” (variação/rota específica)
- Função de **enviar e-mail** (ex.: formulário/contato)

---

## Estrutura do repositório

Arquivos/pastas principais identificados na raiz do projeto: :contentReference[oaicite:2]{index=2}

- `core/` — app(s) do projeto (regras de negócio, views, templates, etc.)
- `django2/` — projeto Django (settings/urls/wsgi/asgi)
- `media/produtos/` — armazenamento de imagens enviadas (upload de produtos)
- `manage.py` — comandos do Django
- `requirements.txt` — dependências
- `info.txt` — anotações/informações do projeto
- `.gitignore`

> Observação: os nomes seguem a convenção típica do Django (projeto + apps), com pasta de mídia separada para uploads.

---

## Stack

- Python
- Django
- MySQL
- HTML/CSS (templates)

---

