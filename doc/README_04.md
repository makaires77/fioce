## Iniciando o desenvolvimento com Integração e Entrega Contínua (CI/CD) com Docker e GitHub Actions
Vamos descrever os passos iniciais considerando os três principais sistemas operacionais: Windows, Linux e macOS.

### 1. Desenvolvimento Local com VSCode:

1. **Configurando o Ambiente**:
    - Inicie um novo projeto no VSCode.
    - Configure um ambiente virtual Python para manter as dependências isoladas, vamos chamar de venv:
      ```bash
      python -m venv venv
      ```
    - Ative o ambiente virtual:
      - **Windows**: `.\venv\Scripts\Activate`
      - **Linux/macOS**: `source venv/bin/activate`
    - No VSCode, selecione esse ambiente virtual como interpretador Python.

2. **Desenvolvendo as Funções e Classes**:
    - Crie seus arquivos, em python serão os arquivos `.py`, para implementar suas classes e funções.

### 2. Preparando para o Docker:

1. **Dockerfile**:
    - Crie um `Dockerfile` na raiz do projeto.

2. **docker-compose.yml** (se necessário):
    - Crie um `docker-compose.yml` na raiz do projeto.

**Nota**: Certifique-se de ter o Docker Desktop instalado:
- **Windows/macOS**: Baixe o Docker Desktop da [página oficial](https://www.docker.com/products/docker-desktop).
- **Linux**: Dependendo da distribuição, você pode precisar instalar o Docker Engine e o Docker Compose separadamente. Siga as instruções da [documentação oficial do Docker](https://docs.docker.com/engine/install/).

### 3. Controle de Versão com Git e GitHub:

1. **Inicializando um Repositório Git**:
    ```bash
    git init
    ```

2. **Primeiro Commit**:
    ```bash
    git add .
    git commit -m "Initial commit with classes and functions"
    ```

3. **Conectando com GitHub**:
    - Crie um repositório no GitHub.
    - Conecte seu repositório local ao GitHub:
      ```bash
      git remote add origin [URL_DO_REPOSITÓRIO]
      ```

4. **Envio para o GitHub**:
    ```bash
    git push -u origin main
    ```

### 4. CI/CD com GitHub Actions:

1. **Configurando GitHub Actions**:
    - Na raiz do projeto, crie um diretório chamado `.github` e, dentro dele, outro chamado `workflows`.
    - Crie um arquivo YAML dentro de `workflows`, por exemplo, `ci_cd_pipeline.yml`.

2. **Pipeline Básica para CI/CD**:

    No `ci_cd_pipeline.yml`:

    ```yaml
    name: CI/CD Pipeline

    on: [push]

    jobs:
      build:
        runs-on: ubuntu-latest

        steps:
        - name: Checkout Code
          uses: actions/checkout@v2

        - name: Build Docker Image
          run: docker build -t my_scraper_service .

        - name: Push Docker Image (Optional)
          run: |
            echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
            docker tag my_scraper_service:latest $DOCKER_USERNAME/my_scraper_service:latest
            docker push $DOCKER_USERNAME/my_scraper_service:latest
          env:
            DOCKER_USERNAME: ${{ secrets.DOCKER_USERNAME }}
            DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}
    ```

3. **Secrets do GitHub**:
    - No GitHub, vá para o repositório, clique na aba "Settings" > "Secrets".
    - Adicione `DOCKER_USERNAME` e `DOCKER_PASSWORD` como segredos.

### 5. Iteração e Melhoria:

Com tudo configurado, agora você pode iterar seu código localmente no VSCode. Ao fazer commits e pushes para o GitHub, o CI/CD será automatizado com o GitHub Actions. Use esta configuração para manter um desenvolvimento contínuo.

**Notas adicionais para usuários Windows, Linux e macOS**:

- **Terminal/Command Prompt**: As instruções dadas são para um terminal Unix-like. Usuários de Windows podem usar o Command Prompt, PowerShell ou o Windows Subsystem for Linux (WSL). Se usar o WSL, certifique-se de ter todas as ferramentas necessárias instaladas no ambiente WSL e não no Windows nativo.
  
- **Instalação do Git**: 
  - **Windows**: Baixe e instale o Git a partir do [site oficial](https://git-scm.com/download/win).
  - **macOS**: Pode ser instalado usando Homebrew com `brew install git` ou baixando do [site oficial](https://git-scm.com/download/mac).
  - **Linux**: Normalmente, pode ser instalado via gerenciador de pacotes da distribuição, como `apt install git` para Debian/Ubuntu ou `yum install git` para CentOS.
  
- **Caminhos de Arquivos**: Os caminhos dos arquivos no Windows usam `\` enquanto Linux/macOS usam `/`. Se estiver escrevendo scripts ou Dockerfiles que precisam ser compatíveis entre plataformas, esteja ciente dessas diferenças. No entanto, muitas ferramentas modernas e linguagens de script (incluindo Python) podem lidar com ambos os formatos de caminho ou oferecer maneiras de criar caminhos compatíveis.

Seguindo essas instruções e considerações, você deve ser capaz de desenvolver e implantar seu projeto de forma eficaz em qualquer uma dessas