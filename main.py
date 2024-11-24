from Usuario import Usuario 

def main():

    usuario1 = Usuario("Lucas", "123")
    usuario1.login()
    usuario1.modificar_senha()

if __name__ == "__main__":
    main()