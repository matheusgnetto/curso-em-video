c = float(input('Digite a temperatura em °C: '))
k = c + 273
f = (1.8 * c) + 32
print('A temperatura de {:.1f}°C, corresponde a: \n Kelvin = {:.1f}K \n Fahrenheit = {:.1f}°F'.format(c, k, f))
