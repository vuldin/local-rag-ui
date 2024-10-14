import streamlit as st
import requests

# Set up title and input
st.title("Potty Training Assistant")
st.write("Ask any questions about potty training!")

query = st.text_input("Enter your question:")

# Submit button
if st.button("Submit"):
    # Send the request and stream the response
    with requests.post(
        "http://localhost:8000/stream",
        headers={"Content-Type": "application/json"},
        json={"input": {"query": query}},
        stream=True
    ) as response:
        if response.status_code == 200:
            st.write("Response:")
            response_text = ""  # Collect the response here
            response_container = st.empty()  # Placeholder for progressive update
            
            for chunk in response.iter_lines():
                if chunk:
                    # Decode the chunk and get relevant content
                    decoded_line = chunk.decode("utf-8")
                    
                    # Extract only the part after "data: " and ignore run_id
                    if decoded_line.startswith('data: '):
                        data_part = decoded_line.split("data: ")[1].strip()
                        data_part = data_part.replace('"', '')  # Remove extra quotes
                        data_part = data_part.replace("\\n", "\n")  # Replace \n with actual line breaks
                        response_text += data_part  # Append cleaned chunk
                        response_container.markdown(response_text)  # Display with line breaks
        else:
            st.write("Error:", response.status_code)
            st.write(response.text)
