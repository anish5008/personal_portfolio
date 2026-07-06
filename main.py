from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/experience')
def experience():
    experiences = [
        {
            "date": "Jan 2026 - Present",
            "title": "Current Internship",
            "company": "Building-U",
            "desc": "Contributing to technical projects, environmental sustainability and support on the business team."
        },
        {
            "date": "Summer 2025",
            "title": "Summer Cohort Scholar",
            "company": "Girls Who Code",
            "desc": "Immersive study in software engineering frameworks, web development cycles, and collaborative project management."
        },
        {
            "date": "2025",
            "title": "Hackathon Participant",
            "company": "HackClub Campfire",
            "desc": "Designed, built, and shipped functional game under intense sprint deadlines during the global campfire hackathon."
        },
        {
            "date":"11th Grade (first half)",
            "title": "Volunteer Art Tutor",
            "company": "Addarsh After School Academy",
            "desc": "Designed creative instructional plans and mentored young students in foundational sketching and painting techniques."
        },
        {
            "date": "2025",
            "title": "AI Skills Fest Badge Winner",
            "company": "Microsoft",
            "desc": "Earned official credentialing in foundational artificial intelligence concepts and core machine learning paradigms."
        }
    ]
    return render_template('experience.html', experiences=experiences)

@app.route('/awards')
def awards_page():
    journalism = [
        {"title": "Author & Poet",
         "detail": "Poem 'Drifting Apart' published by Live Poets Society of NJ (Summer 2025)"},
        {"title": "Financial Literacy Author",
         "detail": "Published 'A Lazy Teen’s Guide to Save Money' – financial advice tailored for Gen Z."},
        {"title": "Founder",
         "detail": "Beyond Books Literary Magazine – Managed and organized international digital distribution."}
    ]

    competitions = [
        {"title": "Two-Time Winner", "detail":"Deck the Bins Art Competition | 72 regional winners selected out of 400 entries in 2025 and 72 regional winners selected out of 300 entries in 2026."},
        {"title":"3rd Place Regional Winner", "detail":"North Florida Tamil Sangam's First-Ever Kolam Competition | Celebrated for intricate traditional visual art layout."},
        {"title":"State Qualifier","detail": "FBLA (Future Business Leaders of America)"},
        {"title": "State Fine Art Competitor",
         "detail": "State Level Drawing Competition hosted at the Nexus Mall in Chennai, India."},
        {"title": "Selected Photographer",
         "detail": "Honored as a featured portfolio selection in the Junior Photography Competition."},
        {"title": "Cultural Fine Art Winner",
         "detail": "Earned a Special Mention in the Jacksonville Tamil Mandram Pongal Drawing Competition."}
    ]

    honors = [
        {"title":"Borlaug Scholar", "detail":"World Food Prize Academic Honor Metric for research into global food security infrastructure."},
        {"title": "Florida Seal of Biliteracy", "detail":"Awarded by the state for high advanced fluency in Tamil (May 2026)"}
    ]

    return render_template('awards.html', journalism=journalism, competitions=competitions, honors=honors)

@app.route('/skills')
@app.route('/skills')
def skills():
    technical_skills = [
        "Python", "Java", "HTML5 & CSS3", "Flask",
        "Data Science & Analytics", "Prompt Engineering", "Machine Learning Core"
    ]

    return render_template('skills.html',
                               technical_skills=technical_skills)

@app.route('/hobbies')
def hobbies():
    dance_performances = [
        {"event": "School Multicultural Showcase", "type": "Double Feature Performance",
         "desc": "Choreographed and executed two distinct routines with modern K-Pop and traditional Tamil Classical dance movements."},
        {"event": "CSX Company Asian Heritage Celebration", "type": "Guest Performance",
         "desc": "Invited to perform a dynamic Bollywood dance arrangement celebrating regional heritage and diversity."},
        {"event": "Jacksonville Tamil Mandram", "type": "Community Arts Feature",
         "desc": "Coordinated and performed custom cultural choreography for local community assemblies."}
    ]
    creative_hobbies = [
        {"title": "Canvas Painting & Fine Arts",
         "desc": "Focus on multiple canvas works using acrylic and sketch mediums, turning imaginative concepts into physical pieces."},
        {"title": "Fitness, Strength Training & Pilates",
         "desc": "Committed to personal physical development, utilizing structured strength training and pilates workouts to build focus and stamina."},
    ]
    return render_template('hobbies.html', dance_performances=dance_performances, creative_hobbies=creative_hobbies)

@app.route('/achievements')
def achievements():
    cords_and_societies = [
        {"title": "National Art Honor Society (NAHS) Secretary",
         "desc": "Elected officer handling  logistics and communications"},
        {"title": "Honor Cord Recipients",
         "desc": "Earned active distinction graduation cords for National Honor Society (NHS), National English Honor Society (NEHS), National Arts Honor Society (NAHS), Best Buddies and Key Club."},
        {"title": "Robotics Club Fundraising Manager",
         "desc": "Led events to cumulate community sponsorships to secure a critical $1,500 rookie team operational budget."}
    ]
    activities = [
        {"title": "JRC Team Captain", "time": "9th & 10th Grade",
         "desc": "Led structural drill, and physical training as an appointed organizational student captain."},
        {"title": "Road Safety Patrol Member", "time": "11th Grade",
         "desc": "Managed environmental safety procedures for campus security operations."},
        {"title": "Business Clubs", "time": "High School",
         "desc": "Competed and trained within the Future Business Leaders of America (FBLA) and DECA business management programs."},
        {"title": "Best Buddies Chapter Member", "time": "High School",
         "desc": "Volunteered in peer support systems dedicated to enhancing inclusive global student communities."},
        {"title": "School Plays", "time": "9th & 10th Grade",
         "desc": "Performed lead dramatic roles in two major high school stage productions: an original play detailing the 'Miracles of Jesus' and William Shakespeare's 'The Tempest'."},
        {"title": "Long Distance Endurance Runner", "time": "High School",
         "desc": "Conquered supreme physical limits by finishing the Donna Half Marathon (13.1 Miles) among other smaller races"}
    ]
    return render_template('achievements.html', cords_and_societies=cords_and_societies, activities=activities)

if __name__ == '__main__':
    app.run(debug=True)


