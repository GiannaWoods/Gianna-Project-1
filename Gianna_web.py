import streamlit as st
import pandas as pd 
from datetime import datetime

# Page Config
st.set_page_config(
  page_title ='Gianna Woods | Portfolio',
  page_icon='💕',
  layout = 'wide'
)

# Custom CSS (optional - for styling)
st.markdown('''
                <style>
                    .main-header {font-size: 42px; font-weight: bold; text-align:center;}
                    .sub-header {font-size: 24px; text-align:center; color: #666;}
                </style>
            ''', unsafe_allow_html = True)

# Sidebar
st.sidebar.title('📍 Navigation')
page = st.sidebar.radio('Go to',
                        ['🏠 Home', '🤠 About', '💼 Projects', '🛠 Skills' ,'📝 Resume', '📩 Contact' ])

# Home Page
if page == '🏠 Home':
  st.markdown('<p class="main-header">Gianna Woods</p>', unsafe_allow_html=True)
  st.markdown('<p class="sub-header">Student| Medgar Evers College</p>', unsafe_allow_html=True)

  # Three Columns for stats
  col1, col2, col3 = st.columns(3)

  with col1:
      st.metric('GPA', '3.0', '📝')
  with col2:
      st.metric('Projects', '7', '🏫')
  with col3:
      st.metric('Skills', '9', '🤖')

  st.write('---')

  # Introduction with columns
  col1, col2 = st.columns([2,1])
  with col1:
    st.subheader('Welcome to my webpage🌸')
    st.write('''
                I am a student at Medgar Evers College studying Management, Computer science,as well as Business.
                I'm studying these courses to develop my own world wide business one day. 
               
                🌏 **Current Focus:** Building a worldwide business
                
               💹 **Currently Learning:**Business Administration
                 🏝️ **Fun Fact:** I love to travel
            ''')
    with col2:             
        # Placeholder for image
        st.image("https://cdn.pixabay.com/photo/2024/12/09/22/27/cat-9256270_640.png", use_column_width=True)

    # About Page
elif page == '🤠 About':
  st.title('About Me')

 # Timeline of my Professional Journey
  st.subheader('My Journey 🗺️')

  with st.expander('2024 - Present: Medgar Evers College'):
    st.write('''
                - Major: Business Administration
                - Relevant Coursework: Internet & Emerging Technologies,Management, English, And business
                - Activities: Dance team
            ''')

  with st.expander('2014 - 2018: Brooklyn High School '):
    st.write('''
                - Graduated with a GPA of 4.0
                - AP History A (Score: 8)
                - Captain Of dance team 
            ''')

  st.subheader('Interests & Hobbies 💃🏼')
  interests = ['Hairstylist', 'Dance Teacher', 'Videography', 'Gymnastics', 'Travel', 'Vollyball']

  # Display the interests in columns
  cols = st.columns(3)
  for i, interest in enumerate(interests):
    with cols[i % 3]:
      st.info(f'🔷 {interest}')
      
elif page == '💼 Projects':
  st.title('My Projects')
  st.write('Here are some projects I have worked on:')

  # Project 1
  with st.container():
    col1, col2 = st.columns([1, 2])
  
    with col1:
       st.image('top-view-green-painted-rock-turtle-white-table-art-supplies-brushes-gouache-paints-children-project-diy-concept-step-385703898.jpg')

    with col2:
        st.subheader('🐢Snapping Turtle-clay study')
        st.write('Clay sculpture study exploring instinct, protection,and form.')
        st.caption('**clay,Food coloring')


  # Project 2 
  with st.container():
    col1, col2 = st.columns([1,2])
    with col1:
      st.image('1-BIG_FimagePROJ114.jpg', use_column_width = True)
     
    with col2:
      st.subheader('🗿Architectural Study')
      st.write('Mixed media exploration of balance, space, and constructed form.')
      st.caption('**Cardboard and paper')

