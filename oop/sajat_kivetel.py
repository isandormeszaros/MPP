class NincsPisztaciaException(Exception):
    def __init__(self, uzenet):
        self.uzenet = uzenet

try:
    fagyi_izek = ["csoki", "vanillia", "szamóca", "málna"]
    if "pisztácia" not in fagyi_izek:
        raise NincsPisztaciaException("Elfogyott a pisztácia")
except NincsPisztaciaException as e:
    print(e)

