import streamlit as st
import base64

# Set the title of the app
st.title("HTML Preview")


# Add a text area for the user to paste the HTML code
html_code = st.text_area("Paste HTML code here", height=300)

# Add a button to render the HTML code
if st.button("Render Preview"):
    # Write the HTML code to a temporary file
    with open("temp.html", "w", encoding='utf-8') as f:
        f.write(f"<!DOCTYPE html><html><head><meta charset='utf-8'><title>Preview</title></head><body>{html_code}</body></html>")
    
    # Use an IFrame to display the HTML preview
    preview_url = f"data:text/html;base64,{base64.b64encode(open('temp.html', 'r', encoding='utf-8').read().encode()).decode()}"
    st.components.v1.iframe(src=preview_url, height=500, scrolling=True)
    
