"""
Text Generation Internship Task
Inference Example

This script demonstrates the basic workflow of sending a prompt
to a text-generation model and receiving generated text.
"""

def generate_text(prompt):
    """
    Example text-generation function.

    In a real API implementation, this function would send the
    prompt to the selected hosted/local language model.
    """

    # Placeholder response for demonstration
    response = (
        "This is an example generated response for the following prompt:\n\n"
        + prompt
    )

    return response


if __name__ == "__main__":
    prompt = "Write a short story about a student who discovers a book in his college library."

    output = generate_text(prompt)

    print("Prompt:")
    print(prompt)

    print("\nGenerated Output:")
    print(output)
