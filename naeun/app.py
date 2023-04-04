from tkinter.tix import COLUMN
from pyparsing import empty
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.set_page_config(layout="wide")

empty1,con1,empty2 = st.columns([0.5,0.7,0.5])
empty1,con2,empty2 = st.columns([0.2,1.0,0.2])
# empyt1,con2,con3,empty2 = st.columns([0.1,0.1,1.0,0.1])
empyt1,con3,empty2 = st.columns([0.1,1.0,0.1])
empyt1,con4,empty2 = st.columns([0.1,1.0,0.1])
empyt1,con5,con6,empty2 = st.columns([0.1,1.0,1.0,0.1])

def main() :

    with empty1 :
        empty() # 여백부분1
   
    with con1 :
        st.image('img/zoom_50.gif') # ('img/zoom-zooooom_resize.gif')

    with con2 :
        st.image("img/logo.png")

    with con3 :
        st.sidebar.image("img/side_logo2.png", width= 400, use_column_width=False)
        st.sidebar.image("img/madeby2.png", width= 150, use_column_width=False)
        st.sidebar.markdown("---")
        st.sidebar.header("Main")
      

    with con4 :
        st.subheader("코로나19와 비대면 원격 수업")
        st.write("신종 코로나바이러스 감염증(코로나19)으로 비대면 원격 서비스 활용이 늘어나면서, <멋쟁이사자처럼 AIS> 7기 수업 역시 줌(Zoom)을 통한 온라인 수업으로 진행되고 있습니다.")
        st.write("이런 온라인 강의는 대부분 관리 효율성을 위해 어느 정도 모니터링이 필요하며, 7기 수강생들 역시 모니터링 매니저님 덕분에 수업 집중도를 높일 수 있었습니다.")
        st.write("하지만 모니터링 매니저님 혼자서 다수의 줌 화면을 확인하는 데는 피로도가 높을 것으로 판단하였고, 저희 팀은 모니터링 매니저님의 업무 효율성을 높일 수 있는, <온라인 화상 수업 서포팅 프로그램> 을 프로젝트 주제로 선정했습니다.")
        st.image("img/주제_선정_배경_resize.png")

    with con5 :
        video_file = open('img/final.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
     
    with con6 :
        st.markdown("자리비움 탐지 시연 영상")
        st.markdown("while문으로 구현된 웹캠이 실행되면, 인물 탐지를 시작합니다.")
        st.markdown("6초간 자리비움이 탐지되면 '□회 자리비움' 로그가 남겨집니다.")
        st.markdown("자리비움 기준은 사용자 지정이 가능합니다.")

    with empty2 :
        empty() # 여백부분2
        
if __name__ == "__main__":
    main()