# Chat CBD
Chat CBD: A Trippy AI Chatbot 🌿💬
  - Chat CBD is a playful experiment leveraging OpenAI's API to create a chatbot that mimcs the experience of becoming "stoned" over time. As the conversation continues, the AI's Reponses grow increasingly laid-back and out of the box
# Installation Steps:

-  Prerequistites -
    Before running the project, ensure you have the following dependencies installed:
      - `openai`: Python client for the OpenAI API.
      - `colorama`: For colored terminal output.
      - `google.colab`: For managing environment variables in Google Colab (optional, depending on setup).
      - `textwrap`: To format long text responses.
# How It Works:
1. System Instructions
2. Send Previous Conversation to AI
3. Increase the Temperature
4. User Interaction
5. Output
# 1. System Instructions
  - The chatbot starts by setting a system message that guides its tone and style of communication. Initially, the AI responds in a grounded, mellow, and chill way, akin to a relaxed surfer.
    ```python
    instructions = """You are an AI called Chat CBD. With every response, you have a surfer dude slang similar to Chicken Joe from the movie Surf's Up.
                  You will start out talking as a normal person (very chill and mellow) grounded in reality."""
    ```
# 2. Send Previous Conversation to AI
  - As the conversation progresses, each new user input and AI response is added to the conversation history. Without this, the AI would not remember the previous user input and be without a conversation history knowledge.
    ```python
    def fetch_conversation_content_and_parameters(instructions, previous_conversation, new_question, temperature):
    ```
# 3. Increase the Temperature
  - The AI's responses are adjusted based on the increasing temperature, which is a parameter that controls the creativity of the model's output. The temperature value is gradually increased to introduce more creative and "stoned" responses. This is what drives the shift from grounded to more out-of-the-box language.
    ```python
    temperature = 0.0 
    if temperature < 1.0: 
        temperature += 0.1  
    ```
# 4. User Interaction
  - Users input their names, and then they can engage in a conversation with the chatbot.
      ```python
      def prompt_for_user():
      user_name = input("Enter Your Name: ")
          return user_name
      ```
# 5. Output
  - The AI's responses are printed in the terminal with colored text in order for the viewer to better distinguishes between the AI's response and their own. Each response is formatted to fit the terminal window for easy reading.
      ```python
      wrapper = textwrap.TextWrapper(width=90)
      word_list = wrapper.wrap(text=response)
      for response in word_list:
          print(Fore.RED + (f"       {response}"))
      ```

