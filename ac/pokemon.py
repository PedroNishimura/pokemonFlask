from requests import api
from dataclasses import dataclass
from enum import Enum, auto
"""
Integrantes:

xxxxxxxxxxxxxxxxxxxx - RA


Instruções para TODOS os exercícios/funções abaixo:

1. Veja as instruções de como instalar e executar o PokéAPI.

2. None e strings em branco são sempre consideradas inválidas 
quando utilizadas como parâmetros.

3. Não se preocupe com erros de tipo (como por exemplo, passar 
uma string para uma função que trabalha com números). Esse tipo 
de coisa não está nos testes.

4. Todos os nomes de pokémons nos testes estão em letras minúsculas.
   Entretanto, se você quiser aceitar MAIÚSCULAS ou até mesmo 
   mIsTuRaDo, aplicando uma chamada à lower() ou coisa semelhante, 
   isso fica a seu critério.
   Os testes não verificam diferenças de maiúsculas/minúsculas.

5. Desconsiderando-se os erros de tipo, se algum parâmetro puder 
ser determinado como inválido antes que alguma chamada a um 
servidor externo seja realizada, então ele deve ser detectado 
como tal sem que o servidor seja contactado, mesmo se ele estiver 
off-line.

6. Em todos os casos onde procura-se algum tipo de pokémon pelo 
nome ou pelo número e o mesmo não existir, uma exceção 
PokemonNaoExisteException deve ser lançada.

7. Modere as suas conexões com a URL externa pública da 
PokéAPI (https://pokeapi.co).
    O motivo disso é que eles irão bloquear IPs que fizerem um 
    número muito grande de requisições em um intervalo de tempo 
    muito curto.
    No entanto, você não deverá ter problemas para usar a API 
    pública se não estiver abusando e usando apenas na sua casa.

8. Consulte a documentação em (https://pokeapi.co/docs/v2.html).

9. Não se esqueça de configurar o arquivo config.json para que 
o script dos testes possa encontrar os servidores locais da 
PokéAPI.

10. Seguem alguns exemplos de URLs que podem servir para te ajudar:
    https://pokeapi.co/api/v2/pokemon/39/
    https://pokeapi.co/api/v2/pokemon/jigglypuff/
    https://pokeapi.co/api/v2/pokemon-species/39/
    https://pokeapi.co/api/v2/pokemon-species/jigglypuff/
    https://pokeapi.co/api/v2/growth-rate/1/

Não altere estas URLs. Elas são utilizadas para conectar no 
PokéAPI.
"""
site_pokeapi = "http://pokeapi.co"

"""
Use isso como parâmetro "timeout" em todas as chamadas ao requests.
Por exemplo:
    api.get(f"{site_pokeapi}/api/v2/", timeout = limite)
"""
limite = (4, 12)

"""
Isso daqui serve para deixar o código mais rápido, fazendo 
cache dos resultados de chamadas. Não altere isso.
"""
def cached(what):
    from functools import wraps
    cache = {}
    @wraps(what)
    def caching(n):
        if n not in cache: cache[n] = what(n)
        return cache[n]
    return caching

"""
Vamos precisar desta exceção. Não altere o código delas.
"""
class PokemonNaoExisteException(Exception):
    pass

dic_cores = {
    "brown": "marrom",
    "yellow": "amarelo",
    "blue": "azul",
    "pink": "rosa",
    "gray": "cinza",
    "purple": "roxo",
    "red": "vermelho",
    "white": "branco",
    "green": "verde",
    "black": "preto"
}

dic_tipos = {
    "normal": "normal",
    "fighting": "lutador",
    "flying": "voador",
    "poison": "veneno",
    "ground": "terra",
    "rock": "pedra",
    "bug": "inseto",
    "ghost": "fantasma",
    "steel": "aço",
    "fire": "fogo",
    "water": "água",
    "grass": "grama",
    "electric": "elétrico",
    "psychic": "psíquico",
    "ice": "gelo",
    "dragon": "dragão",
    "dark": "noturno",
    "fairy": "fada"
}

