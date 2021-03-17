import unittest
from requests import api
from pokemon_teste_base import *

parar_no_primeiro_erro = False

ultimo_pokemon = 893

class TestPokemon(unittest.TestCase):

    @teste("Não mexeu onde não deveria", 0, "offline", penalidade = 20)
    def test_A_00a_genero_ok(self):
        if len(Genero) != 2 or Genero.MASCULINO == Genero.FEMININO or str(Genero.MASCULINO) != "masculino" or str(Genero.FEMININO) != "feminino":
            raise Exception("Você bagunçou com a classe Genero.")

    @teste("Não mexeu onde não deveria", 0, "offline", penalidade = 20)
    def test_A_00b_especie_pokemon_ok(self):
        self.assertEqual(pidgeotto.nome, "pidgeotto")
        self.assertEqual(pidgeotto.cor, "marrom")
        self.assertEqual(pidgeotto.evoluiu_de, "pidgey")
        self.assertEqual(pidgeotto.evolui_para, ["pidgeot"])

    @teste("Não mexeu onde não deveria", 0, "offline", penalidade = 20)
    def test_A_00c_especie_pokemon_imutavel(self):
        def xxx1(): pidgeotto.nome = "dollynho"
        def xxx2(): pidgeotto.cor = "verde"
        def xxx3(): pidgeotto.evoluiu_de = "sua mãe"
        def xxx4(): pidgeotto.evolui_para = ["seu pai"]
        qualquer_erro(xxx1, self)
        qualquer_erro(xxx2, self)
        qualquer_erro(xxx3, self)
        qualquer_erro(xxx4, self)
        self.assertEqual(pidgeotto.nome, "pidgeotto")
        self.assertEqual(pidgeotto.cor, "marrom")
        self.assertEqual(pidgeotto.evoluiu_de, "pidgey")
        self.assertEqual(pidgeotto.evolui_para, ["pidgeot"])

    @teste("Não mexeu onde não deveria", 0, "offline", penalidade = 20)
    def test_A_00d_pokemon_ok(self):
        pq = Pokemon("Homer Simpson", "Bart", pikachu, 50000, Genero.MASCULINO)
        self.assertEqual(pq.nome_treinador, "Homer Simpson")
        self.assertEqual(pq.apelido, "Bart")
        self.assertEqual(pq.tipo, pikachu)
        self.assertEqual(pq.experiencia, 50000)
        self.assertEqual(pq.genero, Genero.MASCULINO)

    @teste("Não mexeu onde não deveria", 0, "offline", penalidade = 20)
    def test_A_00e_pokemon_imutavel(self):
        pq = Pokemon("Homer Simpson", "Bart", pikachu, 50000, Genero.MASCULINO)
        def xxx1(): pq.nome_treinador = "Margie Simpson"
        def xxx2(): pq.apelido = "Lisa"
        def xxx3(): pq.tipo = raikou
        def xxx4(): pq.experiencia = 6666
        def xxx5(): pq.genero = Genero.FEMININO
        qualquer_erro(xxx1, self)
        qualquer_erro(xxx2, self)
        qualquer_erro(xxx3, self)
        qualquer_erro(xxx4, self)
        qualquer_erro(xxx5, self)
        self.assertEqual(pq.nome_treinador, "Homer Simpson")
        self.assertEqual(pq.apelido, "Bart")
        self.assertEqual(pq.tipo, pikachu)
        self.assertEqual(pq.experiencia, 50000)
        self.assertEqual(pq.genero, Genero.MASCULINO)

    @teste("Não mexeu onde não deveria", 0, "offline", penalidade = 20)
    def test_A_00f_cached_ok(self):
        contador = 0
        @cached
        def foo(x):
            nonlocal contador
            contador += 1
            return x
        self.assertEqual(0, contador)
        self.assertEqual("a", foo("a"))
        self.assertEqual(1, contador)
        self.assertEqual("a", foo("a"))
        self.assertEqual(1, contador)
        self.assertEqual("a", foo("a"))
        self.assertEqual(1, contador)
        self.assertEqual("b", foo("b"))
        self.assertEqual(2, contador)
        self.assertEqual("b", foo("b"))
        self.assertEqual(2, contador)
        self.assertEqual("c", foo("c"))
        self.assertEqual(3, contador)

    @teste("Não mexeu onde não deveria", 0, "offline", penalidade = 20)
    def test_A_00g_excecoes_ok(self):
        self.assertTrue(isinstance(PokemonNaoExisteException(), Exception))
    
    @teste("Configuração do projeto", 1, "offline")
    def test_A_00h_configuracao_ok(self):
        ler_configuracao()

    @teste("Tratamento de erros", 1, "offline")
    def test_A_01y_nao_existe(self):
        pokemon_nao_existe(lambda : nome_do_pokemon(   0), self)
        pokemon_nao_existe(lambda : nome_do_pokemon(  -1), self)
        pokemon_nao_existe(lambda : nome_do_pokemon(  -2), self)
        pokemon_nao_existe(lambda : nome_do_pokemon(-666), self)
        pokemon_nao_existe(lambda : nome_do_pokemon(5000), self)

    @teste("Tratamento de erros", 1, "offline")
    def test_A_01z_nao_existe_pegadinha(self):
        pokemon_nao_existe(lambda : nome_do_pokemon(10001), self)

    @teste("Tratamento de erros", 1, "offline")
    def test_A_08z_negativo(self):
        valor_errado(lambda : nivel_do_pokemon("pikachu",   -1), self)
        valor_errado(lambda : nivel_do_pokemon("pikachu",   -2), self)
        valor_errado(lambda : nivel_do_pokemon("pikachu", -666), self)

    @teste("Configuração do projeto", 1, "pokeapi")
    def test_B_00g_pokeapi_ok(self):
        pass

    @teste("Caminho feliz da pokeapi", 10, "pokeapi")
    def test_B_01b_ok(self):
        self.assertEqual(nome_do_pokemon(  1), "bulbasaur")
        self.assertEqual(nome_do_pokemon( 55), "golduck")
        self.assertEqual(nome_do_pokemon( 25), "pikachu")
        self.assertEqual(nome_do_pokemon(700), "sylveon")
        self.assertEqual(nome_do_pokemon(807), "zeraora")
        nome_do_pokemon(ultimo_pokemon)

    @teste("Tratamento de erros", 1, "pokeapi")
    def _test_B_01c_numero_grande_demais(self):
        pokemon_nao_existe(lambda : nome_do_pokemon(ultimo_pokemon + 1), self)
        pokemon_nao_existe(lambda : nome_do_pokemon(4999), self)

    @teste("Caminho feliz da pokeapi", 10, "pokeapi")
    def test_B_02a_ok(self):
        self.assertEqual(numero_do_pokemon("marill"), 183)
        self.assertEqual(numero_do_pokemon("eevee"), 133)
        self.assertEqual(numero_do_pokemon("psyduck"), 54)
        self.assertEqual(numero_do_pokemon("skitty"), 300)
        self.assertEqual(numero_do_pokemon("zeraora"), 807)

    @teste("Coisas que não existem", 1, "pokeapi")
    def test_B_02b_nao_existe(self):
        pokemon_nao_existe(lambda : numero_do_pokemon("dollynho"), self)
        pokemon_nao_existe(lambda : numero_do_pokemon("dobby"), self)
        pokemon_nao_existe(lambda : numero_do_pokemon("peppa-pig"), self)
        pokemon_nao_existe(lambda : numero_do_pokemon("batman"), self)
        pokemon_nao_existe(lambda : numero_do_pokemon("spiderman"), self)

    @teste("Coisas que não existem", 1, "pokeapi")
    def test_B_02c_vazio(self):
        pokemon_nao_existe(lambda : numero_do_pokemon(""), self)

    @teste("Caminho feliz da pokeapi", 10, "pokeapi")
    def test_B_03a_ok(self):
        self.assertEqual(color_of_pokemon("marill"), "blue")
        self.assertEqual(color_of_pokemon("togekiss"), "white")
        self.assertEqual(color_of_pokemon("magneton"), "gray")
        self.assertEqual(color_of_pokemon("eevee"), "brown")
        self.assertEqual(color_of_pokemon("psyduck"), "yellow")
        self.assertEqual(color_of_pokemon("skitty"), "pink")
        self.assertEqual(color_of_pokemon("gastly"), "purple")
        self.assertEqual(color_of_pokemon("ledyba"), "red")
        self.assertEqual(color_of_pokemon("torterra"), "green")
        self.assertEqual(color_of_pokemon("xurkitree"), "black")

    @teste("Coisas que não existem", 1, "pokeapi")
    def test_B_03b_nao_existe(self):
        pokemon_nao_existe(lambda : color_of_pokemon("dollynho"), self)
        pokemon_nao_existe(lambda : color_of_pokemon("dobby"), self)
        pokemon_nao_existe(lambda : color_of_pokemon("peppa-pig"), self)
        pokemon_nao_existe(lambda : color_of_pokemon("batman"), self)
        pokemon_nao_existe(lambda : color_of_pokemon("spiderman"), self)

    @teste("Coisas que não existem", 1, "pokeapi")
    def test_B_03c_vazio(self):
        pokemon_nao_existe(lambda : color_of_pokemon(""), self)

    @teste("Caminho feliz da pokeapi", 5, "pokeapi")
    def test_B_04a_ok(self):
        self.assertEqual(cor_do_pokemon("marill"), "azul")
        self.assertEqual(cor_do_pokemon("togekiss"), "branco")
        self.assertEqual(cor_do_pokemon("magneton"), "cinza")
        self.assertEqual(cor_do_pokemon("eevee"), "marrom")
        self.assertEqual(cor_do_pokemon("psyduck"), "amarelo")
        self.assertEqual(cor_do_pokemon("skitty"), "rosa")
        self.assertEqual(cor_do_pokemon("gastly"), "roxo")
        self.assertEqual(cor_do_pokemon("ledyba"), "vermelho")
        self.assertEqual(cor_do_pokemon("torterra"), "verde")
        self.assertEqual(cor_do_pokemon("xurkitree"), "preto")

    @teste("Coisas que não existem", 1, "pokeapi")
    def test_B_04b_nao_existe(self):
        pokemon_nao_existe(lambda : cor_do_pokemon("dollynho"), self)
        pokemon_nao_existe(lambda : cor_do_pokemon("dobby"), self)
        pokemon_nao_existe(lambda : cor_do_pokemon("peppa-pig"), self)
        pokemon_nao_existe(lambda : cor_do_pokemon("batman"), self)
        pokemon_nao_existe(lambda : cor_do_pokemon("spiderman"), self)

    @teste("Coisas que não existem", 1, "pokeapi")
    def test_B_04c_vazio(self):
        pokemon_nao_existe(lambda : cor_do_pokemon(""), self)

    @teste("Caminho feliz da pokeapi", 10, "pokeapi")
    def test_B_05a_ok(self):
        assert_equals_unordered_list(["grama"], tipos_do_pokemon("chikorita"), self)
        assert_equals_unordered_list(["terra"], tipos_do_pokemon("hippowdon"), self)
        assert_equals_unordered_list(["normal", "fada"], tipos_do_pokemon("jigglypuff"), self)
        assert_equals_unordered_list(["fogo"], tipos_do_pokemon("darumaka"), self)
        assert_equals_unordered_list(["pedra", "voador"], tipos_do_pokemon("archeops"), self)
        assert_equals_unordered_list(["água"], tipos_do_pokemon("feebas"), self)
        assert_equals_unordered_list(["voador", "noturno"], tipos_do_pokemon("murkrow"), self)
        assert_equals_unordered_list(["água", "elétrico"], tipos_do_pokemon("chinchou"), self)
        assert_equals_unordered_list(["lutador", "fantasma"], tipos_do_pokemon("marshadow"), self)
        assert_equals_unordered_list(["aço"], tipos_do_pokemon("klink"), self)
        assert_equals_unordered_list(["lutador", "inseto"], tipos_do_pokemon("heracross"), self)
        assert_equals_unordered_list(["veneno", "noturno"], tipos_do_pokemon("drapion"), self)
        assert_equals_unordered_list(["psíquico", "gelo"], tipos_do_pokemon("jynx"), self)
        assert_equals_unordered_list(["dragão"], tipos_do_pokemon("dratini"), self)

    @teste("Coisas que não existem", 1, "pokeapi")
    def test_B_05b_nao_existe(self):
        pokemon_nao_existe(lambda : tipos_do_pokemon("dollynho"), self)
        pokemon_nao_existe(lambda : tipos_do_pokemon("dobby"), self)
        pokemon_nao_existe(lambda : tipos_do_pokemon("peppa-pig"), self)
        pokemon_nao_existe(lambda : tipos_do_pokemon("batman"), self)
        pokemon_nao_existe(lambda : tipos_do_pokemon("spiderman"), self)

    @teste("Coisas que não existem", 1, "pokeapi")
    def test_B_05c_vazio(self):
        pokemon_nao_existe(lambda : tipos_do_pokemon(""), self)

    @teste("Caminho feliz da pokeapi", 7, "pokeapi")
    def test_B_06a_ok(self):
        self.assertEqual(evolucao_anterior("togetic"), "togepi")
        self.assertEqual(evolucao_anterior("togekiss"), "togetic")
        self.assertEqual(evolucao_anterior("eelektrik"), "tynamo")
        self.assertEqual(evolucao_anterior("eelektross"), "eelektrik")
        self.assertEqual(evolucao_anterior("pikachu"), "pichu")
        self.assertEqual(evolucao_anterior("raichu"), "pikachu")

    @teste("Casos especiais da pokeapi", 3, "pokeapi")
    def test_B_06b_nao_tem(self):
        self.assertIs(evolucao_anterior("togepi"), None)
        self.assertIs(evolucao_anterior("tynamo"), None)
        self.assertIs(evolucao_anterior("pichu"), None)

    @teste("Coisas que não existem", 1, "pokeapi")
    def test_B_06c_nao_existe(self):
        pokemon_nao_existe(lambda : evolucao_anterior("dollynho"), self)
        pokemon_nao_existe(lambda : evolucao_anterior("dobby"), self)
        pokemon_nao_existe(lambda : evolucao_anterior("peppa-pig"), self)
        pokemon_nao_existe(lambda : evolucao_anterior("batman"), self)
        pokemon_nao_existe(lambda : evolucao_anterior("spiderman"), self)

    @teste("Coisas que não existem", 1, "pokeapi")
    def test_B_06d_vazio(self):
        pokemon_nao_existe(lambda : evolucao_anterior(""), self)

    @teste("Caminho feliz da pokeapi", 10, "pokeapi")
    def test_B_07a_simples(self):
        self.assertEqual(nivel_do_pokemon("blastoise",   110000), 49) # 4
        self.assertEqual(nivel_do_pokemon("mewtwo",     1000000), 92) # 1
        self.assertEqual(nivel_do_pokemon("magikarp",       900),  8) # 1
        self.assertEqual(nivel_do_pokemon("magikarp",   1000000), 92) # 1
        self.assertEqual(nivel_do_pokemon("slowbro",      65000), 40) # 2
        self.assertEqual(nivel_do_pokemon("octillery",   280000), 65) # 2
        self.assertEqual(nivel_do_pokemon("fraxure",     280000), 60) # 1
        self.assertEqual(nivel_do_pokemon("lunatone",     20000), 29) # 3
        self.assertEqual(nivel_do_pokemon("skitty",       50000), 39) # 3
        self.assertEqual(nivel_do_pokemon("torchic",      40000), 35) # 4
        self.assertEqual(nivel_do_pokemon("oddish",        5000), 19) # 4

    @teste("Casos especiais da pokeapi", 5, "pokeapi")
    def test_B_07b_complexos(self):
        self.assertEqual(nivel_do_pokemon("zangoose",      9000), 17) # 5
        self.assertEqual(nivel_do_pokemon("milotic",      65000), 37) # 5
        self.assertEqual(nivel_do_pokemon("lumineon",    160000), 55) # 5
        self.assertEqual(nivel_do_pokemon("ninjask",     300000), 72) # 5
        self.assertEqual(nivel_do_pokemon("zangoose",    580000), 97) # 5
        self.assertEqual(nivel_do_pokemon("makuhita",       600), 10) # 6
        self.assertEqual(nivel_do_pokemon("gulpin",        7000), 21) # 6
        self.assertEqual(nivel_do_pokemon("seviper",     150000), 50) # 6
        self.assertEqual(nivel_do_pokemon("drifblim",   1000000), 87) # 6

    @teste("Casos especiais da pokeapi", 1, "pokeapi")
    def test_B_07c_limites(self):
        self.assertEqual(nivel_do_pokemon("pinsir",           0),   1) # 1
        self.assertEqual(nivel_do_pokemon("bibarel",          0),   1) # 2
        self.assertEqual(nivel_do_pokemon("aipom",            0),   1) # 3
        self.assertEqual(nivel_do_pokemon("makuhita",         0),   1) # 6
        self.assertEqual(nivel_do_pokemon("magikarp",      1249),   9) # 1
        self.assertEqual(nivel_do_pokemon("metapod",        999),   9) # 2
        self.assertEqual(nivel_do_pokemon("magikarp",      1250),  10) # 1
        self.assertEqual(nivel_do_pokemon("butterfree",    1000),  10) # 2
        self.assertEqual(nivel_do_pokemon("charmeleon",   29948),  32) # 4
        self.assertEqual(nivel_do_pokemon("charmeleon",   29949),  33) # 4
        self.assertEqual(nivel_do_pokemon("hariyama",     71676),  40) # 6
        self.assertEqual(nivel_do_pokemon("hariyama",     71677),  41) # 6
        self.assertEqual(nivel_do_pokemon("togepi",      799999),  99) # 3
        self.assertEqual(nivel_do_pokemon("gengar",     1059859),  99) # 4
        self.assertEqual(nivel_do_pokemon("zangoose",    599999),  99) # 5
        self.assertEqual(nivel_do_pokemon("swalot",     1639999),  99) # 6
        self.assertEqual(nivel_do_pokemon("sylveon",    1000000), 100) # 2
        self.assertEqual(nivel_do_pokemon("jigglypuff", 1000000), 100) # 3
        self.assertEqual(nivel_do_pokemon("ledian",      800000), 100) # 3
        self.assertEqual(nivel_do_pokemon("vaporeon", 999999999), 100) # 2
        self.assertEqual(nivel_do_pokemon("vileplume",  1059860), 100) # 4
        self.assertEqual(nivel_do_pokemon("zangoose",    600000), 100) # 5
        self.assertEqual(nivel_do_pokemon("swalot",     1640000), 100) # 6

    @teste("Coisas que não existem", 1, "pokeapi")
    def test_B_07d_nao_existe(self):
        pokemon_nao_existe(lambda : nivel_do_pokemon("dollynho", 1234), self)
        pokemon_nao_existe(lambda : nivel_do_pokemon("dobby", 1234), self)
        pokemon_nao_existe(lambda : nivel_do_pokemon("peppa-pig", 1234), self)
        pokemon_nao_existe(lambda : nivel_do_pokemon("batman", 1234), self)
        pokemon_nao_existe(lambda : nivel_do_pokemon("spiderman", 1234), self)

    @teste("Coisas que não existem", 1, "pokeapi")
    def test_B_07e_vazio(self):
        pokemon_nao_existe(lambda : nivel_do_pokemon("", 1234), self)

 
def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestPokemon)
    unittest.TextTestRunner(verbosity = 2, failfast = parar_no_primeiro_erro).run(suite)
    #pontos_main.mostrar_pontos()

if __name__ == '__main__':
    try:
        runTests()
    finally:
        SobeServidores.apocalipse()