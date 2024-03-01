def lao_dte(data):
    lao_text_arry = [char for char in data]

    sala1 = ['ແ', 'ເ', 'ໂ']
    sala2 = ['າ', 'ຽ']
    sala3 = ['ິ', 'ີ', 'ຶ', 'ື', 'ຸ', 'ູ', 'ຳ']
    sala4 = ['ະ', 'າ',]
    sala5 = ['ໄ', 'ໃ', 'ໍ']
    sala6 = ['ໍ']
    sala7 = ['ອ','ວ']
    payasana = ['ກ','ຫ','ຂ', 'ຄ', 'ງ', 'ຈ', 'ສ', 'ຊ', 'ຍ', 'ດ', 'ຕ', 'ຖ', 'ທ', 'ນ', 'ບ', 'ປ', 'ຜ', 'ຝ', 'ພ', 'ຟ', 'ມ', 'ຢ', 'ຣ', 'ລ', 'ວ', 'ອ', 'ຮ']
    vannayud = ['່', '້', '໋']
    vannayud1 = ['ົ', 'ັ', 'ິ', 'ີ', 'ຶ', 'ື']
    payasana1 = ['ຫ','ຂ', 'ຄ']
    payasana2 = ['ງ', 'ຍ', 'ມ', 'ນ', 'ລ', 'ວ', 'ຼ']
    payasana3 = ['ໝ', 'ໜ',]
    tuasakod = ['ກ', 'ງ', 'ຍ', 'ດ', 'ນ', 'ບ', 'ມ', 'ວ', 'ອ']
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    eng = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']

    text_len = len(lao_text_arry)

    x = 0
    text = []

    while x < text_len:
        tps = ''
        if lao_text_arry[x] in sala1[1] and lao_text_arry[x+1] in sala1[1]: #sala1 fix ເ ເ ແ
            tps += lao_text_arry[x] + lao_text_arry[x+1]
            x += 2
            if x < text_len and lao_text_arry[x] in payasana:
                tps += lao_text_arry[x]
                x += 1
                if x < text_len and lao_text_arry[x] in vannayud:
                    tps += lao_text_arry[x]
                    x += 1
                    if x < text_len and lao_text_arry[x] in tuasakod:
                        tps += lao_text_arry[x]
                        x += 1
                elif x < text_len and lao_text_arry[x] in sala4:
                        tps += lao_text_arry[x]
                        x += 1  
                elif x < text_len and lao_text_arry[x] in vannayud1:
                    tps += lao_text_arry[x]
                    x += 1
                    if x < text_len and lao_text_arry[x] in vannayud:
                        tps += lao_text_arry[x]
                        x += 1
                        if x < text_len and lao_text_arry[x] in tuasakod:
                            tps += lao_text_arry[x]
                            x += 1
                    if x < text_len and lao_text_arry[x] in tuasakod:
                        tps += lao_text_arry[x]
                        x += 1
                elif x < text_len and lao_text_arry[x] in tuasakod:
                    tps += lao_text_arry[x]
                    x += 1

        elif lao_text_arry[x] in sala1:
            tps += lao_text_arry[x]
            x += 1
            if x < text_len and lao_text_arry[x] in payasana:
                tps += lao_text_arry[x]
                x += 1
                if x < text_len and lao_text_arry[x] in vannayud:
                    tps += lao_text_arry[x]
                    x += 1
                    if x < text_len and lao_text_arry[x] in tuasakod:
                        tps += lao_text_arry[x]
                        x += 1
                elif x < text_len and lao_text_arry[x] in sala4:
                        tps += lao_text_arry[x]
                        x += 1  
                elif x < text_len and lao_text_arry[x] in vannayud1:
                    tps += lao_text_arry[x]
                    x += 1
                    if x < text_len and lao_text_arry[x] in vannayud:
                        tps += lao_text_arry[x]
                        x += 1
                        if x < text_len and lao_text_arry[x] in tuasakod:
                            tps += lao_text_arry[x]
                            x += 1
                            if x + 1 < text_len:
                                if lao_text_arry[x] in tuasakod and not lao_text_arry[x+1] in sala2 + sala3 + sala4 + sala6 + sala7 + vannayud + vannayud1:
                                    tps += lao_text_arry[x]
                                    x += 1
                    if x < text_len and lao_text_arry[x] in tuasakod:
                        tps += lao_text_arry[x]
                        x += 1
                elif x < text_len and lao_text_arry[x] in tuasakod:
                    tps += lao_text_arry[x]
                    x += 1

        elif x < text_len and lao_text_arry[x] in sala5:
            tps += lao_text_arry[x]
            x += 1
            if x < text_len and lao_text_arry[x] in payasana:
                tps += lao_text_arry[x]
                x += 1
                if x < text_len and lao_text_arry[x] in sala4:
                    tps += lao_text_arry[x]
                    x += 1   
                elif x < text_len and lao_text_arry[x] in vannayud:
                        tps += lao_text_arry[x]
                        x += 1
                        if x < text_len and lao_text_arry[x] in sala4:
                            tps += lao_text_arry[x]
                            x += 1

        elif x < text_len and lao_text_arry[x] in payasana1:
            tps += lao_text_arry[x]
            x += 1
            if x < text_len and lao_text_arry[x] in payasana2:
                tps += lao_text_arry[x]
                x += 1
                if x < text_len and lao_text_arry[x] in vannayud:
                    tps += lao_text_arry[x]
                    x += 1
                    if x < text_len and lao_text_arry[x] in sala3 or lao_text_arry[x] in sala2 or lao_text_arry[x] in vannayud1:
                            tps += lao_text_arry[x]
                            x += 1
                            if x < text_len and lao_text_arry[x] in vannayud:
                                tps += lao_text_arry[x]
                                x += 1
                                if x < text_len and lao_text_arry[x] in tuasakod:
                                            tps += lao_text_arry[x]
                                            x += 1
                            elif x < text_len and lao_text_arry[x] in tuasakod:
                                    tps += lao_text_arry[x]
                                    x += 1
                    elif x < text_len and lao_text_arry[x] in sala4:
                        tps += lao_text_arry[x]
                        x += 1

                elif x < text_len and lao_text_arry[x] in sala3 or sala7 or lao_text_arry[x] in vannayud1:
                        tps += lao_text_arry[x]
                        x += 1
                        if x < text_len and lao_text_arry[x] in vannayud:
                            tps += lao_text_arry[x]
                            x += 1
                            if x < text_len and lao_text_arry[x] in tuasakod:
                                        tps += lao_text_arry[x]
                                        x += 1
                        elif x < text_len and lao_text_arry[x] in tuasakod:
                                tps += lao_text_arry[x]
                                x += 1
            
            elif x < text_len and lao_text_arry[x] in vannayud:
                    tps += lao_text_arry[x]
                    x += 1
                    if lao_text_arry[x] in sala2:
                        tps += lao_text_arry[x]
                        x += 1
                        if x < text_len and lao_text_arry[x] in tuasakod:
                                    tps += lao_text_arry[x]
                                    x += 1

            elif x < text_len and lao_text_arry[x] in sala2:
                tps += lao_text_arry[x]
                x += 1
                if x < text_len and lao_text_arry[x] in tuasakod:
                    tps += lao_text_arry[x]
                    x += 1

            elif x < text_len and lao_text_arry[x] in sala4:
                tps += lao_text_arry[x]
                x += 1

            elif x < text_len and lao_text_arry[x] in sala3 or lao_text_arry[x] in vannayud1:
                        tps += lao_text_arry[x]
                        x += 1
                        if x < text_len and lao_text_arry[x] in vannayud:
                            tps += lao_text_arry[x]
                            x += 1
                            if x < text_len and lao_text_arry[x] in tuasakod:
                                        tps += lao_text_arry[x]
                                        x += 1
                        elif x < text_len and lao_text_arry[x] in tuasakod:
                                tps += lao_text_arry[x]
                                x += 1
            
            elif x < text_len and lao_text_arry[x] in sala4:
                    tps += lao_text_arry[x]
                    x += 1

        elif x < text_len and lao_text_arry[x] in payasana3:
            if x < text_len and lao_text_arry[x] in payasana3:
                tps += lao_text_arry[x]
                x += 1
                if x < text_len and lao_text_arry[x] in vannayud:
                    tps += lao_text_arry[x]
                    x += 1
                    if x < text_len and lao_text_arry[x] in sala3 or lao_text_arry[x] in sala2 or lao_text_arry[x] in vannayud1:
                            tps += lao_text_arry[x]
                            x += 1
                            if x < text_len and lao_text_arry[x] in vannayud:
                                tps += lao_text_arry[x]
                                x += 1
                                if x < text_len and lao_text_arry[x] in tuasakod:
                                            tps += lao_text_arry[x]
                                            x += 1
                            elif x < text_len and lao_text_arry[x] in tuasakod:
                                    tps += lao_text_arry[x]
                                    x += 1
                    elif x < text_len and lao_text_arry[x] in sala4:
                        tps += lao_text_arry[x]
                        x += 1

                elif x < text_len and lao_text_arry[x] in sala3 or sala7 or lao_text_arry[x] in vannayud1:
                        tps += lao_text_arry[x]
                        x += 1
                        if x < text_len and lao_text_arry[x] in vannayud:
                            tps += lao_text_arry[x]
                            x += 1
                            if x < text_len and lao_text_arry[x] in tuasakod:
                                        tps += lao_text_arry[x]
                                        x += 1
                        elif x < text_len and lao_text_arry[x] in tuasakod:
                                tps += lao_text_arry[x]
                                x += 1
            
            elif x < text_len and lao_text_arry[x] in vannayud:
                    tps += lao_text_arry[x]
                    x += 1
                    if lao_text_arry[x] in sala2:
                        tps += lao_text_arry[x]
                        x += 1
                        if x < text_len and lao_text_arry[x] in tuasakod:
                                    tps += lao_text_arry[x]
                                    x += 1

            elif x < text_len and lao_text_arry[x] in sala2:
                tps += lao_text_arry[x]
                x += 1
                if x < text_len and lao_text_arry[x] in tuasakod:
                    tps += lao_text_arry[x]
                    x += 1

            elif x < text_len and lao_text_arry[x] in sala4:
                tps += lao_text_arry[x]
                x += 1

            elif x < text_len and lao_text_arry[x] in sala3 or lao_text_arry[x] in vannayud1:
                        tps += lao_text_arry[x]
                        x += 1
                        if x < text_len and lao_text_arry[x] in vannayud:
                            tps += lao_text_arry[x]
                            x += 1
                            if x < text_len and lao_text_arry[x] in tuasakod:
                                        tps += lao_text_arry[x]
                                        x += 1
                        elif x < text_len and lao_text_arry[x] in tuasakod:
                                tps += lao_text_arry[x]
                                x += 1
            
            elif x < text_len and lao_text_arry[x] in sala4:
                    tps += lao_text_arry[x]
                    x += 1
        
        elif lao_text_arry[x] in payasana:
            tps += lao_text_arry[x]
            x += 1
            if x < text_len and lao_text_arry[x] in vannayud:
                    tps += lao_text_arry[x]
                    x += 1
                    if lao_text_arry[x] in sala2:
                        tps += lao_text_arry[x]
                        x += 1
                        if x < text_len and lao_text_arry[x] in tuasakod:
                                    tps += lao_text_arry[x]
                                    x += 1

            elif x < text_len and (lao_text_arry[x] in sala3 or lao_text_arry[x] in sala2 or lao_text_arry[x] in vannayud1):
                tps += lao_text_arry[x]
                x += 1
                if x < text_len and lao_text_arry[x] in vannayud:
                    tps += lao_text_arry[x]
                    x += 1
                    if x < text_len and lao_text_arry[x] in tuasakod:
                            tps += lao_text_arry[x]
                            x += 1
                elif x + 1 < text_len:
                    if lao_text_arry[x] in tuasakod and not lao_text_arry[x+1] in sala2 + sala3 + sala4 + sala6 + sala7 + vannayud + vannayud1:
                        tps += lao_text_arry[x]
                        x += 1
                    elif lao_text_arry[x] in tuasakod and lao_text_arry[x+1] in sala7:
                        if x + 2 < text_len:
                            if x < text_len and lao_text_arry[x] in tuasakod and not lao_text_arry[x+2] in sala2 or sala3 or sala4 or sala6 or vannayud or vannayud1:
                                tps += lao_text_arry[x]
                                x += 1
                elif x < text_len and lao_text_arry[x] in tuasakod:
                    tps += lao_text_arry[x]
                    x += 1

            elif x < text_len and lao_text_arry[x] in sala2:
                tps += lao_text_arry[x]
                x += 1
                if x < text_len and lao_text_arry[x] in tuasakod:
                    tps += lao_text_arry[x]
                    x += 1

            elif x < text_len and lao_text_arry[x] in sala4:
                tps += lao_text_arry[x]
                x += 1

            elif x < text_len and lao_text_arry[x] in sala6:
                tps += lao_text_arry[x]
                x += 1
                if x < text_len and lao_text_arry[x] in vannayud:
                    tps += lao_text_arry[x]
                    x += 1
        
        elif  x < text_len and lao_text_arry[x] in number:
              tps += lao_text_arry[x]
              x += 1
              while x < text_len and lao_text_arry[x] in number:
                tps += lao_text_arry[x]
                x += 1

        elif  x < text_len and lao_text_arry[x] in eng:
              tps += lao_text_arry[x]
              x += 1
              while x < text_len and lao_text_arry[x] in eng:
                tps += lao_text_arry[x]
                x += 1

        else:
            tps += lao_text_arry[x]
            x += 1
        
        text.append(tps)
    
    return text

def lao_dtd(data):
    text = ''
    for t in data:
        text += t

    return text