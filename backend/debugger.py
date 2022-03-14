""" Module which contains the setup for an attachable debugger """
import multiprocessing

import debugpy


def initialize_django_debugger():
    """ Method to intialise debugging server """
    if multiprocessing.current_process().pid > 1:

        debugpy.listen(("0.0.0.0", 5678))
        print(
            "⏳ VS Code debugger can now be attached, press F5 in VS Code ⏳",
            flush=True,
        )
        debugpy.wait_for_client()
        print("� VS Code debugger attached, enjoy debugging �", flush=True)
