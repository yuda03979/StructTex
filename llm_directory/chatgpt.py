import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class ChatGPT:

    def __init__(self):
        pass

    def predict(
            self,
            prompt,
            max_tokens=200,
            temperature=0.02,
            top_p=1.0,
            n=1,
            stop=None
    ) -> str:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            n=n,
            stop=stop
        )
        print(response)
        return response[1].choices[0].message.content
    # should return: error_message, llm_response