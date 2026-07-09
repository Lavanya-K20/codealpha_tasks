from googletrans import Translator

translator = Translator()

print("===== Language Translator =====")
print("1. Telugu")
print("2. Hindi")
print("3. Tamil")
print("4. Kannada")
print("5. Malayalam")
print("6. Chinese")
print("7. Japanese")
print("8. French")

choice = input("Enter your choice (1-8): ")

languages = {
    "1": "te",
    "2": "hi",
    "3": "ta",
    "4": "kn",
    "5": "ml",
    "6": "zh-cn",
    "7": "ja",
    "8": "fr"
}

if choice in languages:
    text = input("Enter English text: ")

    result = translator.translate(text, dest=languages[choice])

    print("\nTranslated Text:")
    print(result.text)
else:
    print("Invalid Choice!")