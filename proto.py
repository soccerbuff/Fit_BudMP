import random
import streamlit as st
import streamlit.components.v1 as comp
import links as l
import dk
import base64

#Generate Workout video for a Beginner
def beginner_wk(name,age,gender,wt,ht):
    st.header("Beginner Workout for the day:")
    st.caption("We need further inputs to generate your workout for the day.")
    health=st.selectbox("Do you have any health issues?",("-","Yes","No"))
    if(health=='Yes'):
        issue=st.selectbox("What health issue do you have?",("-","Cardiovascular","Physical Inactivity","Respiratory","Orthopedic","Other"))
        if(issue=="Cardiovascular"):
            if(age<=45):
                st.video(l.cardio_u45)
            elif(age>45):
                st.video(l.cardio_g45)
        elif(issue=="Respiratory"):
            if(age<=45):
                st.video(l.respu45)
            elif(age>45):
                st.video(l.resp45)
        elif(issue=="Physical Inactivity"):
            if(gender=="Female"):
                aero=st.radio("Do you want an aerobic workout?",('No','Yes'))
                if(aero=='Yes'):
                    st.video(l.aero_w)
                else:
                    pass
            elif(gender!='Female' or aero=='No'):
                pass              
        elif(issue=="Orthopedic"):
            ortho_iss=st.selectbox("Which of the above problems do you have?",("-","Recovering from an fracture","Spine issues","Arthritis(Joint Pains)","Any Other"))
            if(ortho_iss=="Recovering from an fracture"):
                pass
            elif(ortho_iss=="Spine_issues"):
                pass
            elif(ortho_iss=="Arthritis(Joint Pains)"):
                pass
            elif(ortho_iss=="Any Other"):
                pass
        elif(issue=="Other"):
            st.text_input=("Enter your problem.")
    else:
        fit_goal=st.selectbox("What is your fitness goal?",("-","Weight Loss(Cut)","Weight Gain(Bulk)","Endurance","Yoga"))
        #Weight Loss
        if(fit_goal=="Weight Loss(Cut)"):
            part=st.selectbox("What area of the body do you want to work on?",("Upper Body","Lower Body","Core"))
            if(part=="Upper Body"):
                pass
            elif(part=="Lower Body"):
                pass
            elif(part=="Core"):
                pass
        #Weight Gain
        elif(fit_goal=="Weight Gain(Bulk)"):
            part=st.selectbox("What area of the body do you want to work on?",("Upper Body","Lower Body","Core"))
            if(part=="Upper Body"):
                pass
            elif(part=="Lower Body"):
                pass
            elif(part=="Core"):
                pass
        #Endurance   
        elif(fit_goal=="Endurance"):
            pass
        #yoga
        elif(fit_goal=="Yoga"):
            pass
        
#Generate Workout Video For Advanced user        
def advanced_workout(name,age,gender,wt,ht):
    st.caption("We need further inputs to generate your workout for the day.")
    ath=st.selectbox("Are you an Athelete?",('-','Yes','No'))
    if(ath=='Yes'):
        ss=st.selectbox("Do you want to perform Sport-Specific Exercises?",('-','Yes','No'))
        if(ss=='Yes'):
            sport=st.selectbox("What Sport Specific exercise do you want to perform?",('-',"Football","Cricket","BasketBall"))
            if(sport=='Football'):
                st.video(l.plyo_f)
            elif(sport=='Cricket'):
                st.video(l.plyo_c)
            elif(sport=='Basketball'):
                st.video(l.plyo_b)
    elif(ath=='No'):
        choice_adv=st.selectbox("What area do you want to work on?",('-','Advanced Strength and Conditioning','Endurance'))
        if(choice_adv=='Advanced Strength and Conditioning'):
            part=st.selectbox("What area of the body do you want to work on?",('Upper Body','Lower Body','Core(Abs)'))
            if(part=="Upper Body"):
                if(gender=='Male'):
                    st.video(l.men_upper)
                elif(gender=='Female'):
                    st.video(l.wm_upper)
            elif(part=="Lower Body"):
                if(gender=='Male'):
                    st.video(l.adv_lower_m)
                elif(gender=='Female'):
                    st.video(l.adv_lower_w)
            elif(part=="Core(Abs)"):
                pass
            
