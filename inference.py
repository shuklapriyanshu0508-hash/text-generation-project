from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MODEL_ID = "HuggingFaceTB/SmolLM2-360M-Instruct"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(MODEL_ID)

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)


def generate_text(prompt):
    inputs = tokenizer(
        prompt,
        return_tensors="pt"
    ).to(device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )

    input_length = inputs["input_ids"].shape[1]

    return tokenizer.decode(
        outputs[0][input_length:],
        skip_special_tokens=True
    )


if __name__ == "__main__":
    prompt = (
        "Write a short story about a student who discovers "
        "the best book in his college library."
    )

    print("Prompt:")
    print(prompt)

    print("\nGenerated Output:")
    print(generate_text(prompt))
