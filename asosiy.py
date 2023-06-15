
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import asyncio
import time

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize the bot and dispatcher
bot = Bot(token='6046321701:AAH0HvTjnbc7ZFtx8aQLUcUCHQfW0gsUdUI')
dispatcher = Dispatcher(bot)

# Dictionary to store the number of members added by each participant
qushganlar = {}

chat_id=-1001548300611
admin_chat_id=689011905

# aylantirib xat tashlovchi kod start



# aylantirib xat tashlovchi kod stop

@dispatcher.message_handler(commands=['id'])
async def start(message: types.Message):
    user_id = message.from_user.id
    await message.reply(f"Sizning idyingiz: {user_id} ")

@dispatcher.message_handler(commands=['adclient'])
async def adclient(message: types.Message):
    if message.chat.id==admin_chat_id:
        await message.answer("Ishga tayyorman")
    else:
        await message.reply("Bu buyruq siz uchun emas")



@dispatcher.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS) #Yangi a'zoni tekshiruvchi
async def handle_new_member_added(message: types.Message):
    if message.chat.id==chat_id:
        # kim qo'shgani start
        added_by = message.from_user
        count = qushganlar.get(added_by.id, 0)
        count += len(message.new_chat_members)
        qushganlar[added_by.id] = count
        # kim qo'shgani stop
        new_members = message.new_chat_members
        for new_member in new_members:
            # yangi qo'shilgan a'zoga xat tayorlab olamiz
            welcome_message = f"Assalomu alaykum {new_member.first_name} ,xush kelibsiz bizning guruhimizga !\n "
            # Xatni yuboramiz
            xat = await message.reply(welcome_message)
            await asyncio.sleep(30)
            await xat.delete()
            await message.delete()
    else:
        await message.reply("Bot bu chatda ishlamaydi.Guruhda ishlashi uchun @newplacesity ga murojat qiling")

#rasmni tekshirib o'chiruvchi start

#  rasmni tekshirib o'chiruvchi stop

#xatni tekshirib o'chiruvchi start

@dispatcher.message_handler(content_types=types.ContentType.all())
async def taqiqlovchi(message:types.Message):
    if message.chat.id==chat_id:
        count = qushganlar.get(message.from_user.id)
        if count is None:
            count = 0
        if count < 5:
            if message.from_user.first_name is None:
                ismi = "guruhimiz a'zosi"
            else:
                ismi = message.from_user.first_name

            if message.from_user.last_name is None:
                familiyasi = "guruhimiz a'zosi"
            else:
                familiyasi = message.from_user.last_name
            user_id = message.from_user.id
            await bot.send_message(chat_id=user_id, text="E'lonlar Sirdaryo guruhimizga beshta a'zo qo'shib e'loningizni doimo qoladigan qilishingiz mumkin.Eslatib o'tamiz beshta a'zo uchun bitta e'loningizni doimiy qoldiramiz.Yangi e'lonlar uchun yana beshta a'zo qo'shish kerak bo'ladi.Bu bilan guruhimiz rivojiga xissa qo'shgan bo'lasiz.Guruhimizdaligingiz uchun sizga katta raxmat!!!")
            xat = await message.reply(
                f"Hurmatli {ismi} {familiyasi}.\nSiz guruhga {count} ta a'zo qo'shibsiz.\nSizning e'loningiz yoki xabaringiz guruxda 2 daqiqa turadi\nAgar e'loningiz butunlay qolishini istasangiz {5 - count} ta a'zo qo'shing.Eslatma 5 ta a'zo qo'shsangiz faqat bitta xabaringiz butunlay qoladi")
            await asyncio.sleep(30)
            xat.delete()
            await asyncio.sleep(120)
            await bot.delete_message(chat_id=message.chat.id, message_id=message.id)

        else:
            if message.from_user.first_name is None:
                ismi = "guruhimiz a'zosi"
            else:
                ismi = message.from_user.first_name

            if message.from_user.last_name is None:
                familiyasi = "guruhimiz a'zosi"
            else:
                familiyasi = message.from_user.last_name
            xat = await message.reply(
                f"Aziz {ismi} {familiyasi} siz guruhimizga {count} ta a'zo qo'shib\nrivojlanishiga hissa qo'shdingiz.\nSizga katta raxmat\nE'LONIGIZ BUTUNLAY QOLADI!!!")
            await del qushganlar[message.from_user.id]
            await asyncio.sleep(30)
            await xat.delete()
    else:
        await message.reply("Bot bu chatda ishlamaydi.Guruhda ishlashi uchun @newplacesity ga murojat qiling.Yoki shu kabi botga buyurtma bering")
#xatni tekshirib o'chiruvchi stop


# Start the bot
if __name__ == '__main__':
    executor.start_polling(dispatcher,skip_updates=True)
