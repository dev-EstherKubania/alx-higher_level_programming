#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []  # Renamed from new_list
    for i in range(list_length):
        try:
            result.append(my_list_1[i] / my_list_2[i])
        except (TypeError, ZeroDivisionError, IndexError) as error:
            if isinstance(error, ZeroDivisionError):
                print("division by 0")
            elif isinstance(error, TypeError):
                print("wrong type")
            elif isinstance(error, IndexError):
                print("out of range")
            result.append(0)
        finally:
            pass
    return result
