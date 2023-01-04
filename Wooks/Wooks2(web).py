import streamlit as st
from streamlit_webrtc import (webrtc_streamer)
import OpenSSL
import requests
import av


rs = requests.get("http://localhost:8501/", verify=False)

webrtc_streamer(key="1")
    





