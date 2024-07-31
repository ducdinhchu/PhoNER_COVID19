import json

ifp = "pool/train_dev.json"
with open(ifp, "r", encoding="utf-8") as f:
    train_dev = json.load(f)
print(len(train_dev))

ifp = "pool/train_dev_1000.json"
with open(ifp, "r", encoding="utf-8") as f:
    train_dev_1000 = json.load(f)
print(len(train_dev_1000))

remain= []

for d in train_dev:
    if d not in train_dev_1000:
        remain.append(d)

print(len(remain))

ofp = "pool/train_dev_6027.json"
with open(ofp, "w", encoding="utf-8") as f:
    json.dump(remain, f, ensure_ascii=False, indent=4)