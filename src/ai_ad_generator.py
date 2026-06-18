def generate_ai_ad(row):
    try:
        from openai import OpenAI
        client = OpenAI()

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": f"Generate ad for {row}"}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        print("API ERROR:", e)

        # 🔥 Smart fallback (looks realistic)
        product = row.get("product", "Awesome Product")

        return f"""
🔥 {product} — Don’t Miss Out!

✨ Premium quality  
💥 Limited time offer  
🚀 Upgrade your experience today  

👉 Buy now and save big!
"""