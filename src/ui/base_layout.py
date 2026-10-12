import streamlit as st



def style_background_home():
    st.markdown("""
        <style>
             
             .stApp {background: #5865F2 !important;
             
             }

             .stApp div[data-testid="stColumn"] {
                background-color:#E0E3FF !important;
                padding:15px !important;
                border-radius: 25px !important;
                width: 200px !important;
                max-width: 200px !mportant;
                min-width: 200px !important;
                height:310px !important;
                max-width: 310px !important;
                min-width: 310px !important;
             }


        </style>
                  """
                ,unsafe_allow_html=True)



def style_background_dashboard():
     st.markdown("""
        <style>
             
             .stApp {background: #E0E3FF !important;
             }




        </style>
                  """
                ,unsafe_allow_html=True)



def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@652&display=swap');

           /* hide top bar of streamlit */

              #MainMenu, footer, header {
                  visibility: hidden;
            }
            .block-container{
                  padding-top:1.5rem !important
            }
            

            h1 {
                font-family: 'Climate crisis', sans-serif !important;
                font-size: 2.2rem !important;
                line-height:0.95 !important;
                margin-bottom:0rem !important;
              
            }

             h2 {
                 font-family: 'Climate crisis', sans-serif !important;
                 font-size:2.2rem !important;
                 line-height:0.95 !important;
                margin-bottom:0rem !important;
                  
            }

               h3, h4, p {
                 font-family: 'outfit', sans-serif; 
                 
            }

                    button{
                            border-radius: 1.5rem !important;
                            background-color: #5865F2 !important;
                            color: white !important;
                            padding: 10px 20px !important;
                            border: none !important;
                            transition: background-color 0.25s ease-in-out !important;
                            }        
                       
                    button [kind="secondary"] {
                                            border-radius: 1.5rem !important;
                                            background-color: #E8459E !important;
                                            color: white !important;
                                            padding: 10px 20px !important;
                                            border: none !important;
                                            transition: background-color 0.25s ease-in-out !important;
                                            } 
            
                    button [kind="tertiary"] {
                                            border-radius: 1.5rem !important;
                                            background-color: black !important;
                                            color: white !important;
                                            padding: 10px 20px !important;
                                            border: none !important;
                                            transition: background-color 0.25s ease-in-out !important;
                                            }                 
                         
                   button:hover {
                        transform: scale(1.05)}     
            
            
            
            
                    </style>
                              """
                            ,unsafe_allow_html=True)
            


      
