import json

file_path = 'data/word/test_word.json'
data = []
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        record = json.loads(line.strip())
        data.append(record)
        
# print(len(data))
# print(data[0])

ins = "Bạn là một hệ thống nhận diện thực thể được đặt tên (Named Entity Recognition - NER) chuyên nghiệp. Nhiệm vụ của bạn là nhận một văn bản làm đầu vào và trích xuất các thực thể được đặt tên từ văn bản đó."

for d in data:
    words = d["words"]
    tags = d["tags"]
    sentence = ' '.join(words)
    output = []
    for i, t in enumerate(tags):
        if t != "O":
            output.append({"entity": words[i], "label": t})
    d["input"] = sentence
    d["output"] = output
    d["instruction"] = ins

ofp = "pool/test_word_f.json"
with open(ofp, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

