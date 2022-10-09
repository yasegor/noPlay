import plyer


def is_tasks_value_0(count):
    plyer.notification.notify(
        message=f'Количество висящих тасков: {count}, а игровой режим включен.',
        title='Перезапуск системы через 10 секунд'
    )


def no_tasks_value_1():
    plyer.notification.notify(
        message='Все таски выполнены, а игровой режим выключен',
        title='Перезапуск системы через 10 секунд'
    )