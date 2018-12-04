def read_personen_check(filename):
    fobj = open(filename, 'r')
    dateidict = {}
    try:
        for line in fobj:
            daten = line.split(';')
            dateidict[daten[0]] = [int(float(daten[3])), int(daten[4].strip('\n'))]

    except IOError:
        return 'Filename existiert nicht!'
    except IndexError:
        return 'verwende bitte \';\' als Seperator'
    except ValueError:
        return 'Int Konversion nicht moeglich'
    else:
        return dateidict

    fobj.close()


if __name__ == '__main__':
    print(read_personen_check('text.txt'))