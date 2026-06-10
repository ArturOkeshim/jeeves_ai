import base64
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://api.vsegpt.ru/v1",
)


def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def main() -> None:
    image_path = "img/1/photo_2026-06-09_19-36-04.jpg"
    base64_image = encode_image(image_path)

    response = client.chat.completions.create(
        model="vis-anthropic/claude-sonnet-4.6",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Что здесь написано?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
        temperature=0.8,
        max_tokens=20000,
    )

    print("Response:", response.choices[0].message.content)


if __name__ == "__main__":
    main()
