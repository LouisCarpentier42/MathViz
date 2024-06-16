
import streamlit as st
import numpy as np
import plotly.express as px
import time
import ast

import turtle_graphics

##########################################################################################
# SETUP APPLICATION
##########################################################################################
st.set_page_config(
    page_title="TurtleGraphics",
    page_icon=":turtle:",
    layout="centered"
)


##########################################################################################
# SETUP PARAMETERS FOR FOLLOW NUMBER TURTLE
##########################################################################################

def number_turtle_parameters():
    # The number
    number = st.selectbox(
        label='Number to follow',
        options=['Rational number', 'pi', 'e', 'phi'],
    )
    if number == 'Rational number':
        c1, c2 = st.columns(2)
        numerator = c1.number_input(
            label='Numerator',
            value=1,
            step=1
        )
        denominator = c2.number_input(
            label='Denominator',
            min_value=1,
            value=7,
            step=1
        )
        number = (numerator, denominator)
    st.session_state.number_turtle_graphics.number = number
    # The base
    st.session_state.number_turtle_graphics.base = st.number_input(
        label='Base',
        min_value=2,
        max_value=36,
        value=10,
        step=1
    )
    # The number of steps
    st.session_state.number_turtle_graphics.nb_iterations = st.number_input(
        label='Number of steps',
        min_value=1,
        value=1000,
        step=1
    )
    return st.session_state.number_turtle_graphics


##########################################################################################
# SETUP PARAMETERS FOR INCREASING ANGLE TURTLE
##########################################################################################

def increasing_angle_turtle_parameters():
    # The initial angle
    st.session_state.increasing_angle_turtle_graphics.angle = st.number_input(
        label='Angle',
        value=1.0,
        step=1e-3,
        format='%.4f'
    )
    # The number of steps
    st.session_state.increasing_angle_turtle_graphics.nb_iterations = st.number_input(
        label='Number of steps',
        min_value=1,
        value=1000,
        step=1
    )
    return st.session_state.increasing_angle_turtle_graphics


##########################################################################################
# SETUP PARAMETERS FOR SUBSTITUTION BASED TURTLE
##########################################################################################

def substitution_turtle_parameters():
    st.session_state.substitution_turtle_graphics.start = st.text_input(
        label='Start string',
        value='x'
    )

    dictionary_as_string = st.text_input(
        label='Substitution dictionary',
        value='{"x": "y + x + y", "y": "x - y - x"}'
    )
    st.session_state.substitution_turtle_graphics.substitutions = ast.literal_eval(dictionary_as_string)
    st.session_state.substitution_turtle_graphics.nb_substitutions = st.number_input(
        label='Number of substitutions',
        min_value=1,
        value=5,
        step=1
    )
    st.session_state.substitution_turtle_graphics.angle = st.number_input(
        label='Angle',
        min_value=1,
        max_value=179,
        value=60,
        step=1
    )
    return st.session_state.substitution_turtle_graphics


##########################################################################################
# SIDEBAR
##########################################################################################

if 'turtle_graphics' not in st.session_state:
    st.session_state.turtle_graphics = {
        'Follow digits of number': number_turtle_parameters,
        'Follow increasing angle': increasing_angle_turtle_parameters,
        'Follow substitution process': substitution_turtle_parameters
    }
    st.session_state.number_turtle_graphics = turtle_graphics.NumberTurtleGraphics()
    st.session_state.increasing_angle_turtle_graphics = turtle_graphics.IncreasingAngleTurtleGraphics()
    st.session_state.substitution_turtle_graphics = turtle_graphics.SubstitutionTurtleGraphics()


with st.sidebar:
    st.title('Animation settings')
    show_animation = st.toggle('Animate', value=True)
    if show_animation:
        nb_frames = st.number_input(
            label='Number of frames',
            min_value=1,
            value=100,
            step=1
        )
        button_pressed_run_animation = st.button('Run animation')

    st.title('Turtle settings')
    st.selectbox(
        label='Path of the turtle',
        options=st.session_state.turtle_graphics,
        key='turtle_strategy'
    )
    st.session_state.selected_turtle = st.session_state.turtle_graphics[st.session_state.turtle_strategy]()



##########################################################################################
# VISUALIZATION
##########################################################################################


xs, ys = st.session_state.selected_turtle.run()

def update_layout(f):
    f.update_layout(
        height=600,
        width=600,
        showlegend=False
    )
    f.update_xaxes(visible=False)
    f.update_yaxes(visible=False)
    f.update_yaxes(
        scaleanchor="x",
        scaleratio=1,
      )


if show_animation:
    if button_pressed_run_animation:

        def update_plot():
            splits = np.linspace(0, len(xs), min(nb_frames + 1, len(xs)), dtype=int)

            for i, split in enumerate(splits[1:]):
                f = px.line(x=xs[:split], y=ys[:split])
                update_layout(f)
                plotly_chart.plotly_chart(f)
                percent = int(i / len(splits) * 100)
                progress_bar.progress(percent, text=f"{percent}% Complete")
                time.sleep(0.01)
            progress_bar.progress(100, text=f"100% Complete")

        progress_bar = st.progress(0)
        plotly_chart = st.empty()
        update_plot()

else:
    fig = px.line(x=xs, y=ys)
    update_layout(fig)
    st.plotly_chart(fig, use_container_width=True)

