---
layout: lecture
type: lecture
date: 2025-08-10
title: Tutorial Inicial de GitHub
tldr: "Guia completo passo a passo para configurar Git e GitHub no Ubuntu."
thumbnail: /static_files/presentations/gpp_mds.png
permalink: /lectures/Lec5/
hide_from_announcments: false
links: 
    - url: https://docs.github.com/pt/get-started
      name: Documentação Oficial
    - url: https://git-scm.com/book/pt-br/v2
      name: Pro Git Book
---

# Tutorial: Git e GitHub no Ubuntu - Sua Primeira Jornada

Bem-vindo! Neste tutorial, você vai configurar sua máquina Ubuntu para trabalhar com Git e GitHub, e criar seu primeiro projeto versionado. Ao final, você terá um repositório funcionando e saberá usar os comandos essenciais do Git.

**O que você vai criar:** Um projeto simples chamado "meu-primeiro-repo" que você vai versionar localmente e enviar para o GitHub.

**Tempo estimado:** 30-40 minutos

---

## Parte 1: Preparando Seu Ambiente Ubuntu

### Passo 1: Verificar se o Git está instalado

Abra o terminal (pressione `Ctrl + Alt + T`) e digite:

```bash
git --version
```

**O que você deve ver:** Algo como `git version 2.34.1` (o número pode variar).

Se aparecer uma mensagem de erro dizendo que o comando não foi encontrado, vamos instalar o Git no próximo passo.

### Passo 2: Instalar o Git (se necessário)

Se o Git não estiver instalado, execute estes comandos:

```bash
sudo apt update
sudo apt install git -y
```

Digite sua senha quando solicitado. Aguarde a instalação concluir.

**Verifique novamente:**

```bash
git --version
```

Agora você deve ver a versão do Git instalada. ✓

---

## Parte 2: Configurando Sua Identidade no Git

Antes de usar o Git, precisamos dizer quem você é. Isso é importante porque cada modificação que você fizer ficará registrada com seu nome.

### Passo 3: Configurar seu nome

```bash
git config --global user.name "Seu Nome Completo"
```

*Substitua "Seu Nome Completo" pelo seu nome real, mantendo as aspas.*

### Passo 4: Configurar seu email

```bash
git config --global user.email "seu.email@exemplo.com"
```

*Use o mesmo email que você vai usar no GitHub.*

### Passo 5: Ativar cores no terminal

Isso deixa os comandos Git mais fáceis de ler:

```bash
git config --global color.ui auto
```

### Passo 6: Verificar suas configurações

```bash
git config --list
```

**O que você deve ver:** Uma lista com suas configurações, incluindo seu nome e email.

---

## Parte 3: Criando Sua Conta no GitHub

### Passo 7: Criar conta no GitHub

