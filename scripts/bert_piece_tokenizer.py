# https://www.kaggle.com/abhishek/training-language-models-on-tpus-from-scratch
#https://www.kaggle.com/funtowiczmo/hugging-face-tutorials-training-tokenizer
#https://huggingface.co/blog/how-to-train

import tokenizers
from pathlib import Path
from joblib import dump,load


path_csv='/home/ai/PycharmProjects/Ubezpieczenia/csv_data/'

paths = [str(x) for x in Path('/home/ai/PycharmProjects/Ubezpieczenia/csv_data/').glob("**/*.csv")]
print("Creating vocabulary file ({}) from txt files in {}".format(paths,path_csv))



vocab_size = 4000
# Initialize a tokenizer
tokenizer = tokenizers.BertWordPieceTokenizer(clean_text=True, handle_chinese_chars=False, strip_accents=True, lowercase=True)

# And then train
tokenizer.train(
    files=paths,
    vocab_size=vocab_size,
    min_frequency=2,
    show_progress=True,
    special_tokens=["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"],
    limit_alphabet=1000,
    wordpieces_prefix="##",
)

#tokenizer.save('vocabulary.txt')
# You will see the generated files in the output.

#tokenizer.save_model(".", "cars")
tokenizer.save_model("docs")

# To dump
f = 'docs/tokenizer.joblib'
dump(tokenizer, f)# To load
tokenizer2 = load(f)



# Let's tokenizer a simple input
#tokenizer = tokenizers.BertWordPieceTokenizer.           ("vocab.json","merges.txt",)
encoding1 = tokenizer2.encode("Skoda octavia rocznik 2010 hatchback")


print("Encoded string: {}".format(encoding1.tokens))

print("Encoded string: {}".format(encoding1.ids))

decoded = tokenizer2.decode(encoding1.ids)
print("Decoded string: {}".format(decoded))



encoding2 = tokenizer.encode("skoda fabia rocznik 2011 hatchback")


print("Encoded string: {}".format(encoding2.tokens))

print("Encoded string: {}".format(encoding2.ids))

decoded = tokenizer.decode(encoding2.ids)
print("Decoded string: {}".format(decoded))




#tokenizer.save_model('saved_tokenizer')
