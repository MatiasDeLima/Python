minha_senha = "12344321";

def verificar_senha(nova_senha):
    if len(nova_senha) > 6:
        print("Válida");
    else:
        print("Inválida");