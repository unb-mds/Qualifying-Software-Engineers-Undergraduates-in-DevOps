# Projeto: Gerador de Grafo de Contribuidores do GitHub

Este projeto gera um grafo visual dos contribuidores de uma organização do GitHub, mostrando suas conexões baseadas na colaboração em repositórios.

## Pré-requisitos

Certifique-se de ter os seguintes itens instalados em sua máquina:

1. Python 3.8 ou superior.
2. Gerenciador de pacotes `pip`.
3. Biblioteca `matplotlib`, `networkx`, `pandas` e `requests`.

Você pode instalar as dependências com:

```bash
pip install matplotlib networkx pandas requests
```

## Configuração do Token de Acesso do GitHub

1. Gere um token de acesso pessoal no GitHub com permissões para acessar repositórios da organização. [Saiba mais aqui](https://github.com/settings/tokens).
2. Substitua o valor da variável `TOKEN` no código pelo seu token:
   ```python
   TOKEN = "seu_token_github"
   ```

## Execução

1. Clone este repositório para sua máquina:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd seu-repositorio
   ```
3. Crie um ambiente virtual:
   ```bash
   python -m venv env
   ```
4. Ative o ambiente virtual:
   ```bash
   source env/bin/activate
   ```   
3. Execute o script principal:
   ```bash
   python3 generate_graph.py
   ```

## Resultado

- O grafo gerado será salvo na pasta `~/Downloads` com o nome `generate_graph.jpeg`.
- As fotos dos contribuidores serão armazenadas na pasta `photos`.

## Personalização

- **Organização GitHub**: Altere o valor de `ORG_NAME` no script para o nome da organização desejada:
  ```python
  ORG_NAME = "nome_da_organizacao"
  ```
- **Exclusão de Contribuidores**: Para excluir contribuidores específicos, adicione-os ao conjunto `excluded_contributors`.

## Licença

Este projeto é disponibilizado sob a licença [MIT](LICENSE).

