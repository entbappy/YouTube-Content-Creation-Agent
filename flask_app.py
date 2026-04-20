from flask import Flask, request, render_template_string
import os
from dotenv import load_dotenv
import google.generativeai as genai
from tavily import TavilyClient

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

MODEL_INFO = "gemini-2.0-flash"
MODEL_SCRIPT = "gemini-2.0-flash"

app = Flask(__name__)

INDEX_HTML = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>StoryForge Demo</title>
    <style>
      body{font-family:Arial,Helvetica,sans-serif;background:#0f1724;color:#e6eef8;padding:2rem}
      .card{background:rgba(255,255,255,0.04);padding:1rem;border-radius:10px;max-width:900px;margin:1rem auto}
      input[type=text]{width:100%;padding:0.6rem;border-radius:6px;border:1px solid #2b3946;background:#071021;color:#e6eef8}
      button{background:#2563eb;color:#fff;padding:0.6rem 1rem;border-radius:6px;border:none}
      pre{background:#071021;padding:1rem;border-radius:8px;white-space:pre-wrap}
    </style>
  </head>
  <body>
    <div class="card">
      <h1>🌐 StoryForge Agent — Flask Demo</h1>
      <form method="post" action="/generate">
        <label for="topic">Enter topic or query</label>
        <input type="text" id="topic" name="topic" required placeholder="e.g. climate change latest news">
        <div style="margin-top:0.5rem">
          <label><input type="checkbox" name="script" value="1"> Generate short video script</label>
        </div>
        <div style="margin-top:0.8rem"><button type="submit">Generate</button></div>
      </form>
    </div>
    {% if summary %}
    <div class="card">
      <h2>📚 AI-Generated Summary</h2>
      <pre>{{ summary }}</pre>
    </div>
    {% endif %}
    {% if script %}
    <div class="card">
      <h2>🎥 Video Script</h2>
      <pre>{{ script }}</pre>
    </div>
    {% endif %}
  </body>
</html>
"""


def get_realtime_info(query):
    try:
        resp = tavily_client.search(query=query, max_results=3, topic="general")
        if resp and resp.get("results"):
            summaries = []
            for r in resp["results"]:
                title = r.get("title", "")
                snippet = r.get("snippet", "")
                url = r.get("url", "")
                summaries.append(f"**{title}**\n\n{snippet}\n\n🔗 {url}")
            source_info = "\n\n---\n\n".join(summaries)
        else:
            source_info = f"No recent updates found on '{query}'."
    except Exception as e:
        return f"Error fetching info: {e}"

    prompt = f"""
You are a professional researcher and content creator with expertise in multiple fields.
Using the following real-time information, write an accurate, engaging, and human-like summary
for the topic: '{query}'.

Requirements:
- Keep it factual, insightful, and concise (around 200 words).
- Maintain a smooth, natural tone.
- Highlight key takeaways or trends.
- Avoid greetings or self-references.

Source information:
{source_info}

Output only the refined, human-readable content.
"""
    try:
        model = genai.GenerativeModel(MODEL_INFO)
        response = model.generate_content(prompt)
        return response.text.strip() if response and getattr(response, 'text', None) else source_info
    except Exception as e:
        return f"Error generating summary: {e}"


def generate_video_script(info_text):
    prompt = f"""
You are a creative scriptwriter.
Turn this real-time information into an engaging short video script (for YouTube Shorts or Instagram Reels).
Use a conversational tone with a strong hook and a clear call to action at the end.
Keep it around 100–120 words.

{info_text}
"""
    try:
        model = genai.GenerativeModel(MODEL_SCRIPT)
        response = model.generate_content(prompt)
        return response.text.strip() if response and getattr(response, 'text', None) else "Could not generate video script."
    except Exception as e:
        return f"Error generating script: {e}"




@app.route("/", methods=["GET"])
def index():
    return render_template_string(INDEX_HTML)



@app.route("/generate", methods=["POST"])
def generate():
    topic = request.form.get("topic", "").strip()
    want_script = request.form.get("script")
    summary = None
    script = None
    if topic:
        summary = get_realtime_info(topic)
        if want_script:
            script = generate_video_script(summary)
    return render_template_string(INDEX_HTML, summary=summary, script=script)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
