from rockman.features.redux_toolkit import ReduxToolkit
from rockman.helpers.python_helper import PythonHelper
from rockman.util.console import Console

class Django:
    def __init__(self):
        self.redux_toolkit = ReduxToolkit()
        self.console = Console()
        self.python_helper = PythonHelper()
        self.current_list = 0
        self.current_choice = ""

    def choice(self):
        if self.current_choice == 'init':
            self.console.print("Creating new django end point")
            self.console.print("___________________________")
            self.python_helper.init()

        elif self.current_choice == "add_method":
            self.console.print("Creating new django end point method")
            self.console.print("___________________________")
        elif self.current_choice == "end":
            pass
        elif self.current_choice == "back":
            pass
        else:
            self.console.print("Not implemented")
        
        return self.current_choice
    
    def list_first_choices(self):
        choices = self.console.add_default_choices(['init', 'add_method'])
        self.current_choice = self.console.get_inputs(choices)
    
    def list_second_choices(self):
        if self.current_choice == 'init':
            self.choice()
        elif self.current_choice == 'add_method':
            self.choice()
        else:
            self.console.print("Not implemented")
    
    def list(self):
        if self.current_list == 1:
            self.list_first_choices()
        elif self.current_list == 2:
            self.list_second_choices()
        else:
            self.console.print("Not implemented")
    

    
