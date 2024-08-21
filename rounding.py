def rd(number, decimal_places=2, decimal_separator='.', minus_sign='-', separate_thousands=False, thousands_separator=' ', integer_places=0, round_type='5up', verbose=False) -> str:
    """Cerny rounding"""
    #round_type=['None', '5up', 'Floor', 'Ceiling']
    #check input
    if type(decimal_places) != int:
        raise ValueError("Decimal places must be an integer")
    decimal_places = int(decimal_places)
    round_up = {'0':'1', '1':'2', '2':'3', '3':'4', '4':'5', '5':'6', '6':'7', '7':'8', '8':'9', '9':'0'}
    ret_string = ''
    raw_string = str(number).strip()
    raw_string = raw_string.replace(thousands_separator, '')
    minus_place = raw_string.find(minus_sign)
    raw_string = raw_string.replace(minus_sign, '')
    decimal_place = raw_string.find(decimal_separator)
    # když začíná .tak mi to nefunguje
    if decimal_place == 0:
        raw_string = '0' + raw_string
        decimal_place = 1
    raw_string = raw_string.replace(decimal_separator, '')
    if verbose: print('decimal_place', decimal_place)
    if verbose: print('raw_string', raw_string)
    if decimal_place == -1:
        decimal_place = len(raw_string)
    if round_type != 'None':
        # potrebuju se dostat na decision_number
        decision_place = decimal_place + decimal_places
        if verbose: print('decision_place', decision_place)
        if (decision_place < 0):
            # zaokrouhluju 999 na -4 a vic des.mist a víc, takže 1000 na -4 je 0000
            if verbose: print('decision_place je < 0, vratim 0')
            ret_string = '0'
            decimal_place = 1
            #decimal_place = abs(decimal_places)
        elif (decision_place >= len(raw_string)):
            # vratim cele a nasledne dodelam '0' na dalsich des mistech
            if verbose: print('decision_place je >= len(raw_string):', len(raw_string), '- vratim cele a dodelam 0')
            ret_string = raw_string
        else:
            #jdu zaokrouhlovat
            if raw_string[decision_place] in ('0', '1', '2', '3', '4') and round_type != 'Ceiling' or round_type == 'Floor':
                #zaokrouhluju dolu
                ret_string += raw_string[:decision_place]
                if verbose: print('zaokrouhluju dolu, decision number je:', raw_string[decision_place], ', vracím:', ret_string)
            else:
                #zaokrouhluju nahoru
                for i in range (decision_place, -1, -1):
                    if i == 0:
                        ret_string = '1'
                        decimal_place += 1
                        if verbose: print('jsem na nultém místě a mám to zaokrouhlit nahoru, vracím 1 a ostatní doplním 0 až do decimal place:', decimal_place)
                        break
                    else:
                        if raw_string[(i-1)] != '9':
                            ret_string = raw_string[:(i-1)] + round_up[raw_string[(i-1)]]
                            if verbose: print('hotovo, decision number je:', raw_string[i], 'na místě:', i, 'a předchozí není 9, vracím:', ret_string)
                            break
                        if verbose: print('zaokrouhluju nahoru, decision number je:', raw_string[i], 'na místě:', i)

        # pokud jsem zaokrouhloval na - des mista, meno bylo typ 799.9, tak musim doplnit chybejici 0
        # ta je bud do des. mista, nebo do abs(decimal_places), pokud jdem zadal abs(-decimal_places) > decimal_place
        if len(ret_string) < decimal_place:
            ret_string += '0'*(decimal_place - len(ret_string))
    else:
        ret_string = raw_string
    # doplnim des. čárku a chybějící des. místa
    if len(ret_string) > decimal_place - decimal_places:
        ret_string=ret_string[:decimal_place] + decimal_separator + ret_string[decimal_place:]
        if len(ret_string) - decimal_place <= decimal_places:
            ret_string += '0'*(decimal_places - (len(ret_string) - decimal_place) + 1)
    if decimal_place < integer_places:
        ret_string = '0'*(integer_places - decimal_place) + ret_string
        decimal_place = integer_places
    # nechci přidat mínus k nule!
    try:
        x = float(ret_string)
        if x == 0 and minus_place > -1:
            minus_place = -1
    except Exception as e:
        pass
    if separate_thousands:
        for i, j in enumerate(range(decimal_place -1, -1, -1)):
            #print(ret_string[j])
            if i % 3 == 2 and j > 0:
                ret_string=ret_string[:j] + thousands_separator + ret_string[j:]
    if minus_place > -1:
        ret_string = minus_sign + ret_string
    return ret_string

def main():
    x = ' '
    while x != '':
        x=input("Zadejte číslo:")
        y=input("Des. místa:")
        try:
            y = int(y)
        except Exception as e:
            print (e)
            print ('Using rounding to 0 decimal places')
            y = 0
        #print(f'{x} rounded to {y} decimal places: {rd(x, y)}')
        print(f'{x} rounded to {y} decimal places:', rd(x, y, **{'separate_thousands':True}))
        #print(f'{x} rounded to {y} decimal places:', rd(None, None, **{'separate_thousands':True}))

if __name__ == '__main__':
    main()
