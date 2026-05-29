import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask
from threading import Thread

# إعدادات البوت (التوكن يتم سحبه تلقائياً من إعدادات Render)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = 2040
API_HASH = "b18441a1ff607e10a989891a5462e627"

app = Client("shahad_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# القاموس
replies = {
    "آيلتس": ("اختبار آيلتس (IELTS):", "https://t.me/httpsmO9QD5Mbb_FhYzRk/30"),
    "تواصل": ("التواصل:", "https://t.me/httpsmO9QD5Mbb_FhYzRk/3"),
    "موعد": ("موعد التقديم:", "https://t.me/httpsmO9QD5Mbb_FhYzRk/17"),
    "تقديم": ("التقديم:", "https://t.me/httpsmO9QD5Mbb_FhYzRk/18"),
    "مستندات": ("المستندات المطلوبة:", "https://t.me/httpsmO9QD5Mbb_FhYzRk/20"),
    "درجات": ("الدرجات:", "https://t.me/httpsmO9QD5Mbb_FhYzRk/21"),
    "خطط": ("الخطط:", "https://t.me/httpsmO9QD5Mbb_FhYzRk/22"),
    "جدول": ("الجدول:", "https://t.me/httpsmO9QD5Mbb_FhYzRk/23"),
    "فروع": ("فروع الجامعة:", "https://t.me/httpsmO9QD5Mbb_FhYzRk/24"),
    "إعادة": ("إعادة قيد:", "https://t.me/httpsmO9QD5Mbb_FhYzRk/25"),
    "انسحاب": ("الانسحاب:", "https://t.me/httpsmO9QD5Mbb_FhYzRk/26"),
    "تأجيل": ("التأجيل:", "https://t.me/httpsmO9QD5Mbb_FhYzRk/27"),
    "دمج": ("الدمج:", "https://t.me/httpsmO9QD5Mbb_FhYzRk/28"),
    "تسريع": ("التسريع الأكاديمي:", "https://t.me/httpsmO9QD5Mbb_FhYzRk/29"),
    "ستيب": ("اختبار ستيب (STEP):", "https://t.me/httpsmO9QD5Mbb_FhYzRk/4"),
    "خدمات": ("الخدمات:", "https://t.me/httpsmO9QD5Mbb_FhYzRk/16"),
    "بنك": ("بنك ستيب:", "https://t.me/httpsmO9QD5Mbb_FhYzRk/6"),
    "تجميعات": ("التجميعات والملخصات:", "https://t.me/httpsmO9QD5Mbb_FhYzRk/31"),
    "ملخصات": ("التجميعات والملخصات:", "https://t.me/httpsmO9QD5Mbb_FhYzRk/31"),
    "ارشيف": ("أرشيف التحضيري:", "https://t.me/httpsmO9QD5Mbb_FhYzRk")
}

@app.on_message(filters.text & ~filters.private)
async def smart_reply(client, message):
    text = message.text
    for keyword, (caption, url) in replies.items():
        if keyword in text:
            await message.reply(caption, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رابط المعلومة", url=url)]]))
            break

# إعداد سيرفر الويب لـ Render
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "Bot is running"

def run_web():
    web_app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))

if __name__ == "__main__":
    Thread(target=run_web).start()
    app.run()
