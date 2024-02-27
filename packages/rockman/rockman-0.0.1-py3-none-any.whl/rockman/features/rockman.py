from rockman.features.react import React
from rockman.features.django import Django
from rockman.util.console import Console


class Rockman:
    def __init__(self, model_name, api_name):
        self.model_name = model_name
        self.api_name = api_name
        self.result_string = ""
        self.console = Console()
        self.react = React()
        self.django = Django()
        self.current_list = 0
        self.main_choice = ""
        self.current_choice = ""

    def list_first_choices(self):
        choices = self.console.add_default_choices(['django', 'react', 'react-native', 'flutter', 'vue', 'angular', 'exit'])
        self.main_choice = self.console.get_inputs(choices)
        self.current_choice = self.main_choice
        self.next_list()
    
    def next_list(self):
        self.current_list += 1
        if self.main_choice == 'react':
            self.react.list(self.current_list, self.current_choice)

        if self.main_choice == 'django':
            self.django.list(self.current_list, self.current_choice)

        if self.main_choice == 'end':
            self.end_session()

        if self.main_choice == 'back':
            self.current_list -= 2
            if self.current_list < 0:
                self.current_list = 0
                self.list_first_choices()
            else:
                self.next_list()
            self.next_list()
    
    def start_session(self):
        self.console.print("Welcome to Artisan")
        self.console.print("What do you want to do?")
        self.list_first_choices()
        self.next_list()

    def continue_session(self):
        self.next_list()

    def end_session(self):
        self.console.print("Thank you for using Artisan")
        self.console.print("Bye!")

    def not_implemented(self):
        self.console.print("Not implemented")
    
    def get_model_and_api_names(self):
        self.model_name = self.console.get_input("model name")
        self.api_name = self.console.get_input("api name")

    def generate_redux_toolkit(self):
        self.result_string = self.redux_toolkit.update_template()
        self.redux_toolkit.save_template_service()
        self.redux_toolkit.save_template_injected_endpoint()

    
