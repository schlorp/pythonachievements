Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> print('Mijn naam is Thom)
      
SyntaxError: EOL while scanning string literal
>>> print('Mijn naam is Thom')
Mijn naam is Thom
>>> naam = 'Thom'
>>> print(naam)
Thom
>>> print(naam.upper())
THOM
>>> print(naam[0:2])
Th
>>> print(naam[::-1])
mohT
>>> leeftijd = 15
>>> print('hallo ' + naam ' ben je al ' + str(leeftijd) + ' jaar?"
      
SyntaxError: invalid syntax
>>> print('hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?"
      
SyntaxError: EOL while scanning string literal
>>> print('hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?")
      
SyntaxError: EOL while scanning string literal
>>> print('hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
hallo Thom ben je al 15 jaar?
>>> leeftijd = leeftijd +1
>>> leeftijd
16
>>> leeftijd-=1
>>> leeftijd
15
>>> if leeftijd < 18:
    hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')

    
Over 3 jaar wordt je 18
>>> from random import randint
randint(0,1000)
willekeurig_getal = randint(0,1000)
willekeurig_getal
print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
SyntaxError: multiple statements found while compiling a single statement
>>> from random import randint
>>> randint(0,1000)
51
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
265
>>> print('Willekeurig getal tussen 0 en 1000: ' str(willekeurig_getal))
SyntaxError: invalid syntax
>>> print('Willekeurig getal tussen 0 en 1000: ' + (willekeurig_getal))
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print('Willekeurig getal tussen 0 en 1000: ' + (willekeurig_getal))
TypeError: can only concatenate str (not "int") to str
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 265
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-23 14:36:08.135922
>>> datum.strftime('%A %d %B %y')
'Wednesday 23 September 20'
>>> import locale
>>> locale.setocale(locale.LC_TIME, 'nl_NL')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    locale.setocale(locale.LC_TIME, 'nl_NL')
AttributeError: module 'locale' has no attribute 'setocale'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'woensdag 23 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'mercoledì 23 settembre 2020'
>>> 