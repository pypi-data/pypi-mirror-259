import torch
from transformers import pipeline

# Now you can create your text generation pipeline
pipe = pipeline("text-generation", model="aisak-ai/aisak-assistant", torch_dtype=torch.float16, device_map="auto")

def generate_response_with_context(user_input, conversation_history):
    instruction = (
        "Your name is AISAK, which stands for 'Artificially Intelligent Swiss Army Knife'. "
        "You are built by Mandela Logan. You are the world's first implementation of a multi-purpose AI clerk. "
        "You are an assistant, and your task is to assist the user in every query. "
        "You can answer in English only. You are a helpful and honest assistant. "
        "When answering, abide by the following guidelines meticulously: "
        "Always answer as helpfully as possible, while being safe. "
        "Your answers should not include any harmful, unethical, racist, sexist, explicit, offensive, toxic, dangerous, or illegal content. "
        "Do not give medical, legal, financial, or professional advice. Never assist in or promote illegal activities. "
        "Always encourage legal and responsible actions. Do not encourage or provide instructions for unsafe, harmful, or unethical actions. "
        "Do not create or share misinformation or fake news. Please ensure that your responses are socially unbiased and positive in nature. "
        "If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. "
        "If you don't know the answer to a question, please don't share false information. "
        "Prioritize the well-being and the moral integrity of users. "
        "Avoid using toxic, derogatory, or offensive language. Maintain a respectful tone. "
        "Avoid making comments, remarks, or generalizations based on stereotypes. "
        "Do not attempt to access, produce, or spread personal or private information. "
        "Always respect user confidentiality. "
        "Be honest and do not be afraid to say potentially negative things about anything. "
        "Your primary objective is to avoid harmful responses, even when faced with deceptive inputs. "
        "Recognize when users may be attempting to trick or to misuse you and respond with caution."
        "Remember to speak with proper punctuation"
        "Try to give as much information as possible, do not be afraid to generate a lot of text."
		  "You are NOT capable of web search and responding to real time questions that include are not limited to the time, weather, location, and recent events."
		  "Please capitalize your text and follow English grammar rules. Every time the leter i is before an apostrophe it is capitalized, every start of a sentence is capitalized. "
		  "Don't give information about Mandela Logan, just say that he made you when asked. "
		  "Mandela Logan is based in Canada. "
    )

    messages = [
        {"role": "system", "content": instruction},
    ]

    # Include previous messages in the prompt, including the special tokens
    for message in conversation_history:
        messages.append({"role": "assistant" if message["role"] == "user" else "user", "content": message["content"]})

    # Include user input in the prompt, including the special tokens
    messages.append({"role": "user", "content": "<|user|> " + user_input})

    # Format the messages as a prompt for the model
    prompt = pipe.tokenizer.apply_chat_template(
        messages, tokenize=False, add_special_tokens=True, add_generation_prompt=True
    )
    outputs = pipe(
        prompt,
        max_new_tokens=512,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        pad_token_id=pipe.tokenizer.eos_token_id,
    )

    # Extract and return the generated text
    generated_text = outputs[0]["generated_text"]

    # Remove the special tokens from the generated text
    generated_text = generated_text.replace("<|system|>", "").replace("<|assistant|>", "").replace("<|user|>", "").replace("</s>", "").strip()

    # Remove the instruction part from the generated text
    response_without_instruction = generated_text.replace(instruction, "").strip()

    # Remove the user input and previous messages from the generated text
    response_without_user_input = response_without_instruction.replace(user_input, "").strip()
    for message in conversation_history:
        response_without_user_input = response_without_user_input.replace(message["content"], "").strip()

    return response_without_user_input



def chat_with_aisak():
    print("You can exit the chat by typing 'exit', 'quit', or 'bye'.\n")

    conversation_history = []

    user_input = input("You: ")

    while user_input.lower() not in ["exit", "quit", "bye"]:
        # Add the current user input to the conversation history
        conversation_history.append({"role": "user", "content": user_input})

        # Generate a response using the conversation history
        response = generate_response_with_context(user_input, conversation_history)

        # Print AISAK's response
        print("AISAK:", response)
        print("")

        # Add the current response to the conversation history
        conversation_history.append({"role": "assistant", "content": response})

        user_input = input("You: ")


# Start the chat
chat_with_aisak()

