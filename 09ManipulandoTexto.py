'''
frase.strip() - remove os espaços inuteis no inicio e no final da frase
frase.rstrip() - remove os espaços a direita
frase.lstrip() - remove os espaços a esquerda

print("""Lorem ipsum dolor sit amet consectetur, adipisicing elit.
Vitae vel corrupti praesentium labore! Illum accusantium ad,
temporibus eius nesciunt explicabo, quas et quis error culpa nemo
repellendus atque labore recusandae!""")'''


frase = 'Curso em Video Python'
dividido = frase.split()
print(frase.upper().count('O'))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
print(frase.find('Video'))
print(frase.lower().find('video'))
print(frase.split())
print(dividido[0])
print(dividido[2][3])

