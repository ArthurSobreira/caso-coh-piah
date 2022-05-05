import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos
    fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")
    print()
    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    sum = 0
    for c in range(0, 6):
        sum += abs(as_a[c] - as_b[c])
    grau = sum / 6
    if grau < 0:
        grau = grau * (-1)

    return grau


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    # Listas de sentenças, frases e palavras no texto.
    list_sen = separa_sentencas(texto)
    list_fra = []
    for c in list_sen:
        list_fra.append(separa_frases(c))
    list_pal = []
    for i in list_fra:
        for j in i:
            list_pal.append(separa_palavras(j.lower()))
    list_tot_pal = []
    for c in list_pal:
        for i in c:
            list_tot_pal.append(i)

    # Tamanho médio de palavra.
    sum_pal = 0
    tot_pal = 0
    for c in list_tot_pal:
        sum_pal += (len(c))
        tot_pal += 1
    tam_med_pal = (sum_pal/tot_pal)

    # Relação Type-Token.
    list_pal_dif = []
    for c in list_tot_pal:
        if c.lower() not in list_pal_dif:
            list_pal_dif.append(c)
    rel_typ_tok = (len(list_pal_dif) / tot_pal)

    # Razão Hapax Legomana
    pal_uni = n_palavras_unicas(list_tot_pal)
    raz_hap_leg = (pal_uni/tot_pal)

    # Tamanho médio de sentença
    sum_car_sen = 0
    for c in list_sen:
        sum_car_sen += len(c)
    tam_med_sen = sum_car_sen / (len(list_sen))

    # Complexidade de sentença
    tot_fra = 0
    for c in list_fra:
        for i in c:
            tot_fra += 1
    comp_sen = tot_fra / (len(list_sen))

    # Tamanho médio de frase
    sum_car_fra = 0
    for c in list_fra:
        for i in c:
            sum_car_fra += (len(i))
    tam_med_fra = sum_car_fra / tot_fra

    return [tam_med_pal, rel_typ_tok, raz_hap_leg, tam_med_sen, comp_sen, tam_med_fra]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    list_ass = []
    for c in range(0, len(textos)):
        ass = calcula_assinatura(textos[c])
        simi = compara_assinatura(ass, ass_cp)
        list_ass.append(simi)
    infec = (list_ass.index(min(list_ass))) + 1

    return infec


def main():
    ass_inf = le_assinatura()
    print()
    list_txt = le_textos()
    print()

    return print(f'O autor do texto {avalia_textos(list_txt, ass_inf)} está infectado com COH-PIAH')


if __name__ == '__main__':
    main()
