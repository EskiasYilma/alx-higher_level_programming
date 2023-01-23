#!/usr/bin/python3
def safe_print_division(a, b):
    div = None
    try:
        div = a / b
        return div
    except Exception as e:
        return div
    finally:
        print("Inside result: {}".format(div))
