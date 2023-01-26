import view

def start():
    while True:
        op = view.get_op()
        if op == 1:
            view.add_student()
        elif op == 2:
            view.add_subject()
        # elif op == 3:
        #     view.print_only_name()
        elif op == 4:
            view.print_table()
        # elif op == 5:
        #     sorting.sort_id()
        elif op == 6:
            break
