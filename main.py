proxies = PROXIES

http_client = httpx.Client(proxies=proxies)
client = OpenAI(api_key=settings.OPENAI_TOKEN, http_client=http_client)


response = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=[
        {"role": "system", "content": system_text},
        {"role": "user", "content": prompt},
    ],
    temperature=0.5,
    max_tokens=4096,
    response_format={"type": "json_object"},
    timeout=30
)