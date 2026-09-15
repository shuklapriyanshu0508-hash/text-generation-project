import os
from openai import OpenAI

# OpenAI API client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def generate_text(prompt):
    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return response.output_text


if __name__ == "__main__":
    prompt = (
        "Write a short story about a student who discovers "
        "the best book in his college library."
    )

    print("Prompt:")
    print(prompt)

    print("\nGenerated Output:")
    print(generate_text(prompt))
