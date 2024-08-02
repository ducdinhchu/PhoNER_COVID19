import json

def calc_f1_score(y_true, y_pred):
    tp, fp, fn = 0, 0, 0
    for true_label, pred_label in zip(y_true, y_pred):
        if true_label == pred_label:
            tp += 1
        else:
            if pred_label not in y_true:
                fp += 1
            if true_label not in y_pred:
                fn += 1
    if (2 * tp + fp + fn) != 0:
        return (2 * tp) / (2 * tp + fp + fn)
    else:
        return 1

import re

def find_dicts_in_string(s):
    pattern = r'\{[^{}]*\}'
    matches = re.findall(pattern, s)
    return matches

def calc_f1_score_error(label, predict):
    tp, fp, fn = 0, 0, 0
    truth = json.loads(label)
    predict = find_dicts_in_string(predict)
    predict = [json.loads(p) for p in predict]
    y_true, y_pred = [], []
    for t in truth:
        if enti_type in t["entity_type"]:
            y_true.append(t["entity_value"] + "@" + t["entity_type"])
    for t in predict:
        if enti_type in t["entity_type"]:
            y_pred.append(t["entity_value"] + "@" + t["entity_type"])
    return calc_f1_score(y_true, y_pred)

ifp = "pool/results_ner2016.json"
with open(ifp, "r", encoding="utf-8") as f:
    data = json.load(f)
# print(len(data))

enti_type = "PER"
f1_score = 0

for d in data:
    try:
        truth = json.loads(d["label"])
        predict = json.loads(d["predict"])
        y_true, y_pred = [], []
        for t in truth:
            if enti_type in t["entity_type"]:
                y_true.append(t["entity_value"] + "@" + t["entity_type"])
        for t in predict:
            if enti_type in t["entity_type"]:
                y_pred.append(t["entity_value"] + "@" + t["entity_type"])
        f1_score += calc_f1_score(y_true, y_pred)
        # break
    except Exception as e:
        f1_score_error = calc_f1_score_error(d["label"], d["predict"])
        f1_score += f1_score_error
        # break

print(f1_score/len(data))