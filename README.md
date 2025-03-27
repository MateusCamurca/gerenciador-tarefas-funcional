
 Projeto: Gerenciador de Tarefas (Programação Funcional)

Este projeto foi desenvolvido como atividade prática da disciplina de Programação Funcional.

Descrição:
Sistema de linha de comando para gerenciar tarefas pessoais, com funcionalidades para adicionar, listar, concluir e filtrar tarefas com diferentes prioridades.

Linguagem
Python 3.x

Conceitos de Programação Funcional Aplicados
- Função Lambda
- List Comprehension
- Closure
- Função de Alta Ordem

 Estrutura
- `/codigo`: código-fonte da aplicação
- `/documentacao`: requisitos e relatório
- `/testes`: arquivos de teste

 Execução
```bash
python gerenciador_tarefas.py
```

 Autores
- Mateus Araujo Camurca - 2318990
- Cleany Teixeira Viana - 2317477
-  Maria Jose de Sousa - 2313652
- Francisco Matheus Rodrigues ferreira - 2314659
-  Erika Karine Duarte da Silva - 2313639


 Guia de Uso

 Pré-requisitos

- Python 3.6 ou superior instalado
- Terminal ou prompt de comando

 Como executar o projeto

1. Clone o repositório ou baixe os arquivos:

```bash
git clone https://github.com/MateusCamurca/gerenciador-tarefas-funcional.git
```

Ou baixe o `.zip`, extraia e entre na pasta do projeto:

```bash
cd gerenciador-tarefas-funcional/codigo
```

2. Execute o programa:

```bash
python gerenciador_tarefas.py
```

---

 Funcionalidades disponíveis

Ao executar o programa, ele já cria algumas tarefas de exemplo e mostra:

-  Tarefas pendentes
-  Tarefas concluídas
-  Tarefas com prioridade alta (usando lambda)
-  Tarefas com prioridade média (usando closure)

---

 Conceitos de Programação Funcional usados

- Função Lambda: usada para filtrar tarefas por prioridade
- List Comprehension: para listar tarefas pendentes e concluídas
- Closure: criada para gerar validadores de prioridade
- Função de Alta Ordem: `filtrar_tarefas` recebe funções como critério de filtragem
