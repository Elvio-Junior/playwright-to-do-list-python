# Objetivo
 
Este projeto tem o objetivo de demonstrar conceitos e formas de utilizar o framework Playwright para a criação de testes e2e e de API. Utilizaremos o Python

# Pré-requisitos

## Sistemas Operacionais

- macOS 11 e superiores
- Linux 
    - Ubuntu 20.04 e 22.04
    - Debian 11
- Windows e WSL

## Python
    - Python 3.8 e superiores
    - Gerenciador de Pacotes do Python (pip)

## Make
    Ferramenta para controlar a geração de executáveis a partir de arquivos fonte

# Playwright

Framework de testes automatizados construido sobre o Puppeteer. Está disponível para as seguintes linguagens de programação
    - Node.js
    - Python
    - .NET
    - Java

## Organização

O Playwright possui a seguinte organização de pastas/arquivos:
    - tests: Pasta principal dos testes. 

## Iniciar um projeto Playwright

Para iniciar um projeto de automação de testes digite pela linha de comando
    - pip install pytest-playwright
    - playwright install

# Projeto

# Instalação - Python

Para instalar os recursos necessários é necessário criar o ambiente virtual pelo comando `make env-create`

Em seguida ativar o ambiente virtual pelo comando `source py-venv/bin/activate` e instalar as dependencias pelo comando `make install`

## Execução dos Testes

Existe algumas maneiras de executar os testes, sendo:
    - Executação dos testes: `make py-test`
    - Executar testes somente com o browser Chrome: `make py-test-chromium`
    - Executar testes somente do To Do Page: `make py-test-to-do-list`
    - Executar testes somente da Api: `make py-test-api`
    - Executar testes em modo Debug: `make py-test-debug`
    - Executar relatórios dos testes: `make py-test-report`
    - Executar a geração de testes: `make py-generate-tests`

# Referências
- https://www.python.org/
- https://playwright.dev/
- https://docs.pytest.org/en/7.4.x/

# Ferramentas para o Desenvolvimento

    As seguintes ferramentas são necessárias e/ou sugeridas para o projeto

## Instalação:
- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/)

## IDE
- [VSCode](https://code.visualstudio.com/download)