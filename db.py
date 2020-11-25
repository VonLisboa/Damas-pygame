import os
import json


class DataBase:
    def __init__(self):
        if not os.path.exists('jogoDamas.json'):
            self.__create()
        else:
            with open('jogoDamas.json') as json_file:
                self.data = json.load(json_file)

    def __create(self):
        self.data = {"resolucao": 0, "corPeca": 0, "corTabuleiro": 0}
        self.__save()

    def load_configurations(self):
        return self.data["corTabuleiro"], self.data["corPeca"], self.data["resolucao"]

    def load_cor_tabuleiro(self):
        return self.data["corTabuleiro"]

    def load_cor_peca(self):
        return self.data["corPeca"]

    def load_resolucao(self):
        return self.data["resolucao"]

    def update_cor(self, val):
        self.data["corTabuleiro"] = val
        self.__save()

    def update_resolucao(self, val):
        self.data["resolucao"] = val
        self.__save()

    def update_cor_peca(self, val):
        self.data["corPeca"] = val
        self.__save()

    def __save(self):
        with open('jogoDamas.json', 'w') as outfile:
            json.dump(self.data, outfile)

