
import streamlit as st
import numpy as np
import plotly.express as px
import time
import ast

from mathviz import turtle_graphics

##########################################################################################
# SETUP APPLICATION
##########################################################################################
st.set_page_config(
    page_title="TurtleGraphics",
    page_icon=":turtle:",
    layout="wide"
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


def controllable_turtle():
    reset = st.button('Reset')
    if reset:
        st.session_state.controllable_turtle_graphics.reset()
        st.session_state.xs = [0.0]
        st.session_state.ys = [0.0]

    c1, c2 = st.columns([0.4, 0.6])
    do_step = c1.button('Step')
    st.session_state.step_size = c2.number_input(
        label='Step size',
        min_value=0.0,
        max_value=10.0,
        value=1.0,
        step=0.1,
        label_visibility="collapsed"
    )
    if do_step:
        st.session_state.controllable_turtle_graphics.step(st.session_state.step_size)
        st.session_state.xs.append(st.session_state.controllable_turtle_graphics.x)
        st.session_state.ys.append(st.session_state.controllable_turtle_graphics.y)

    c1, c2 = st.columns([0.3, 0.7])
    do_rotation = c1.button('Rotate')
    rotation = c2.number_input(
        label='Angle',
        min_value=-360,
        max_value=360,
        value=90,
        step=1,
        label_visibility="collapsed"
    )
    if do_rotation:
        st.session_state.controllable_turtle_graphics.rotate(rotation)
        st.session_state.xs.append(st.session_state.controllable_turtle_graphics.x)
        st.session_state.ys.append(st.session_state.controllable_turtle_graphics.y)

    return st.session_state.controllable_turtle_graphics


##########################################################################################
# SETUP
##########################################################################################

if 'turtle_graphics' not in st.session_state:
    st.session_state.turtle_graphics = {
        'Control the turtle': controllable_turtle,
        'Follow digits of number': number_turtle_parameters,
        'Follow increasing angle': increasing_angle_turtle_parameters,
        'Follow substitution process': substitution_turtle_parameters
    }
    st.session_state.xs = [0.0]
    st.session_state.ys = [0.0]
    st.session_state.controllable_turtle_graphics = turtle_graphics.TurtleGraphics()
    st.session_state.number_turtle_graphics = turtle_graphics.NumberTurtleGraphics()
    st.session_state.increasing_angle_turtle_graphics = turtle_graphics.IncreasingAngleTurtleGraphics()
    st.session_state.substitution_turtle_graphics = turtle_graphics.SubstitutionTurtleGraphics()


settings_column, draw_column = st.columns([0.3, 0.7])
settings_column.title('Animation')
show_animation = settings_column.toggle('Animate', value=True)
if show_animation:
    nb_frames = settings_column.number_input(
        label='Number of frames',
        min_value=1,
        value=100,
        step=1
    )
    button_pressed_run_animation = settings_column.button('Run animation')

settings_column.title('Turtle')
settings_column.selectbox(
    label='Path of the turtle',
    options=st.session_state.turtle_graphics,
    key='turtle_strategy'
)
with settings_column:
    st.session_state.selected_turtle = st.session_state.turtle_graphics[st.session_state.turtle_strategy]()


##########################################################################################
# VISUALIZATION
##########################################################################################



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


if isinstance(st.session_state.selected_turtle, turtle_graphics.TurtleGraphics):
    fig = px.line(x=st.session_state.xs, y=st.session_state.ys)
    update_layout(fig)
    import math
    x_head = st.session_state.xs[-1] + math.cos(st.session_state.selected_turtle.angle) * st.session_state.step_size
    y_head = st.session_state.ys[-1] + math.sin(st.session_state.selected_turtle.angle) * st.session_state.step_size
    fig.add_annotation(
        dict(
            x=x_head,  # X position of the arrow head
            y=y_head,  # Y position of the arrow head
            ax=st.session_state.xs[-1],  # X position of the arrow tail
            ay=st.session_state.ys[-1],  # Y position of the arrow tail
            xref="x", yref="y",
            axref="x", ayref="y",
            text="",  # No text for the annotation
            showarrow=True,
            arrowhead=2,  # Arrow head style
            arrowsize=1,  # Size of the arrow
            arrowwidth=2,  # Width of the arrow line
            arrowcolor="red"  # Color of the arrow
        )
    )

    draw_column.plotly_chart(fig, use_container_width=True)

else:

    xs, ys = st.session_state.selected_turtle.run()

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

            progress_bar = draw_column.progress(0)
            plotly_chart = draw_column.empty()
            update_plot()

    else:
        fig = px.line(x=xs, y=ys)
        update_layout(fig)
        draw_column.plotly_chart(fig, use_container_width=True)

