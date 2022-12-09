import time
import logging

from aiogram import Bot,Dispatcher,executor, types

Token = "5982317757:AAGP8AHd9nAhWrD9pDunsf83b6XvMRWWVEE"

bot = Bot(token = Token)
disp = Dispatcher(bot = bot)

def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую тысячу символов
        wiki_text=ny.content[:1000]
        # Разделяем по точкам
        wiki_mas=wiki_text.split('.')
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wiki_txt2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not('==' in x):
                    # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if(len((x.strip()))>3):
                   wiki_text2=wiki_txt2+x+'.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wiki_txt2=re.sub('\([^()]*\)', '', wiki_txt2)
        wiki_text2=re.sub('\([^()]*\)', '', wiki_txt2)
        wiki_text2=re.sub('\{[^\{\}]*\}', '', wiki_txt2)
        # Возвращаем текстовую строку
        return wiki_txt2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'В энциклопедии нет информации об этом'

@dp.message_handler()
async def echo(message: types.Message):

    await  message.reply(u_id, getwiki(message.text))

@disp.message_handler(commands=['/start']) 
async def start_handler(message: types.Message):
    u_id = message.from_user.id     #user_id
    user_full_name = message.from_user.full_name
    logging.info(f'{u_id = } {user_full_name = } {time.asctime()}')        #write to logging
    
    await  message.reply(f"Привет, {user_full_name}. Отправьте мне любое слово, и я найду его значение на Wikipedia")
    
if __name__ == "__main__":
    executor.start_polling(disp)
