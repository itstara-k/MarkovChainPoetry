import markovify
import os
import re

#read_poems(int) -> str: Returns a string object text containing the raw text of n poems; n determines dataset size
def read_poems(num_poems):
    text = ""
    poems = [os.path.join(os.path.join('writing_samples', filename)) for filename in os.listdir('writing_samples')]
    num_poems_read = 0
    for poem in poems:
        if num_poems_read < num_poems:
            with open(poem, encoding="utf8") as f:
                text += f.read()
                num_poems_read += 1
        else:
            break
        
    return text

def clean_text(text):
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r' +', ' ', text)
    return text

small_dataset = clean_text(read_poems(5))
medium_dataset = clean_text(read_poems(12))
large_dataset = clean_text(read_poems(24))

small_text_model = markovify.Text(small_dataset)
medium_text_model = markovify.Text(medium_dataset)
large_text_model = markovify.Text(large_dataset)

print("----Small Dataset----")
print(small_text_model.make_short_sentence(max_chars=250, min_chars=100, tries=100)) #100-250 chars = ~20 words -> short poem
print("\n")
print(small_text_model.make_short_sentence(max_chars=450, min_chars=200, tries=100))  #200-450 chars = ~40 words -> medium poem
print("\n")
print(small_text_model.make_short_sentence(max_chars=650, min_chars=300, tries=100))  #300-650 chars = ~60 words -> long poem
print("\n")
print(small_text_model.make_short_sentence(max_chars=850, min_chars=400, tries=100))  #400-850 chars = ~80 words -> extra long poem
print("\n")

print("----Medium Dataset----")
print(medium_text_model.make_short_sentence(max_chars=250, min_chars=100, tries=100))
print("\n")
print(medium_text_model.make_short_sentence(max_chars=450, min_chars=200, tries=100)) 
print("\n")
print(medium_text_model.make_short_sentence(max_chars=650, min_chars=300, tries=100))
print("\n")
print(medium_text_model.make_short_sentence(max_chars=850, min_chars=400, tries=100))
print("\n")

print("----Large Dataset----")
print(large_text_model.make_short_sentence(max_chars=250, min_chars=100, tries=100)) 
print("\n") 
print(large_text_model.make_short_sentence(max_chars=450, min_chars=200, tries=100)) 
print("\n")
print(large_text_model.make_short_sentence(max_chars=650, min_chars=300, tries=100))
print("\n")
print(large_text_model.make_short_sentence(max_chars=850, min_chars=400, tries=100))
print("\n")


