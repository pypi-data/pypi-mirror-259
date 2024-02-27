import typer
import inquirer

class Console:
    def get_input(self, input_name):
        return typer.prompt(f"Enter {input_name}:")
        
    def get_inputs(self, choices):
        questions = [
        inquirer.List('size',
                        message="What size do you need?",
                        choices=choices,
                    ),
        ]
        answers = inquirer.prompt(questions)

        return answers
    
    def print(self, message):
        typer.echo(message)

    def add_default_choices(self, choices):
        choices.append('back')
        choices.append('end')
        return choices

console = Console()

choices = ['service', 'inject endpoint']
inputs = console.get_inputs(choices)
