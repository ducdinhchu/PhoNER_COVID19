from transformers import AutoTokenizer
import os
import glob
import matplotlib.pyplot as plt
import json

tokenizer = AutoTokenizer.from_pretrained("Viet-Mistral/Vistral-7B-Chat", token="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")

ifp = "/home/duccd4/Documents/PhoNER_COVID19/pool/train_dev_1000.json"
with open(ifp, "r", encoding="utf-8") as f:
    data = json.load(f)
print(len(data))

# # lengths = []   
# # for v in data.values():
# #     tokens = tokenizer(v)
# #     lengths.append(len(tokens.input_ids))
# # print(sorted(lengths))

lengths = []
for d in data:
    tokens = tokenizer(d["instruction"] + d["input"])
    # tokens = tokenizer(d["output"])
    # tokens = tokenizer(d["question"])
    lengths.append(len(tokens.input_ids))
    # if len(tokens.input_ids) > 2048:
    #     print(d["question"])

print(sorted(lengths))
print(len(lengths))

# print(len(data))
# # print(data.keys())

# # lengths = []

# # for value in data.values():
# #     tokens = tokenizer(value)
# #     lengths.append(len(tokens.input_ids))

# # print(sorted(lengths))  

