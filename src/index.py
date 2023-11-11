from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print(
        "Luonnin jälkeen:",
        f"\nMehuvarasto: {mehua}",
        f"\nOlutvarasto: {olutta}",
        "\nOlut getterit:"
        f"\nsaldo = {olutta.saldo}",
        f"\ntilavuus = {olutta.tilavuus}",
        f"\npaljonko_mahtuu = {olutta.paljonko_mahtuu()}",
        "\nMehu setterit:",
        "\nLisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(
        f"Mehuvarasto: {mehua}",
        "\nOtetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(
        f"Mehuvarasto: {mehua}",
        "\nVirhetilanteita:",
        "\nVarasto(-100.0);")
    huono = Varasto(-100.0)
    print(
        huono,
        "\nVarasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(
        huono,
        f"\nOlutvarasto: {olutta}",
        "\nolutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(
        f"Olutvarasto: {olutta}",
        f"\nMehuvarasto: {mehua}",
        "\nmehua.lisaa_varastoon(-666.0)")


if __name__ == "__main__":
    main()
