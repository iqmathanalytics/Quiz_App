
import streamlit as st

# Define all the questions, options, and answers
quiz_questions = [
    {"question": "Which key combination moves the cursor to the beginning of a worksheet in Excel?", "options": ["Home", "Ctrl + Home", "Ctrl + End", "Alt + Home"], "answer": "Ctrl + Home"},
    {"question": "How do you extend the cell selection with the keyboard?", "options": ["Shift + Click", "Shift + Arrow Key", "Ctrl + Shift + Arrow Key", "Alt + Shift + Arrow Key"], "answer": "Shift + Arrow Key"},
    {"question": "What does pressing 'Ctrl + Space' in Excel do?", "options": ["Selects the entire worksheet", "Selects the entire row", "Selects the entire column", "Opens the space menu"], "answer": "Selects the entire column"},
    {"question": "Which shortcut inserts a new worksheet in Excel?", "options": ["Ctrl + N", "Shift + F11", "Ctrl + T", "Ctrl + K"], "answer": "Shift + F11"},
    {"question": "How can you save a workbook using keyboard shortcuts?", "options": ["Ctrl + B", "Ctrl + S", "Ctrl + Save", "Shift + S"], "answer": "Ctrl + S"},
    {"question": "What function does 'Ctrl + A' perform when the active cell is not in a table?", "options": ["Selects the active table", "Selects the entire row", "Selects the entire worksheet", "Selects the entire column"], "answer": "Selects the entire worksheet"},
    {"question": "Which of the following is used to open the Print dialog in Excel?", "options": ["Ctrl + P", "Ctrl + Print", "Alt + P", "Shift + P"], "answer": "Ctrl + P"},
    {"question": "To apply bold formatting to selected cells, which shortcut should be used?", "options": ["Ctrl + I", "Ctrl + U", "Ctrl + B", "Alt + B"], "answer": "Ctrl + B"},
    {"question": "Which of these shortcuts will copy the selected cells?", "options": ["Ctrl + X", "Ctrl + C", "Ctrl + V", "Ctrl + Z"], "answer": "Ctrl + C"},
    {"question": "If you need to undo the last action, which shortcut would you use?", "options": ["Ctrl + Y", "Ctrl + U", "Ctrl + Z", "Ctrl + W"], "answer": "Ctrl + Z"},
    {"question": "What does 'Ctrl + End' do in Excel?", "options": ["Moves to the last cell with content", "Ends the Excel program", "Clears the selected cells", "Ends the current function"], "answer": "Moves to the last cell with content"},
    {"question": "Which key combination is used to extend the selection to the last non-empty cell in Excel?", "options": ["Shift + Arrow Key", "Ctrl + Shift + Arrow Key", "Ctrl + Arrow Key", "Alt + Shift + Arrow Key"], "answer": "Ctrl + Shift + Arrow Key"},
    {"question": "To insert a hyperlink in a cell, you would use:", "options": ["Ctrl + K", "Ctrl + L", "Ctrl + H", "Ctrl + J"], "answer": "Ctrl + K"},
    {"question": "What does pressing 'Alt + Page Down' do in Excel?", "options": ["Moves to the bottom of the current page", "Moves one screen to the right", "Moves one screen to the left", "Prints the current page"], "answer": "Moves one screen to the right"},
    {"question": "How would you open the 'Find and Replace' dialog using keyboard shortcuts?", "options": ["Ctrl + F", "Ctrl + H", "Ctrl + R", "Ctrl + S"], "answer": "Ctrl + H"},
    {"question": "Which function is NOT associated with copying, cutting, and pasting in Excel?", "options": ["Ctrl + C", "Ctrl + V", "Ctrl + X", "Ctrl + Z"], "answer": "Ctrl + Z"},
    {"question": "What is the effect of pressing 'Ctrl + Home' in Excel?", "options": ["Closes the current workbook", "Moves to the beginning of the worksheet", "Saves the current workbook", "Prints the current worksheet"], "answer": "Moves to the beginning of the worksheet"},
    {"question": "Which shortcut will cut the selected cells?", "options": ["Ctrl + X", "Ctrl + C", "Ctrl + V", "Ctrl + Z"], "answer": "Ctrl + X"},
    {"question": "To apply or remove underline formatting, you would use:", "options": ["Ctrl + B", "Ctrl + I", "Ctrl + U", "Ctrl + Y"], "answer": "Ctrl + U"},
    {"question": "What does 'Ctrl + F' open in Excel?", "options": ["Find dialog", "File menu", "Format cells dialog", "Font settings"], "answer": "Find dialog"},
    {"question": "How can you move one screen up in the worksheet using the keyboard?", "options": ["Page Up", "Page Down", "Ctrl + Page Up", "Alt + Page Up"], "answer": "Page Up"},
    {"question": "If you wanted to select the entire row where your active cell is located, which shortcut would you use?", "options": ["Ctrl + Space", "Shift + Space", "Alt + Space", "Ctrl + Shift + Space"], "answer": "Shift + Space"},
    {"question": "To quickly navigate to the edge of data regions, you should press:", "options": ["Ctrl + Arrow Key", "Arrow Key alone", "Shift + Arrow Key", "Alt + Arrow Key"], "answer": "Ctrl + Arrow Key"},
    {"question": "What action is performed by 'Ctrl + B' in Excel?", "options": ["Bold formatting", "Open bookmarks", "Insert a blank row", "Start a new bullet list"], "answer": "Bold formatting"},
    {"question": "What does 'Shift + F11' accomplish in Excel?", "options": ["Opens the field settings", "Inserts a new worksheet", "Applies a filter", "Finds and replaces text"], "answer": "Inserts a new worksheet"},
]

# Initialize session state if not already done
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.user_answers = [None] * len(quiz_questions)

# Define the action to be taken on pressing the submit button
def submit_answers():
    st.session_state.show_score = True
    st.session_state.current_question = 0  # Reset for restart purposes

# Display questions and handle navigation
st.title("Excel Skills Quiz")
if not st.session_state.get('show_score', False):
    q = quiz_questions[st.session_state.current_question]
    st.subheader(f"Question {st.session_state.current_question + 1} of {len(quiz_questions)}")
    st.write(q['question'])
    user_answer = st.radio("Choose one option:", q['options'], key=str(st.session_state.current_question))
    st.session_state.user_answers[st.session_state.current_question] = user_answer

    if st.button("Next"):
        if st.session_state.current_question < len(quiz_questions) - 1:
            st.session_state.current_question += 1
        else:
            st.session_state.current_question = 0  # Reset to start on submission
            submit_answers()
else:
    # Calculate score
    score = sum(1 for i, question in enumerate(quiz_questions) if question['answer'] == st.session_state.user_answers[i])
    st.subheader(f"Quiz Complete! Your score is {score} out of {len(quiz_questions)}.")
    if st.button("Restart Quiz"):
        st.session_state.user_answers = [None] * len(quiz_questions)
        st.session_state.show_score = False
