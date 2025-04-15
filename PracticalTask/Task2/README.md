# SurveyMonkey Survey Creator

This Python script automatically creates a survey on SurveyMonkey using their public API.  
It reads a structured JSON file with survey questions and a text file with email addresses of recipients.

---

## Modify Questions via Terminal

### Add a Question

```bash
python3 -c '
import json
f = "questions.json"
with open(f) as file: data = json.load(file)
data["Survey Title"]["Page Title"]["Added via terminal"] = {
  "Description": "Question 4?",
  "Answers": ["3", "2", "1"]
}
with open(f, "w") as file: json.dump(data, file, indent=2)
'
```
### Add an Open-Ended Question

```bash
python3 -c '
import json
f = "questions.json"
with open(f) as file: data = json.load(file)
data["Survey Title"]["Page Title"]["Your feedback"] = {
  "Description": "Tell us anything you'd like",
  "Answers": []
}
with open(f, "w") as file: json.dump(data, file, indent=2)
'
```

### Delete a Question

```bash
python3 -c '
import json
f = "questions.json"
with open(f) as file: data = json.load(file)
del data["Survey Title"]["Page Title"]["Question 1 text"]
with open(f, "w") as file: json.dump(data, file, indent=2)
'
```

---

## Run the Script

After editing the questions, run the main script:

```bash
python3 survey_creator.py
```

Each run creates a new survey with the updated questions.

---
