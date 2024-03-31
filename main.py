import streamlit as st
st.set_page_config(layout="wide", page_icon = "🎸", page_title="memorize the fretboard")

from components import SettingsForm, ControlButtons, NoteDisplay

_, display_col, settings_col = st.columns((3, 3, 1))

st.session_state.setdefault("selected_notes", [])
st.session_state.setdefault("n_notes", 1)
st.session_state.setdefault("bpm", 60)
st.session_state.setdefault("n_exercises", 100)
st.session_state.setdefault("running", False)

with settings_col:
    form = SettingsForm()
    form.display()

    buttons = ControlButtons()
    buttons.display()

with display_col:
    st.markdown("<br>"*8, unsafe_allow_html=True)
    with st.empty():
        
        if st.session_state.running:
            display = NoteDisplay()
            display.display()

                