"""
1. Dado o número de um pokémon, qual é o nome dele?


Observações:
- Presuma que nunca irá existir mais do que 5000 pokémons 
diferentes.
- Também não existe pokémon de número zero ou negativo.
- Assim sendo, nem precisa fazer a requisição nesses casos.
- Se o pokémon não existir, lance uma PokemonNaoExisteException.
"""
@cached
def nome_do_pokemon(numero):
    if numero < 1 or numero >= 5000: raise PokemonNaoExisteException()
    resposta = api.get(f"{site_pokeapi}/api/v2/pokemon/{numero}", timeout = limite)
    if resposta.status_code == 404: raise PokemonNaoExisteException()
    if resposta.status_code != 200: raise Exception(f"{resposta.status_code} - {resposta.text}")
    dic = resposta.json()
    return dic['name']


"""
2. Dado o nome de um pokémon, qual é o número dele?

Observações:
- Não se esqueça de verificar os casos onde o pokémon procurado não exista 
(PokemonNaoExisteException).
"""
@cached
def numero_do_pokemon(nome):
    if nome is None or nome == "": raise PokemonNaoExisteException()
    resposta = api.get(f"{site_pokeapi}/api/v2/pokemon/{nome}", timeout = limite)
    if resposta.status_code == 404: raise PokemonNaoExisteException()
    if resposta.status_code != 200: raise Exception(f"{resposta.status_code} - {resposta.text}")
    dic = resposta.json()
    return dic['id']

#print(numero_do_pokemon("pikachu"))

"""
3. Dado o nome de um pokémon, qual é o nome da cor (em inglês) predominante dele?

Observações:
- Não se esqueça de verificar os casos onde o pokémon procurado não exista.
"""
@cached
def color_of_pokemon(nome):
    if nome is None or nome == "": raise PokemonNaoExisteException()
    resposta = api.get(f"{site_pokeapi}/api/v2/pokemon-species/{nome}", timeout = limite)
    if resposta.status_code == 404: raise PokemonNaoExisteException()
    if resposta.status_code != 200: raise Exception(f"{resposta.status_code} - {resposta.text}")
    dic = resposta.json()
    return dic['color']['name']




"""
4. Dado o nome de um pokémon, qual é o nome da cor (em português) 
predominante dele?

Observações:
- Os nomes de cores possíveis de pokémons em português são APENAS 
as "marrom", "amarelo", "azul", "rosa", "cinza", "roxo", 
"vermelho", "branco", "verde" e "preto".
- No entanto, a pokeapi ainda não foi traduzida para o português! 
Como você pode dar um jeito nisso?

Dicas:
- Faça uma invocação à função color_of_pokemon acima.
"""
@cached
def cor_do_pokemon(nome):
    if nome is None or nome == "": raise PokemonNaoExisteException()
    resposta = api.get(f"{site_pokeapi}/api/v2/pokemon-species/{nome}", timeout = limite)
    if resposta.status_code == 404: raise PokemonNaoExisteException()
    if resposta.status_code != 200: raise Exception(f"{resposta.status_code} - {resposta.text}")
    resposta = resposta.json()
    cor = color_of_pokemon(nome)
    if cor in dic_cores.keys():
        cor = dic_cores[cor]
    resposta['color']['nome'] = cor
    return resposta['color']['nome']

"""
5. Dado o nome de um pokémon, quais são os tipos no qual ele se 
enquadra?
Os nomes dos tipos de pokémons em português são "normal", 
"lutador", "voador", "veneno", "terra", "pedra", "inseto", 
"fantasma", "aço", "fogo", "água", "grama", "elétrico", "psíquico", "gelo", "dragão", "noturno" e "fada".
Todo pokémon pode pertencer a um ou a dois tipos diferentes. 
Retorne uma lista (ou um set ou uma tupla ou coisa similar, 
se preferir) contendo os tipos, mesmo que haja somente um.
Se houver dois tipos, a ordem não é importante.

Observações:
- Não se esqueça de verificar os casos onde o pokémon procurado não exista.
"""
@cached
def tipos_do_pokemon(nome):
    if nome is None or nome == "": raise PokemonNaoExisteException()
    resposta = api.get(f"{site_pokeapi}/api/v2/pokemon-species/{nome}", timeout = limite)
    if resposta.status_code == 404: raise PokemonNaoExisteException()
    if resposta.status_code != 200: raise Exception(f"{resposta.status_code} - {resposta.text}")
    resposta = resposta.json()
    lista_Ingles = []
    for cont in range(0, len(resposta['egg_groups']), 1):
        lista_Ingles.append(resposta['egg_groups'][cont]['name'])
    lista = []
    for tipo in lista_Ingles:
        if tipo in dic_tipos.keys():
            lista.append(dic_tipos[tipo])
    return lista

