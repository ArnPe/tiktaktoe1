import tkinter as tk
import random


class TiktaktoLangas:
    def __init__(self, pagrindinis):
        self.pagrindinis = pagrindinis
        self.pagrindinis.title("Tik-Tak-Toe")

        self.lenta = [[' ' for _ in range(3)] for _ in range(3)]
        self.dabartinis_zaidejas = 'X'
        self.zaidejo_taskai = {'X': 0, 'O': 0}
        self.mygtukai = [[None for _ in range(3)] for _ in range(3)]

        self.sukurti_mygtukus()
        self.atnaujinti_taskus()

    def sukurti_mygtukus(self):
        for eilute in range(3):
            for stulpelis in range(3):
                mygtukas = tk.Button(self.pagrindinis, text=' ', font=('normal', 24), width=5, height=2,
                                     command=lambda e=eilute, s=stulpelis: self.mygtuko_paspaudimas(e, s))
                mygtukas.grid(row=eilute, column=stulpelis)
                self.mygtukai[eilute][stulpelis] = mygtukas

    def mygtuko_paspaudimas(self, eilute, stulpelis):
        if self.lenta[eilute][stulpelis] == ' ':
            self.lenta[eilute][stulpelis] = self.dabartinis_zaidejas
            self.mygtukai[eilute][stulpelis].config(text=self.dabartinis_zaidejas)
            if self.patikrinti_laimejima(self.dabartinis_zaidejas):
                self.zaidejo_taskai[self.dabartinis_zaidejas] += 1
                self.atnaujinti_taskus()
                self.isvalyti_lenta()
            elif self.visi_laisvi():
                self.isvalyti_lenta()
            else:
                self.dabartinis_zaidejas = 'X' if self.dabartinis_zaidejas == 'O' else 'O'
                if self.dabartinis_zaidejas == 'O':
                    self.kompiuterio_ejimas()

    def kompiuterio_ejimas(self):
        galimi_ejimai = [(eilute, stulpelis) for eilute in range(3) for stulpelis in range(3) if
                         self.lenta[eilute][stulpelis] == ' ']
        eilute, stulpelis = random.choice(galimi_ejimai)
        self.lenta[eilute][stulpelis] = 'O'
        self.mygtukai[eilute][stulpelis].config(text='O')
        if self.patikrinti_laimejima('O'):
            self.zaidejo_taskai['O'] += 1
            self.atnaujinti_taskus()
            self.isvalyti_lenta()
        elif self.visi_laisvi():
            self.isvalyti_lenta()
        else:
            self.dabartinis_zaidejas = 'X'

    def patikrinti_laimejima(self, zaidejas):
        for eilute in self.lenta:
            if all(langelis == zaidejas for langelis in eilute):
                return True
        for stulpelis in range(3):
            if all(self.lenta[eilute][stulpelis] == zaidejas for eilute in range(3)):
                return True
        if all(self.lenta[i][i] == zaidejas for i in range(3)) or all(
                self.lenta[i][2 - i] == zaidejas for i in range(3)):
            return True
        return False

    def visi_laisvi(self):
        return all(langelis != ' ' for eilute in self.lenta for langelis in eilute)

    def atnaujinti_taskus(self):
        taskai_label = tk.Label(self.pagrindinis,
                                text=f"Taskai: X {self.zaidejo_taskai['X']} - O {self.zaidejo_taskai['O']}",
                                font=('normal', 16))
        taskai_label.grid(row=3, columnspan=3)

    def isvalyti_lenta(self):
        for eilute in range(3):
            for stulpelis in range(3):
                self.lenta[eilute][stulpelis] = ' '
                self.mygtukai[eilute][stulpelis].config(text=' ')
        self.dabartinis_zaidejas = 'X'


if __name__ == "__main__":
    pagrindinis = tk.Tk()
    programa = TiktaktoLangas(pagrindinis)
    pagrindinis.mainloop()
