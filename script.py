from PIL import Image, ImageDraw, ImageFont

def generate_binance_receipt(amount: int, date_str: str, template_path="template.png"):
    withdrawal_details = f"-{amount} USDT"
    withdrawal_amount = f"{amount+1} USDT"
    top_time = date_str.split(" ")[1][:5]   # HH:MM
    date_value = date_str

    # Template image ဖွင့်
    img = Image.open(template_path).convert("RGBA")
    draw = ImageDraw.Draw(img)

    # Font (Windows -> Arial.ttf, Linux -> DejaVuSans.ttf)
    font_large = ImageFont.truetype("arial.ttf", 60)
    font_small = ImageFont.truetype("arial.ttf", 40)

    # Coordinates (အမှန်တကယ် screenshot နဲ့ ကိုက်အောင်ပြန်ညှိဖို့လိုမယ်)
    draw.text((250, 200), withdrawal_details, fill="black", font=font_large)   # -XXX USDT
    draw.text((250, 500), withdrawal_amount, fill="black", font=font_small)    # Withdrawal Amount
    draw.text((60, 30), top_time, fill="black", font=font_small)               # Top time
    draw.text((250, 850), date_value, fill="black", font=font_small)           # Date

    img.save("output.png")
    print("✅ Receipt saved as output.png")

# စမ်းရန်
if __name__ == "__main__":
    generate_binance_receipt(500, "2025-08-20 15:38:31")
