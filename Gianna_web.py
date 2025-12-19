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
       st.image("https://share.google/MnG7T5CmOGhRFThmx.jpg",caption="Test project",use_column_width=True)

    with col2:
        st.subheader('🛒 E-Commerce Price Tracker')
        st.write('Python web scraper that monitors Amazon prices and sends alerts')
        st.caption('**Technologies:** Phone, Ipad, Computer')


  # Project 2 
  with st.container():
    col1, col2 = st.columns([1,2])
    with col1:
      st.image("https://share.google/TPL7F66j0Nnreze1K", use_column_width=True)
    use_column_width=True)
    with col2:
      st.subheader('📊 Student Grade Calulator')
      st.write('Interactive web app for calculating and visualizing grades')
      st.caption('**Technologies:** Python, Pandas, Plotly')

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
  with open('file:///C:/Users/Gianna.Woods/Downloads/Gianna%20N.%20Woods%20resum%C3%A8.docx.pdf') as pdf_file:
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
    



      
