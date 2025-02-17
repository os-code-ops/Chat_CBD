# Chat CBD
Chat CBD: A Trippy AI Chatbot 🌿💬
  - Chat CBD is a playful experiment leveraging OpenAI's API to create a chatbot that mimcs the experience of becoming "stoned" over time. As the conversation continues, the AI's Reponses grow increasingly laid-back and out of the box
# Installation Steps:
-  **Prerequistites** -
    Before running the project, ensure you have the following dependencies installed:
      - `openai`: Python client for the OpenAI API.
      - `colorama`: For colored terminal output.
      - `google.colab`: For managing environment variables in Google Colab (optional, depending on setup)
        -  **Local environment** (with .env): `main_env.py`
            -  install using : `pip install openai` and/or `pip install openai coloroma` and `pip install python-dotenv`
        -  **Google Colab environment**: `main_gcolab.py`
            -  install using : `!pip install openai` and `!pip install coloroma`
      - `textwrap`: To format long text responses.
-  **Get Started** - If you use...
      -  **Local environment**
        -  copy/paste `main_env.py` or clone repository using (https://github.com/os-code-ops/Chat_CBD.git)
      -  **Google Colab environment** - copy/paste `main_gcolab.py` into a [Google Colab Notebook](https://colab.google/)
-  **Set Up OpenAI API Key**
  -  Create a key [here](https://auth.openai.com/authorize?audience=https%3A%2F%2Fapi.openai.com%2Fv1&auth0Client=eyJuYW1lIjoiYXV0aDAtc3BhLWpzIiwidmVyc2lvbiI6IjEuMjEuMCJ9&client_id=DRivsnm2Mu42T3KOpqdtwB3NYviHYzwD&device_id=19e2dad0-18f1-44b5-bbad-a00a4e7c0e7f&ext-login-allow-phone=true&ext-use-new-phone-ui=true&issuer=https%3A%2F%2Fauth.openai.com&max_age=0&nonce=OEEwYnRrV09hRGYzazZqaVNGaFpMRUloeENfSGp5RDN2TkRRRDA0REt5OQ%3D%3D&redirect_uri=https%3A%2F%2Fplatform.openai.com%2Fauth%2Fcallback&response_mode=query&response_type=code&scope=openid+profile+email+offline_access&screen_hint=signup&state=UEN6NC0yQkdPMzliMHpWYXNkeE15WFJ%2BdjRkNjB2ckhfU2NHfkVXZUJVMg%3D%3D&flow=treatment)
    -  Follow this video to set up your OpenAI API Key (https://www.youtube.com/watch?v=gBSh9JI28UQ)  
      -  **Local environment**
          -  create `.env` file and add your key: `OPENAI_API_KEY=<<YOUR_API_KEY>>`
      -  **Google Colab environment**
          -  Make a secret key using your OpenAI API Key and call it `OPENAI_API_KEY`:
            -  ![image](https://github.com/user-attachments/assets/29ced41c-6e71-4b26-a637-b2c7ea44ac4a)
-  **Run Code**
      -  **Local environment**
          -  run script: `main_env.py`
      -  **Google Colab environment**
          -  run script: `main_gcolab.py`

    

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

