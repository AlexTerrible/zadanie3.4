groc_dict = {
    'Piekarnia' : ['Chleb', 'Pączek', 'Bułki'],
    'Warzywniak' : ['Marchew', 'Seler', 'Rukola']
}
suma = 0
for i in range (len(groc_dict['Piekarnia'])):
    groc_dict['Piekarnia'][i] = groc_dict['Piekarnia'][i].upper()
for i in range (len(groc_dict['Warzywniak'])):
    groc_dict['Warzywniak'][i] = groc_dict['Warzywniak'][i].upper()
for key, value in groc_dict.items():
    for j in value:
        suma = suma + 1
    print('Idę do %s, kupuję tu następujące rzeczy: %s' % (key.upper(), value))
print ('W sumie kupuje %s produktów.' % (suma))
print ('dodanie pierwszego commita')
print ('dodanie drugiego commita')
print ('Specjalne pozdrowienia')
