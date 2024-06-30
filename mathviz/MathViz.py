import streamlit as st

st.set_page_config(
    page_title="Welcome to MathViz",
    page_icon="👋",
)

st.title("👋 Welcome to MathViz! 👋")

st.markdown(
    """
    Welcome to `MathViz`, a Python project designed to bring mathematical 
    patterns to life through visualizations. Oftentimes, mathematics starts
    from a simple set of rules. However, intricate patterns may arise by 
    applying these rules. The goal of `MathViz` is to play around with these
    rules and see the patterns that come to live!
    """
)

st.markdown(
    """
    ## Current features
    1. [Turtle graphics](Turtle_Graphics). We let a turtle walk around 
       according to a simple set of rules. By adding a pen to the turtle, we can visualize
       his path! 
    2. [Random moving point](Random_Moving_Point). We have a set of points
       in a 2D plane. We also have one special point, that randomly moves towards one of the
       other points. Where will the point be located? 
    3. More features will be added in the future! 
    """
)

st.markdown(
    """
    ## Contributing

    Contributions are welcome! If you have a new visualization idea or 
    improvements for existing ones, feel free to open an issue or submit 
    a pull request. Let's work together to expand the mathematical MathViz.
    """
)