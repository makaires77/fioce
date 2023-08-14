# Modelando contextos delimitados do mundo real com DDD
Quando as necessidades de implementação de software saem do nível de aprendizado e passam para o nível de solução profissional de problemas é indispensável pensar em termos de Arquitetura de Soluções e Arquitetura de Software. 

Os seja, basicamente é preciso tomar decisões como as tecnologias irão interagir com os artefatos de software para atender necessidades do mundo real, esse mundo real é modelado para poder ser entendido pelo software. A maneira mais popular e difundida de realizar essa modelagem é o que se chama de DDD (Domain Driven Design, em tradução livre, Arquitetura Orientada a Domínios). Os Domínios são partes da realidade que atenderemos com o software, onde geraremos o valor para os usuários e stakeholder que demandam e financiam o desenvolvimento.

A Arquitetura Orientada a Domínios (Domain-Driven Design ou DDD) é uma abordagem à estruturação de software que se concentra no domínio principal do software e suas lógicas complexas. Ela destaca a importância de modelar o domínio em software e se baseia na colaboração entre especialistas técnicos e de domínio.

Ao usar DDD para organizar funções, módulos, pacotes e serviços, você se concentraria principalmente nos conceitos centrais do domínio e em como eles se relacionam. Vamos examinar como você fará isso:

### 1. Entidades e Agregados:

Essas são as classes que representam os conceitos principais do seu domínio. Elas contêm a lógica e as regras de negócios. Em uma estrutura de pastas, isso pode parecer:

```
meu_projeto/
├── domain/
│   ├── entities/
│   │   ├── usuario.py
│   │   └── produto.py
│   ├── aggregates/
│   │   └── pedido.py
```

### 2. Repositórios:

Os repositórios são responsáveis por lidar com a persistência e recuperação de suas entidades e agregados. Eles atuam como uma camada entre o domínio e o acesso aos dados.

```
├── domain/
│   ├── repositories/
│   │   ├── usuario_repository.py
│   │   ├── produto_repository.py
│   │   └── pedido_repository.py
```

### 3. Serviços de Aplicação:

Os serviços de aplicação formam a camada que interage com o domínio. Eles contêm a lógica para execução de casos de uso específicos do aplicativo.

```
├── application/
│   ├── services/
│   │   ├── autenticacao_service.py
│   │   ├── carrinho_service.py
```

### 4. Serviços de Domínio:

Estes são diferentes dos serviços de aplicação. Os serviços de domínio contêm a lógica de negócios que não pertence naturalmente a uma entidade ou agregado.

```
├── domain/
│   ├── services/
│   │   ├── preco_service.py
```

### 5. Interfaces:

Aqui, você define como o software interage com o mundo exterior, seja através de APIs, GUIs, etc.

```
├── interfaces/
│   ├── api/
│   │   ├── endpoints/
│   │   ├── serializers.py
│   ├── web/
│   │   ├── templates/
│   │   ├── static/
```

### 6. Infraestrutura:

Esta pasta contém todas as implementações que são específicas de certas tecnologias (por exemplo, bancos de dados, serviços de mensagens).

```
├── infrastructure/
│   ├── db/
│   │   ├── models.py
│   │   ├── migrations/
│   ├── messaging/
│   │   ├── kafka/
│   │   ├── rabbitmq/
```

### Resumo:

O DDD destaca a modelagem do domínio principal e a colaboração estreita com especialistas de domínio. A estrutura acima reflete essa abordagem, separando claramente as responsabilidades em camadas e focando na lógica do domínio. Embora a estrutura acima seja um guia, a chave é garantir que ela represente fielmente o domínio e as operações do seu software.