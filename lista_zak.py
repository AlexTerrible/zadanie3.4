groc_dict = {
    'Piekarnia' : ['Chleb', 'Pączek', 'Bułki'],
    'Warzywniak' : ['Marchew', 'Seler', 'Rukola']
}
print(groc_dict['Piekarnia'])
for i in range (len(groc_dict['Piekarnia'])):
    groc_dict['Piekarnia'][i] = groc_dict['Piekarnia'][i].upper()
for i in range (len(groc_dict['Warzywniak'])):
    groc_dict['Warzywniak'][i] = groc_dict['Warzywniak'][i].upper()
for key, value in groc_dict.items():
    print('Idę do %s, kupuję tu następujące rzeczy: %s' % (key.upper(), value))