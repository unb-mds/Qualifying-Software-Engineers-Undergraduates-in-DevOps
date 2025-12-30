---
layout: lecture
type: lecture
date: 2025-08-12
title: Instalação do Ubuntu
tldr: "Guia completo para instalar Ubuntu no seu computador, dual boot ou máquina virtual."
thumbnail: /static_files/presentations/gpp_mds.png
permalink: /lectures/Lec6/
hide_from_announcments: false
links: 
    - url: https://ubuntu.com/download/desktop
      name: Download Ubuntu
    - url: https://ubuntu.com/tutorials/install-ubuntu-desktop
      name: Tutorial Oficial
---

# Guia de Instalação do Ubuntu

Este tutorial vai te guiar pelo processo de instalação do Ubuntu, seja em dual boot com Windows ou em uma máquina virtual.

**Tempo estimado:** 30-60 minutos

---

## Opção 1: Máquina Virtual (Recomendado para iniciantes)

A máquina virtual permite rodar o Ubuntu dentro do seu sistema atual, sem risco de perder dados.

### Passo 1: Baixar o VirtualBox

1. Acesse [virtualbox.org](https://www.virtualbox.org/wiki/Downloads)
2. Baixe a versão para seu sistema operacional (Windows, macOS ou Linux)
3. Execute o instalador e siga as instruções

### Passo 2: Baixar a ISO do Ubuntu

1. Acesse [ubuntu.com/download/desktop](https://ubuntu.com/download/desktop)
2. Baixe a versão LTS mais recente (ex: Ubuntu 24.04 LTS)
3. Aguarde o download do arquivo `.iso` (~5GB)

### Passo 3: Criar a Máquina Virtual

1. Abra o VirtualBox
2. Clique em **"Novo"**
3. Configure:
   - **Nome:** Ubuntu
   - **Tipo:** Linux
   - **Versão:** Ubuntu (64-bit)
4. Clique em **Próximo**

### Passo 4: Configurar Memória RAM

- **Mínimo recomendado:** 4096 MB (4GB)
- **Ideal:** 8192 MB (8GB) se você tiver 16GB+ de RAM total

### Passo 5: Criar Disco Virtual

1. Selecione **"Criar um disco rígido virtual agora"**
2. Escolha **VDI (VirtualBox Disk Image)**
3. Selecione **"Dinamicamente alocado"**
4. Defina o tamanho: **mínimo 25GB**, recomendado **50GB**

### Passo 6: Configurar a Máquina Virtual

Antes de iniciar, ajuste algumas configurações:

1. Selecione a VM criada e clique em **"Configurações"**
2. **Sistema > Processador:** Aumente para 2-4 CPUs
3. **Vídeo > Tela:** Aumente memória de vídeo para 128MB
4. **Armazenamento:** Clique no ícone de CD vazio, depois no ícone de CD à direita e selecione a ISO do Ubuntu

### Passo 7: Instalar o Ubuntu

1. Clique em **"Iniciar"** para ligar a VM
2. Selecione **"Try or Install Ubuntu"**
3. Escolha o idioma **Português do Brasil**
4. Clique em **"Instalar Ubuntu"**
5. Selecione o layout de teclado
6. Escolha **"Instalação normal"**
7. Selecione **"Apagar disco e instalar Ubuntu"** (é seguro, só afeta o disco virtual!)
8. Configure seu fuso horário
9. Crie seu usuário e senha
10. Aguarde a instalação (~15-20 minutos)
11. Reinicie quando solicitado

### Passo 8: Instalar Guest Additions (Opcional mas recomendado)

Após iniciar o Ubuntu instalado:

1. No menu do VirtualBox: **Dispositivos > Inserir imagem de CD dos Adicionais para Convidado**
2. Abra o terminal no Ubuntu (`Ctrl + Alt + T`)
3. Execute:

```bash
sudo apt update
sudo apt install build-essential dkms linux-headers-$(uname -r)
sudo /media/$USER/VBox_GAs_*/VBoxLinuxAdditions.run
```

4. Reinicie a VM

Agora você terá tela redimensionável e área de transferência compartilhada!

---

## Opção 2: Instalando Ubuntu em Dual Boot com Windows


Bem-vindo! Neste tutorial, você vai aprender a instalar o Ubuntu no seu computador mantendo o Windows. Ao final, você terá os dois sistemas operacionais funcionando e poderá escolher qual usar cada vez que ligar o computador.

**O que você vai conseguir:** Um computador com Windows e Ubuntu instalados, podendo escolher qual sistema usar na inicialização.

**Tempo estimado:** 1-2 horas

**O que você vai precisar:**
- Um computador com Windows 10 ou 11
- Um pendrive vazio de pelo menos 8GB
- Conexão com a internet
- Paciência e atenção aos detalhes

---

## ⚠️ IMPORTANTE: Leia Antes de Começar

**Faça backup dos seus dados importantes!** Embora a instalação em dual boot seja segura quando feita corretamente, sempre existe um pequeno risco. Copie seus documentos, fotos e arquivos importantes para um HD externo ou nuvem.

**Este tutorial é para computadores com BIOS UEFI** (a maioria dos computadores modernos). Se seu computador for muito antigo (anterior a 2011), o processo pode ser diferente.

---

## Parte 1: Preparando o Espaço no Disco

Antes de instalar o Ubuntu, precisamos criar espaço livre no disco rígido.

### Passo 1: Abrir o Gerenciamento de Disco do Windows

1. Pressione `Windows + X` no teclado
2. Clique em "Gerenciamento de Disco"

**O que você deve ver:** Uma janela mostrando todos os discos e partições do seu computador.

### Passo 2: Identificar a partição principal

Procure a maior partição, geralmente chamada "C:" ou com o rótulo "Windows".

**O que você deve ver:** Uma barra azul mostrando quanto espaço está usado e quanto está livre.

### Passo 3: Reduzir o volume do Windows

1. Clique com o botão direito na partição C:
2. Selecione "Reduzir Volume"
3. Aguarde enquanto o Windows calcula o espaço disponível

### Passo 4: Definir quanto espaço alocar para o Ubuntu

Quando a janela aparecer, você verá "Quantidade de espaço a ser reduzida em MB".

**Quanto espaço reservar?**
- Mínimo: 30.000 MB (30 GB) - básico
- Recomendado: 50.000 MB (50 GB) - confortável
- Ideal: 100.000 MB (100 GB) - para quem vai usar bastante

Digite o valor escolhido e clique em "Reduzir".

**O que você deve ver:** Um espaço preto com o rótulo "Não Alocado" aparece no gráfico.

Perfeito! Você criou espaço para o Ubuntu. ✓

---

## Parte 2: Baixando o Ubuntu

### Passo 5: Acessar o site oficial do Ubuntu

1. Abra seu navegador
2. Vá para: [ubuntu.com/download/desktop](https://ubuntu.com/download/desktop)

### Passo 6: Baixar a versão LTS

1. Clique no botão verde "Download Ubuntu" (versão LTS)
2. O download começará automaticamente (arquivo de cerca de 4-5 GB)
3. Aguarde o download completar

**Observação:** A versão LTS (Long Term Support) é a mais estável e recomendada para iniciantes.

**O que você baixou:** Um arquivo .iso, que é uma imagem do sistema operacional.

---

## Parte 3: Criando o Pendrive de Instalação

### Passo 7: Baixar o Rufus

1. Vá para: [rufus.ie](https://rufus.ie)
2. Role a página até "Download"
3. Clique em "Rufus 4.x" (versão portátil está ok)
4. Salve o arquivo

### Passo 8: Inserir o pendrive

1. Conecte seu pendrive USB no computador
2. **IMPORTANTE:** Certifique-se de que não há nada importante nele, pois será apagado

### Passo 9: Executar o Rufus

1. Abra o arquivo do Rufus que você baixou
2. Clique em "Sim" se o Windows pedir permissão

**O que você deve ver:** Uma janela pequena com várias opções.

### Passo 10: Configurar o Rufus

1. **Dispositivo:** Deve mostrar seu pendrive automaticamente
2. **Seleção de boot:** Clique em "SELECIONAR" e escolha o arquivo .iso do Ubuntu que você baixou
3. **Esquema de partição:** Deixe em "GPT"
4. **Sistema de destino:** Deixe em "UEFI (não CSM)"

**Deixe todas as outras opções como estão.**

### Passo 11: Criar o pendrive bootável

1. Clique no botão "INICIAR"
2. Se aparecer uma janela sobre "modo de escrita de imagem", deixe como "Escrever no modo Imagem ISO" e clique OK
3. Uma mensagem avisará que todos os dados do pendrive serão destruídos - clique OK
4. Aguarde o processo completar (5-10 minutos)

**O que você deve ver:** Uma barra de progresso que vai até 100%, depois uma mensagem "PRONTO" em verde.

Clique em "FECHAR". Seu pendrive está pronto! ✓

---

## Parte 4: Desativando o Fast Boot e Secure Boot

Para instalar o Ubuntu, precisamos ajustar algumas configurações do Windows.

### Passo 12: Desativar o Fast Boot (Inicialização Rápida)

1. Pressione `Windows + X`
2. Clique em "Opções de Energia"
3. Clique em "Configurações de energia adicionais" (lado direito)
4. Clique em "Escolher a função dos botões de energia" (lado esquerdo)
5. Clique em "Alterar configurações não disponíveis no momento"
6. **Desmarque** a caixa "Ativar inicialização rápida"
7. Clique em "Salvar alterações"

### Passo 13: Acessar a BIOS/UEFI

Agora vamos reiniciar o computador e entrar na BIOS. O método varia por fabricante:

**Como entrar na BIOS:**
1. Clique em Iniciar → Energia → Reiniciar
2. **Durante a reinicialização**, pressione repetidamente uma destas teclas (depende do fabricante):
   - **Dell:** F2 ou F12
   - **HP:** F10 ou Esc
   - **Lenovo:** F2 ou F1
   - **Asus:** F2 ou Delete
   - **Acer:** F2 ou Delete

**Dica:** Se não conseguir, pesquise no Google: "como entrar na BIOS [marca do seu computador]"

### Passo 14: Desativar o Secure Boot

**IMPORTANTE:** A aparência da BIOS varia muito entre fabricantes. Procure por estas opções:

1. Procure uma aba ou menu chamado "Security" ou "Boot"
2. Encontre a opção "Secure Boot"
3. Mude de "Enabled" para "Disabled"
4. Pressione F10 para salvar e sair (ou procure a opção "Save and Exit")
5. O computador vai reiniciar normalmente

**O que você fez:** Permitiu que o computador inicialize com outros sistemas operacionais além do Windows. ✓

---

## Parte 5: Iniciando pelo Pendrive

### Passo 15: Reiniciar e acessar o menu de boot

1. Com o pendrive ainda conectado, reinicie o computador
2. Durante a inicialização, pressione a tecla de Boot Menu:
   - **Dell:** F12
   - **HP:** F9 ou Esc
   - **Lenovo:** F12
   - **Asus:** F8 ou Esc
   - **Acer:** F12

**O que você deve ver:** Um menu com opções de dispositivos para inicializar.

### Passo 16: Selecionar o pendrive

1. Use as setas do teclado para selecionar seu pendrive USB
2. Pressione Enter

**O que você deve ver:** O logo do Ubuntu e uma tela de carregamento.

Aguarde cerca de 1-2 minutos. Seja paciente, é normal demorar um pouco.

---

## Parte 6: Experimentando o Ubuntu (Modo Live)

### Passo 17: Escolher o idioma

**O que você deve ver:** Uma tela perguntando "Try Ubuntu" ou "Install Ubuntu".

1. No lado esquerdo, selecione "Português do Brasil"
2. Clique em "Experimentar o Ubuntu"

**O que acontece:** O Ubuntu vai carregar sem instalar nada. Você pode testá-lo sem medo!

### Passo 18: Explorar o Ubuntu (opcional mas recomendado)

Parabéns! Você está usando o Ubuntu sem ter instalado nada. Aproveite para:
- Abrir o navegador Firefox
- Testar se o Wi-Fi funciona
- Verificar se o som funciona
- Explorar a interface

**Tudo funcionando bem?** Ótimo! Vamos prosseguir com a instalação.

---

## Parte 7: Instalando o Ubuntu

### Passo 19: Iniciar o instalador

Na área de trabalho do Ubuntu, clique duas vezes no ícone "Instalar Ubuntu".

### Passo 20: Selecionar o idioma

1. Confirme "Português do Brasil"
2. Clique em "Continuar"

### Passo 21: Escolher o layout do teclado

1. Selecione "Portuguese (Brazil)"
2. Teste digitando na caixa de texto: `ç á ã é`
3. Clique em "Continuar"

### Passo 22: Configurar atualizações e software

**O que você deve ver:** Duas opções de instalação.

Recomendado para iniciantes:
- Selecione "Instalação normal"
- **Marque** as caixas:
  - ✓ Baixar atualizações enquanto instala
  - ✓ Instalar software de terceiros (drivers Wi-Fi, placas gráficas)

Clique em "Continuar".

### Passo 23: Tipo de instalação (PASSO CRÍTICO ⚠️)

**Esta é a parte mais importante do tutorial. Leia com atenção!**

**O que você deve ver:** Opções sobre como instalar o Ubuntu.

**ESCOLHA:** "Instalar o Ubuntu ao lado do Windows Boot Manager"

**NÃO ESCOLHA:** 
- ❌ "Apagar disco e instalar o Ubuntu" (isso apaga o Windows!)
- ❌ "Outra opção" (apenas para usuários avançados)

**O que você deve ver:** Um gráfico mostrando Windows e um espaço para o Ubuntu.

### Passo 24: Ajustar o tamanho das partições

1. Você verá uma divisória que pode arrastar
2. Arraste para definir quanto espaço quer dar para cada sistema
3. O espaço que você liberou na Parte 1 deve estar disponível

Clique em "Instalar Agora".

### Passo 25: Confirmar as alterações

**O que você deve ver:** Uma janela mostrando as mudanças que serão feitas no disco.

Revise cuidadosamente. Deve mostrar:
- Partições do Windows intactas
- Novas partições sendo criadas para o Ubuntu

Clique em "Continuar".

---

## Parte 8: Configurações Finais

### Passo 26: Selecionar fuso horário

1. Clique no mapa próximo à sua localização ou digite "Sao Paulo"
2. Clique em "Continuar"

### Passo 27: Criar sua conta

Preencha os campos:

1. **Seu nome:** Digite seu nome completo
2. **Nome do computador:** Um nome para identificar seu PC (ex: ubuntu-seunome)
3. **Nome de usuário:** Seu login (ex: joao)
4. **Senha:** Crie uma senha forte
5. **Confirmar senha:** Digite a senha novamente

**Escolha:** "Solicitar minha senha para entrar"

Clique em "Continuar".

### Passo 28: Aguardar a instalação

**O que você deve ver:** Uma barra de progresso e slides mostrando recursos do Ubuntu.

**Tempo de espera:** 15-30 minutos (varia conforme a velocidade do computador)

☕ Este é um bom momento para um café!

### Passo 29: Concluir a instalação

Quando a instalação terminar, você verá uma mensagem "Instalação concluída".

1. Clique em "Reiniciar agora"
2. Quando aparecer "Please remove installation medium...", **retire o pendrive**
3. Pressione Enter

O computador vai reiniciar.

---

## Parte 9: Primeiro Boot em Dual Boot

### Passo 30: O menu do GRUB

**O que você deve ver:** Uma tela preta/roxa com um menu escrito "GNU GRUB".

**Opções disponíveis:**
- Ubuntu (será selecionado automaticamente)
- Advanced options for Ubuntu
- Windows Boot Manager

**Para usar o Ubuntu:** Apenas aguarde 10 segundos ou pressione Enter

**Para usar o Windows:** Use as setas para selecionar "Windows Boot Manager" e pressione Enter

### Passo 31: Fazer login no Ubuntu

1. Clique no seu nome de usuário
2. Digite sua senha
3. Pressione Enter

**O que você deve ver:** A área de trabalho do Ubuntu!

🎉 **Parabéns! Você instalou o Ubuntu em dual boot com sucesso!** ✓

---

## Parte 10: Primeiras Configurações no Ubuntu

Agora que o Ubuntu está instalado, vamos fazer algumas configurações iniciais.

### Passo 32: Conectar ao Wi-Fi (se necessário)

1. Clique no ícone de rede no canto superior direito
2. Selecione sua rede Wi-Fi
3. Digite a senha
4. Clique em "Conectar"

### Passo 33: Atualizar o sistema

Abra o Terminal pressionando `Ctrl + Alt + T` e digite:

```bash
sudo apt update
sudo apt upgrade -y
```

Digite sua senha quando solicitado.

**O que está acontecendo:** O Ubuntu está baixando e instalando as atualizações mais recentes.

**Tempo de espera:** 5-15 minutos na primeira vez.

Quando terminar, digite:

```bash
reboot
```

O sistema vai reiniciar.

### Passo 34: Instalar atualizações adicionais (se houver)

Após reiniciar e fazer login:

1. Se aparecer uma notificação sobre atualizações, clique nela
2. Clique em "Instalar agora"
3. Digite sua senha
4. Aguarde concluir

### Passo 35: Explorar o Ubuntu

Parabéns! Agora você pode:

**Experimentar os aplicativos pré-instalados:**
- Firefox (navegador)
- LibreOffice (editor de textos, planilhas)
- Arquivos (gerenciador de arquivos)
- Ubuntu Software (loja de aplicativos)

**Instalar novos programas:**
1. Abra "Ubuntu Software"
2. Procure por aplicativos
3. Clique em "Instalar"

---

## 🎉 Parabéns!

Você completou a instalação do Ubuntu em dual boot! Agora você tem:

✓ Windows e Ubuntu no mesmo computador  
✓ Capacidade de escolher qual sistema usar na inicialização  
✓ Ubuntu totalmente configurado e atualizado  
✓ Conhecimento básico sobre o processo de instalação  

---

## Perguntas Frequentes

### Como escolher qual sistema usar?

Toda vez que ligar o computador, o menu GRUB aparece. Use as setas para escolher e pressione Enter.

### E se eu quiser que o Windows seja o padrão?

Por padrão, o Ubuntu é selecionado automaticamente. Para mudar isso, você precisará editar as configurações do GRUB (um tutorial mais avançado).

### Como acessar meus arquivos do Windows no Ubuntu?

1. Abra "Arquivos"
2. No painel esquerdo, você verá o disco do Windows
3. Clique nele para acessar seus arquivos

### Posso desinstalar o Ubuntu depois?

Sim! Mas isso requer outro tutorial. Você precisará remover as partições do Ubuntu e restaurar o bootloader do Windows.

### O Ubuntu é mais rápido que o Windows?

Geralmente sim, especialmente em computadores mais antigos. O Ubuntu usa menos recursos de memória e processamento.

### Preciso de antivírus no Ubuntu?

Não necessariamente. O Ubuntu é muito menos vulnerável a vírus que o Windows, especialmente se você instalar software apenas das fontes oficiais.

---

## Comandos Úteis para Iniciantes

Aqui estão alguns comandos do Terminal que você vai usar frequentemente:

```bash
# Atualizar lista de pacotes
sudo apt update

# Atualizar o sistema
sudo apt upgrade

# Instalar um programa
sudo apt install nome-do-programa

# Remover um programa
sudo apt remove nome-do-programa

# Limpar arquivos desnecessários
sudo apt autoremove

# Ver informações do sistema
neofetch
```

---

## Próximos Passos

Agora que você tem o Ubuntu instalado, pode:

1. **Personalizar a aparência** em Configurações → Aparência
2. **Instalar seus programas favoritos** via Ubuntu Software
3. **Aprender comandos do Terminal** (muito útil!)
4. **Explorar extensões** para a interface GNOME
5. **Configurar atalhos de teclado** personalizados

## Recursos para Aprender Mais

- [Documentação oficial do Ubuntu](https://help.ubuntu.com)
- [Ubuntu Brasil - Comunidade](https://ubuntu-br.org)
- [Ask Ubuntu - Fórum de perguntas](https://askubuntu.com)

---

**Bem-vindo ao mundo do código aberto!** Você deu um grande passo ao instalar Linux. Com o tempo, você vai descobrir um mundo novo de possibilidades e aprender muito sobre como os computadores realmente funcionam.

Continue explorando, experimentando e, acima de tudo, divirta-se! 🚀