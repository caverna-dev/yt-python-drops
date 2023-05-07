# import secundario

def executa_soma(x, y):
    return x + y

def solicita_numero():
    return input("Informe um numero: ")

if __name__ == "__main__":
    a = int(solicita_numero())
    b = int(solicita_numero())
    print(executa_soma(a, b))