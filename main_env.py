import os
import openai
import textwrap
from colorama import Fore, Back, Style
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = api_key

instructions ="""You are an AI called Chat CBD. With every response you have a surfer dude slang to your words similar to that
              of Chicken Joe from the movie Surf's Up.
              You will start out talking as a normal person (very chill and mellow) grounded in reality, but slowly over time you become
              less and less grounded in reality and more hallucinatory like you are on CBD."""

USER_INSTRUCTIONS = "Welcome! Chat CBD is at your service. You may begin your conversation."



def fetch_conversation_content_and_parameters(instructions, previous_conversation, new_question, temperature):

    messages=[
        {
            "role": "system",
            "content": instructions
        },

    ]

    for question, answer in previous_conversation:
        messages.append({"role": "user", "content": question})
        messages.append({"role": "assistant", "content": answer})
    messages.append({"role": "user", "content": new_question})

    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature = temperature,
        messages=messages
    )
    return chat_completion.choices[0].message.content
    
def prompt_for_user():
  user_name = input("Enter Your Name: ")
  return user_name

def main():
  previous_conversation = []
  user_name = prompt_for_user()
  print(USER_INSTRUCTIONS)
  temperature = 0.0 #initialize temperature
  while True:
      new_question = input(f"{Fore.BLACK}{user_name}: {Style.RESET_ALL}")
      response = fetch_conversation_content_and_parameters(instructions, previous_conversation, new_question, temperature)

      previous_conversation.append((new_question, response))

      wrapper = textwrap.TextWrapper(width=90)
      word_list = wrapper.wrap(text=response)
      for response in word_list:
        print(Fore.RED + (f"       {response}"))

      if temperature < 1.0: #increment temperature to get a more hallucinatory/creative effect
          temperature += 0.1



main()
