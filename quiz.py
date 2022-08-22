contador = 0
alternativas=['a','b','c','d','e']

print('Olá! Este é o quiz sobre conscientização de DSTs e educação sexual em geral!\n')


def pergunta1():
    global contador
    questao = True
    
    print('1) O que significa DST?\n')
    print('a) Doença super transmissível\n')
    print('b) Doença sexualmente transmissível\n')
    print('c) Doença sem transmissão\n')
    print('d) Dark Souls Três\n')
    print('e) Não existe o termo DST\n')
    r = input('A alternativa correta é?\n')
    if r in alternativas:
        questao=False
    else:
        while questao:
            r = input('Responda com apenas (a, b, c, d ou e): \n')
            if r in alternativas:
                questao=False
    if r == 'b':
        contador += 12.5
        print('\nVocê acertou!\n')
    else:
        contador += 0
        print('\nVocê errou! DST é uma sigla para doença sexualmente transmissível, logo a resposta correta é a letra B.\n')
    return contador
    


print (pergunta1(), '\n')


def pergunta2():
    global contador
    questao = True
    
    print('2) São exemplos de DST:\n')
    print('a) HIV, gonorreia e HPV\n')
    print('b) HIV, câncer e gonorreia\n')
    print('c) HPV, Covid-19 e sífilis\n')
    print('d) HPV, HIV e dengue\n')
    print('e) Dengue, covid-19 e câncer\n')
    r = input('A alternativa correta é?\n')
    if r in alternativas:
        questao=False
    else:
        while questao:
            r = input('Responda com apenas (a, b, c, d ou e):\n ')
            if r in alternativas:
                questao=False
    if r == 'a':
        contador += 12.5
        print ('\nVocê acertou!\n')
    else:
        contador += 0
        print('\nVocê errou! Câncer não é uma doença transmissível, Covid-19 e dengue não são transmitidas essencialmente por contato sexual, logo a opção correta é a letra A.\n')
    return contador 
    
print (pergunta2(), '\n')


def pergunta3():
    global contador
    questao = True
    
    print('3) Sobre o uso de métodos contraceptivos e as doenças sexualmente transmissíveis, marque a alternativa INCORRETA:\n')
    print('a) A camisinha é um método que previne a gravidez, além de proteger contra algumas doenças sexualmente transmissíveis.\n')
    print('b) A camisinha é o único método que devemos nos preocupar.\n')
    print('c) De todos os métodos contraceptivos, a camisinha é o mais eficaz na proteção contra DSTs.\n')
    print('d) Algumas doenças sexualmente transmissíveis podem ser evitadas com medidas de higiene.\n')
    print('e) Conhecer bem seu parceiro é extremamente importante.\n')
    r = input('A alternativa correta é?\n')

    if r in alternativas:
        questao=False
    else:
        while questao:
            r = input('Responda com apenas (a, b, c, d ou e):\n')
            if r in alternativas:
                questao=False


    if r == 'b':
        contador += 12.5
        print ('\nVocê acertou!\n')
    else:
        contador += 0
        print('\nVocê errou! Existem diversos outros métodos igualmente importantes na prevenção de DST’s,\n'
    'apesar da camisinha ser o principal e o mais efetivo, logo a resposta incorreta é a letra B.\n')
    return contador 
    
print (pergunta3(), '\n')


def pergunta4():
    global contador
    questao = True
    
    print('4) Marque a alternativa CORRETA. Quem pode ser afetado por DST?\n')
    print('a) Homens\n')
    print('b) Mulheres\n')
    print('c) Animais\n')
    print('d) Todas as opções\n')
    print('e) Nenhuma das opções\n')
    r = input('A alternativa correta é?\n')

    if r in alternativas:
        questao=False
    else:
        while questao:
            r = input('Responda com apenas (a, b, c, d ou e):\n')
            if r in alternativas:
                questao=False


    if r == 'd':
        contador += 12.5
        print ('\nVocê acertou!\n')
    else:
        contador += 0
        print('\nVocê errou! Qualquer um está sujeito às DST’s, inclusive os animais que tem DST’s exclusivamente deles, portanto a resposta é a letra D.\n')
    return contador 
    
print (pergunta4(), '\n')


def pergunta5():
    global contador
    questao = True
    
    print('5) O vírus HIV, causador da AIDS, continua sendo, a cada ano, responsável por milhares de óbitos na população infectada.\n', 
    'É comum relacionar o falecimento do soropositivo às doenças oportunistas. A existência de doenças oportunistas deve-se ao fato de o vírus HIV:\n')
    print('a) Liberar toxinas que contribuem para a proliferação dessas doenças.\n')
    print('b) Fornecer antígenos patogênicos ao seu portador.\n')
    print('c) Destruir os anticorpos responsáveis pelo sistema imune.\n')
    print('d) Potencializar a reprodução de microrganismos patológicos.\n')
    print('e) Parasitar as células de defesa do organismo humano.\n')
    r = input('A alternativa correta é?\n')

    if r in alternativas:
        questao=False
    else:
        while questao:
            r = input('Responda com apenas (a, b, c, d ou e):\n')
            if r in alternativas:
                questao=False


    if r == 'e':
        contador += 12.5
        print ('\nVocê acertou!\n')
    else:
        contador += 0
        print('\nVocê errou! HIV é um vírus que ataca o portador continuamente, fazendo com que a imunidade dele caia,\n',
    'tornando o portador mais vulnerável a outros tipos de doenças e vírus, logo a resposta certa é a letra E\n')
    return contador 
    

