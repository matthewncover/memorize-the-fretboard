import streamlit as st

from components import SettingsForm, ControlButtons, NoteDisplay

display_col, settings_col = st.columns([2, 1])

st.session_state.setdefault("selected_notes", [])
st.session_state.setdefault("n_notes", 1)
st.session_state.setdefault("bpm", 60)
st.session_state.setdefault("n_exercises", 5)
st.session_state.setdefault("running", False)

with settings_col:
    form = SettingsForm()
    form.display()

    buttons = ControlButtons()
    buttons.display()

with display_col:
    with st.empty():
        
        if st.session_state.running:
            display = NoteDisplay()
            display.display()

                