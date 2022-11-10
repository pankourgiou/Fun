#You will need to import transformers module running pip install transformers and pytorch by running pip install torch
from transformers import pipeline
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

# generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')
# generator = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')
prompt = 'Write me a review on Iron Maiden discography'
res = generator(prompt, max_length=1000, do_sample=True, temperature=0.9)
print(res[0]['generated_text'])
