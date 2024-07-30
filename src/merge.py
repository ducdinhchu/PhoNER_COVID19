import json
import random

ifp = "pool/train_word.json"
with open(ifp, "r", encoding="utf-8") as f:
    train = json.load(f)
print(len(train))

ifp = "pool/dev_word.json"
with open(ifp, "r", encoding="utf-8") as f:
    dev = json.load(f)
print(len(dev))

train_dev = train + dev
random.shuffle(train_dev)
print(len(train_dev))

ofp = "pool/train_dev.json"
with open(ofp, "w", encoding="utf-8") as f:
    json.dump(train_dev, f, ensure_ascii=False, indent=4)