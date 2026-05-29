from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

BOT_TOKEN = "8819650642:AAGg5vxB7CMDFnmaDE7vCDMDnqxba4MFHOQ"

# تهيئة البوت
app = Client("shahad_bot", api_id=2040, api_hash="b18441a1ff607e10a989891a5462e627", bot_token=BOT_TOKEN)

@app.on_message(filters.text & ~filters.private)
async def smart_reply(client, message):
    text = message.text
    
    if "آيلتس" in text:
        await message.reply("اختبار آيلتس (IELTS):", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رابط الآيلتس", url="https://t.me/httpsmO9QD5Mbb_FhYzRk/30")]]))
    elif "تواصل" in text:
        await message.reply("التواصل:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رابط التواصل", url="https://t.me/httpsmO9QD5Mbb_FhYzRk/3")]]))
    elif "موعد" in text:
        await message.reply("موعد التقديم:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رابط الموعد", url="https://t.me/httpsmO9QD5Mbb_FhYzRk/17")]]))
    elif "تقديم" in text:
        await message.reply("التقديم:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رابط التقديم", url="https://t.me/httpsmO9QD5Mbb_FhYzRk/18")]]))
    elif "مستندات" in text:
        await message.reply("المستندات المطلوبة:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رابط المستندات", url="https://t.me/httpsmO9QD5Mbb_FhYzRk/20")]]))
    elif "درجات" in text:
        await message.reply("الدرجات:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رابط الدرجات", url="https://t.me/httpsmO9QD5Mbb_FhYzRk/21")]]))
    elif "خطط" in text:
        await message.reply("الخطط:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رابط الخطط", url="https://t.me/httpsmO9QD5Mbb_FhYzRk/22")]]))
    elif "جدول" in text:
        await message.reply("الجدول:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رابط الجدول", url="https://t.me/httpsmO9QD5Mbb_FhYzRk/23")]]))
    elif "فروع" in text:
        await message.reply("فروع الجامعة:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رابط الفروع", url="https://t.me/httpsmO9QD5Mbb_FhYzRk/24")]]))
    elif "إعادة" in text:
        await message.reply("إعادة قيد:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رابط إعادة القيد", url="https://t.me/httpsmO9QD5Mbb_FhYzRk/25")]]))
    elif "انسحاب" in text:
        await message.reply("الانسحاب:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رابط الانسحاب", url="https://t.me/httpsmO9QD5Mbb_FhYzRk/26")]]))
    elif "تأجيل" in text:
        await message.reply("التأجيل:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رابط التأجيل", url="https://t.me/httpsmO9QD5Mbb_FhYzRk/27")]]))
    elif "دمج" in text:
        await message.reply("الدمج:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رابط الدمج", url="https://t.me/httpsmO9QD5Mbb_FhYzRk/28")]]))
    elif "تسريع" in text:
        await message.reply("التسريع الأكاديمي:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رابط التسريع", url="https://t.me/httpsmO9QD5Mbb_FhYzRk/29")]]))
    elif "ستيب" in text:
        await message.reply("اختبار ستيب (STEP):", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رابط ستيب", url="https://t.me/httpsmO9QD5Mbb_FhYzRk/4")]]))
    elif "خدمات" in text:
        await message.reply("الخدمات:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رابط الخدمات", url="https://t.me/httpsmO9QD5Mbb_FhYzRk/16")]]))
    elif "بنك" in text:
        await message.reply("بنك ستيب:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رابط بنك ستيب", url="https://t.me/httpsmO9QD5Mbb_FhYzRk/6")]]))
    elif "تجميعات" in text or "ملخصات" in text:
        await message.reply("التجميعات والملخصات:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رابط التجميعات", url="https://t.me/httpsmO9QD5Mbb_FhYzRk/31")]]))
    elif "ارشيف" in text:
        await message.reply("أرشيف التحضيري:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رابط الأرشيف", url="https://t.me/httpsmO9QD5Mbb_FhYzRk")]]))

app.run()
