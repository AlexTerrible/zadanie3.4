groc_dict = {
    'Piekarnia' : ['Chleb', 'Pączek', 'Bułki'],
    'Warzywniak' : ['Marchew', 'Seler', 'Rukola']
}
for key, value in groc_dict.items():
    print('Idę do %s, kupuję tu następujące rzeczy: %s' % (key, value))