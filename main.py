from num_sys_convert import NumSysConvert

def main():
    convert = NumSysConvert(float(input("podaj liczbe\n")), int(input("podaj ilosc\n")))
    print(convert.binary())
    print(convert.ternary())

if __name__ == '__main__':
    main()