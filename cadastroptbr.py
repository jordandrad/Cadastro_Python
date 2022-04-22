from time import sleep

class Usuario:
    def __init__(self, name, username, password, birth, age, email, plan):
        self.name = name
        self.username = username
        self.username_list = []
        self.password_list = []
        self.password = password
        self.birth = birth
        self.age = age
        self.email = email
        self.plan = plan
        self.plan_list =  ['basico', 'intermediario', 'premium']
        self.username_list = self.username
        self.password_list = self.password

    def change_password(self, old_password, new_password):
        if self.password == old_password:
            self.password = new_password
            print('Senha alterada com sucesso!')
        else:
            print('Erro, tente novamente!')

    def change_plan(self, new_plan):
        if new_plan in self.plan_list:
            self.plan = new_plan
            print(f'Plano alterado para {new_plan} com sucesso!')
        else:
            print('Erro, tente novamente!')

    def show_info(self):
        print(f'''Nome: {self.name}
Senha:{self.password} 
Nome de usuário: {self.username}
Data de nascimento: {self.birth}
Idade:{self.age}
Email: {self.email}
Plano Atual: {self.plan}''')

    def verify_user(self, verify_name, verify_password):
         if verify_name in self.username_list and verify_password in self.password_list:
             print('Autenticação concluída!')
         else:
             print('Dados incorretos!')





print('Olá, seja bem vindo(a)! Por favor preencha os dados abaixo: ')
usuario1 = Usuario(input('Nome:'),input('Nome de usuário:') ,input('Senha:'), input('Data de nascimento:'), input('Idade:'), input('Email:'), input('Plano:'))


menu = 0
while menu < 5:

    print('Menu:')
    print('''
    1. Mudar senha
    2. Mudar plano
    3. Ver meus dados
    4. Verificação de segurança
    5. Encerrar programa''')
    menu = int(input('Escolha uma opção: '))
    if menu == 1:
        usuario1.change_password(input('Senha antiga: '), input('Nova senha: '))
    elif menu == 2:
        print(f'Seu plano atual: {usuario1.plan}')
        usuario1.change_plan(input(''' 
        Planos disponíveis:
        basico
        intermediario
        premium 
        Digite o plano que você deseja:  '''))

    elif menu == 3:
        sleep(2)
        usuario1.show_info()

    elif menu == 4:
        usuario1.verify_user(input('Nome de usuário:'), input('Senha: '))

    else:
        print('Programa finalizado, até mais! ;)')
