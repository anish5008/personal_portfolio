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
            "desc": "Working on technical projects while helping with sustainability initiatives and supporting the business team."
        },
        {
            "date": "Summer 2025",
            "title": "Summer Cohort Scholar",
            "company": "Girls Who Code",
            "desc": "Learned software engineering, web development, and worked on projects with other students."
        },
        {
            "date": "2025",
            "title": "Hackathon Participant",
            "company": "HackClub Campfire",
            "desc": "Worked as a team of three to build a game from scratch."
        },
        {
            "date":"11th Grade (first half)",
            "title": "Volunteer Art Tutor",
            "company": "Addarsh After School Academy",
            "desc": "Helped younger students improve their drawing and painting skills by planning simple art lessons."
        },
        {
            "date": "2025",
            "title": "AI Skills Fest Badge Winner",
            "company": "Microsoft",
            "desc": "Completed the AI Skills Fest program and earned a badge for learning the basics of AI and machine learning."
        }
    ]
    return render_template('experience.html', experiences=experiences)

@app.route('/awards')
def awards_page():
    journalism = [
        {
            "title": "Author & Poet",
            "detail": "My poem 'Drifting Apart' was published by Live Poets Society of New Jersey in 2025"
        },
        {
            "title": "Financial Literacy Author",
            "detail": "Wrote and published 'A Lazy Teen’s Guide to Save Money' on an online magazine to help teens learn basic money management."
        },
        {
            "title": "Founder",
            "detail": "Started Beyond Books Literary Magazine and helped organize and share student writing online."
        }
    ]

    competitions = [
        {
            "title": "Two-Time Winner",
            "detail": "Won the Deck the Bins Art Competition in both 2025 and 2026 as one of 72 regional winners."
        },
        {
            "title": "3rd Place Regional Winner",
            "detail": "Placed third in the North Florida Tamil Sangam's first Kolam Competition."
        },
        {
            "title": "State Qualifier",
            "detail": "Qualified for the Florida FBLA State Leadership Conference."
        },
        {
            "title": "State Fine Art Competitor",
            "detail": "Competed in a state-level drawing competition held at Nexus Mall in Chennai."
        },
        {
            "title": "Selected Photographer",
            "detail": "My photography was chosen to be featured in the Junior Photography Competition."
        },
        {
            "title": "Cultural Fine Art Winner",
            "detail": "Received a Special Mention award in the Jacksonville Tamil Mandram Pongal Drawing Competition."
        }
    ]

    honors = [
        {
            "title":"Borlaug Scholar",
            "detail":"Recognized by the World Food Prize Foundation for learning about global food security."
        },
        {
            "title": "Florida Seal of Biliteracy",
            "detail":"Awarded by the state for advanced fluency in Tamil (May 2026)"
        }
    ]

    return render_template('awards.html', journalism=journalism, competitions=competitions, honors=honors)

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
        {
            "event": "School Multicultural Showcase",
            "type": "Double Feature Performance",
            "desc": "Performed two dances that combined K-pop and traditional Tamil dance styles."
        },
        {
            "event": "CSX Company Asian Heritage Celebration",
            "type": "Guest Performance",
            "desc": "Performed a Bollywood dance to celebrate Asian Heritage Month."
        },
        {
            "event": "Jacksonville Tamil Mandram",
            "type": "Community Arts Feature",
            "desc": "Performed cultural dance routines at community events."
        }
    ]
    creative_hobbies = [
        {
            "title": "Canvas Painting & Fine Arts",
            "desc": "I enjoy painting with acrylics and sketching different ideas whenever I have free time."
        },
        {
            "title": "Fitness, Strength Training & Pilates",
            "desc": "I like staying active through strength training, running, and Pilates to improve my fitness."
        }
    ]
    return render_template('hobbies.html', dance_performances=dance_performances, creative_hobbies=creative_hobbies)

@app.route('/achievements')
def achievements():
    cords_and_societies = [
        {
            "title": "National Art Honor Society (NAHS) Secretary",
            "desc": "Helped organize meetings, communicate with members, and support club activities."
        },
        {
            "title": "Honor Cord Recipient",
            "desc": "Earned graduation cords through participation in NHS, NEHS, NAHS, Best Buddies, and Key Club."
        },
        {
            "title": "Robotics Club Fundraising Manager",
            "desc": "Helped organize fundraisers that raised about $1,500 for our rookie robotics team."
        }
    ]
    activities = [
        {
            "title": "JRC Team Captain",
            "time": "9th & 10th Grade",
            "desc": "Led drill practice and physical training while helping organize the team."
        },
        {
            "title": "Road Safety Patrol Member",
            "time": "11th Grade",
            "desc": "Helped students stay safe around the school during arrival and dismissal."
        },
        {
            "title": "Business Clubs",
            "time": "High School",
            "desc": "Participated in FBLA and DECA competitions and learned about business and leadership."
        },
        {
            "title": "Best Buddies Chapter Member",
            "time": "High School",
            "desc": "Took part in activities that encouraged inclusion and friendship for students with disabilities."
        },
        {
            "title": "School Plays",
            "time": "9th & 10th Grade",
            "desc": "Acted in two school productions, including a play about the Miracles of Jesus and Shakespeare's 'The Tempest.'"
        },
        {
            "title": "Long Distance Runner",
            "time": "High School",
            "desc": "Completed the Donna Half Marathon (13.1 miles) and participated in several other races."
        }
    ]

    return render_template('achievements.html', cords_and_societies=cords_and_societies, activities=activities)

if __name__ == '__main__':
    app.run(debug=True)


