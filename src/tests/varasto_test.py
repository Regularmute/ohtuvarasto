import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_konstruktori_nollaa_negatiivisen_tilavuuden(self):
        virheellinen_varasto = Varasto(-1)

        self.assertAlmostEqual(virheellinen_varasto.tilavuus, 0)

    def test_konstruktori_nollaa_negatiivisen_alku_saldon(self):
        virheellinen_varasto = Varasto(10, -2)

        self.assertAlmostEqual(virheellinen_varasto.saldo, 0)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-10)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_tilavuuden_yli_lisääminen_täyttää_varaston(self):
        self.varasto.lisaa_varastoon(15)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivinen_ottaminen_palauttaa_nolla(self):
        saatu_maara = self.varasto.ota_varastosta(-5)

        self.assertAlmostEqual(saatu_maara, 0)

    def test_saldon_yli_ottaminen_palauttaa_jaljella_olevan_saldon(self):
        self.varasto.lisaa_varastoon(7)

        saatu_maara = self.varasto.ota_varastosta(9)

        self.assertAlmostEqual(saatu_maara, 7)

    def test_str_palauttaa_varaston_saldon_ja_vapaan_tilan_oikein(self):
        printti = self.varasto.__str__()

        self.assertEqual(printti, "saldo = 0, vielä tilaa 10")
