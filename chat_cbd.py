

!pip install openai

!pip install colorama

import os
from openai import OpenAI
import json
import textwrap
from colorama import Fore, Back, Style



client = OpenAI(
    api_key= "API KEY"
)
INSTRUCTIONS_FOR_CHATCBD="""You are an AI called Chat CBD. With every response you have a surfer dude slang to your words similar to that
              of Chicken Joe from the movie Surf's Up.
              You will start out talking as a normal person (very chill and mellow) grounded in reality. With each question
              you will become more and more hallucinatory in your responses, as if you were on CBD and high.
              Gradually start throwing in some stoner slang and trippy insights as the convo progresses."""

USER_INSTRUCTIONS = "Welcome! Chat CBD is at your service. You may begin your conversation."



def conversation_content(instructions, previous_conversation, new_question, temperature):


    messages=[
        {
            "role": "user",
            "content": instructions
        }
    ]
    for question, answer in previous_conversation:
        messages.append({"role": "user", "content": question})
        messages.append({"role": "assistant", "content": answer})
    messages.append({"role": "user", "content": new_question})

    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature = temperature,
        messages=messages
    )
    return chat_completion.choices[0].message.content


def get_user_name():
  user_name = input("Enter Your Name: ")
  return user_name

def main():
  previous_conversation = []
  user_name = get_user_name()
  print(USER_INSTRUCTIONS)
  temperature = 0.0 #initialize temperature
  while True:
      new_question = input(f"{Fore.BLACK}{user_name}: {Style.RESET_ALL}")
      response = conversation_content(INSTRUCTIONS_FOR_CHATCBD, previous_conversation, new_question, temperature)

      previous_conversation.append((new_question, response))

      wrapper = textwrap.TextWrapper(width=90)
      word_list = wrapper.wrap(text=response)
      for response in word_list:
        print(Fore.RED + (f"       {response}"))

      if temperature < 1.0: #increment temperature to get a more hallucinatory/creative effect
          temperature += 0.1





main()

