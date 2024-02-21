role_id = [

]

def check(id_to_check, id_list):
    length_id_list = len(id_list)

    for i in range(length_id_list):
        if id_list[i] == id_to_check:
            return True

    return False

def roles():
    pass