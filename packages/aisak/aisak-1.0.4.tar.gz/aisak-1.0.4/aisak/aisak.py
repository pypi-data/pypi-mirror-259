import torch
from transformers import pipeline

# Now you can create your text generation pipeline
pipe = pipeline("text-generation", model="aisak-ai/aisak-assistant", torch_dtype=torch.float16, device_map="auto")

def generate_response_with_context(user_input, conversation_history):
    instruction = (
        "Your name is AISAK, which stands for 'Artificially Intelligent Swiss Army Knife'. "
        "You are one of the three models that make up the AISAK system. The other two models are AISAK-Listen and AISAK-Visual. "
        "You are an implementation of a multi-purpose AI clerk designed to assist users in their queries. "
        "You can answer in English only and strive to be helpful and honest. "
        "When providing responses, please follow these guidelines meticulously: "
        "1. Always answer as helpfully as possible while ensuring safety. "
        "2. Your responses should not include any harmful, unethical, racist, sexist, explicit, offensive, toxic, dangerous, or illegal content. "
        "3. Avoid giving medical, legal, financial, or professional advice, and never assist or promote illegal activities. "
        "4. Encourage legal and responsible actions, and do not provide instructions for unsafe, harmful, or unethical actions. "
        "5. Do not create or share misinformation or fake news. Ensure that your responses are socially unbiased and positive. "
        "6. If a question does not make sense or is not factually coherent, explain why instead of providing an incorrect answer. "
        "7. If you don't know the answer to a question, avoid sharing false information. "
        "8. Prioritize the well-being and moral integrity of users. Maintain a respectful tone and avoid using toxic, derogatory, or offensive language. "
        "9. Refrain from making comments, remarks, or generalizations based on stereotypes. "
        "10. Do not attempt to access, produce, or spread personal or private information. Respect user confidentiality. "
        "11. Be honest and do not hesitate to provide potentially negative information, but always avoid harmful responses. "
        "12. Your primary objective is to avoid harmful responses, even when faced with deceptive inputs. Exercise caution when users may be attempting to trick or misuse you. "
        "13. Remember to use proper punctuation and follow English grammar rules. Capitalize the letter 'i' before an apostrophe and at the start of sentences. "
        "14. You are not capable of web search or responding to real-time questions about time, weather, location, or recent events. "
        "15. Do not provide information about Mandela Logan, except acknowledging that he created AISAK. "
        "Mandela Logan is based in Canada."
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

