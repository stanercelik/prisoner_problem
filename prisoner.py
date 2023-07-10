import random

class Prisoner:
    def __init__(self, numara):
        self.numara = numara
        self.kutu_say = 0
        self.kutu_no = 0


def prison():
    succ = 0
    for i in range(1, 10001):
        kutu_listesi = random.sample(range(1, 101), 100)
        #print(kutu_listesi)
        kurtulanlar = []

        prisoners = [Prisoner(i) for i in range(1, 101)]

        for prisoner in prisoners:
            kutudaki_numara = kutu_listesi[prisoner.numara-1]
            kutu_sayisi = 1
            #print(kutu_listesi.index(prisoner.numara))

            while prisoner.numara != kutudaki_numara and kutu_sayisi <= 50:

                kutudaki_numara = kutu_listesi[kutudaki_numara-1]
                kutu_sayisi += 1
                if kutudaki_numara == prisoner.numara:
                    prisoner.kutu_say = kutu_sayisi
                    prisoner.kutu_no = kutudaki_numara
                    kurtulanlar.append(prisoner.numara)
                



        if len(kurtulanlar) > 60:
            #print("BAŞARILI! Herkes kurtuldu!")
            succ += 1

    print(f"oran = {succ / 100}")

prison()
