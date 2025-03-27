# Lista que armazenará as tarefas
tarefas = []

# Função para adicionar uma tarefa
def add_task(nome, prioridade):
    tarefas.append({
        'nome': nome,
        'prioridade': prioridade,
        'concluida': False
    })

# Função para listar tarefas pendentes usando list comprehension
def list_pending_tasks():
    return [t for t in tarefas if not t['concluida']]

# Função para listar tarefas concluídas
def list_completed_tasks():
    return [t for t in tarefas if t['concluida']]

# Função para marcar uma tarefa como concluída
def complete_task(nome):
    for t in tarefas:
        if t['nome'] == nome:
            t['concluida'] = True

# Função de alta ordem para filtrar tarefas usando um critério (função como argumento)
def filtrar_tarefas(lista, criterio):
    return list(filter(criterio, lista))

# Função que retorna uma closure para validar prioridade
def gerar_validador_de_prioridade(prioridade_desejada):
    def validador(tarefa):
        return tarefa['prioridade'] == prioridade_desejada
    return validador

# Função que usa lambda para criar critério de filtro por prioridade
def filter_tasks_by_priority(prioridade):
    return filtrar_tarefas(tarefas, lambda t: t['prioridade'] == prioridade)

# Exemplo de uso:
if __name__ == '__main__':
    add_task('Estudar para prova', 'alta')
    add_task('Fazer compras', 'media')
    add_task('Lavar o carro', 'baixa')

    complete_task('Fazer compras')

    print("Tarefas Pendentes:")
    for t in list_pending_tasks():
        print(f"- {t['nome']} ({t['prioridade']})")

    print("Tarefas Concluídas:")
    for t in list_completed_tasks():
        print(f"- {t['nome']} ({t['prioridade']})")

    print("Tarefas com prioridade alta:")
    alta = filter_tasks_by_priority('alta')
    for t in alta:
        print(f"- {t['nome']} ({t['prioridade']})")

    print("Tarefas com prioridade média usando closure:")
    validador_media = gerar_validador_de_prioridade('media')
    media = filtrar_tarefas(tarefas, validador_media)
    for t in media:
        print(f"- {t['nome']} ({t['prioridade']})")
