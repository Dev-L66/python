import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o")
text = "Hey, my name is Alex."
tokens = encoder.encode(text)
print("Tokens",tokens)

decoded = encoder.decode([25216, 11, 922, 1308, 382, 12734, 13])
print("Decode", decoded)