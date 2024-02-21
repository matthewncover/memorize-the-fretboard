import streamlit as st
import time, numpy as np

class SettingsForm:
    def __init__(self):
        self.natural_notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.sharp_notes = ['A#', 'C#', 'D#', 'F#', 'G#']

    def display(self):
        with st.form(key='settings'):

            natural_col, sharp_col = st.columns([1, 1])
            selected_notes = []

            with natural_col:
                for note in self.natural_notes:
                    if st.checkbox(note, key=note):
                        selected_notes.append(note)

            with sharp_col:
                for note in self.sharp_notes:
                    if st.checkbox(note, key=note):
                        selected_notes.append(note)

            n_notes = st.slider('Number of notes at a time', 1, 3, 1, 1)
            bpm = st.slider('BPM', 40, 180, 60, 5)
            n_exercises = st.slider('Number of exercises', 10, 100, 5, 1)

            if st.form_submit_button('Submit'):
                st.session_state.selected_notes = selected_notes
                st.session_state.n_notes = n_notes
                st.session_state.bpm = bpm
                st.session_state.n_exercises = n_exercises


class ControlButtons:
    def __init__(self):
        pass

    def display(self):
        if st.button("start"):
            st.session_state.running = True

        if st.button("stop"):
            st.session_state.running = False


class NoteDisplay:
    def __init__(self):
        pass

    def display(self):
        for _ in range(st.session_state.n_exercises):
            random_note_set = np.random.choice(st.session_state.selected_notes, st.session_state.n_notes, replace=False)
            
            st.markdown(f"<h1 style='font-size: 100px;'>{', '.join(random_note_set)}</h1>", unsafe_allow_html=True)
            time.sleep(60 / st.session_state.bpm)

            if not st.session_state.running:
                break