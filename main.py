from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/experience')
def experience_page():
    experiences = [
        {"role": "Current internship", "company": "Building-U", "date": "Jan 2026 - Present"},
        {"role": "Summer Cohort", "company": "Girls Who Code", "date": "Summer 2025"},
        {"role": "participant", "company": "HackClub campfire hackathon", "date": "2025"}
    ]
    return render_template('experience.html', experiences=experiences)

@app.route('/awards')
def awards_page():
    awards = [
        {"title": "two-time winner", "context": "Deck the Bins art competition", "tag": "🏆 2025 & 2026"},
        {"title": "Founder", "context": "Beyond Books Literary Magazine", "tag": ""},
        {"title": "Borlaug Scholar", "context": "Academic and Honor metrix", "tag": ""}
    ]
    return render_template('awards.html', awards=awards)

@app.route('/skills')
def skills_page():
    skills = [
        "Python (Intermediate)",
        "Java",
        "JavaScript",
        "HTML & CSS",
        "Intro to Data Science",
        "Prompt Engineering"
    ]
    return render_template('skills.html', skills=skills)

if __name__ == '__main__':
    app.run(debug=True)





