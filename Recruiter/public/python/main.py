from aiogram import Bot, Dispatcher, Router, F
from playwright.async_api import async_playwright
from time import sleep
import requests
import asyncio

router = Router()

async def main(router):
    bot = Bot(token="TOKEN")
    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


@router.message(F.text.lower() == "/start")
async def start_msg(msg):
    await msg.answer("Отправьте мне ссылку на свое резюме!")


@router.message()
async def go(msg):
    await msg.answer("Ваше резюме будет просмотрено!")
    browser = False
    session = requests.Session()
    session.post(url="http://localhost:1636/login.php", data={"username": "hr", "password": "S7t:rWRG$)=3Nfzmha@cZ"})

    try:
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch()
            context = await browser.new_context()
            
            page = await context.new_page()
            await page.goto("http://localhost:1636")
            await context.add_cookies([{"name": "PHPSESSID", "value": f"{session.cookies.get_dict()['PHPSESSID']}", "httpOnly": True, "path": "/", "domain": "localhost"}])
            await page.goto(msg.text)
        
            sleep(10)
            await browser.close()
            browser = False
            
    except Exception as e:
        print(e)
    finally:
        if browser:
            await browser.close()


if __name__ == '__main__':
    print("Бот запустился")
    asyncio.run(main(router))
