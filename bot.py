from groq import Groq



client = Groq()
def ask(prompt):
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
        {
            "role": "user",
            "content": prompt
        }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        stop=None
    )

    print(completion.choices[0].message.content)


while True:
    prompt = input("You: hello, how are you?\n"
    "Enter your prompt (or type 'exit' to quit): ")
    if prompt.lower() in ["exit", "quit"]:
        break   

    ask(prompt)