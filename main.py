from colorama import Fore

from PIL import Image
import time
import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt


def decisonTree(answers):
    try:
        df = pandas.read_csv("data.csv")
        d = {'Flash': 1, 'Hulk': 0, 'Mulher invisivel':2 , 'Superman' :3}
        df['Hero'] = df['Hero'].map(d)
        
        features = ['Poder especial', 'perigo', 'considera', 'Universo', 'mundo', 'medo', 'precisa','cor']
        X = df[features]
        y = df['Hero']
        dtree = DecisionTreeClassifier()
        dtree = dtree.fit(X, y)

        tree.plot_tree(dtree, feature_names=features)
    except FileNotFoundError:
        print('Falha ao abrir o arquivo')

    return(dtree.predict([answers]))


def getReadAnswers(questions, answers):
    for i in questions:
        print(i)
        try:
            answer = int(input(Fore.CYAN + ' Answer :' +  Fore.RESET))
            if (answer < 1 or answer > 4): 
                raise ValueError(Fore.RED + "Resposta fora do range permitido" + Fore.RESET)
            answers.append(answer)
        except:
            raise TypeError(Fore.RED + "Caractere invalido" + Fore.RESET)
    return answer

def getSimilarHero(hero):
    
    if(hero == 0):
        im = Image.open('hulk.jpg')
        im.show()
    elif(hero == 1):
        im = Image.open('flash.jpg')
        im.show()
    elif(hero == 2):
        im = Image.open('invisivel.jpg')
        im.show()
    elif(hero == 3):
        im = Image.open('superman.jpg')
        im.show()

if __name__ == '__main__':
    answers = []
    questions = [Fore.GREEN + f'\n1) Se você fosse uma super heroína, qual seria seu poder especial? {Fore.RESET}  \n Q(1 - Voar) (2 - Super Força) (3 - Invisibilidade) (4 - Ser imortal):',
                 Fore.GREEN+ f'\n2) A vida das pessoas que você mais ama corre perigo. O que você faz?  {Fore.RESET} \n Q(1 - Procurado Ajuda) (2 - Fugo) (3 - Me escondo) (4 - Protego com Minha vida):',
                 Fore.GREEN+ f'\n3) Você se considera mais...  {Fore.RESET} \n Q(1 - Gentil e docil) (2 - Estiloso e confiante) (3 - Timido) (4 - Esperto)',
                 Fore.GREEN+ f'\n4) Qual seu universo de heróis favorito?  {Fore.RESET} \n Q(1 - DC ) ( 2 - Marvel ) (3 - Os dois) (4 - The boys ):',
                 Fore.GREEN+ f'\n5) Se você pudesse livrar o mundo de algo, o que seria?  {Fore.RESET} \n Q(1 - Injustiças ) ( 2 - Doenças ) (3 - Preconceito) (4 - Outro ):',
                 Fore.GREEN+ f'\n6) Qual seu maior medo?  {Fore.RESET} \n Q(1 - Filmes de Terror ) ( 2 - Palhaços  ) (3 - Morrer) (4 - Outro ):',
                 Fore.GREEN+ f'\n7) Você precisa urgentemente de...  {Fore.RESET} \n Q(1 - Um amor) (2 - Um Doce ) (3 - Adrenalina) (4 - Felicidade):',
                 Fore.GREEN+ f'\n8) Escolha uma Cor  {Fore.RESET} \n Q(1 - Vermelho) (2 - Azul ) ( 3 - Verde) (4 - Preto):']

    print('Bem vindo ao chat bot!')
    print('---------------------------------------------------------------------------------')
    print('Vamos Definir seu heroi favorito de acordo com as suas respostas!!')
    print('---------------------------------------------------------------------------------')
    getReadAnswers(questions, answers)
    print(Fore.YELLOW + '\nBaseado nas suas respostas iremos fazer a IA calcular o heroi que mais se encaixa com você!' + Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX +'\nCalculando...' + Fore.RESET)
    time.sleep(3)
    hero = decisonTree(answers)
    getSimilarHero(hero)
  