# api_forum

## Objetivo do Projeto:

Construir uma API para um fórum online, permitindo que os usuários criem tópicos, façam postagens e interajam com outros membros.

## Funcionalidades Principais:

### Usuários:
- Implementar um sistema de autenticação para permitir que os usuários se registrem, façam login e gerenciem seus perfis.
- Adicionar campos como nome de usuário, email e senha para os usuários.

### Tópicos:
- Permitir que os usuários criem tópicos no fórum.
- Associar cada tópico a um autor e registrar a data de criação.

### Postagens:
- Possibilitar que os usuários façam postagens dentro de tópicos.
- Registrar o autor, a data da postagem e o conteúdo do post.

### Comentários:
- Adicionar funcionalidade para os usuários comentarem em postagens.
- Registrar o autor, a data do comentário e o conteúdo do comentário.

### Votação:
- Implementar um sistema de votação para tópicos e comentários.
- Permitir que os usuários votem positivamente ou negativamente.

### Filtros e Ordenação:
- Adicionar opções de filtragem e ordenação para tópicos e postagens (por data, votos, etc.).

### Notificações:
- Implementar um sistema de notificação para alertar os usuários sobre novas postagens em tópicos que estão seguindo.

### Pesquisa:
- Adicionar uma funcionalidade de pesquisa para permitir que os usuários encontrem tópicos ou postagens relevantes.

## Tecnologias Utilizadas:

- Django e Django REST framework:
    - Utilize o Django para a estrutura geral do projeto.
    - Faça uso extensivo do Django REST framework para criar a API RESTful.

- Banco de Dados:
    - Escolha um banco de dados como o PostgreSQL ou SQLite para armazenar dados do fórum.

- Autenticação:
    - Implemente autenticação com tokens JWT para proteger rotas sensíveis.

- Testes:
    - Escreva testes unitários e de integração para garantir a robustez da API.

- Documentação:
    - Utilize ferramentas como coreapi e drf-yasg para criar documentação automática da API.

## Fluxo de Desenvolvimento Sugerido:

1. Configuração do Projeto:
    Configure um novo projeto Django **done**.
    Instale e configure o Django REST framework **done**.

2. Modelagem de Dados:
    Crie modelos para usuários, tópicos, postagens, comentários e votos **done**.

3. Serializers:
    Desenvolva Serializers para cada modelo **done**.

4. Views e Roteamento:
    Implemente Views para realizar operações CRUD nos modelos.
    Configure rotas para as Views usando Roteadores do DRF.

5. Autenticação e Permissões:
    Configure autenticação JWT para proteger rotas.
    Defina permissões para controlar o acesso aos recursos.

6. Implementação de Funcionalidades:
    Adicione lógica para criação de tópicos, postagens, comentários e votos.
    Desenvolva as funcionalidades de notificação, pesquisa e ordenação.

7. Testes e Documentação:
    Escreva testes abrangentes.
    Crie documentação detalhada da API.

8. Refatoração e Melhorias:
    Refatore o código conforme necessário.
    Adicione recursos extras ou melhore a usabilidade.