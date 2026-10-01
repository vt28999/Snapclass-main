import streamlit as st
from src.screens.home_screens import home_screens
from src.screens.student_screens import student_screens
from src.screens.teacher_screens import teacher_screens


def main():

      if 'login_type' not in st.session_state:
            st.session_state['login_type'] = None



      match st.session_state['login_type']: 
            case 'teacher':
                  teacher_screens() 
            case 'student':
                  student_screens()  
            case None:
                  home_screens()             

main()