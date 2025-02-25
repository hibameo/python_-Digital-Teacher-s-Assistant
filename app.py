import streamlit as st
import pandas as pd
import os

# Initialize Data Files
LESSON_PLAN_FILE = "lesson_plans.csv"
ATTENDANCE_FILE = "attendance.csv"
ASSIGNMENTS_FILE = "assignments.csv"
ANNOUNCEMENTS_FILE = "announcements.txt"

def load_data(file, columns):
    if not os.path.exists(file):
        return pd.DataFrame(columns=columns)
    return pd.read_csv(file)

def save_data(df, file):
    df.to_csv(file, index=False)

def main():
    st.title("📚 Digital Teacher's Assistant")
    menu = ["Lesson Planning", "Attendance Tracker", "Assignments", "Notices"]
    choice = st.sidebar.selectbox("Select a Section", menu)

    # **Initialize variables inside main() function**
    lesson_plans = load_data(LESSON_PLAN_FILE, ["Date", "Subject", "Topic", "Notes"])
    attendance = load_data(ATTENDANCE_FILE, ["Date", "Student Name", "Status"])
    assignments = load_data(ASSIGNMENTS_FILE, ["Subject", "Assignment", "Due Date"])

    if choice == "Lesson Planning":
        st.subheader("📖 Lesson Planning")
        with st.form("lesson_form"):
            date = st.date_input("Select Date")
            subject = st.text_input("Subject")
            topic = st.text_input("Topic")
            notes = st.text_area("Additional Notes")
            submit = st.form_submit_button("Save Lesson Plan")

            if submit:
                new_entry = pd.DataFrame([[date, subject, topic, notes]], columns=lesson_plans.columns)
                lesson_plans = pd.concat([lesson_plans, new_entry], ignore_index=True)
                save_data(lesson_plans, LESSON_PLAN_FILE)
                st.success("Lesson Plan Saved Successfully!")

        st.dataframe(lesson_plans)

if __name__ == "__main__":
    main()
