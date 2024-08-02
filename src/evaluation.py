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

def calc_f1_score_error(label, predict):
    tp, fp, fn = 0, 0, 0
    truth = json.loads(d["label"])
    for t in truth:
        tstr = json.dumps(t, ensure_ascii=False, indent=4)
        print(tstr)
        if tstr in predict:
            print("yes")
    # for true_label, pred_label in zip(y_true, y_pred):
    #     if true_label == pred_label:
    #         tp += 1
    #     else:
    #         fp += 1
    #         fn += 1
    # if (2 * tp + fp + fn) != 0:
    #     return (2 * tp) / (2 * tp + fp + fn)
    # else:
    #     return 1

ifp = "pool/results_ner2016.json"
with open(ifp, "r", encoding="utf-8") as f:
    data = json.load(f)
# print(len(data))

enti_type = "MISC"

y_true_all, y_pred_all = [], []

f1_score = 0
i = 0
cnt = 0

for d in data:
    try:
        truth = json.loads(d["label"])
        predict = json.loads(d["predict"])
        continue
        y_true, y_pred = [], []
        for t in truth:
            if enti_type in t["entity_type"]:
                y_true.append(t["entity_value"] + "@" + t["entity_type"])
        for t in predict:
            if enti_type in t["entity_type"]:
                y_pred.append(t["entity_value"] + "@" + t["entity_type"])
        f1_score += calc_f1_score(y_true, y_pred)
        i += 1
        # print(y_true, y_pred)
        if y_true == y_pred:
            cnt += 1
        y_true_all.append(y_true)
        y_pred_all.append(y_pred)
        # break
    except Exception as e:
        # print(f"error\n{d['label']}\n{d['predict']}")
        print(calc_f1_score_error(d["label"], d["predict"]))

# print(y_true_all)
# print(cnt / len(y_true_all))

# score = strict_f1_score(y_true_all, y_pred_all)
print(i, f1_score/len(data))