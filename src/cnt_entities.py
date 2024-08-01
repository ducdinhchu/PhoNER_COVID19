import json

ifp = "pool/train_dev_3000.json"
with open(ifp, "r", encoding="utf-8") as f:
    data = json.load(f)
print(len(data))

loc, sym = 0, 0
for d in data:
    tags = d["tags"]
    for t in tags:
        if t == "B-TRANSPORTATION":
            loc += 1
        if t == "B-DATE":
            sym += 1
            
print(loc, sym)