---
layout: lecture
type: lecture
date: 2025-08-13
title: Configurando Ambiente a partir de um Projeto GitHub
tldr: "Como clonar um repositório e configurar todo o ambiente de desenvolvimento do projeto."
thumbnail: /static_files/presentations/gpp_mds.png
permalink: /lectures/Lec7/
hide_from_announcments: false
links: 
    - url: https://docs.github.com/pt/repositories/creating-and-managing-repositories/cloning-a-repository
      name: Documentação Git Clone
    - url: https://code.visualstudio.com/docs
      name: VS Code Docs
---

# Tutorial: Instalando e Executando Projetos do GitHub

Bem-vindo! Neste tutorial, você vai aprender a baixar (clonar) projetos do GitHub para seu computador e executá-los localmente. Ao final, você saberá como pegar qualquer projeto público do GitHub e fazê-lo funcionar na sua máquina.

**O que você vai conseguir:** Baixar um projeto real do GitHub e executá-lo no seu computador.

**Tempo estimado:** 30-45 minutos

**Pré-requisitos:** 
- Git instalado e configurado (veja o tutorial anterior)
- Ubuntu instalado
- Conexão com a internet

---

## Parte 1: Entendendo a Estrutura de um Projeto

Antes de clonar projetos, vamos entender o que procurar.

### Passo 1: Acessar um projeto exemplo no GitHub

