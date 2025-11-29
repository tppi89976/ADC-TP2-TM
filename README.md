TP2 - Liga Futebol Portugal (Consola, Persistência JSON)

Este projeto é uma aplicação de consola desenvolvida em Python para gestão de utilizadores, clubes e inscrições na "Liga Futebol Portugal". A aplicação utiliza persistência em ficheiros JSON e inclui funcionalidades de logging, administração, permissões e menus dinâmicos adaptados ao tipo de utilizador.

Funcionalidades Principais:

Persistência de Dados:

Todos os dados são armazenados em ficheiros JSON na pasta data/ (users.json, clubes.json, logs.json).

Funções de leitura e escrita garantem que os ficheiros existam e que os dados sejam carregados e guardados corretamente.

Gestão de Utilizadores:

Registo de novos utilizadores com username, nome, email e password.

Login de utilizadores existentes com autenticação via hash de password (SHA-256).

Atualização de perfil e alteração de password.

Eliminação de conta com confirmação.

Um administrador padrão é criado automaticamente (username: admin, password: admin123).

Gestão de Clubes

Submissão de inscrições de clubes, bloqueando duplicados e respeitando uma data limite (INSCRICAO_DEADLINE).

Listagem de todos os clubes inscritos.

Exportação das inscrições para ficheiro CSV com timestamp.

As ações de inscrição e exportação são registadas em logs.

Administração e Logs

Administradores podem listar todas as inscrições e consultar os logs das ações realizadas.

A função de logging regista cada ação importante com timestamp, actor e detalhes.

Menus Dinâmicos

Menu para utilizadores anónimos: registo, login e sair.

Menu para utilizadores autenticados, adaptado ao role (utilizador, gestor, administrador):

Utilizador: atualizar perfil, alterar password, eliminar conta, submeter inscrição.

Gestor: visualizar equipas inscritas, exportar equipas para CSV.

Administrador: todas as funcionalidades anteriores, mais acesso completo aos logs e à listagem de todas as inscrições.

Segurança e Validações

Passwords armazenadas de forma segura com hash SHA-256.

Bloqueio de inscrições duplicadas.

Verificação do prazo máximo de submissão de inscrições.

Confirmação ao eliminar conta.

Estrutura de Código

Toda a lógica da aplicação está centralizada em app.py, incluindo funções para persistência, autenticação, logging, gestão de clubes, administração e menus interativos. Não existem módulos separados; tudo está integrado num único ficheiro para facilitar execução e testes.

Como Executar

Certifique-se que tem Python 3 instalado.

Execute a aplicação via terminal:

python app.py


O diretório data/ e os ficheiros JSON são criados automaticamente se não existirem.

Utilize o administrador padrão (admin/admin123) para aceder a funcionalidades administrativas.

Logs e Histórico

Todas as ações importantes (login, logout, registo, submissão de inscrição, exportação, alterações de perfil e password) são registadas no ficheiro logs.json.


Utilizadores (users.json): username, nome, email, role, password hash, data de criação.

Clubes (clubes.json): nome do clube, contacto, cidade, inscrito por, timestamp.

Logs (logs.json): timestamp, actor, ação, detalhes.

Considerações Finais