print (pergunta5(), '\n')


def pergunta6():
    global contador
    questao = True
    
    print('6) Analise as afirmativas sobre prevenção de DST’s:\n', 
    'I – Existem camisinhas femininas que oferecem proteção contra DST’S\n',
    'II – Pílulas anticoncepcionais protegem contra DST’s\n',
    'III – Camisinha é o método mais eficaz na prevenção contra DST’s',
    'Estão Corretas:\n')
    print('a) I, II, II\n')
    print('b) I, II\n')
    print('c) I, III\n')
    print('d) II, III\n')
    print('e) nenhuma das alternativas\n')
    r = input('A alternativa correta é?\n')

    if r in alternativas:
        questao=False
    else:
        while questao:
            r = input('Responda com apenas (a, b, c, d ou e):\n')
            if r in alternativas:
                questao=False


    if r == 'c':
        contador += 12.5
        print ('\nVocê acertou!\n')
    else:
        contador += 0
        print('\nVocê errou! Pílulas anticoncepcionais apenas evitam uma possível gravidez, mas não protegem contra DST’s,\n', 
    'logo, apenas a afirmativa I e III estão corretas, logo, letra C.\n')
    return contador 
    

print (pergunta6(), '\n')


def pergunta7():
    global contador
    questao = True
    
    print('7) O HPV é causador:\n')
    print('a) da sífilis\n')
    print('b) da gonorréia.\n')
    print('c) da AIDS.\n')
    print('d) do cancro mole.\n')
    print('e) do câncer de útero.\n')
    r = input('A alternativa correta é?\n')

    if r in alternativas:
        questao=False
    else:
        while questao:
            r = input('Responda com apenas (a, b, c, d ou e):\n')
            if r in alternativas:
                questao=False


    if r == 'e':
        contador += 12.5
        print ('\nVocê acertou!\n')
    else:
        contador += 0
        print('\nO HPV acaba causando células cancerígenas, por uma razão de que o nosso sistema imunológico\n',
    'não consegue combater o vírus, desenvolvendo assim, células anormais, logo a resposta correta é a letra E\n')
    return contador 
    
print (pergunta7(), '\n')


def pergunta8():
    global contador
    questao = True
    
    print('8) Sobre a pornografia devemos afirmar:\n')
    print('a) É a melhor referência no estudo de métodos de prevenção\n')
    print('b) Representa corretamente as relações sexuais\n')
    print('c) Não é nem um pouco recomendado pois a pornografia retrata cenários que não condizem com a realidade, causando\n',
    'problemas psicológicos no usuário, além de objetificar principalmente mulheres\n')
    print('d) Pornografia é um hábito que não causa vícios\n')
    print('e) Pornografia não objetifica as pessoas\n')
    r = input('A alternativa correta é?\n')

    if r in alternativas:
        questao=False
    else:
        while questao:
            r = input('Responda com apenas (a, b, c, d ou e):\n')
            if r in alternativas:
                questao=False


    if r == 'c':
        contador += 12.5
        print ('\nVocê acertou!\n')
    else:
        contador += 0
        print('\nUma coisa que muitos não tomam consciência sobre o consumo da pornografia, é que as relações retratadas\n',
    'não condizem de forma alguma com a realidade e acabam desencadeando diversos problemas psicológicos seja de vício\n',
    'baixa autoestima e até mesmo depressão, além de objetificar as pessoas, principalmente mulheres, fazendo com que a pessoa\n',
    'que consome a pornografia comece a ter uma visão errônea das pessoas, logo a resposta correta é a letra C\n')
    return contador 
    

print (pergunta8(), '\n')

print('Fim de jogo!')
print('Você fez', contador, 'pontos!\n')

if contador >= 87.5:
    print ('Ótimo! Você foi muito bem, e ja domina o assunto,\n'
'fique a vontade para pesquisar mais sobre!\n')

elif contador == 75 or contador == 50:
    print ('Boa! Você tem um bom conhecimento em educação sexual, com mais um pouco\n'
'de estudo, você já vai estar dominando!\n')

elif contador == 25:
    print ('Você não foi tão bem... Mas não se desanime! Com um pouco de\n',
'esforço nos estudos você irá melhorar rapidinho!\n')

else: 
    print ('Que pena, voce foi muito mal..., aprofunde mais os seus conhecimentos\n',
'relacionados a educação sexual, que você irá melhor na próxima vez!\n',
'E não se esqueça educação sexual é super importante, pois previne você e seu parceiro(a)\n',
'de possíveis doenças, gravidez, entre diversos outros possíveis problemas futuros!\n')


print('Obrigado por jogar!')