"""
6. Dado o nome de um pokémon, liste de qual pokémon ele evoluiu.
Por exemplo, evolucao_anterior('venusaur') == 'ivysaur'
Retorne None se o pokémon não tem evolução anterior. 
Por exemplo, evolucao_anterior('bulbasaur') == None

Observações:
- Não se esqueça de verificar os casos onde o pokémon 
procurado não exista.
"""
@cached
def evolucao_anterior(nome):
    raise Exception("Não implementado.")

"""
7. A medida que ganham pontos de experiência, os pokémons sobem 
de nível. É possível determinar o nível (1 a 100) em que um 
pokémon se encontra com base na quantidade de pontos de 
experiência que ele tem.
Entretanto, cada tipo de pokémon adota uma curva de level-up 
diferente. Assim sendo, dado um nome de pokémon e uma 
quantidade de pontos de experiência, retorne o nível em que 
este pokémon está.
Valores negativos de experiência devem ser considerados 
inválidos.

Observações:
- Não se esqueça de verificar os casos onde o pokémon procurado 
não exista.
- Lance uma exceção ValueError para os casos onde o valor da 
experiência é negativo.
- Não realize os cálculos diretamente nesta função implementando 
nela alguma fórmula matemática. Utilize a API para fazer os 
cálculos.
"""
def nivel_do_pokemon(nome, experiencia):
    resposta1 = api.get(f"{site_pokeapi}/api/v2/pokemon-species/{nome}", timeout = limite)
    teste = resposta1.json()['growth_rate']['url']
    resposta2 = api.get(teste)

"""
Até agora, temos representado as espécies de pokemóns apenas como uma string, no entanto podemos representá-los com uma classe.
Esta classe representa uma espécie de pokémon, e cada instância carrega dentro de si o nome de uma espécie de pokémon, a cor e as informações da evolução.
"""
@dataclass(frozen = True)
class EspeciePokemon:
    nome: str
    cor: str
    evoluiu_de: str
    evolui_para: list

"""
Vamos precisar desta classe logo abaixo.
"""
class Genero(Enum):
    FEMININO = auto()
    MASCULINO = auto()

    @staticmethod
    def decodificar(valor):
        for g in Genero:
            if g.name.lower() == valor:
                return g
        raise ValueError()
    def __str__(self):
        return self.name.lower()

"""
Agora, nós implementaremos alguns métodos desta classe (Pokemon). 
Não deve-se confundí-la com EspeciePokemon.
Vamos supor que você tenha dois pokémons da espécie Ponyta. 
Para diferenciá-los, decida chamar um de "veloz" e o outro de 
"ligeirinho".
Seu amigo também tem uma Ponyta, que ele chama de "quentinha".
Nesse caso, "veloz", "ligeirinho" e "quentinha" são três Ponytas 
diferentes, pertencentes a dois treinadores diferentes.
Além disso, esses diferentes pokémons, embora da mesma espécie, 
também podem ser de sexos diferentes e com diferentes quantidades 
de pontos de experiência.
"""
class Pokemon:

    def __init__(self, nome_treinador, apelido, tipo, experiencia, genero):
        if experiencia < 0: raise ValueError()
        self.__nome_treinador = nome_treinador
        self.__apelido = apelido
        self.__tipo = tipo
        self.__experiencia = experiencia
        self.__genero = genero

    #Não mexa nisso.
    def __setattr__(self, attr, value):
        if attr.find("__") == -1: raise AttributeError(attr)
        super().__setattr__(attr, value)

    @property
    def nome_treinador(self):
        return self.__nome_treinador

    @property
    def apelido(self):
        return self.__apelido

    @property
    def tipo(self):
        return self.__tipo

    @property
    def experiencia(self):
        return self.__experiencia

    @property
    def genero(self):
        return self.__genero

