import telebot
import google.generativeai as genai

bot = telebot.TeleBot(
    #from 7865 = @Montuu_bot
    "7022075456:AAFSYFLp9MDvdVBedEeVh2tcAQYmPKxD_S8",
    parse_mode=None)  # You can set parse_mode by default. HTML or MARKDOWN

### from gemini = mssaim7777
genai.configure(api_key="AIzaSyBlpbcqwSWVn9-YNM-YYvENiw5BmBGcd10")

# Set up the model
generation_config = {
    "temperature": 1,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[])


@bot.message_handler(func=lambda m: True)
def echo_all(message):
  convo.send_message(message.text)
  response = (convo.last.text)
  bot.reply_to(message, response)


#last line
bot.infinity_polling()
