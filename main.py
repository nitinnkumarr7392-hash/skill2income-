from flask import Flask, render_template, request

app = Flask(__name__)

def generate_plan(skill):
    skill = skill.lower()

    if "video" in skill:
        return {
            "platforms": "YouTube, Instagram Reels, Fiverr",
            "earning": "₹15,000 - ₹60,000 per month",
            "plan": "Day 1-7: Editing practice\nDay 8-15: Create 5 sample videos\nDay 16-25: Start freelancing\nDay 26-30: Client outreach daily"
        }

    elif "coding" in skill or "programming" in skill:
        return {
            "platforms": "Upwork, Freelancer, GitHub Sponsors",
            "earning": "₹25,000 - ₹1,00,000 per month",
            "plan": "Day 1-7: Build 2 small projects\nDay 8-15: Create portfolio\nDay 16-25: Apply to 10 jobs daily\nDay 26-30: Improve advanced skills"
        }

    elif "design" in skill:
        return {
            "platforms": "99Designs, Fiverr, Canva Marketplace",
            "earning": "₹20,000 - ₹80,000 per month",
            "plan": "Day 1-7: Practice design basics\nDay 8-15: Create 10 sample designs\nDay 16-25: Upload on platforms\nDay 26-30: Start pitching clients"
        }

    else:
        return {
            "platforms": "Fiverr, Upwork, YouTube",
            "earning": "₹10,000 - ₹50,000 per month",
            "plan": "Day 1-7: Improve your skill\nDay 8-15: Create sample work\nDay 16-25: Upload online\nDay 26-30: Daily outreach"
        }

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        skill = request.form["skill"]
        data = generate_plan(skill)
        return render_template("result.html", skill=skill, data=data)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
