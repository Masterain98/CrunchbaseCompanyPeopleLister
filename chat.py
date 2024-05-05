import json
import time
import requests
import os

HEADER = {
    "accept": "application/json, text/event-stream",
    "content-type": "application/json",
    "authorization": f"Bearer {os.getenv("GPT_TOKEN")}"
}


def make_chat(question: str):
    main_json = {
        "messages": [
            {
                "role": "system",
                "content": "\nYou are ChatGPT, a large language model trained by OpenAI.\nKnowledge cutoff: 2023-04\nCurrent model: gpt-4-32k\nCurrent time: 4/19/2024, 12:38:27 PM\nLatex inline: $x^2$ \nLatex block: $$e=mc^2$$\n\n"
            },
            {
                "role": "user",
                "content": question
            }
        ],
        "stream": True,
        "model": "gpt-4-32k",  # model name, 32k always faster but cost more
        "temperature": 0.5,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "top_p": 1
    }

    s = requests.Session()
    full_text = ""

    with s.post(f"https://{os.getenv("GPT_HOSTNAME")}/v1/chat/completions", stream=True, json=main_json,
                headers=HEADER) as r:
        for chunk in r.iter_lines():
            data = chunk.decode("utf-8")
            data = data.replace("data: ", "")
            if data and data != "[DONE]":
                try:
                    this_response = json.loads(data)
                    this_text = this_response["choices"][0]["delta"]["content"]
                except (json.decoder.JSONDecodeError, KeyError) as e:
                    # Very likely to be 429 error; stop the script; coffee break
                    print(f"GPT Response Error: {e}\nResponse: {data}")
                    time.sleep(60*10)
                full_text += this_text
    print(full_text)
    return full_text