Abra seu navegador e vá para: [github.com/microsoft/Web-Dev-For-Beginners](https://github.com/microsoft/Web-Dev-For-Beginners)

Este é um projeto de exemplo que vamos usar para aprender.

### Passo 2: Identificar arquivos importantes

**O que você deve ver:** A página principal do repositório com vários arquivos e pastas.

Procure por estes arquivos importantes (nem todo projeto tem todos):

- **README.md** - Explicações sobre o projeto (SEMPRE leia primeiro!)
- **LICENSE** - Licença do projeto
- **package.json** - Projeto Node.js/JavaScript
- **requirements.txt** - Projeto Python
- **pom.xml** ou **build.gradle** - Projeto Java
- **.gitignore** - Arquivos que o Git ignora
- **Dockerfile** - Configuração Docker

### Passo 3: Ler o README

1. Role a página para baixo
2. Leia o README.md que aparece automaticamente

**O que procurar no README:**
- Descrição do projeto
- Pré-requisitos necessários
- Instruções de instalação
- Como executar o projeto
- Exemplos de uso

**Regra de ouro:** SEMPRE leia o README antes de tentar executar qualquer projeto!

---

## Parte 2: Clonando Seu Primeiro Projeto

Vamos praticar clonando um projeto simples de página web.

### Passo 4: Encontrar a URL do repositório

1. No repositório do GitHub, procure o botão verde "Code"
2. Clique nele

**O que você deve ver:** Um menu com opções HTTPS, SSH e GitHub CLI.

### Passo 5: Copiar a URL

Escolha uma das opções:

**Opção A - HTTPS (mais fácil):**
1. Certifique-se que "HTTPS" está selecionado
2. Clique no ícone de copiar ao lado da URL

**Opção B - SSH (se você configurou SSH):**
1. Clique em "SSH"
2. Clique no ícone de copiar

A URL será algo como:
- HTTPS: `https://github.com/usuario/projeto.git`
- SSH: `git@github.com:usuario/projeto.git`

### Passo 6: Criar uma pasta para seus projetos

Abra o terminal (`Ctrl + Alt + T`) e digite:

```bash
mkdir ~/projetos
cd ~/projetos
```

**O que você fez:** Criou uma pasta chamada "projetos" na sua home e entrou nela.

### Passo 7: Clonar o repositório

Cole a URL que você copiou no comando:

```bash
git clone https://github.com/microsoft/Web-Dev-For-Beginners.git
```

**O que você deve ver:** 
- Mensagens de progresso
- "Cloning into 'Web-Dev-For-Beginners'..."
- Uma barra de progresso
- "done."

**Tempo de espera:** Varia conforme o tamanho do projeto (10 segundos a alguns minutos).

### Passo 8: Entrar na pasta do projeto

```bash
cd Web-Dev-For-Beginners
```

### Passo 9: Listar os arquivos

```bash
ls -la
```

**O que você deve ver:** Todos os arquivos e pastas do projeto, incluindo a pasta oculta `.git`.

Parabéns! Você clonou seu primeiro projeto! ✓

---

## Parte 3: Executando um Projeto HTML/CSS/JavaScript Simples

Vamos criar e executar um projeto web básico para praticar.

### Passo 10: Criar um projeto de teste simples

Vamos criar nosso próprio projeto simples:

```bash
cd ~/projetos
mkdir meu-site-teste
cd meu-site-teste
```

### Passo 11: Criar um arquivo HTML

```bash
cat > index.html << 'EOF'
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu Primeiro Site</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Olá, GitHub!</h1>
        <p>Este é meu primeiro projeto clonado e executado.</p>
        <button onclick="mudaCor()">Clique aqui</button>
    </div>
    <script src="script.js"></script>
</body>
</html>
EOF
```

### Passo 12: Criar um arquivo CSS

```bash
cat > style.css << 'EOF'
body {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.container {
    background: white;
    padding: 40px;
    border-radius: 10px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    text-align: center;
}

button {
    background: #667eea;
    color: white;
    border: none;
    padding: 15px 30px;
    font-size: 16px;
    border-radius: 5px;
    cursor: pointer;
    margin-top: 20px;
}

button:hover {
    background: #764ba2;
}
EOF
```

### Passo 13: Criar um arquivo JavaScript

```bash
cat > script.js << 'EOF'
function mudaCor() {
    const cores = ['#667eea', '#f093fb', '#4facfe', '#43e97b', '#fa709a'];
    const corAleatoria = cores[Math.floor(Math.random() * cores.length)];
    document.body.style.background = corAleatoria;
    alert('Cor mudada!');
}
EOF
```

### Passo 14: Abrir o projeto no navegador

Para projetos HTML simples, você pode abrir diretamente:

```bash
firefox index.html
```

ou

```bash
google-chrome index.html
```

**O que você deve ver:** Uma página bonita com um botão. Clique no botão para ver a mágica! ✓

---

## Parte 4: Executando um Projeto Python

Agora vamos aprender a executar projetos Python.

### Passo 15: Verificar se Python está instalado

```bash
python3 --version
```

**O que você deve ver:** Algo como "Python 3.10.12"

Se não estiver instalado:

```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

### Passo 16: Criar um projeto Python de exemplo

```bash
cd ~/projetos
mkdir calculadora-python
cd calculadora-python
```

### Passo 17: Criar o arquivo Python

```bash
cat > calculadora.py << 'EOF'
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def main():
    print("=== Calculadora Simples ===")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    
    escolha = input("\nEscolha uma operação (1-4): ")
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if escolha == '1':
        print(f"\nResultado: {somar(num1, num2)}")
    elif escolha == '2':
        print(f"\nResultado: {subtrair(num1, num2)}")
    elif escolha == '3':
        print(f"\nResultado: {multiplicar(num1, num2)}")
    elif escolha == '4':
        print(f"\nResultado: {dividir(num1, num2)}")
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
EOF
```

### Passo 18: Executar o programa Python

```bash
python3 calculadora.py
```

**O que você deve ver:** Um menu interativo. Teste fazendo algumas operações!

Para sair, apenas conclua uma operação ou pressione `Ctrl + C`.

Você executou seu primeiro programa Python! ✓

### Passo 19: Criar um arquivo requirements.txt

Projetos Python maiores usam bibliotecas externas. Vamos ver como funcionam:

```bash
cat > requirements.txt << 'EOF'
requests==2.31.0
colorama==0.4.6
EOF
```

### Passo 20: Instalar dependências Python

```bash
pip3 install -r requirements.txt
```

**O que você deve ver:** Mensagens de instalação das bibliotecas.

**O que você fez:** Instalou as dependências que o projeto precisa. ✓

---

## Parte 5: Executando um Projeto Node.js

Projetos JavaScript modernos usam Node.js. Vamos aprender a executá-los.

### Passo 21: Instalar Node.js e npm

```bash
sudo apt update
sudo apt install nodejs npm -y
```

### Passo 22: Verificar a instalação

```bash
node --version
npm --version
```

**O que você deve ver:** Números de versão para ambos.

### Passo 23: Criar um projeto Node.js de exemplo

```bash
cd ~/projetos
mkdir app-node
cd app-node
```

### Passo 24: Inicializar um projeto Node.js

```bash
npm init -y
```

**O que você deve ver:** Um arquivo `package.json` foi criado.

### Passo 25: Instalar uma dependência

```bash
npm install express
```

**O que você deve ver:** 
- Uma pasta `node_modules` sendo criada
- Um arquivo `package-lock.json` sendo criado
- Mensagens de instalação

**O que aconteceu:** O npm baixou a biblioteca Express e todas as suas dependências.

### Passo 26: Criar um servidor web simples

```bash
cat > server.js << 'EOF'
const express = require('express');
const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
    res.send(`
        <html>
            <head>
                <title>Servidor Node.js</title>
                <style>
                    body {
                        font-family: Arial;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    }
                    .card {
                        background: white;
                        padding: 40px;
                        border-radius: 10px;
                        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
                    }
                </style>
            </head>
            <body>
                <div class="card">
                    <h1>🚀 Servidor Node.js Funcionando!</h1>
                    <p>Você está executando um projeto do GitHub!</p>
                </div>
            </body>
        </html>
    `);
});

