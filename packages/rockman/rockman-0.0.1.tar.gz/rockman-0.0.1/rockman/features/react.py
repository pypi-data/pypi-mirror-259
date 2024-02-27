from rockman.features.redux_toolkit import ReduxToolkit
from rockman.util.console import Console

class React:
    def __init__(self):
        self.redux_toolkit = ReduxToolkit()
        self.console = Console()
        self.current_list = 0
        self.current_choice = ""

    def choice(self):
        if self.current_choice == 'api':
            self.console.print("Creating api")
            self.console.print("___________________________")
        elif self.current_choice == "endpoint":
            self.console.print("Creating api")
            self.console.print("___________________________")
        elif self.current_choice == "end":
            pass
        elif self.current_choice == "back":
            pass
        else:
            self.console.print("Not implemented")
        
        return self.current_choice
    
    def list_first_choices(self):
        choices = self.console.add_default_choices(['redux_toolkit', 'components'])
        self.current_choice = self.console.get_inputs(choices)
    
    def list_second_choices(self):
        if self.current_choice == 'redux_toolkit':
            self.redux_toolkit.list(self.current_list)
        else:
            self.console.print("Not implemented")
    
    def list(self):
        if self.current_list == 1:
            self.list_first_choices()
        elif self.current_list == 2:
            self.list_second_choices()
        else:
            self.console.print("Not implemented")
    

    
