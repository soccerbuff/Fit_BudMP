import streamlit as st

def BMI(w,h):
    
    bmi = w/(h**2)# height in m,wt in kg
    return bmi

def BMR(g, a, w, h,bmi):
    # height in m,weight in kg

    if (g == "Male"):
        bmr = (10 * w) + (6.25 * h * 100) - (5 * a) + 5
    else:
        bmr = (10 * w) + (6.25 * h * 100) - (5 * a) - 16
        
    activity = st.selectbox('What is magnitude of your daily Activity?', (' ', 'Sedentary', 'Light Exercise', 'Moderate Exercise', 'Active Exercise'))
    if (activity == 'Sedentary'):
        tdee = bmr * 1.2
    if (activity == 'Light Exercise'):
        tdee = bmr * 1.375
    if (activity == 'Moderate Exercise'):
        tdee = bmr * 1.55
    if (activity == 'Active Exercise'):
        tdee = bmr * 1.725
    try:
        st.success("The estimated TDEE or body weight maintenance energy requirement is {} Calories per week".format(int(tdee)))
    except:
        pass

    if (bmi < 18.5):

        if (activity == 'Sedentary'):
            st.subheader("Energy intake (in calories) to gain weight:")
            st.caption("Mild weight gain (0.25kg/week) : {}".format(int( 1.13 * tdee)))
            st.caption("Weight gain (0.5kg/week) : {}".format(int( 1.27 * tdee)))
            st.caption("Mild weight gain (1kg/week) : {}".format(int( 1.54 * tdee)))

        if (activity == 'Light Exercise'):
            st.subheader("Energy intake (in calories) to gain weight:")
            st.caption("Mild weight gain (0.25kg/week) : {}".format(int( 1.12 * tdee)))
            st.caption("Weight gain (0.5kg/week) : {}".format(int( 1.23 * tdee)))
            st.caption("Mild weight gain (1kg/week) : {}".format(int( 1.47 * tdee)))

        if (activity == 'Moderate Exercise'):
            st.subheader("Energy intake (in calories) to gain weight:")
            st.caption("Mild weight gain (0.25kg/week) : {}".format(int( 1.1 * tdee)))
            st.caption("Weight gain (0.5kg/week) : {}".format(int( 1.22 * tdee)))
            st.caption("Mild weight gain (1kg/week) : {}".format(int( 1.44 * tdee)))

        if (activity == 'Active Exercise'):
            st.subheader("Energy intake (in calories) to gain weight:")
            st.caption("Mild weight gain (0.25kg/week) : {}".format(int( 1.1 * tdee)))
            st.caption("Weight gain (0.5kg/week) : {}".format(int( 1.21 * tdee)))
            st.caption("Mild weight gain (1kg/week) : {}".format(int( 1.41 * tdee)))

    if (bmi > 18.5 and bmi < 25):
        if (activity == 'Sedentary'):
            st.subheader("Energy intake (in calories) to lose weight:")
            st.caption("Mild weight loss (0.25kg/week) : {}".format(int( 0.87 * tdee)))

            st.subheader("Energy intake (in calories) to gain weight:")
            st.caption("Mild weight gain (0.25kg/week) : {}".format(int( 1.13 * tdee)))
            st.caption("Weight gain (0.5kg/week) : {}".format(int( 1.25 * tdee)))
            st.caption("Mild weight gain (1kg/week) : {}".format(int( 1.5 * tdee)))

        if (activity == 'Light Exercise'):
            st.subheader("Energy intake (in calories) to lose weight:")
            st.caption("Mild weight loss (0.25kg/week) : {}".format(int( 0.89 * tdee)))
            st.caption("Weight loss (0.5kg/week) : {}".format(int( 0.78 * tdee)))

            st.subheader("Energy intake (in calories) to gain weight:")
            st.caption("Mild weight gain (0.25kg/week) : {}".format(int( 1.1 * tdee)))
            st.caption("Weight gain (0.5kg/week) : {}".format(int( 1.22 * tdee)))
            st.caption("Mild weight gain (1kg/week) : {}".format(int( 1.44 * tdee)))

        if (activity == 'Moderate Exercise'):
            st.subheader("Energy intake (in calories) to lose weight:")
            st.caption("Mild weight loss (0.25kg/week) : {}".format(int( 0.9 * tdee)))
            st.caption("Weight loss (0.5kg/week) : {}".format(int( 0.79 * tdee)))

            st.subheader("Energy intake (in calories) to gain weight:")
            st.caption("Mild weight gain (0.25kg/week) : {}".format(int( 1.1 * tdee)))
            st.caption("Weight gain (0.5kg/week) : {}".format(int( 1.21 * tdee)))
            st.caption("Mild weight gain (1kg/week) : {}".format(int( 1.41 * tdee)))

        if (activity == 'Active Exercise'):
            st.subheader("Energy intake (in calories) to lose weight:")
            st.caption("Mild weight loss (0.25kg/week) : {}".format(int( 0.9 * tdee)))
            st.caption("Weight loss (0.5kg/week) : {}".format(int( 0.79 * tdee)))
            st.caption("Extreme Weight loss (1kg/week) : {}".format(int( 0.79 * tdee)))

            st.subheader("Energy intake (in calories) to gain weight:")
            st.caption("Mild weight gain (0.25kg/week) : {}".format(int( 1.1 * tdee)))
            st.caption("Weight gain (0.5kg/week) : {}".format(int( 1.21 * tdee)))
            st.caption("Mild weight gain (1kg/week) : {}".format(int( 1.41 * tdee)))

    if (bmi > 25):
        if (activity == 'Sedentary'):
            st.subheader("Energy intake (in calories) to lose weight:")
            st.caption("Mild weight loss (0.25kg/week) : {}".format(int( 0.90 * tdee)))
            st.caption("Extreme Weight loss (1kg/week) : {}".format(int( 0.79 * tdee)))

            st.subheader("Energy intake (in calories) to gain weight:")
            st.caption("Mild weight gain (0.25kg/week) : {}".format(int( 1.1 * tdee)))
            st.caption("Weight gain (0.5kg/week) : {}".format(int( 1.21 * tdee)))
            st.caption("Mild weight gain (1kg/week) : {}".format(int( 1.42 * tdee)))

        if (activity == 'Light Exercise'):
            st.subheader("Energy intake (in calories) to lose weight:")
            st.caption("Mild weight loss (0.25kg/week) : {}".format(int( 0.91 * tdee)))
            st.caption("Weight loss (0.5kg/week) : {}".format(int( 0.82 * tdee)))
            st.caption("Extreme Weight loss (1kg/week) : {}".format(int( 0.64 * tdee)))

            st.subheader("Energy intake (in calories) to gain weight:")
            st.caption("Mild weight gain (0.25kg/week) : {}".format(int( 1.09 * tdee)))
            st.caption("Weight gain (0.5kg/week) : {}".format(int( 1.18 * tdee)))
            st.caption("Mild weight gain (1kg/week) : {}".format(int( 1.36 * tdee)))

        if (activity == 'Moderate Exercise'):
            st.subheader("Energy intake (in calories) to lose weight:")
            st.caption("Mild weight loss (0.25kg/week) : {}".format(int( 0.91 * tdee)))
            st.caption("Weight loss (0.5kg/week) : {}".format(int( 0.83 * tdee)))
            st.caption("Extreme Weight loss (1kg/week) : {}".format(int( 0.66 * tdee)))

            st.subheader("Energy intake (in calories) to gain weight:")
            st.caption("Mild weight gain (0.25kg/week) : {}".format(int( 1.09 * tdee)))
            st.caption("Weight gain (0.5kg/week) : {}".format(int( 1.17 * tdee)))
            st.caption("Mild weight gain (1kg/week) : {}".format(int( 1.34 * tdee)))

        if (activity == 'Active Exercise'):
            st.subheader("Energy intake (in calories) to lose weight:")
            st.caption("Mild weight loss (0.25kg/week) : {}".format(int( 0.92 * tdee)))
            st.caption("Weight loss (0.5kg/week) : {}".format(int( 0.84 * tdee)))
            st.caption("Extreme Weight loss (1kg/week) : {}".format(int( 0.68 * tdee)))

            st.subheader("Energy intake (in calories) to gain weight:")
            st.caption("Mild weight gain (0.25kg/week) : {}cal".format(int( 1.08 * tdee)))
            st.caption("Weight gain (0.5kg/week) : {}".format(int( 1.16 * tdee)))
            st.caption("Mild weight gain (1kg/week) : {}".format(int( 1.32 * tdee)))

