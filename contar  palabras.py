def contar_palabra(texto):
    texto = texto.split ()
    palabra = {}
    for i in texto:
        if i in palabra:
            palabra[i]+= 1
        else:
            palabra[i] = 1
    return palabra

def mas_repetida(palabra):
    mas_usada = ''
    max_frecuencia = 0
    for word, freq in palabra.items():
        if freq > max_frecuencia:
            mas_usada = word
            max_frecuencia = freq
    return mas_usada, max_frecuencia

texto='la Universidad politecnica salesiana es una institucion de educacion superior humanista y politecnica, de inspiracion cristiana con caracter catolico e indole salesiana; dirigida de maera preferencial a jovenes de los sectores populares, busca formar honrrados ciudadanos y buenos cristianos,con excelencia humana y academica con  capacidad investigativa e innovadora, que contribuyen al desarrollo sostenible local y nacional.'
print(contar_palabra(texto))
print(mas_repetida(contar_palabra(texto)))
      
    
