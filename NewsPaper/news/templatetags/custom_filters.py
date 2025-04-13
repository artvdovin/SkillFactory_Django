from django import template


register = template.Library()


CURRENCIES_SYMBOLS = {
   'rub': 'Р',
   'usd': '$',
}
bad_words = ['чемпионат','финале','двигатель','программы','функционал']

@register.filter()
def currency(value, code='rub'):
   """
   value: значение, к которому нужно применить фильтр
   code: код валюты
   """
   postfix = CURRENCIES_SYMBOLS[code]

   return f'{value} {postfix}'

@register.filter()
def censor(value):
   words = value.split()  # Используем другое имя для списка слов
   censor_list = []
         
   for word in words:
      if word.lower() in bad_words:
            # Заменяем все символы слова, кроме первого, на символ "*"
         censor_word = word[0] + '*' * (len(word) - 1)

         censor_list.append(censor_word)
      else:
         censor_list.append(word)

   return ' '.join(censor_list)      


