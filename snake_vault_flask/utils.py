# :----------------------------------------------------------------------- INFO
# :[Snake-Vault-Flask/snake_vault_flask/utils.py]
# :author        : fantomH
# :created       : 2024-06-03 11:11:09 UTC
# :updated       : 2024-08-18 15:10:09 UTC
# :description   : Flask utils.

from flask import current_app

# :-----/ (function) get_app_context() /-----:
def get_app_context():
    '''(function) get_app_context()

    Print attributes of all app_context attributes name and value.
    '''

    with current_app.app_context():
        print()
        print("================================================================================")
        print("Attributes accessible within app_context:")
        for attr_name in dir(current_app):
            if not attr_name.startswith('_'):
                attr_value = getattr(current_app, attr_name)
                print(f"{attr_name}: {attr_value}")
        print("================================================================================")
        print()
