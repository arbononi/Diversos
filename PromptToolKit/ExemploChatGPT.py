from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.application import Application
from prompt_toolkit.layout import Layout, HSplit
from prompt_toolkit.widgets import TextArea, Label, Button, Dialog
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style

def iniciar_formulario():
    cpf_field = TextArea(height=1, prompt='CPF: ')
    nome_field = TextArea(height=1, prompt='Nome: ')
    data_nasc_field = TextArea(height=1, prompt='Data de Nascimento: ')

    resultado = {}

    def salvar():
        resultado['cpf'] = cpf_field.text
        resultado['nome'] = nome_field.text
        resultado['data_nasc'] = data_nasc_field.text
        app.exit()

    btn_salvar = Button(text="Salvar", handler=salvar)

    dialog = Dialog(
        title="Cadastro de Paciente",
        body=HSplit([
            cpf_field,
            nome_field,
            data_nasc_field
        ]),
        buttons=[btn_salvar],
        modal=True,
        with_background=True
    )

    layout = Layout(dialog)
    app = Application(layout=layout, full_screen=False)
    app.run()
    
    return resultado

dados = iniciar_formulario()
print("\n✅ Dados preenchidos:")
print(f"CPF: {dados['cpf']}")
print(f"Nome: {dados['nome']}")
print(f"Data de nascimento: {dados['data_nasc']}")
