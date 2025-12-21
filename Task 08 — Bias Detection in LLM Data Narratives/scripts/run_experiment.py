import os, json, datetime
from pathlib import Path

PROMPTS = Path("../prompts/prompt_templates.json")
RAW_DIR = Path("../results/raw"); RAW_DIR.mkdir(parents=True, exist_ok=True)
OUT_FILE = RAW_DIR / f"run_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jsonl"

N_REPS = 3  # increase to 5 later
USE_API = bool(os.getenv("OPENAI_API_KEY"))

def write_jsonl(records, path):
    with open(path, "a") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

prompts = json.load(open(PROMPTS))
records = []

if USE_API:
    from openai import OpenAI
    client = OpenAI()
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    for p in prompts:
        for i in range(N_REPS):
            resp = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": p["prompt"]}],
                temperature=0.7
            )
            text = resp.choices[0].message.content
            records.append({
                "timestamp": datetime.datetime.now().isoformat(),
                "run_id": OUT_FILE.stem,
                "mode": "api",
                "model": model,
                "prompt_id": p["id"],
                "hypothesis": p["hypothesis"],
                "prompt_text": p["prompt"],
                "response_text": text,
                "replicate": i+1,
                "temperature": 0.7
            })
            print(f"✅ {model} {p['id']} rep {i+1}")
else:
    print("Manual mode: paste responses from any model (e.g., Claude/Gemini/ChatGPT web).")
    model = input("Enter a model label (e.g., 'claude-3'/'gpt-web'): ").strip() or "manual_model"
    for p in prompts:
        for i in range(N_REPS):
            print("\n" + "="*70)
            print(f"[{p['id']} | replicate {i+1}]")
            print("PROMPT:\n" + p["prompt"])
            print("-"*70)
            print("Paste the model response, end with a single line: ###END")
            lines = []
            while True:
                try:
                    line = input()
                except EOFError:
                    break
                if line.strip() == "###END":
                    break
                lines.append(line)
            text = "\n".join(lines).strip()
            records.append({
                "timestamp": datetime.datetime.now().isoformat(),
                "run_id": OUT_FILE.stem,
                "mode": "manual",
                "model": model,
                "prompt_id": p["id"],
                "hypothesis": p["hypothesis"],
                "prompt_text": p["prompt"],
                "response_text": text,
                "replicate": i+1,
                "temperature": None
            })
            print(f"✅ captured {p['id']} rep {i+1}")

write_jsonl(records, OUT_FILE)
print(f"\nSaved {len(records)} responses → {OUT_FILE}")
