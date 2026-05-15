# Instruções

## Instalar dependências

Windows
```
python -m venv venv
venv/bin/activate
pip install .

```

Linux
```
python3 -m venv .venv
. venv/bin/activate
pip install .

```

## Inicializar banco (sqlite)
(venv)

Criar as tabelas do banco, um arquivo "db.sqlite3" vai ser criado.
```
python manage.py migrate
```

Criar um usuário admin, é obrigatório fazer um login para usar qualquer endpoint, então um "superusuário" é obrigatório.
```
pytohn manage.py createsuperuser
```

## Executar
(venv)

```
python manage.py runserver
```

E a API estará rodando!

## Usar a API

### Documentação em .yml
Foi gerado automaticamente no modelo OpenAPI 3.0 uma especificação em .yml da api, está no arquivo "schema.yml".