elif page == '🛠 Skills':
  st.title('Technical Skills')

  # Skills with progress bars
  st.subheader('Programming Languages')

  skills_data = {
    'Python' : 85,
    'HTML/CSS' : 70,
    'JavaScript' : 60,
    'SQL' : 50,
    'Technical Writing' : 40
  }

  for skill, level in skills_data.items():
    col1, col2 = st.columns([1,3])
    with col1:
      st.write(skill)
    with col2:
      st.progress(level/100)

  st.subheader('Tools & Technologies')

  col1, col2, col3 = st.columns(3)
  with col1:
    st.success('Facebook')
    st.info('TikTok')
    st.warning('Google Drive')

  with col2:
    st.success('PowerPoint')
    st.info('Instagram')
    st.warning('Google Docs')
    
  with col3:
    st.success('Presentations')
    st.info('CNN')
    st.warning('Twitter')

elif page == '📝 Resume':
  st.title('Resume')

  # Read PDF from my GitHub repository
  with open('<html><head><meta content="text/html; charset=UTF-8" http-equiv="content-type"><style type="text/css">@import url(https://themes.googleusercontent.com/fonts/css?kit=RFda8w1V0eDZheqfcyQ4EGb3DKsRMD34dqg1gT8Z-p6isjtAVhoKeKPV_uAAgBOSk3k702ZOKiLJc3WVjuplzPesZW2xOQ-xsNqO47m55DA);ol{margin:0;padding:0}table td,table th{padding:0}.c15{border-right-style:solid;padding:7.2pt 7.2pt 7.2pt 7.2pt;border-bottom-color:#000000;border-top-width:0pt;border-right-width:0pt;border-left-color:#000000;vertical-align:top;border-right-color:#000000;border-left-width:0pt;border-top-style:solid;border-left-style:solid;border-bottom-width:0pt;width:358.5pt;border-top-color:#000000;border-bottom-style:solid}.c13{border-right-style:solid;padding:7.2pt 7.2pt 7.2pt 7.2pt;border-bottom-color:#000000;border-top-width:0pt;border-right-width:0pt;border-left-color:#000000;vertical-align:top;border-right-color:#000000;border-left-width:0pt;border-top-style:solid;border-left-style:solid;border-bottom-width:0pt;width:165pt;border-top-color:#000000;border-bottom-style:solid}.c16{color:#2079c7;font-weight:700;text-decoration:none;vertical-align:baseline;font-size:9pt;font-family:"Open Sans";font-style:normal}.c5{color:#666666;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:12pt;font-family:"Merriweather";font-style:normal}.c3{color:#666666;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:9pt;font-family:"Merriweather";font-style:normal}.c23{color:#000000;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:9pt;font-family:"Open Sans";font-style:normal}.c19{color:#3d85c6;font-weight:700;text-decoration:none;vertical-align:baseline;font-size:9pt;font-family:"Merriweather";font-style:normal}.c28{color:#3d85c6;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:9pt;font-family:"Merriweather";font-style:normal}.c11{color:#000000;font-weight:700;text-decoration:none;vertical-align:baseline;font-size:9pt;font-family:"Open Sans";font-style:normal}.c22{color:#ffffff;font-weight:700;text-decoration:none;vertical-align:baseline;font-size:9pt;font-family:"Merriweather";font-style:normal}.c20{color:#6fa8dc;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:9pt;font-family:"Merriweather";font-style:normal}.c4{color:#666666;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:6pt;font-family:"Merriweather";font-style:normal}.c10{color:#000000;font-weight:700;text-decoration:none;vertical-align:baseline;font-size:36pt;font-family:"Merriweather";font-style:normal}.c8{color:#666666;font-weight:700;text-decoration:none;vertical-align:baseline;font-size:12pt;font-family:"Merriweather";font-style:normal}.c12{color:#666666;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:11pt;font-family:"Merriweather";font-style:normal}.c1{padding-top:30pt;padding-bottom:0pt;line-height:1.0;text-align:left;margin-right:15pt;height:24pt}.c14{padding-top:30pt;padding-bottom:0pt;line-height:1.0;text-align:left;margin-right:15pt}.c21{padding-top:0pt;padding-bottom:6pt;line-height:1.0;text-align:left;margin-right:15pt}.c26{padding-top:6pt;padding-bottom:0pt;line-height:1.0;text-align:left;margin-right:15pt}.c17{padding-top:0pt;padding-bottom:0pt;line-height:1.1500000000000001;text-align:left;margin-right:15pt}.c7{padding-top:0pt;padding-bottom:0pt;line-height:1.0;text-align:left;margin-right:15pt}.c2{padding-top:6pt;padding-bottom:0pt;line-height:1.3;text-align:left;margin-right:15pt}.c25{padding-top:16pt;padding-bottom:0pt;line-height:1.3;text-align:left;margin-right:15pt}.c6{padding-top:16pt;padding-bottom:0pt;line-height:1.0;text-align:center;margin-right:15pt}.c0{border-spacing:0;border-collapse:collapse;margin-right:auto}.c29{background-color:#ffffff;max-width:525.6pt;padding:28.8pt 43.2pt 43.2pt 43.2pt}.c24{height:80pt}.c9{height:9pt}.c27{color:#b7b7b7}.c18{height:588pt}.title{padding-top:0pt;color:#000000;font-weight:700;font-size:36pt;padding-bottom:6pt;font-family:"Merriweather";line-height:1.0;text-align:left}.subtitle{padding-top:0pt;color:#000000;font-size:9pt;padding-bottom:0pt;font-family:"Open Sans";line-height:1.1500000000000001;text-align:left}li{color:#666666;font-size:9pt;font-family:"Merriweather"}p{margin:0;color:#666666;font-size:9pt;font-family:"Merriweather"}h1{padding-top:30pt;color:#2079c7;font-weight:700;font-size:9pt;padding-bottom:0pt;font-family:"Open Sans";line-height:1.0;text-align:left}h2{padding-top:16pt;color:#000000;font-weight:700;font-size:11pt;padding-bottom:0pt;font-family:"Merriweather";line-height:1.0;page-break-after:avoid;text-align:left}h3{padding-top:5pt;color:#666666;font-size:8pt;padding-bottom:5pt;font-family:"Open Sans";line-height:1.0;page-break-after:avoid;text-align:left}h4{padding-top:8pt;-webkit-text-decoration-skip:none;color:#666666;text-decoration:underline;text-decoration-skip-ink:none;font-size:11pt;padding-bottom:0pt;font-family:"Trebuchet MS";line-height:1.3;page-break-after:avoid;text-align:left}h5{padding-top:8pt;color:#666666;font-size:11pt;padding-bottom:0pt;font-family:"Trebuchet MS";line-height:1.3;page-break-after:avoid;text-align:left}h6{padding-top:8pt;color:#666666;font-size:11pt;padding-bottom:0pt;font-family:"Trebuchet MS";line-height:1.3;page-break-after:avoid;font-style:italic;text-align:left}</style></head><body class="c29 doc-content"><p class="c9 c26"><span class="c4"></span></p><table class="c0"><tr class="c24"><td class="c15" colspan="1" rowspan="1"><p class="c21 title" id="h.gjdgxs"><span class="c10">Gianna N. Woods</span></p><p class="c9 c17 subtitle" id="h.30j0zll"><span class="c23"></span></p></td><td class="c13" colspan="1" rowspan="1"><p class="c17"><span class="c11">CONTACT DETAILS</span></p><p class="c17"><span class="c11">Cell: 347-547-4056</span></p><p class="c17"><span class="c11">Email:giannawoods213@gmail.com</span></p></td></tr><tr class="c18"><td class="c15" colspan="1" rowspan="1"><h1 class="c1" id="h.1fob9te"><span class="c16"></span></h1><h1 class="c14" id="h.3znysh7"><span class="c16">EXPERIENCE</span></h1><p class="c2"><span class="c8">Private Babysitter</span></p><p class="c2"><span class="c3">2022-Present</span></p><p class="c2"><span class="c3">-Maintains daily schedule. </span></p><p class="c2"><span class="c3">-Keeps children&#39;s living and play areas tidy.</span></p><p class="c2"><span class="c3">-Provides structure and communicates consistent behavioral expectations.</span></p><p class="c2"><span class="c3">Assistant Dance Instructor</span></p><p class="c2"><span class="c8">St. Stephen Outreach 2020-Present</span></p><p class="c2"><span class="c3">-Assist in the design and purchasing of costumes for dance recitals and concerts</span></p><p class="c2"><span class="c3">-Choreograph performances and select music for dance recitals and concerts</span></p><h1 class="c14" id="h.2et92p0"><span>EDUCATION</span><span class="c27">&nbsp;</span></h1><p class="c7 c9"><span class="c12"></span></p><p class="c7"><span class="c5">Medgar Ever college</span></p><p class="c7"><span class="c12">2024-present</span></p><p class="c7 c9"><span class="c12"></span></p><p class="c7"><span class="c12">KIPP NYC College Prep High School</span></p><p class="c7"><span class="c3">Graduated 2024</span></p><p class="c7"><span class="c3">-Leadership Award</span></p><p class="c7"><span class="c3">-Certificate of Excellence in Leadership</span></p><p class="c7"><span class="c3">-Certificate of Excellence for Grit</span></p><p class="c7"><span class="c3">-Dance Award</span></p><p class="c7 c9"><span class="c3"></span></p><p class="c7"><span class="c5">KIPP AMP Middle School</span></p><p class="c7"><span class="c3">Class of 2020</span></p><p class="c7"><span class="c3">-Leadership Award</span></p><p class="c7"><span class="c3">-2nd Honors Academic Award</span></p><p class="c7"><span class="c3">-Certificate of Excellence</span></p><p class="c7"><span class="c3">-Dance Award</span></p><p class="c7"><span class="c3">-Voice Award</span></p><h1 class="c1" id="h.tyjcwt"><span class="c16"></span></h1></td><td class="c13" colspan="1" rowspan="1"><p class="c25"><span class="c20">MAIN &nbsp;INTERESTS</span></p><p class="c6"><span class="c3">- Fashion &amp; Design</span></p><p class="c6"><span class="c3">-Customer Service</span></p><p class="c6"><span class="c3">-Mathematics</span></p><p class="c6"><span class="c3">- Geometry</span></p><p class="c6"><span class="c3">-physics </span></p><p class="c6 c9"><span class="c3"></span></p><p class="c6 c9"><span class="c3"></span></p><p class="c6"><span class="c28">MAIN OBJECTIVE</span></p><p class="c6"><span class="c3">&bull; Reliable, mature, and creative Freshman In college seeking a part-time retail sales associate position in order to gain experience and insight into the fashion industry for a future career in fashion and design.</span></p><p class="c6 c9"><span class="c22"></span></p><p class="c6"><span class="c19">ACCOMPLISHMENTS</span></p><p class="c6"><span class="c3">- Middle School Dance Team Leader</span></p><p class="c6"><span class="c3">-High School Dance Team Captain</span></p><p class="c6"><span class="c3">-College dance team choreographer </span></p><p class="c6"><span class="c3">-Leadership Award Recipient</span></p><p class="c6 c9"><span class="c3"></span></p><p class="c6 c9"><span class="c3"></span></p></td></tr></table><p class="c2 c9"><span class="c3"></span></p></body></html>') as pdf_file:
    PDFbyte = pdf_file.read()
  
  st.download_button(
    label ='🔻 Download Full Resume (PDF)',
    data = PDFbyte,
    file_name = 'my_resume.pdf',
    mime ='application/pdf'
  )

elif page == '📩 Contact':
  st.title("Let's Connect!")

  col1, = st.columns(1)

  with col1:
    st.subheader('Send me a message.')

    st.write('''
        📧 **Email:**Giannawoods213@gmail.com
        
        🏢 **LinkedIn:** [linkedin.com/in/Gianna](https://linkedin.com)

        👩‍💻 **Github:** [https://github.com/Giannawoods](https://github.com)

        📷 **Instagram:** [@giaisthebest](https://instagram.com)

    ''')

    # Fun interative element
    st.subheader('Current Status')

    status = st.selectbox(
        "I'm currently:",
        [
            '👩‍💻 Coding',
            '📕 Studying',
            '🏢 Working',
            '👩🏼‍🏫 Teaching',
            '😴 Sleeping',
        ]
    )


    st.info(f'Status: {status}')

    # Footer
    st.write('---')
    st.markdown(
        f'<center>Made with 💗 using Streamlit | © {Datetime.now().year} Gianna Woods </center>',
        unsafe_allow_html = True
    )
    



      
