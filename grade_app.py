import streamlit as st

def grade_mark(mark):
    if mark < 0 and mark >100 :
        return invalid
    elif mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >=60:
        return "D"
    else:
        return "E"

if "students" not in st.session_state:
    st.session_state.students = []

st.title("Student Grade Manager")


def add_student():
    name = st.session_state.name
    mark = st.session_state.mark

    if not name.strip():
        st.session_state.error = "Name cannot be empty!"
        return

    st.session_state.students.append({
        "name": name.strip(),
        "mark": mark
    })

    st.session_state.success = "Student added successfully!"

    # Clear inputs
    st.session_state.name = ""
    st.session_state.mark = 0


# Initialize input values
if "name" not in st.session_state:
    st.session_state.name = ""

if "mark" not in st.session_state:
    st.session_state.mark = 0

# Form
with st.form("add"):

    st.text_input("Name", key="name")

    st.number_input(
        "Mark",
        min_value=0,
        max_value=100,
        key="mark"
    )

    st.form_submit_button(
        "Add",
        on_click=add_student
    )

# Messages
if st.session_state.get("error"):
    st.error(st.session_state.error)
    st.session_state.error = None

if st.session_state.get("success"):
    st.success(st.session_state.success)
    st.session_state.success = None


if st.session_state.students:
    results=[]
    for student in st.session_state.students:
        results.append({
            "Name":student["name"],
            "Mark":student["mark"],
            "Grade":grade_mark(student["mark"])
        })

    st.subheader("Student Results")
    st.table(results)

    marks = [student["mark"] for student in st.session_state.students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    col1, col2, col3 = st.columns(3)

    col1.metric("Average", f"{average:.2f}")
    col2.metric("Highest", highest)
    col3.metric("Lowest", lowest)

else:
    st.info("No student records found. Please add a student.")