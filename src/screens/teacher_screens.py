import streamlit as st

from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard

from src.database.db import check_teacher_exists, create_teacher, supabase, check_pass



def teacher_screens():

    style_background_dashboard()
    style_base_layout()

    if "teacher_data" in st.session_state:
        teacher_dasboard()

    elif ('teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == "login"):
        teacher_screens_login()

    elif st.session_state.teacher_login_type == "register":
        teacher_screens_register()

def teacher_dasboard():
    teacher_data = st.session_state.teacher_data
    st.header(f"""Welcome {teacher_data['name']}""")

def teacher_login(username, password):
    if not username or not password:
        return False

    response = supabase.table("teachers").select("*").eq(
        "username", username
    ).execute()

    if not response.data:
        return False

    teacher = response.data[0]

    if check_pass(password, teacher["password"]):
        st.session_state.user_role = 'teacher'
        st.session_state.teacher_data = teacher
        st.session_state.is_login = True
        return True

    return False
        

def teacher_screens_login():

    c1, c2 = st.columns(  2, vertical_alignment='center', gap='xxlarge')
   
    with c1:
        header_dashboard()

    with c2:
        if st.button("Go back Home",type="secondary",key="teacher_login_back"):
            st.session_state['login_type'] = None
            st.rerun()

    st.header("Login your Teacher profile")
    teacher_username = st.text_input("Enter username", placeholder="vivek_tiwary")
    teacher_pass = st.text_input("Enter password", type="password", placeholder="Enter password")
    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        if st.button('Login', icon=':material/passkey:', width='stretch',key='teacher_login_btn'):
            if teacher_login(teacher_username, teacher_pass):
                st.toast("Login successful!", icon="✅")
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.toast("invalid username or password", icon="⚠️")
            
    with btnc2:
        if st.button('Register Instead', icon=':material/passkey:', width='stretch', key='_teacher_register_btn'):
            st.session_state['teacher_login_type'] = "register"
            st.rerun()

    footer_dashboard()

def register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm):
    if not teacher_username or not teacher_name or not teacher_pass or not teacher_pass_confirm:
        return False,"all fields are required!"
    if check_teacher_exists(teacher_username):
        return False,"username already taken!"
    if teacher_pass != teacher_pass_confirm:
        return False,"password doesn't match!" 

    try:
        create_teacher(teacher_username, teacher_pass, teacher_name)
        return True, "Successfully Created! login now"
    except Exception as e:
        return False, "Unexpected error!"    
def teacher_screens_register():
    c1, c2 = st.columns( 2,vertical_alignment='center',gap='xxlarge'
    )

    with c1:
        header_dashboard()

    with c2:
        if st.button("Go back Home",type="secondary",key="teacher_register_back"):
            st.session_state['login_type'] = None
            st.rerun()

    st.header("Register your Teacher profile")

    teacher_username = st.text_input("Enter username", placeholder="VIVEK TIWARY", key="teacher_register_username")

    teacher_name = st.text_input("Enter name", placeholder="VIVEK TIWARY", key="teacher_register_name")

    teacher_pass = st.text_input("Enter password",type="password",placeholder="Enter password", key="teacher_register_password")

    teacher_pass_confirm = st.text_input ("Confirm your password", type="password",placeholder="Enter password", key="teacher_register_password_confirm")

    st.divider()
    st.space()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        if st.button("Register now", width="stretch",key="teacher_register_btn"):
           success, message = register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm)
           if success:
               st.success(message)
               import time
               time.sleep(1)
               st.session_state.teacher_login_type = "login"
               st.rerun()
           else:
               st.error(message)
           
    with btnc2:
           if st.button("Login Instead", width="stretch", key="register_login_btn"):
              st.session_state.teacher_login_type = 'login'
              st.rerun()

    footer_dashboard()


