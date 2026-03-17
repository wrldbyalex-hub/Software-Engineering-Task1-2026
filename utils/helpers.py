"""Helper functions for shared UI components in the Python Project app."""

import streamlit as st
# --- Function for home content -----------------------------------------
def show_home_content() -> None:
    """
    Render the introductory 'Why use Python?' section.
    
    Displays a divider, heading, popularity bar chart, source link, two-column layout
    with image and list of Python applications, and colored rainbow text summary.
    
    Used on both the login screen (for non-logged-in users) and the Home Page tab.
    """
    st.divider()
    
    st.markdown("## Why use Python?")
    st.subheader("The popularity of the biggest languages (%)")
    st.write("The rest of the languages are not shown, but account for the remaining 36%.")
    
    # Data for the bar chart
    chart_data = {"Python": 25, "Java": 21, "JavaScript": 8, "C#": 7}
    st.bar_chart(chart_data)
    
    st.markdown("Source: [Statista - Most Popular Programming Languages](https://www.statista.com/statistics/793628/worldwide-developer-survey-most-used-languages/)")  # Better link if you have the exact URL
    
    # Two-column layout for content (better for bigger screens)
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("What can you do with Python?")
        st.image("https://f4.bcbits.com/img/a2712205983_16.jpg")
    
    with col_right:
        st.subheader("...a lot of stuff")
        st.write("Python is a very versatile language, suitable for many applications:")
        st.markdown(
            "- Web development\n"
            "- App development\n"
            "- Creating AI / Machine Learning\n"
            "- Game development\n"
            "- Data Science & Analysis\n"
            "- Cybersecurity\n"
            "- Robotics"
        )
        st.markdown("and so much ***more***.")
        
        st.markdown('''
            :red[As you] :orange[can see,] :green[Python can] :blue[do some] 
            :violet[really cool] :gray[stuff as] :rainbow[shown above.]
        ''')