from flask import Flask, render_template_string

app = Flask(__name__)

page1 = """
<!DOCTYPE html>
<html>
<head>
  <title>Just One Question</title>
  <style>
    body {
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      background: linear-gradient(135deg, #ffdde1, #ee9ca7);
      font-family: 'Poppins', sans-serif;
    }
    .box {
      text-align: center;
    }
    h1 {
      font-size: 2.5rem;
      margin-bottom: 30px;
    }
    button {
      padding: 15px 30px;
      font-size: 1.1rem;
      border: none;
      border-radius: 30px;
      cursor: pointer;
      margin: 20px;
    }
    .yes {
      background: #ff4d6d;
      color: white;
    }
    .no {
      background: white;
      position: absolute;
    }
  </style>
</head>

<body>
  <div class="box">
    <h1>Do you love me? 💖</h1>
    <button class="yes" onclick="location.href='/yes'">Yes 😌</button>
    <button class="no" id="no">No 😏</button>
  </div>

  <script>
    const noBtn = document.getElementById("no");
    noBtn.addEventListener("mouseover", () => {
      const x = Math.random() * (window.innerWidth - 100);
      const y = Math.random() * (window.innerHeight - 50);
      noBtn.style.left = x + "px";
      noBtn.style.top = y + "px";
    });
  </script>
</body>
</html>
"""

page2 = """
<!DOCTYPE html>
<html>
<head>
  <title>Happy 24 Months</title>
  <style>
    body {
      min-height: 100vh;
      background: linear-gradient(135deg, #0f172a, #1e293b);
      color: white;
      display: flex;
      justify-content: center;
      align-items: center;
      font-family: 'Poppins', sans-serif;
      padding: 40px;
    }
    .card {
      background: rgba(255, 255, 255, 0.05);
      border-radius: 20px;
      padding: 40px;
      max-width: 900px;
      line-height: 1.7;
      box-shadow: 0 0 40px rgba(0,0,0,0.3);
    }
    h1 {
      text-align: center;
      margin-bottom: 25px;
      font-size: 2.4rem;
    }
    p {
      font-size: 1.05rem;
      margin-bottom: 15px;
      white-space: pre-line;
    }
    .heart {
      text-align: center;
      font-size: 2rem;
      margin-top: 20px;
    }
  </style>
</head>

<body>
  <div class="card">
    <h1>Dear Kaustubh,</h1>

    <p>
It’s 21st January.

Two years sounds simple when you say it fast, but we know it wasn’t.

These 24 months held laughter that felt like home, fights that taught us silence, distance that tested patience, and a phase where we let go… and umm thinking maybe that was the answer. For three months, we weren’t “us,” but somehow, we were still learning about us.

We didn’t break because we didn’t care.
We paused because we were growing faster than we understood ourselves and we were kiddsss—still are—and somewhere between missing, healing, and figuring life out, we chose each other again. Not out of habit, not out of fear, but with more clarity than before.

Being with you hasn’t been perfect, but it’s been real. You’ve seen me when I was overwhelmed, unavailable, trying to juggle dreams and deadlines. I know there were times you wanted more time, more presence, more of me—and I couldn’t always give it the way you deserved. But my heart never left, even when life pulled me in ten directions.

What I value most is that we didn’t pretend.
We communicated, we messed up, we learned.
We didn’t romanticize pain, and we didn’t run from it either.

Today isn’t about counting flawless days.
It’s about honoring growth.
About choosing honesty over ego.
About choosing us, again.

Thank you for staying, for understanding, for holding space for the version of me that’s still becoming. I don’t promise perfection, but I promise effort, respect, and truth.

Happy 24 months to us.

I love you so muchhhh & thank you for everything.
You are the mosttt important person in my life.
I love you smmmmm !! -Shrutika
    </p>

    <div class="heart">💖</div>
  </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(page1)

@app.route("/yes")
def yes():
    return render_template_string(page2)

if __name__ == "__main__":
    app.run(debug=True)
