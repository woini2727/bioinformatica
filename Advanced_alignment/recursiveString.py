
def main():
    string="gattacaa"
    lista = []
    a=cutString(string)
    for n in a:
        if (n!="("):
            print(n)
def cutString(string):

    if len(string)==1:
        return ""
    else:
        #calcular
        return cutString(string[:(len(string) // 2)]),string[:(len(string)//2)],cutString(string[(len(string) // 2):]),string[(len(string)//2):]
        #return [string[:(len(string)//2)]]
        #return [string[(len(string)//2):]]

if __name__ == '__main__':
    main()