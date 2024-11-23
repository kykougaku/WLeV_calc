import os
import time

def wavelength_to_energy():
    print('波長[nm]を入力してください。')
    try:
        wavelength = float(input())
    except:
        print('数値を入力してください。')
    else:
        energy = 1240 / wavelength
        print(f'エネルギーは{energy}eVです。')

def energy_to_wavelength():
    print('エネルギー[eV]を入力してください。')
    try:
        energy = float(input())
    except:
        print('数値を入力してください。')
    else:
        wavelength = 1240 / energy
        print(f'波長は{wavelength}nmです。')

if __name__ =='__main__':
    while True:
        print('1：波長[nm]　→　エネルギー\n2：エネルギー[eV]　→　波長\n')
        try:
            mode = str(input())
        except:
            print('1または2を入力してください。\n')
        else:
            if mode == '1':
                wavelength_to_energy()
            elif mode == '2':
                energy_to_wavelength()
            else:
                print('1または2を入力してください。\n')
        print('最初に戻ります。\n')
        time.sleep(1)