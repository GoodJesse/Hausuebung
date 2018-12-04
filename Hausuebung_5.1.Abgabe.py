'''
Hausuebung 5.1

Author: JesseZ

4.12.2018

'''

def read_bmi(filename):
    dateidict = {}
    fobj = open(filename, 'r')
    for line in fobj:
        daten = line.split(';')
        dateidict[daten[0]] = [daten[3], daten[4].strip('\n')]
    return dateidict


def calc_bmi(dateidict):
    for pair in dateidict.items():
        pair[1].append(int(float(pair[1][0]) / (float(pair[1][1]) ** 2 / 10000)))
        dateidict[pair[0]] = pair[1]
    return dateidict


def write_bmi(dateidict):
    fobj = open('Ausgabe.csv', 'w')
    sort = dateidict.items()
    sort.sort()
    for line in sort:
        fobj.write('%s;%s;%s;%s\n' % (line[0], line[1][0], line[1][1], line[1][2]))
    fobj.close()


if __name__ == '__main__':
    dateidict = read_bmi('BMI.csv')
    BMI_dict = calc_bmi(dateidict)
    write_bmi(BMI_dict)
