def mmc(a, b):
    if a < b:
        menor = a
        maior = b
    else:
        menor = b
        maior = a

    while menor > 0:
        maior_antes = maior
        maior = menor
        menor = maior_antes % menor

    if maior > menor:
        vmdc = maior
    else:
        vmdc = menor

    return int((a * b) / vmdc)

def mdc(a, b):
    if a < b:
        menor = a
        maior = b
    else:
        menor = b
        maior = a

    while menor > 0:
        maior_antes = maior
        maior = menor
        menor = maior_antes % menor

    if maior > menor:
        vmdc = maior
    else:
        vmdc = menor

    return vmdc

def euclidean_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)

def fatorial(n):
    fat = 1
    while n >= 1:
        fat = fat * n
        n -= 1
    return fat

def celsius_para_fahrenheit(temp_em_celsius):
    return 1.8 * temp_em_celsius + 32

def fahrenheit_para_celsius(temp_em_fahrenheit):
    return (temp_em_fahrenheit - 32) / 1.8

def eh_palindromo(frase):
    i = 0
    f = len(frase) - 1
    metade = len(frase) // 2
    while i < metade:
        if frase[i] != frase[f]:
            return False
        i += 1
        f -= 1
    return True

def horas_minutos_segundos(tempo_em_ms):
    horas = tempo_em_ms // 3600000
    minutos = (tempo_em_ms % 3600000) // 60000
    segundos = ((tempo_em_ms % 3600000) % 60000) / 1000

    return str(horas) + ":" + str(minutos) + ":" + str(segundos)

if __name__ == '__main__':
    print('MMC: ', mmc(5, 8))
    print('MDC: ', mdc(5, 8))
    print('Distância: ', euclidean_distance(1, 2, 2, 2))
    print('Fatorial: ', fatorial(5))
    print('Celsius para Fahrenheit: ', celsius_para_fahrenheit(0), 'ºF')
    print('Fahrenheit para Celsius: ', fahrenheit_para_celsius(100), 'ºC')
    print('Eh Palindromo: ', eh_palindromo("arara"))
    print('Eh Palindromo: ', eh_palindromo("amor a romar"))
    print('HH:MM:SS: ', horas_minutos_segundos(36111100))
