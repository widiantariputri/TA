import numpy as np


class SubKriteria(object):
    def __init__(self, subkriteria):
        self.name = subkriteria
        self.value = list()

    def fill(self, lawan):
        '''
        steps:
            Buat iterasi(element) dari masing2 subkriteria_list dari M
            Baca element
            Gunakan method fill pada element
            Ambil kriteria_list dari lawan
            Iterasi item dari lawan kriteria_list lawan
            Jika element sama -> list akan menjadi 0
                Jika tidak -> tanya input
            Reshape sepanjang len(M)
            Return numpy array
        '''
        arr_value = list()
        for law in lawan:
            for item in lawan:
                if item.name != law.name:
                    value = int(input(
                        f'Masukkan nilai {law.name} terhadap {item.name} :'))
                    arr_value.append(value)
                else:
                    arr_value.append(1)
        arr_value = np.array(arr_value).reshape(len(lawan), len(lawan))
        self.value = arr_value

        print(f'Sub Atribut {self.name}\nNilai: {self.value}')


class Kriteria(object):
    def __init__(self, subkriteria_list):
        '''
        self.subrkteria_list = list dari subkriteria
        self.kriteria_all = mengisi nilai sub kriteria pada kriteria

        '''
        self.subkriteria_list = subkriteria_list

        self.kriteria_all = self.get_sub_criteria(self.subkriteria_list)

    def get_sub_criteria(self, sub):
        '''
        buat list yang berisi object sub kriteria
        contoh: [obj1, obj2, obj3]
        dimana masing2 objek memiliki atribut berupa array
        misal: obj1.value
        '''
        all_kriteria = list()
        for s in sub:
            all_kriteria.append(SubKriteria(s))
        return all_kriteria

    def set_value(self, target):
        '''
        Mengisi nilai pada kriteria

        '''
        for i in range(0, len(self.kriteria_all)):
            self.kriteria_all[i].value = target[i]

    def fill(self, obj):
        '''
            Menanyakan kepada user
            Perulangan dari set kriteria ()
            - Tanya user sub kriteria mana yang ingin diisi
            - tampilkan opsi pengisian(pasti untuk C)
            terhadap sub kriteria C
            track index(misal 0), terhadap index(misal: 1)
            maka identitas[0, 1] == nilai input dan identitas[1, 0] == 1/nilai input
        '''
        for item in self.kriteria_all:
            n = len(obj.subkriteria_list)
            identitas = np.identity(n)
            n = int((pow(n, 2)-n)/2)
            for i in range(0, n):
                # mengisi matriks
                print(f'Opsi: {obj.subkriteria_list}')
                from_ = str(input('Dari : ')).upper()
                to_ = str(input('Terhadap : ')).upper()
                value = int(input('Nilai : '))
                i = obj.subkriteria_list.index(from_)
                j = obj.subkriteria_list.index(to_)

                if i != j:
                    identitas[i][j] = value
                    identitas[j][i] = 1/value

                print(f'Matriks identitas:\n{identitas}')


class Alternative(object):
    def __init__(self):
        self.identitas = np.identity(2)
        self.kode = list()
