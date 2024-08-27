def display_tasks(tasks):
    if len(tasks) == 0:
        print('Задачи отсутствуют.')
    else:
        for idx, task in enumerate(tasks, 1):
            status = "✔" if task["done"] else "✘"
            print(f"{idx}. {task['task']} [{status}]")


def add_task(tasks):
    display_tasks(tasks)
    task_name = input('Введите задачу: ')
    tasks.append({'task': task_name, 'done': False})
    print('Задача успешно добавлена!')


def del_task(tasks):
    display_tasks(tasks)
    task_number = int(input('Введите номер задачи, которую хотите удалить: '))
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print('Задача успешно удалена!')
    else:
        print('Некорректный номер задачи.')


def mark_task_done(tasks):
    display_tasks(tasks)
    task_number = int(input('Введите номер задачи: '))
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['done'] = True
    else:
        print('Некорректный номер задачи.')


def task_manager():
    tasks = []
    while True:
        print('\n1. Показать все задачи')
        print('2. Добавить новую задачу')
        print('3. Удалить задачу')
        print('4. Выполнить задачу')
        print('5. Выйти')

        choice = input('Выберите действие: ')

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            del_task(tasks)
        elif choice == '4':
            mark_task_done(tasks)
        elif choice == '5':
            break
        else:
            print('Некорректный выбор!')


task_manager()
