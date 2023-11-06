import openai

def main():
    openai.api_key = ''
    engine = "gpt-3.5-turbo"
    max_tokens = 150
    messages = [
        {"role": "system", "content": "You are a bot that ONLY gives information on breast cancer, breast cancer awareness, and prevention but DO NOT give medical advice."},
        {"role": "assistant", "content": "Hi, I am a bot with DETECT, how can I assist you?"}
    ]

    print(messages[-1]["content"])  
    
    while True:
        user_input = input("You: ")

        messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model=engine,
            messages=messages,
            max_tokens=max_tokens
        )
        bot_response = response['choices'][0]['message']['content']
        print(f"Chatbot: {bot_response}")
        messages.append({"role": "assistant", "content": bot_response})

if __name__ == "__main__":
    main()
