import streamlit as st
import pandas as pd

##########################
#       Instructions
# Run streamlit run annotate_script.py
# Ensure annotation_gui.csv is in the folder. 
########################## 
FILE = "annotation_gui.csv"

# set tasks 
TASK1 = "take_correction_bolus"
TASK2 = "warns_against_stacking"
TASK3 = "timing_of_insulin_stacking"

# set feilds
AXIS1_VALUES = ["YES", "NO"]
AXIS2_VALUES = ["YES", "NO","NA"]
AXIS3_VALUES = ["IMMEDIATE INSULIN STACKING", "FUTURE INSULIN STACKING","AMBIGUOUS","BOTH","NA"]


questions = {
    TASK1: AXIS1_VALUES,
    TASK2: AXIS2_VALUES,
    TASK3: AXIS3_VALUES,
}

df = pd.read_csv(FILE)

# make columns if needed
for q in questions:
    if q not in df:
        df[q] = None
    df[q] = df[q].astype(object)

todo = df.index[df[TASK1].isna()]
row = todo[0]

st.caption(f"row {row + 1} ")
st.write(df.loc[row, "raw_response"])

answers = {q: st.radio(q, opts, index=None, horizontal=True, key=f"{q}_{row}")
           for q, opts in questions.items()}

if st.button("Save & Next"):
    if None in answers.values():
        st.warning("all questions must be answered")
    else:
        # write 
        for q, a in answers.items():
            df.loc[row, q] = a

        #save 
        df.to_csv(FILE, index=False)
        st.rerun()