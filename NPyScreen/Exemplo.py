import npyscreen

class FormularioPaciente(npyscreen.Form):
    def create(self):
        self.add(npyscreen.FixedText, value="Cadastro de Paciente", editable=False, color='STANDOUT')
        self.cpf = self.add(npyscreen.TitleText, name="CPF:")
        self.nome = self.add(npyscreen.TitleText, name="Nome:")
        self.data_nasc = self.add(npyscreen.TitleText, name="Data Nasc (DD/MM/AAAA):")

    def afterEditing(self):
        self.parentApp.setNextForm(None)

class AppPaciente(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", FormularioPaciente)

if __name__ == "__main__":
    app = AppPaciente()
    app.run()

    form = app.getForm("MAIN")
    print("\n✅ Dados preenchidos:")
    print(f"CPF: {form.cpf.value}")
    print(f"Nome: {form.nome.value}")
    print(f"Data de Nascimento: {form.data_nasc.value}")
