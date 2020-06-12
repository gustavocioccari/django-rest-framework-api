Como utilizar:

Dentro da pasta 'restapi' utilize o comando
    'pip install pipenv' (Apenas se não tiver pipenv instalado)
    'pipenv install Pipfile'
    'python manage.py runserver'

Endpoints:

/users/ - Retorna todos os usuários
/users/user_id - Retorna usuário especificado pelo id
/salaries/ - Retorna todos os salários
/salaries/?user_pk=user_id - Retorna dados de salário do usuário especificado pelo id