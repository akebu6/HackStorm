import streamlit as st
import pandas as pd

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

DEVELOPER_KEY = 'YOUR_DEVELOPER_KEY'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

st.title("Resources to help you get started")
st.write("Here are some resources to help you get started with your hackathon project.")

st.write('---')

# YouTube search
def youtube_search(options, max_results=11):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    part="snippet",
    q=options,
    type="video",
    maxResults=max_results
  )
  
  response = search_response.execute()
  return response.get("items", [])

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.

def main():
  search_query = st.text_input("Search for a video", placeholder="Search any video")
  
  if st.button('Search'):
    results = youtube_search(search_query)
    
    df = pd.DataFrame(
      {
        
        'Title': [result['snippet']['title'] for result in results],
        'Description': [result['snippet']['description'] for result in results],
        'Link': [f"https://www.youtube.com/watch?v={result['id']['videoId']}" for result in results],
      }
    )
    
    st.dataframe(df)

if __name__ == "__main__":
    main()

st.write('---')
st.header("Video Tutorials")
# Video container
with st.container():
  video1, video2 = st.columns(2)
  video3, video4 = st.columns(2)
  
  video1.video('https://www.youtube.com/watch?v=9cKsq14Kfsw')
  video1.markdown('Responsive Bootstrap Website Start To Finish with Bootstrap 4, HTML5 & CSS3')
  video2.video('https://www.youtube.com/watch?v=NNeT-PhaLZk')
  video2.markdown('Responsive Bootstrap Website Start To Finish with Bootstrap 4, HTML5 & CSS3')
  video3.video('https://www.youtube.com/watch?v=EA3X_CtIjFo')
  video3.markdown('Python Machine Learning Projects For Beginners 2023 | Machine Learning With Python | Simplilearn')
  video4.video('https://youtu.be/-6K6-qQrIWc')
  video4.markdown('Python Machine Learning Projects For Beginners 2023 | Machine Learning With Python | Simplilearn')
  
st.write('---')

st.header("Blogs")
st.text_input("Search for a blog", placeholder="Press Enter")

with st.container():
  blog1, blog2 = st.columns(2)
  blog3, blog4 = st.columns(2)
  
  with blog1:
    st.image('https://www.boardinfinity.com/blog/content/images/2022/04/Recent-Blog-Creatives---Pepper--15--1.png')
    st.markdown('Top 10 Prize-Winning Hackathon Project Ideas')
    st.markdown('[Read more](https://www.boardinfinity.com/blog/top-10-prize-winning-hackathon-project-ideas-3/)')
    
  with blog2:
    st.image('https://camo.githubusercontent.com/456a68969501b1efbb80f5a297574abc71ce0d0028fda1f285b358c626e703fd/68747470733a2f2f6d656469612e6973746f636b70686f746f2e636f6d2f766563746f72732f6861636b6174686c6f6e2d766563746f722d696c6c757374726174696f6e2d74696e792d70726f6772616d6d6572732d636f6d7065746974696f6e2d706572736f6e2d766563746f722d6964313138393837333835313f6b3d36266d3d3131383938373338353126733d3631327836313226773d3026683d5551564457466f62565848746349795f314f374a55456a456f64705952467361696436482d3242687262633d')
    st.markdown('Awesome hackathon projects')
    st.markdown('[Read more](https://github.com/Olanetsoft/awesome-hackathon-projects)')  
   
with blog3:
    st.image('https://www.techcareer.net/_next/image?url=https%3A%2F%2Fcdn.gcp.techcareer.net%2FHackathon_lar_Icin_13_Ilginc_Fikir_57e36ead30%2FHackathon_lar_Icin_13_Ilginc_Fikir_57e36ead30.jpg&w=1200&q=75')
    st.markdown('13 Interesting Ideas for Hackathons')
    st.markdown('[Read more](https://www.techcareer.net/en/blog/hackathon-lar-icin-13-ilginc-fikir)') 
     
with blog4:
    st.image('https://d3njjcbhbojbot.cloudfront.net/api/utilities/v1/imageproxy/https://images.ctfassets.net/wp1lcwdav1p1/b2mlsGI3LyFqNoenyNpGD/f1ec8b37b56da9905ee774c6b6f18ec4/data_analyst_projects.png?w=1500&h=680&q=60&fit=fill&f=faces&fm=jpg&fl=progressive&auto=format%2Ccompress&dpr=3&w=1000&h=')
    st.markdown('5 Data Analytics Projects for Beginners')
    st.markdown('[Read more](https://www.coursera.org/articles/data-analytics-projects-for-beginners)')   
    
   