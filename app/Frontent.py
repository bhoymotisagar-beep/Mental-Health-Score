import streamlit as st 
import requests

# Page Configuration

st.set_page_config( 
    page_title="Mental Health Score Predictor", 
    page_icon="🧠", 
    layout="centered"
)

# Title

st.title("🧠 Mental Health Score Predictor")

st.write( 
    "Enter the student's information below to predict " 
    "the estimated mental health score."
)

# Student Information

st.header("👤 Student Information")

age = st.number_input( 
    "Age",
    min_value=10, 
    max_value=100, 
    value=20, 
    step=1 
)

gender = st.selectbox(
    "Gender", 
    [
     "Male", 
     "Female"
    ] 
)

country = st.text_input( 
    "Country", 
    value="India", 
    placeholder="Enter your country"
)

academic_level = st.selectbox( 
    "Academic Level",
    [ 
      "Undergraduate", 
      "Graduate", 
      "High School" 
    ]
)

# Social Media Information

st.header("📱 Social Media Usage")

most_used_platform = st.selectbox(
    "Most Used Social Media Platform",
    [ 
     "Facebook", 
     "LinkedIn", 
     "Instagram", 
     "Snapchat", 
     "Twitter", 
     "YouTube", 
     "TikTok", 
     "LINE", 
     "KakaoTalk",
     "VKontakte",
     "WhatsApp",
     "WeChat" 
    ]

)

purpose_of_use = st.selectbox(
    "Main Purpose of Social Media Use",

    [ 
     "Networking", 
     "Education", 
     "Entertainment", 
     "News"
    ]

)

avg_daily_usage_hours = st.number_input(
    "Average Daily Social Media Usage (Hours)",

    min_value=0.0,
    max_value=24.0, 
    value=3.0, 
    step=1.0
)

daily_unlocks = st.number_input(
    "Daily Phone Unlocks", 
    min_value=2,
    max_value=275, 
    value=5, 
    step=1
)

# Lifestyle Information
st.header("🏃 Lifestyle Information")

study_hours = st.number_input(
    "Study Hours Per Day",
    min_value=0.0, 
    max_value=24.0,
    value=5.0, 
    step=1.0
)

physical_activity_hours = st.number_input(
    "Physical Activity Hours Per Day", 
    min_value=0.0, 
    max_value=24.0,
    value=1.0, 
    step=1.0
)

sleep_hours_per_night = st.number_input(
    "Sleep Hours Per Night", 
    min_value=0.0, 
    max_value=24.0, 
    value=7.0, 
    step=1.0
)

stress_level = st.selectbox(
    "Stress Level",
    [ 
    "Medium", 
    "Low", 
    "Very High",
    "High" 
    ]
)

# Prediction Button # ------------------

st.divider()

if st.button(
    "🔮 Predict Mental Health Score", 
     use_container_width=True
):
    
   # FastAPI endpoint

    url = "http://127.0.0.1:8000/predict"

    # Data must match StudentData

    data = {
        "age": age,
        "gender": gender,
        "country": country,
        "academic_level": academic_level, 
        "most_used_platform": most_used_platform, 
        "purpose_of_use": purpose_of_use,
        "avg_daily_usage_hours": avg_daily_usage_hours, 
        "daily_unlocks": daily_unlocks,
        "study_hours": study_hours, 
        "physical_activity_hours": physical_activity_hours, 
        "sleep_hours_per_night": sleep_hours_per_night, 
        "stress_level": stress_level

        
    }

    try:
        # Send request to FastAPI
        response = requests.post(
            url, 
            json=data
        )

        # Check API response

        if response.status_code == 200:
            result = response.json()

            prediction = result[ "predicted_mental_health_score" ]

            
            st.success("Prediction completed successfully! 🎉")

            st.metric(
                label="Predicted Mental Health Score", 
                value=prediction
            )

        else:
            st.error(
                f"API Error: {response.status_code}"
            )

            st.write(response.text)

    except requests.exceptions.ConnectionError:
        st.error(
            "❌ Could not connect to FastAPI backend."
        )

        st.info(
            "Please make sure your FastAPI server is running " 
            "at http://127.0.0.1:8000"
        )

    except Exception as e:

        st.error(
            f"Something went wrong: {str(e)}"
        )
            