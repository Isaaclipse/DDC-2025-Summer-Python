# 🛂 Digital Passport to Code Island!
print("🌴🏝️ Welcome to Code Island! 🏝️🌴")
print("Before you begin your journey, let's create your DIGITAL PASSPORT.\n")

# Collect basic info
name = input("👤 What's your full name? ")
age = input("🎂 How old are you? ")
emoji = input("😄 What's your favorite emoji? ")
color = input("🎨 What's your favorite color? ")
dream_job = input("💼 What's your dream job? ")
code_name = input("🕵️‍♂️ Choose a cool code name for your passport: ")
island = input("🏖️ Name a magical island you'd love to visit: ")

# Generate passport
print("\n🔒 Generating your secure passport...\n")
print("=========================================")
print("          🌐 CODE ISLAND PASSPORT        ")
print("=========================================")
print(f"👤 Name: {name}")
print(f"🆔 Code Name: {code_name}")
print(f"🎂 Age: {age}")
print(f"🎨 Favorite Color: {color}")
print(f"💼 Dream Job: {dream_job}")
print(f"🌴 Dream Island: {island}")
print(f"😎 Emoji ID: {emoji}")
print("=========================================")
print("🌟 You're now an official explorer of Code Island! 🌟\n")

# Bonus stamps
stamps = ["🌺", "🐚", "🦜", "🌊", "🍍"]
print("🔖 Stamping your passport...")
for s in stamps:
    print(f"{s} ", end="")
print("\n\n✔️ All set! Enjoy your journey.\n")

# ==========================
# 🛠️ YOUR TURN TO CUSTOMIZE!
# ==========================
# Add your own fun facts or sections to the passport here:
music = input("🎵 What's your favorite music genre? ")
snack = input("🍔 What's your favorite snack? ")
animal = input("🐾 What's your favorite animal? ")

# 👉 Example:
hobby = input("🕹️ What's your favorite hobby? ")
game = input("🎮 What's your favorite video game?")

# Print custom section
print("===== BONUS INFO =====")
print(f"🎨 Hobby: {hobby}")
print(f"🎮 Favorite Game: {game}")
print("======================")

# CHALLENGE: Add at least 2 more sections below!
# For example: favorite snack, favorite animal, favorite song, etc.
print(f"🎵 Favorite Music Genre: {music}")
print(f"🍔 Favorite Snack: {snack}")
print(f"🐾 Favorite Animal: {animal}")
print("======================")
print(f"🎨 Hobby: {hobby}")
print(f"🎮 Favorite Game: {game}")

