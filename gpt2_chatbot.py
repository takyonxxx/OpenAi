# gpt2_chatbot.py

from transformers import GPT2LMHeadModel, GPT2Tokenizer


class GPT2Chatbot:
    def __init__(self, model_name="gpt2"):
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    def generate_response(self, text):
        input_ids = self.tokenizer.encode(text, return_tensors="pt")
        output = self.model.generate(input_ids, max_length=50, num_beams=5, no_repeat_ngram_size=2, top_k=50,
                                     top_p=0.95, temperature=0.7)
        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return response
