import streamlit as st
from src.screens.home_screens import home_screens
from src.screens.student_screens import student_screens
from src.screens.teacher_screens import teacher_screens

from src.components.dialog_auto_enroll import auto_enroll_dialog

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



      join_code = st.query_params.get('join-code')
      if join_code:
            if st.session_state.login_type != 'student':
                st.session_state.login_type = 'student'
                st.rerun()

            if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
                 auto_enroll_dialog(join_code)    
main()