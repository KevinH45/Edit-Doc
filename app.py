import streamlit as st
from htmlUtils import convertDocx2MD, convertDocx2HTMl, convertMD2HTML, convertHTML2Docx

baseMdContent = None
mdInput = st.empty()
htmlOutput = None

# START OF THE SIDEBAR
st.sidebar.title("Import DOCX Files")
file = st.sidebar.file_uploader("Choose a DOCX File", type=[".docx"])

if file is not None:
    baseMdContent = convertDocx2MD(file)

# START OF THE ACTUAL PAGE
st.title("Please Edit This Doc!")
mdInput = st.text_area(label="Edit this Document!", value=baseMdContent, height=400)

with st.expander("", expanded=True):
    st.markdown(mdInput)

with st.expander("", expanded=True):
    htmlOutput = convertMD2HTML(mdInput)
    st.write(htmlOutput)

st.sidebar.title("Export Files")
download = st.sidebar.download_button(
    "Export current edits to docx",
    file_name='generated_doc.docx',
    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    data=convertHTML2Docx(htmlOutput))