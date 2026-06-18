def generate_ad(customer):

    customer_id = int(customer["CustomerID"])

    return f"""
<div style="
    border:4px solid #FF6B6B;
    border-radius:20px;
    padding:30px;
    background:#FFF5F5;
    font-family:Arial,sans-serif;
">

<h1 style="
    text-align:center;
    color:#FF4D4D;
">
🌟 Special Just For You! 🌟
</h1>

<h3 style="
    text-align:center;
    color:#333333;
">
Hi Valued Customer #{customer_id}
</h3>

<p style="
    text-align:center;
    font-size:18px;
    color:#444444;
">
Based on your shopping behavior and preferences,
we've selected exclusive offers crafted specifically for you.
</p>

<div style="
    background:white;
    border-radius:15px;
    padding:20px;
    margin-top:20px;
">

<p style="
    color:#DC2626;
    font-size:18px;
    font-weight:bold;
">
✨ Handpicked products you'll love
</p>

<p style="
    color:#7C3AED;
    font-size:18px;
    font-weight:bold;
">
🎁 Exclusive limited-time offers
</p>

<p style="
    color:#0284C7;
    font-size:18px;
    font-weight:bold;
">
🚚 Fast and hassle-free delivery
</p>

</div>

<p style="
    text-align:center;
    margin-top:20px;
    color:#555555;
">
Don't miss out on something created just for your interests.
Your personalized offer is waiting.
</p>

<div style="
    text-align:center;
    margin-top:25px;
">
<span style="
    background:#FF4D4D;
    color:white;
    padding:15px 30px;
    border-radius:30px;
    font-size:20px;
    font-weight:bold;
">
🛒 SHOP NOW
</span>
</div>

<p style="
    text-align:center;
    margin-top:20px;
    color:#777777;
    font-size:14px;
">
Limited Time Offer • Personalized For You
</p>

</div>
"""