app.listen(PORT, () => {
    console.log(`✅ Servidor rodando em http://localhost:${PORT}`);
    console.log('Pressione Ctrl+C para parar');
});
EOF
```

### Passo 27: Executar o servidor

```bash
node server.js
```

**O que você deve ver:** "✅ Servidor rodando em http://localhost:3000"

### Passo 28: Acessar no navegador

Abra seu navegador e vá para: `http://localhost:3000`

**O que você deve ver:** Uma página bonita confirmando que o servidor está funcionando!

Para parar o servidor, volte ao terminal e pressione `Ctrl + C`.

Você executou um servidor Node.js! ✓

---

## Parte 6: Clonando e Executando um Projeto Real do GitHub

Agora vamos aplicar tudo que aprendemos em um projeto real.

### Passo 29: Escolher um projeto para clonar

Vamos clonar um projeto de lista de tarefas (To-Do List) simples:

```bash
cd ~/projetos
git clone https://github.com/docker/getting-started-app.git
cd getting-started-app
```

### Passo 30: Ler o README

```bash
cat README.md
```

ou

```bash
less README.md
```

(Pressione `q` para sair do less)

**O que procurar:** 
- Seção "Prerequisites" (pré-requisitos)
- Seção "Getting Started" ou "Installation"
- Seção "Running" ou "Usage"

### Passo 31: Verificar o tipo de projeto

```bash
ls -la
```

**Identifique o tipo:**
- Se tem `package.json` → Projeto Node.js
- Se tem `requirements.txt` → Projeto Python
- Se tem `index.html` → Projeto web estático
- Se tem `Dockerfile` → Projeto Docker
- Se tem `pom.xml` → Projeto Java
- Se tem `Gemfile` → Projeto Ruby

### Passo 32: Instalar dependências (exemplo Node.js)

Para este projeto específico:

```bash
npm install
```

**O que você deve ver:** Instalação de várias dependências.

### Passo 33: Executar o projeto

Procure no `package.json` por scripts disponíveis:

```bash
cat package.json | grep -A 5 "scripts"
```

**O que você deve ver:** Scripts como "start", "dev", "build", etc.

Para executar:

```bash
npm start
```

ou

```bash
npm run dev
```

(Depende do projeto)

### Passo 34: Acessar a aplicação

Se o projeto iniciar um servidor, você verá algo como:
- "Server running on port 3000"
- "Listening on http://localhost:3000"

Abra o navegador e acesse a URL indicada.

---

## Parte 7: Resolvendo Problemas Comuns

### Problema 1: "comando não encontrado"

**Erro:** `bash: node: command not found`

**Solução:** Instale a ferramenta necessária:

```bash
# Para Node.js
sudo apt install nodejs npm

# Para Python
sudo apt install python3 python3-pip

# Para Git
sudo apt install git
```

### Problema 2: "permissão negada"

**Erro:** `Permission denied`

**Solução:** Adicione `sudo` antes do comando (apenas se for realmente necessário):

```bash
sudo comando-aqui
```

### Problema 3: "porta já em uso"

**Erro:** `Port 3000 is already in use`

**Solução:** Mate o processo que está usando a porta:

```bash
# Encontrar o processo
sudo lsof -i :3000

# Matar o processo (substitua PID pelo número que apareceu)
kill -9 PID
```

Ou use outra porta no arquivo de configuração.

### Problema 4: Dependências faltando

**Erro:** `Cannot find module 'express'`

**Solução:** Instale as dependências:

```bash
# Node.js
npm install

# Python
pip3 install -r requirements.txt
```

### Problema 5: Versão incompatível

**Erro:** `Requires Node.js version 16 or higher`

**Solução:** Atualize a ferramenta ou use um gerenciador de versões:

```bash
# Para Node.js (usando nvm)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc
nvm install 18
nvm use 18
```

---

## Parte 8: Boas Práticas ao Executar Projetos

### Passo 35: Sempre criar ambientes virtuais (Python)

Para projetos Python, use ambientes virtuais:

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar (Linux/Ubuntu)
source venv/bin/activate

# Agora instalar dependências
pip install -r requirements.txt

