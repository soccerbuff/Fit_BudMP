import random
import streamlit as st
import streamlit.components.v1 as comp
import links as l
import dk

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
            elif(gender!='Female' or aero=='No'):
                bmi=dk.BMI(wt,ht)
                if(bmi>=25 and bmi>10):
                    st.video(l.obese_men)
                else:
                    st.video(l.bob_brad)          
        elif(issue=="Orthopedic"):
            ortho_iss=st.selectbox("Which of the above problems do you have?",("-","Recovering from an fracture","Spine issues","Arthritis(KNEES)","Any Other"))
            if(ortho_iss=="Recovering from an fracture"):
                frac=st.selectbox("What kind of fracture?",('-','Collar Bone','5th-Metatarsal','Wrist',))
                if(frac=='Collar Bone'):
                    st.video(l.collar_bone)
                elif(frac=='5th-Metatarsal'):
                    st.video(l.met)
                elif(frac=='Wrist'):
                    st.video(l.wrist)
            elif(ortho_iss=="Spine_issues"):
                disc=st.selectbox("Do you have a disc bulge?",('-','YES','No'))
                if(disc=='YES'):
                    st.video(l.disc_bulge)
                elif(disc=='No'):
                    st.video(l.spine)
            elif(ortho_iss=="Arthritis(KNEES)"):
                st.video(l.arth)
            elif(ortho_iss=="Any Other"):
                st.write("Enter Problem")
        elif(issue=="Other"):
            st.text_input=("Enter your problem.")
    else:
        fit_goal=st.selectbox("What is your fitness goal?",("-","Weight Loss(Cut)","Weight Gain(Bulk)","Endurance","Yoga"))
        #Weight Loss
        if(fit_goal=="Weight Loss(Cut)"):
            part=st.selectbox("What area of the body do you want to work on?",("Upper Body","Lower Body","Core"))
            if(part=="Upper Body"):
                st.video(l.beg_upp)
            elif(part=="Lower Body"):
                st.video(l.beg_leg)
            elif(part=="Core"):
                st.video(l.beg_core)
        #Weight Gain
        elif(fit_goal=="Weight Gain(Bulk)"):
            part=st.selectbox("What area of the body do you want to work on?",("Upper Body","Lower Body","Core"))
            if(part=="Upper Body"):
                st.video(l.beg_upp)
            elif(part=="Lower Body"):
                st.video(l.beg_leg)
            elif(part=="Core"):
                st.video(l.beg_core)
            diet=st.selectbox("Generating the best food for your bulking diet.Select category",('-','Vegetarian','Non-Vegitarian'))
            if(diet=="Vegetarian"):
                st.caption("Dark green leafy vegetables such as kale, spinach, mustard greens, bok choy, arugula, Swiss chard")
                st.caption("Plant-based protein including nuts, seeds, edamame, tofu")
                st.caption("Starchy vegetables like potatoes, sweet potatoes, or squash")
                st.caption("Non starchy vegetables like broccoli, asparagus, or peppers.")
                st.caption("Whole fruit including bananas, berries, pomegranate, and citrus fruits.")
                st.caption("Whole grains such as quinoa, barley, farro, and brown rice")
            elif(diet=="Non-Vegetarian"):
                st.caption("Dairy products including milk, cottage cheese, yogurt, cheese")
                st.caption("Eggs (whole and egg whites)")
                st.caption("Lean meat and poultry such as beef (sirloin, filet, ground beef), poultry (chicken or turkey breast or thighs), pork (tenderloin or pork chops)")
                st.caption("Seafood including salmon, tuna, whitefish, scallops, shrimp, halibut, trout")
        #Endurance  
        elif(fit_goal=="Endurance"):
            st.video(l.beg_end)
        #yoga
        elif(fit_goal=="Yoga"):
            st.video(l.yog_beg)
            
        
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
            elif(sport=='BasketBall'):
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
                if(gender=="Male"):
                    st.video(l.adv_core_m)
                elif(gender=="Female"):
                    st.video(l.adv_core_w)
        if(choice_adv=="Endurance"):
            if(gender=='Male'):
                st.video(l.end_m)
            elif(gender=='Female'):
                dum=st.selectbox("Do you have the availability of dumbells?(5kg)",('-','YES','NO'))
                if(dum=='YES'):
                    st.video(l.end_wdum)
                elif(dum=='NO'):
                    st.video(l.end_wndum)
                    