1. Abra seu navegador e vá para [github.com](https://github.com)
2. Clique em "Sign up" (Criar conta)
3. Siga as instruções usando o **mesmo email** que você configurou no Git
4. Verifique seu email e confirme a conta

### Passo 8: Configurar autenticação SSH (recomendado)

A autenticação SSH é mais segura e prática. Vamos criar uma chave SSH:

```bash
ssh-keygen -t ed25519 -C "seu.email@exemplo.com"
```

**O que vai acontecer:** O terminal vai perguntar onde salvar a chave. Apenas pressione `Enter` para aceitar o local padrão.

Quando pedir uma senha (passphrase), você pode:
- Pressionar `Enter` duas vezes para não usar senha (mais fácil)
- Ou criar uma senha para mais segurança

### Passo 9: Copiar sua chave SSH pública

```bash
cat ~/.ssh/id_ed25519.pub
```

**O que você deve ver:** Uma linha longa começando com `ssh-ed25519`. Selecione TODO o texto e copie (Ctrl+Shift+C).

### Passo 10: Adicionar a chave no GitHub

1. No GitHub, clique na sua foto de perfil (canto superior direito) → Settings
2. No menu lateral, clique em "SSH and GPG keys"
3. Clique no botão verde "New SSH key"
4. Em "Title", escreva algo como "Meu Ubuntu"
5. Em "Key", cole a chave que você copiou
6. Clique em "Add SSH key"

### Passo 11: Testar a conexão

```bash
ssh -T git@github.com
```

Digite `yes` quando perguntar se quer continuar conectando.

**O que você deve ver:** Uma mensagem como "Hi seu-usuario! You've successfully authenticated..."

Parabéns! Você está conectado ao GitHub. ✓

---

## Parte 4: Criando Seu Primeiro Repositório Local

Agora vamos criar um projeto e usar o Git para versioná-lo.

### Passo 12: Criar um diretório para seu projeto

```bash
mkdir ~/meu-primeiro-repo
cd ~/meu-primeiro-repo
```

Você acabou de criar uma pasta e entrou nela.

### Passo 13: Inicializar o repositório Git

```bash
git init
```

**O que você deve ver:** "Initialized empty Git repository..." 

Isso transforma sua pasta em um repositório Git. ✓

### Passo 14: Criar seu primeiro arquivo

```bash
echo "# Meu Primeiro Repositório" > README.md
```

Você acabou de criar um arquivo chamado README.md com um título.

### Passo 15: Ver o status do repositório

```bash
git status
```

**O que você deve ver:** O arquivo README.md aparece em vermelho como "Untracked files" (arquivos não rastreados).

Isso significa que o Git vê o arquivo, mas ainda não está acompanhando as mudanças dele.

---

## Parte 5: Fazendo Seu Primeiro Commit

Um "commit" é como tirar uma foto do estado atual do seu projeto. É um ponto na história que você pode voltar depois.

### Passo 16: Adicionar o arquivo ao stage

```bash
git add README.md
```

Agora o arquivo está "preparado" (staged) para ser commitado.

### Passo 17: Verificar novamente o status

```bash
git status
```

**O que mudou:** Agora o arquivo aparece em verde como "Changes to be committed".

### Passo 18: Fazer o commit

```bash
git commit -m "Adiciona README inicial"
```

A mensagem entre aspas descreve o que você fez. Seja sempre descritivo!

**O que você deve ver:** Algo como "1 file changed, 1 insertion(+)".

### Passo 19: Ver o histórico

```bash
git log
```

**O que você deve ver:** Seu commit aparece com seu nome, email, data e mensagem.

Pressione `q` para sair da visualização do log.

---

## Parte 6: Fazendo Mais Mudanças

Vamos praticar o ciclo completo: modificar → adicionar → commitar.

### Passo 20: Adicionar mais conteúdo ao README

```bash
echo "Este é meu primeiro projeto com Git!" >> README.md
echo "Estou aprendendo controle de versão." >> README.md
```

### Passo 21: Ver as diferenças

```bash
git diff
```

**O que você deve ver:** As linhas que você adicionou aparecem em verde com um `+` na frente.

Pressione `q` para sair.

### Passo 22: Adicionar e commitar de uma vez

```bash
git add README.md
git commit -m "Adiciona descrição ao README"
```

### Passo 23: Ver o histórico novamente

```bash
git log
```

Agora você tem 2 commits! Veja como sua história está crescendo. ✓

---

## Parte 7: Enviando para o GitHub

Agora vamos colocar seu projeto na nuvem, no GitHub.

### Passo 24: Criar um repositório no GitHub

1. Vá para [github.com](https://github.com) e faça login
2. Clique no botão `+` (canto superior direito) → "New repository"
3. Nome do repositório: `meu-primeiro-repo`
4. Deixe como **Public**
5. **NÃO** marque "Initialize this repository with a README"
6. Clique em "Create repository"

### Passo 25: Conectar seu repositório local ao GitHub

O GitHub vai mostrar alguns comandos. Você precisa do comando que começa com `git remote add origin`. Copie sua versão, que terá seu nome de usuário, e execute:

```bash
git remote add origin git@github.com:SEU-USUARIO/meu-primeiro-repo.git
```

*Substitua SEU-USUARIO pelo seu nome de usuário do GitHub.*

### Passo 26: Enviar seus commits para o GitHub

```bash
git push -u origin main
```

ou, se seu branch se chamar master:

```bash
git push -u origin master
```

**O que você deve ver:** Uma barra de progresso e mensagem de sucesso.

### Passo 27: Verificar no navegador

Atualize a página do seu repositório no GitHub. Você deve ver seu README.md e todo o conteúdo lá!

Parabéns! Seu código está na nuvem. ✓

---

## Parte 8: Trabalhando com Branches

Branches (ramificações) permitem trabalhar em novas funcionalidades sem afetar o código principal.

### Passo 28: Criar uma nova branch

```bash
git branch nova-funcionalidade
```

### Passo 29: Ver todas as branches

```bash
git branch
```

**O que você deve ver:** Duas branches, com um `*` ao lado da branch atual (main ou master).

### Passo 30: Mudar para a nova branch

```bash
git checkout nova-funcionalidade
```

**O que você deve ver:** "Switched to branch 'nova-funcionalidade'".

### Passo 31: Fazer mudanças na nova branch

```bash
echo "## Nova Funcionalidade" >> README.md
echo "Trabalhando em algo novo!" >> README.md
```

### Passo 32: Commitar as mudanças

```bash
git add README.md
git commit -m "Adiciona seção de nova funcionalidade"
```

### Passo 33: Voltar para a branch principal

```bash
git checkout main
```

ou:

```bash
git checkout master
```

### Passo 34: Ver o conteúdo do README

```bash
cat README.md
```

**O que você deve notar:** As linhas sobre "Nova Funcionalidade" NÃO aparecem! Isso porque elas só existem na outra branch.

### Passo 35: Fazer merge da nova funcionalidade

```bash
git merge nova-funcionalidade
```

**O que você deve ver:** "Updating..." e uma mensagem de sucesso.

### Passo 36: Verificar o README novamente

```bash
cat README.md
```

Agora as linhas da nova funcionalidade aparecem! O merge trouxe as mudanças. ✓

### Passo 37: Enviar as atualizações para o GitHub

```bash
git push origin main
```

ou:

```bash
git push origin master
```

---

## Parte 9: Comandos Essenciais para o Dia a Dia

Agora que você fez o ciclo completo, aqui estão os comandos que você vai usar constantemente:

### Ver o que mudou

```bash
git status
```

Use sempre que quiser saber o estado do seu repositório.

### Adicionar arquivos específicos

```bash
git add arquivo.txt
```

### Adicionar todos os arquivos modificados

```bash
git add .
```

### Ver diferenças antes de commitar

```bash
git diff
```

Ver diferenças do que já está no stage:

```bash
git diff --staged
```

### Remover arquivo do stage (desfazer git add)

```bash
git reset arquivo.txt
```

O arquivo volta para o estado "modified" mas não perde as mudanças.

### Ver histórico resumido

```bash
git log --oneline
```

### Baixar atualizações do GitHub

```bash
git pull origin main
```

Isso busca e mescla mudanças que possam ter sido feitas no GitHub.

---

## Parte 10: Praticando o Fluxo Completo

Vamos repetir o ciclo completo uma vez para fixar:

### Passo 38: Criar um novo arquivo

```bash
echo "print('Olá, Git!')" > ola.py
```

### Passo 39: Ver o status

```bash
git status
```

O arquivo aparece como untracked.

### Passo 40: Adicionar ao stage

```bash
git add ola.py
```

### Passo 41: Ver o status novamente

```bash
git status
```

Agora está pronto para commit.

### Passo 42: Fazer o commit

```bash
git commit -m "Adiciona script Python de saudação"
```

### Passo 43: Enviar para o GitHub

```bash
git push origin main
```

### Passo 44: Verificar no GitHub

Abra seu repositório no navegador e veja o novo arquivo lá!

---

## 🎉 Parabéns!

Você completou seu primeiro tutorial de Git e GitHub! Agora você sabe:

✓ Instalar e configurar o Git no Ubuntu  
✓ Conectar sua máquina ao GitHub via SSH  
✓ Criar repositórios locais e remotos  
✓ Fazer commits e acompanhar mudanças  
✓ Trabalhar com branches  
✓ Fazer merge de código  
✓ Enviar e receber código do GitHub  

## Próximos Passos

Agora que você domina o básico, pode:

1. **Criar mais repositórios** para seus projetos pessoais
2. **Explorar repositórios públicos** no GitHub para ver código de outros desenvolvedores
3. **Praticar o fluxo diário**: modificar → adicionar → commitar → enviar
4. **Aprender sobre .gitignore** para ignorar arquivos que não devem ser versionados
5. **Explorar o GitHub Desktop** se preferir uma interface gráfica

## Comandos de Referência Rápida

```bash
# Ver status
git status

# Adicionar arquivo
git add arquivo.txt

# Adicionar todos
git add .

# Commitar
git commit -m "mensagem descritiva"

# Enviar para GitHub
git push origin main

# Receber do GitHub
git pull origin main

# Ver histórico
git log

# Criar branch
git branch nome-branch

# Mudar de branch
git checkout nome-branch

# Fazer merge
git merge nome-branch
```

---

**Dúvidas?** Isso é normal! O Git tem muitos comandos, mas com a prática você vai memorizando os mais usados. Continue praticando criando novos projetos e fazendo commits regularmente.