import json
from sklearn.metrics import f1_score

ifp = "pool/results.json"
with open(ifp, "r", encoding="utf-8") as f:
    data = json.load(f)
# print(len(data))

enti_type = "DATE"

y_true_all, y_pred_all = [], []

cnt = 0

for d in data:
    try:
        truth = json.loads(d["label"])
        predict = json.loads(d["predict"])
    except Exception as e:
        print(e)
        print(d["label"])
    
    y_true, y_pred = [], []
    for t in truth:
        if enti_type in t["label"]:
            y_true.append(t["entity"] + "@" + t["label"])
    for t in predict:
        if enti_type in t["label"]:
            y_pred.append(t["entity"] + "@" + t["label"])
    if y_true == y_pred:
        cnt += 1
    y_true_all.append(y_true)
    y_pred_all.append(y_pred)
    # print(f1_score(y_true, y_pred, average="micro"))
    # break

# print(y_true_all, y_pred_all)

print(cnt / len(y_true_all))
    
# score = f1_score(y_true_all, y_pred_all, average=None)
# print(score)