#Generate Workout Video for Intermediate User
def intermediate_wk(name,age,gender,wt,ht):
    st.caption("We need further inputs to generate your workout for the day.")
    health=st.selectbox("Do you have any health issues?",("-","Yes","No"))
    if(health=='Yes'):
        issue=st.selectbox("What health issue do you have?",("-","Cardiovascular","Physical Inactivity","Respiratory","Orthopedic","Other"))
        if(issue=="Cardiovascular"):
            pass
        elif(issue=="Respiratory"):
            pass
        elif(issue=="Physical Inactivity"):
            pass
        elif(issue=="Orthopedic"):
            ortho_iss=st.selectbox("Which of the above problems do you have?",("-","Recovering from an fracture","Spine issues","Arthritis(Joint Pains)","Any Other"))
            if(ortho_iss=="Recovering from an fracture"):
                pass
            elif(ortho_iss=="Spine_issues"):
                pass
            elif(ortho_iss=="Arthritis(Joint Pains)"):
                pass
            elif(ortho_iss=="Any Other"):
                pass
        elif(issue=="Other"):
            st.text_input=("Enter your problem.")
    elif(health=='No'):
        fit_goal=st.selectbox("What is your fitness goal?",("-","Weight Loss(Cut)","Weight Gain(Bulk)","Endurance","Yoga"))
        #Weight Loss
        if(fit_goal=="Weight Loss(Cut)"):
            part=st.selectbox("What area of the body do you want to work on?",("Upper Body","Lower Body","Core"))
            if(part=="Upper Body"):
                pass
            elif(part=="Lower Body"):
                pass
            elif(part=="Core"):
                pass
        #Weight Gain
        elif(fit_goal=="Weight Gain(Bulk)"):
            part=st.selectbox("What area of the body do you want to work on?",("Upper Body","Lower Body","Core"))
            if(part=="Upper Body"):
                pass
            elif(part=="Lower Body"):
                pass
            elif(part=="Core"):
                pass
        #Endurance   
        elif(fit_goal=="Endurance"):
            pass
        #yoga
        elif(fit_goal=="Yoga"):
            pass   
                
st.title("FIT-BUDDY")
menu_options = ("Home Page","Generate Workout", "BMI and BMR calculator")
selection = st.sidebar.selectbox("Menu", menu_options)
name = st.text_input("Enter Your name")
age=st.number_input("Enter Age:",step=1.0)
gender=st.radio("Gender",("Male","Female"))
ht=st.slider('Enter your height (in m)', 0.1, 2.5, 0.01)
wt=st.slider("Enter your weight in kgs:",10,130,55)
if selection=="Generate Workout":
    st.header("Evaluate your fitness level with this basic Squat test.")
    st.subheader("We'll be evaluating your fitness level based on the number of squats you'll be performing in a mintute.")
    st.video("https://www.youtube.com/watch?v=FbqkcH56eRM")
    squat=st.selectbox("How many Squats did you perform?",("-","<20","20-40",">40"))
    fit_level='-'
    if(squat=='<20'):
        fit_level= 'Beginner'
        st.success("You fall under beginner level.Let's Improve!")
    elif(squat=='20-40'):
        fit_level='Intermediate'
        st.success("You fall under Intermediate level.Keep up the good work!")
    elif(squat=='>40'):
        fit_level='Advanced'
        st.success("Your fitness levels are advanced! Let's push the limits!")
    #Based on fitness levels direct inputs
    if(fit_level=='Beginner'):
        beginner_wk(name,age,gender,wt,ht)
    elif(fit_level=="Intermediate"):
        intermediate_wk(name,age,gender,wt,ht)
    elif(fit_level=="Advanced"):
        advanced_workout(name,age,gender,wt,ht)
    else:
        pass
elif selection=="BMI and BMR calculator":
    bmi=dk.BMI(wt,ht)
    bmr=dk.BMR(gender,age,wt,ht,bmi)