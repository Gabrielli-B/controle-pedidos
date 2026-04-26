# Controle de Pedidos

Sistema de gerenciamento de produtos e pedidos desenvolvido em Python com SQLite. O projeto permite cadastrar, listar, atualizar e remover produtos, além de registrar pedidos, controlar o estoque automaticamente e gerar relatórios simples.

## 📋 Sobre o projeto

Este projeto foi desenvolvido com o objetivo de consolidar conhecimentos em:

* Programação orientada a objetos (POO)
* Modularização em Python
* Manipulação de banco de dados com SQLite
* Tratamento de exceções personalizadas
* Validações de dados
* Organização em camadas de responsabilidade

## 🚀 Funcionalidades

* Cadastro de produtos
* Listagem de produtos cadastrados
* Atualização de informações de produtos
* Remoção de produtos
* Criação de novos pedidos
* Controle de estoque
* Registro de itens por pedido
* Visualização de pedidos realizados
* Relatório de itens vendidos
* Validações de preço e estoque
* Tratamento de exceções personalizadas

## 🛠️ Tecnologias utilizadas

* Python 3
* SQLite3

## 📂 Estrutura do projeto

```text
controle-pedidos/
├── menu.py
├── manipulacaoMenu.py
├── manipulacaoBanco.py
├── funcionalidades.py
├── produto.py
├── pedidos.py
├── itensPedido.py
├── validacoes.py
├── excecao.py
├── tabelasBanco.py
└── controle_pedidos.db
```

## 🧠 Conceitos aplicados

* Classes e objetos
* Encapsulamento
* Separação de responsabilidades
* Persistência de dados
* CRUD completo
* Relacionamento entre entidades
* Tratamento de erros com exceções customizadas

## ▶️ Como executar

1. Clone este repositório:

```bash
git clone https://github.com/Gabrielli-B/controle-pedidos
```

2. Acesse a pasta do projeto:

```bash
cd controle-pedidos
```

3. Execute o arquivo principal:

```bash
python menu.py
```

## 📌 Exemplo de uso

Ao executar o sistema, você terá acesso ao seguinte menu:

```text
1 - Cadastrar Produto
2 - Listar Produtos
3 - Atualizar Produto
4 - Remover Produto
5 - Novo Pedido
6 - Ver Pedidos
7 - Relatório Pedidos
8 - Sair
```

## 🎯 Objetivo do projeto

Este projeto foi criado para praticar o desenvolvimento de aplicações em Python com integração a banco de dados, reforçando conceitos fundamentais de backend, organização de código e modelagem de sistemas.

## 📈 Possíveis melhorias futuras

* Interface gráfica
* Relatórios mais detalhados
* Busca de produtos por nome
* Cancelamento de pedidos
* Controle de usuários
* Exportação de relatórios
* Testes automatizados

