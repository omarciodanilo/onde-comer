# 1. Nível básico: core local
Tecnologias: Python, Flask, HTML, CSS e Docker.

## 1.1. Configuração e base do repositório (setup inicial)
Objetivo: garantir que o repositório esteja pronto para receber o código e ser compartilhado.

- [x] Escolher o nome do repositório (`onde-comer`).
- [x] Criar o arquivo `README.md` (descrição do projeto e como usar).
- [x] Incluir o arquivo `LICENSE` (com a licença MIT para Open Source).
- [x] Criar o arquivo `.gitignore` (para ignorar arquivos desnecessários do Python, como `.pyc` e `__pycache__`).
- [X] Criar o arquivo `requirements.txt` para listar todas as bibliotecas necessárias para rodar o projeto.
- [ ] Elaborar o conteúdo do arquivo `README.md` (descrição do projeto e como usar).

## 1.2. Mínimo Produto Viável (MVP)
Objetivo: ter um script Python que resolva a questão central (sugerir um lugar para comer).

### 1.2.1. Preparação e dados
- [X] Definir a estrutura inicial da fonte de dados.
- [X] Definir o tipo de fonte de dados (a ideia é ser o mais simples possível apenas para validar o sistema).
- [X] Criar o arquivo principal do projeto (`main.py`).
- [X] Criar a fonte de dados (escolhida lista de dicionários como fonte de dados inicial para validação).

### 1.2.2. Funcionalidade essencial
- [ ] Implementar a função principal para carregar a lista de restaurantes.
- [ ] Implementar a lógica de filtragem: remover locais que não atendam às escolhas da pessoa usuária.
- [ ] Implementar a função de sugestão: escolher um restaurante aleatoriamente entre as opções filtradas.
- [ ] Criar uma saída no console (CLI) que mostre o nome e os dados do local sugerido de forma amigável.

### 1.2.3. Teste e finalização do MVP
- [ ] Testar a sugestão com diferentes entradas (simuladas).
- [ ] Escrever uma pequena seção de "Como executar" no `README.md`.

## 1.3. Migração para interface Web
Objetivo: melhorar a experiência e a utilidade do assistente.

- [ ] Criar um pequeno Web Service simples (Flask, HTML e CSS), permitindo que o assistente seja usado por meio de uma URL em vez do console.
- [ ] Mudar a fonte de dados para um formato mais escalável (arquivo CSV ou JSON).
- [ ] Testar novamente o sistema.

## 1.4. Empacotamento e replicação
Objetivo: permitir que o aplicativo e suas dependências sejam replicados de forma padronizada e segura.

- [ ] Verificar imagem na Chainguard para o Flask.
- [ ] Elaborar Dockerfile para criar um servidor Flask.
- [ ] Migrar aplicativo para o Docker, através do Dockerfile criado.
- [ ] Testar aplicativo.
