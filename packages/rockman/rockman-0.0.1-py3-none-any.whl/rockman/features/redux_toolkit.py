from rockman.util.console import Console


class ReduxToolkit:
    def __init__(self,model_name,api_name):
        self.model_name = model_name
        self.api_name = api_name
        self.result_string = ""
        self.console = Console()
        self.current_choice = ""
        self.end_session = False
        self.back = False
        pass

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
        choices = self.console.add_default_choices(['api', 'endpoint'])
        self.current_choice = self.console.get_inputs(choices)
    
    def list_second_choices(self):
        choices = self.console.add_default_choices(['restart', 'end'])
        self.current_choice = self.console.get_inputs(choices)
    
    def list(self, current_list):
        if current_list == 1:
            self.list_first_choices()
        elif current_list == 2:
            self.list_second_choices()

        self.choice()