#Generate Workout Video for Intermediate User
def intermediate_wk(name,age,gender,wt,ht):
    st.caption("We need further inputs to generate your workout for the day.")
    health=st.selectbox("Do you have any health issues?",(" ","Yes","No"))
    if(health=='Yes'):
        issue=st.selectbox("What health issue do you have?",(" ","Cardiovascular","Physical Inactivity","Respiratory","Orthopedic","Other"))
        if(issue=="Cardiovascular"):
            pass
        elif(issue=="Respiratory"):
            pass
        elif(issue=="Physical Inactivity"):
            pass
        elif(issue=="Orthopedic"):
            ortho_iss=st.selectbox("Which of the above problems do you have?",(" ","Recovering from an fracture","Spine issues","Arthritis(Joint Pains)","Any Other"))
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
                st.video(l.int_upp)
            elif(part=="Lower Body"):
                st.video(l.int_low)
            elif(part=="Core"):
                st.video(l.int_core)
        #Weight Gain
        elif(fit_goal=="Weight Gain(Bulk)"):
            part=st.selectbox("What area of the body do you want to work on?",("Upper Body","Lower Body","Core"))
            if(part=="Upper Body"):
                st.subheader("Make sure you do this workout with dumbells of comfortable weight")
                st.video(l.int_uppb)
            elif(part=="Lower Body"):
                st.subheader("Make sure you do this workout with dumbells of comfortable weight")
                st.video(l.int_lowb)
            elif(part=="Core"):
                st.video(l.int_coreb)
            diet=st.selectbox("Generating the best food for your bulking diet.Select category",('-','Vegetarian','Non-Vegitarian'))
            if(diet=="Vegetarian"):
                st.caption("Dark green leafy vegetables such as kale, spinach, mustard greens, bok choy, arugula, Swiss chard")
                st.caption("Plant-based protein including nuts, seeds, edamame, tofu")
                st.caption("Starchy vegetables like potatoes, sweet potatoes, or squash")
                st.caption("Non starchy vegetables like broccoli, asparagus, or peppers.")
                st.caption("Whole fruit including bananas, berries, pomegranate, and citrus fruits.")
                st.caption("Whole grains such as quinoa, barley, farro, and brown rice")
            elif(diet=="Non-Vegetarian"):
                st.caption("Dairy products including milk, cottage cheese, yogurt, cheese")
                st.caption("Eggs (whole and egg whites)")
                st.caption("Lean meat and poultry such as beef (sirloin, filet, ground beef), poultry (chicken or turkey breast or thighs), pork (tenderloin or pork chops)")
                st.caption("Seafood including salmon, tuna, whitefish, scallops, shrimp, halibut, trout")
        #Endurance   
        elif(fit_goal=="Endurance"):
            st.video(l.int_end)
        #yoga
        elif(fit_goal=="Yoga"):
            yoga_for=st.selectbox("Yoga for?",('-','Strength','Mobility','Power Yoga'))
            if(yoga_for=='Strength'):
                st.video(l.str_yog)
            elif(yoga_for=='Mobility'):
                st.video(l.flex_yoga)
            elif(yoga_for=='Power yoga'):
                st.video(l.pow_yoga)
                
st.title("FIT-BUDDY")
menu_options = ("Home Page","Generate Workout", "BMI and BMR calculator")
selection = st.sidebar.selectbox("Menu", menu_options)
name = st.text_input("Enter Your name")
age=st.number_input("Enter Age:",min_value=16,step=1)
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
