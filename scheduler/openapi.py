from openai import OpenAI
import dotenv
import os

dotenv.load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_tags(text: str) -> str:
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You will be provided with a block of text, and your task is to extract a list of keywords from it.",
            },
            {"role": "user", "content": text},
        ],
        temperature=0.5,
        max_tokens=64,
        top_p=1,
    )

    tags = completion.choices[0].message.content
    return tags
