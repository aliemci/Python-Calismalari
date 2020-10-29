import numpy as np

def kare_bul(satir, sutun):
    kare_satir, kare_sutun = 0,0

    if satir < 3:
        kare_satir = 0
    elif satir < 6:
        kare_satir = 1
    else:
        kare_satir = 2

    if sutun < 3:
        kare_sutun = 0
    elif sutun < 6:
        kare_sutun = 1
    else:
        kare_sutun = 2

    return [kare_satir, kare_sutun]

def satir_kontrol(deger, satirListesi):
    for satirDegeri in satirListesi:
        if satirDegeri == deger:
            return False
    return True

def sutun_kontrol(deger, sutunListesi):
    for sutunDegeri in sutunListesi:
        if sutunDegeri == deger:
            return False
    return True

def kare_kontrol(deger, satirNo, sutunNo):
    kare_satir, kare_sutun = kare_bul(satirNo, sutunNo)
    sudoku_karesi = sudoku[kare_satir*3:kare_satir*3+3, kare_sutun*3:kare_sutun*3+3]
    for i in sudoku_karesi[:]:
        for j in i:
            if j == deger:
                return False
    return True

def deger_kontrol(deger, satir, sutun, x, y):
    if satir_kontrol(deger, satir):
        if sutun_kontrol(deger, sutun):
            if kare_kontrol(deger, x, y):
                return True
    return False

def sudoku_coz():
    i,j = 0,0
    while i < 9:
        sudokuSatir = sudoku[i,:]
        while j < 9:
            sudokuSutun = sudoku[:,j]
            if sudoku[i,j] == 0:
                for deger in range(1, 10):
                    if deger_kontrol(deger, sudokuSatir, sudokuSutun, i, j):
                        sudoku[i,j] = deger
                        if not sudoku_coz():
                            sudoku[i,j] = 0
                        else:
                            break
                if sudoku[i,j] == 0:
                    return False
                else:
                    return True
            j+=1
        i+=1
        j=0

    return True


if __name__ == "__main__":

    sudoku = [
    [7, 0, 0, 6, 8, 0, 0, 0, 0],
    [6, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 8, 0],
    [0, 1, 0, 8, 6, 0, 0, 7, 0],
    [0, 0, 0, 0, 3, 0, 8, 9, 0],
    [0, 5, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 4, 0, 0, 6, 0, 0, 9],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [0, 0, 3, 0, 0, 2, 5, 0, 0]
    ]

    sudoku = np.array(sudoku)

    if sudoku_coz():
        print(sudoku)
