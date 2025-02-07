from aiogram import Bot, Dispatcher, Router
from config.token import TOKEN
import  sqlite3



con = sqlite3.connect('data/database.db')
cursor = con.cursor()


admin_id = [5413227254]

router = Router()
dp = Dispatcher()
dp.include_router(router)
bot = Bot(TOKEN)