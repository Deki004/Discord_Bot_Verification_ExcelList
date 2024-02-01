import role_giving


def call(message) -> str:
    p_message = message.lower()

    if p_message == "!verify":
        role_giving.roles()
        return

    return "```Not on the list, please verify manually with Gov Name + Gov ID + Screenshot of the Account```"
