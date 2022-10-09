import time
from pyqadmin import admin

import notifier
from keys import *
from habitica import get_data
from registry import show_value, change_value


@admin
def main():
    while True:
        value = show_value()
        tasks = get_data(user_id, token, url, tag)
        tasks_count = len(tasks)

        if not tasks and value == 0:
            exit()

        elif tasks and value == 0:
            notifier.is_tasks_value_0(tasks_count)
            change_value(1)
            time.sleep(10)
            os.system('shutdown -r -t 0')

        elif not tasks and value == 1:
            notifier.no_tasks_value_1()
            change_value(0)
            time.sleep(10)
            os.system('shutdown -r -t 0')

        time.sleep(600)


if __name__ == '__main__':
    main()
