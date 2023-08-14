# Abraçando de vez a complexidade com Portes and Adapters
Se há uma constante é a mudança. Qualquer sistema que você planeje, execute e coloque para rodar vai demandar melhorias, mudanças pequenas (e por vezes radicais) quanto às tecnologias e estratégias utilizadas, uma forma de preparar seus sistemas para isso é facilitar o desacoplamento desde a estratégia de desenvolvimento implementada com a arquitetura de software. A lógica de negócios não pode esperar ou ser limitada pela lógica de software, se não, geralmente, o software não vai conseguir chegar a ser executado no mundo real. Ou pior o sucesso inicial não terá continuidade quando mais usuários demandarem mais recursos de processamento ou mudanças para suas melhores conveniências.

O padrão Arquitetura de Portas e Adaptadores (também conhecido como Hexagonal Architecture ou "Layered Architecture") enfatiza a separação entre a lógica de negócios (o núcleo) e os dispositivos, sistemas e ferramentas externas com os quais o software interage (adaptadores). A principal vantagem dessa abordagem é o isolamento da lógica do domínio, tornando-a agnóstica em relação a detalhes específicos de infraestrutura, interfaces de usuário ou até mesmo frameworks.

Quando combinamos o DDD com a arquitetura de Portas e Adaptadores, nós basicamente tratamos as camadas "Domain" e "Application" do DDD como o núcleo da nossa aplicação e as outras camadas como adaptadores.

### Adaptação da Estrutura:

Aqui está como você pode estruturar seu projeto baseado no DDD e Arquitetura de Portas e Adaptadores:

```plaintext
scraper-service/
│
├── core/ (Núcleo da Aplicação)
│   ├── domain/ (Mesma estrutura DDD, contendo entidades, regras de negócios, etc.)
│   │   ├── entities/
│   │   │   ├── scraper.py
│   │   ├── services/
│   │   │   ├── scraping_service.py
│   │
│   ├── application/ (Camada de Casos de Uso ou Serviços de Aplicação)
│   │   ├── services/
│   │   │   ├── schedule_service.py
│   │
│
├── adapters/ (Adaptadores)
│   ├── api/ (Interface HTTP/API)
│   │   ├── endpoints/
│   │   ├── serializers.py
│   │
│   ├── db/ (Adapter de Banco de Dados)
│   │   ├── models.py
│   │   ├── migrations/
│   │
│   ├── networking/ (Adapter de Networking)
│   │   ├── request_utils.py
│   │
│   └── ... (Outros adaptadores, como fila de mensagens, sistemas de arquivo, etc.)
│
├── config/ (Configurações, como Strings de Conexão, Configurações de API, etc.)
│
├── tests/
│
├── Dockerfile
└── docker-compose.yml
```

### Pontos-chave:

1. **Core**: É o coração do sistema e contém toda a lógica de negócios. Ele não deve ter dependências diretas de frameworks, bancos de dados ou detalhes externos.

2. **Adaptadores**: Representam os pontos de contato entre seu núcleo e o mundo exterior. Cada adaptador traduz as chamadas do mundo externo em um formato que o núcleo pode entender e vice-versa.

3. **Configuração**: Isoladamente, você pode configurar coisas como strings de conexão, chaves de API e outras configurações. Isso ajuda a manter as configurações separadas da lógica e dos adaptadores.

Ao adotar esta estrutura, você garante que sua lógica de negócios (core) é desacoplada dos detalhes de implementação específicos, permitindo flexibilidade, teste facilitado e uma separação clara de responsabilidades. Além disso, torna-se mais fácil substituir ou atualizar partes específicas do sistema (por exemplo, mudar de banco de dados ou introduzir uma nova interface) sem afetar a lógica central do domínio.
