import json
import requests

ACCESS_TOKEN = "CMT0R-q0dcs6i9ZZ0fGmpLP1NAECqMSU.HKuPz94Vt0bZoflMZ9HyNmhxiTUDGhzG47SlOF7gHmvETyE0NVLY6W6l7iBlUAkLE-smLbvodHMtxC4oaDh16iG.B0dZPbR"

API_BASE = "https://api.surveymonkey.com/v3"

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}


def load_questions(path):
    with open(path, "r") as f:
        return json.load(f)

def load_emails(path):
    with open(path, "r") as f:
        return [email.strip() for email in f.readlines() if email.strip()]

def create_survey(name):
    payload = {"title": name}
    res = requests.post(f"{API_BASE}/surveys", headers=HEADERS, json=payload)

    print("Creating survey...")
    print("Status code:", res.status_code)
    print("Response:", res.json())

    if res.status_code != 201:
        raise Exception(f"Survey creation failed: {res.json()}")

    survey_id = res.json()["id"]
    preview_url = res.json().get("preview")
    print(f"Survey created! Preview it here:\n{preview_url}\n")

    return survey_id

def add_page_and_questions(survey_id, page_name, questions):
    page_res = requests.post(
        f"{API_BASE}/surveys/{survey_id}/pages",
        headers=HEADERS,
        json={"title": page_name}
    )

    if page_res.status_code != 201:
        raise Exception(f"Page creation failed: {page_res.json()}")

    page_id = page_res.json()["id"]

    for q_text, q_data in questions.items():
        if q_data["Answers"]:
            question = {
                "headings": [{"heading": q_text}],
                "family": "single_choice",
                "subtype": "vertical",
                "answers": {"choices": [{"text": ans} for ans in q_data["Answers"]]}
            }
        else:
            question = {
                "headings": [{"heading": q_text}],
                "family": "open_ended",
                "subtype": "single"
            }

        q_res = requests.post(
            f"{API_BASE}/surveys/{survey_id}/pages/{page_id}/questions",
            headers=HEADERS,
            json=question
        )

        if q_res.status_code != 201:
            print(f"Failed to create question '{q_text}':", q_res.json())
        else:
            print(f"Question added: {q_text}")

def main():
    questions_data = load_questions("questions.json")

    for survey_name, pages in questions_data.items():
        print(f"\nCreating survey: {survey_name}")
        survey_id = create_survey(survey_name)

        for page_name, questions in pages.items():
            print(f"Adding page: {page_name}")
            add_page_and_questions(survey_id, page_name, questions)

        print(f"Survey '{survey_name}' created with all questions!\n")

if __name__ == "__main__":
    main()
