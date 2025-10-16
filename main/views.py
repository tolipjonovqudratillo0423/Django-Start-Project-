from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def html_code(request):
    return HttpResponse("""
<!-- templates/response.html -->
<!doctype html>
<html lang="uz">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>{{ title|default:"Sahifa" }}</title>
  <style>
    /* Minimal, professional styling — no libs required */
    :root{
      --bg:#0f1724; --card:#0b1220; --muted:#9aa4b2; --accent:#06c; --success:#16a34a; --danger:#ef4444;
      --glass: rgba(255,255,255,0.03);
      font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    }
    html,body{height:100%;margin:0;background:linear-gradient(180deg,#071020 0%, #0b1524 100%);color:#e6eef8}
    .container{max-width:900px;margin:40px auto;padding:28px;background:var(--card);border-radius:14px;box-shadow:0 8px 30px rgba(2,6,23,0.6)}
    header{display:flex;align-items:center;justify-content:space-between;margin-bottom:18px}
    h1{font-size:20px;margin:0}
    p.lead{color:var(--muted);margin:6px 0 0;font-size:14px}
    .banner{padding:10px 14px;border-radius:10px;margin:16px 0;display:flex;gap:12px;align-items:center}
    .success{background:linear-gradient(90deg, rgba(22,163,74,0.12), rgba(22,163,74,0.04));border:1px solid rgba(22,163,74,0.12);color:var(--success)}
    .error{background:linear-gradient(90deg, rgba(239,68,68,0.08), rgba(239,68,68,0.02));border:1px solid rgba(239,68,68,0.08);color:var(--danger)}
    .muted{color:var(--muted);font-size:13px}
    ul.items{list-style:none;padding:0;margin:12px 0 0;display:grid;gap:8px}
    ul.items li{background:var(--glass);padding:12px;border-radius:8px;display:flex;justify-content:space-between;align-items:center}
    .meta{font-size:13px;color:var(--muted)}
    form.inline{display:flex;gap:8px;align-items:center;margin-top:14px}
    input[type="text"]{padding:8px 10px;border-radius:8px;border:1px solid rgba(255,255,255,0.06);background:transparent;color:inherit}
    button{padding:8px 12px;border-radius:8px;border:none;background:var(--accent);color:white;cursor:pointer}
    footer{margin-top:20px;color:var(--muted);font-size:13px;text-align:right}
    .kbd{background:#071826;padding:6px 8px;border-radius:6px;font-size:12px;color:var(--muted)}
  </style>
</head>
<body>
  <div class="container" role="main" aria-labelledby="page-title">
    <header>
      <div>
        <h1 id="page-title">{{ title|default:"Xabarnoma" }}</h1>
        <p class="lead">{{ subtitle|default:"Soddaligi. Ma'nosi. Amaliyoti." }}</p>
      </div>
      <div class="meta">Request ID: <span class="kbd">{{ request_id|default:"—" }}</span></div>
    </header>

    {# Success / Error banners (use when set in context) #}
    {% if success %}
      <div class="banner success" role="status">{{ success }}</div>
    {% endif %}
    {% if error %}
      <div class="banner error" role="alert">{{ error }}</div>
    {% endif %}

    {# Main message area #}
    <section aria-label="message">
      <p class="muted">{{ message|default:"Bu sahifa serverdan kelgan javobni semantik va tartibli ko‘rsatadi. Kontekst orqali title, message va items uzatiladi." }}</p>
    </section>

    {# Example list rendered from context.items #}
    {% if items %}
      <h2 style="margin-top:18px;font-size:15px">Top items</h2>
      <ul class="items" aria-live="polite">
        {% for it in items %}
          <li>
            <div>
              <strong>{{ forloop.counter }}. {{ it.name }}</strong>
              <div class="muted">{{ it.desc|default:"Ta'rif mavjud emas" }}</div>
            </div>
            <div class="muted">{{ it.meta|default:"—" }}</div>
          </li>
        {% endfor %}
      </ul>
    {% else %}
      <p class="muted" style="margin-top:12px">Hali items topilmadi. Yoki server context.items yubormadi.</p>
    {% endif %}

    {# Simple form to accept input (CSRF included) #}
    <form method="post" class="inline" action="{% url 'submit_item' %}">
      {% csrf_token %}
      <input name="name" type="text" placeholder="Nomi" required />
      <input name="desc" type="text" placeholder="Qisqacha ta'rif (ixtiyoriy)" />
      <button type="submit">Qo‘shish</button>
    </form>

    <footer>
      <span class="muted">Server time:</span> <strong>{{ server_time|default:"—" }}</strong>
    </footer>
  </div>
</body>
</html>
""")