# Desativar quando terminar
deactivate
```

**Por quê?** Mantém as dependências isoladas e evita conflitos.

### Passo 36: Verificar o arquivo .gitignore

```bash
cat .gitignore
```

**O que você deve ver:** Lista de arquivos/pastas que o Git ignora.

Itens comuns:
- `node_modules/` - dependências Node.js (não deve ser commitado)
- `venv/` - ambiente virtual Python
- `.env` - variáveis de ambiente (senhas, chaves)
- `dist/` - arquivos compilados

**Importante:** Nunca commite pastas como `node_modules` ou `venv`!

### Passo 37: Procurar por arquivos de configuração

Projetos podem precisar de configuração:

```bash
# Procurar por exemplos de configuração
ls -la | grep example
ls -la | grep sample
```

Comum encontrar:
- `.env.example` → copie para `.env` e edite
- `config.sample.json` → copie para `config.json` e edite

Exemplo:

```bash
cp .env.example .env
nano .env  # Edite as configurações
```

---

## 🎉 Parabéns!

Você completou o tutorial de instalação e execução de projetos do GitHub! Agora você sabe:

✓ Clonar repositórios do GitHub  
✓ Identificar o tipo de projeto  
✓ Ler e seguir instruções do README  
✓ Instalar dependências de diferentes linguagens  
✓ Executar projetos HTML/CSS/JS, Python e Node.js  
✓ Resolver problemas comuns  
✓ Aplicar boas práticas  

---

## Checklist: Executando Qualquer Projeto do GitHub

Use esta lista sempre que for executar um projeto novo:

**□ Passo 1:** Clone o repositório
```bash
git clone URL_DO_REPO
cd nome-do-projeto
```

**□ Passo 2:** Leia o README
```bash
cat README.md
```

**□ Passo 3:** Identifique o tipo de projeto
```bash
ls -la
```

**□ Passo 4:** Verifique pré-requisitos
- Node.js instalado? `node --version`
- Python instalado? `python3 --version`
- Outras ferramentas necessárias?

**□ Passo 5:** Instale dependências

*Para Node.js:*
```bash
npm install
```

*Para Python:*
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**□ Passo 6:** Configure variáveis de ambiente (se necessário)
```bash
cp .env.example .env
nano .env
```

**□ Passo 7:** Execute o projeto

*Para Node.js:*
```bash
npm start
# ou
npm run dev
```

*Para Python:*
```bash
python3 app.py
# ou
python3 main.py
```

*Para HTML estático:*
```bash
firefox index.html
```

**□ Passo 8:** Acesse no navegador (se aplicável)
```
http://localhost:PORTA
```

---

## Comandos de Referência Rápida

### Git
```bash
# Clonar repositório
git clone URL

# Ver status
git status

# Atualizar repositório
git pull
```

### Node.js
```bash
# Instalar dependências
npm install

# Executar scripts
npm start
npm run dev
npm run build

# Instalar pacote específico
npm install nome-pacote
```

### Python
```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Executar script
python3 arquivo.py

# Desativar ambiente virtual
deactivate
```

### Úteis
```bash
# Ver processos na porta
sudo lsof -i :3000

# Matar processo
kill -9 PID

# Ver versão de ferramentas
node --version
python3 --version
git --version
```

---

## Projetos Recomendados para Praticar

Aqui estão alguns projetos iniciantes para você clonar e executar:

### HTML/CSS/JavaScript
1. **Calculator** - `github.com/topics/calculator`
2. **To-Do List** - `github.com/topics/todo-list`
3. **Weather App** - `github.com/topics/weather-app`

### Python
1. **Snake Game** - `github.com/topics/snake-game`
2. **Quiz App** - `github.com/topics/quiz-app`
3. **Password Generator** - `github.com/topics/password-generator`

### Node.js
1. **Chat App** - `github.com/topics/chat-application`
2. **Blog** - `github.com/topics/blog`
3. **API REST** - `github.com/topics/rest-api`

**Dica:** No GitHub, use a busca com filtros:
- Linguagem: JavaScript, Python, etc.
- Stars: >100 (projetos populares)
- Topics: iniciante, tutorial

---

## Próximos Passos

Agora que você domina a execução de projetos, pode:

1. **Contribuir para projetos open source** fazendo forks e pull requests
2. **Modificar projetos existentes** para aprender como funcionam
3. **Criar seus próprios projetos** e publicar no GitHub
4. **Explorar Docker** para executar projetos em containers
5. **Aprender CI/CD** para automatizar deploys

Continue praticando! Cada projeto que você executa ensina algo novo. 🚀