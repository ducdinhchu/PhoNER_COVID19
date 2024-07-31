import json

def calc_f1_score(y_true, y_pred):
    tp, fp, fn = 0, 0, 0

    for true_label, pred_label in zip(y_true, y_pred):
        if true_label == pred_label:
            tp += 1
        else:
            fp += 1
            fn += 1
    if (2 * tp + fp + fn) != 0:
        return (2 * tp) / (2 * tp + fp + fn)
    else:
        return 1

ifp = "pool/results_3000v2_700.json"
with open(ifp, "r", encoding="utf-8") as f:
    data = json.load(f)
# print(len(data))

enti_type = "PATIENT_ID"

y_true_all, y_pred_all = [], []

f1_score = 0

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
    f1_score += calc_f1_score(y_true, y_pred)
    # if y_true == y_pred:
    #     cnt += 1
    # y_true_all.append(y_true)
    # y_pred_all.append(y_pred)
    # break

# print(y_true_all)
# print(cnt / len(y_true_all))

# score = strict_f1_score(y_true_all, y_pred_all)
print(f1_score/len(data))