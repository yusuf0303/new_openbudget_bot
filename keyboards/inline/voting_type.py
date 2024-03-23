from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

voting_type = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [InlineKeyboardButton(text="Telegram orqali ovoz berish ⤴️",
                          url="https://t.me/ochiqbudjet_3_bot?start=032329736008")],
    [InlineKeyboardButton(text="Sayt orqali ovoz berish 🌐",
                          url="https://openbudget.uz/boards/initiatives/initiative/32/e019dabd-f8d6-412d-8ad1-6e74d23a7cc1")],
    [InlineKeyboardButton(text="Ovoz berdim ✅", callback_data="confirm")]
])


checking_number = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton(text="Tasdiqlash ✅", callback_data="verified")],
    [InlineKeyboardButton(text="Bekor qilish ❌", callback_data="failed")]
])
