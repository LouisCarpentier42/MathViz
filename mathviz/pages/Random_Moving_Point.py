
import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time

from mathviz import random_moving_point, readme

##########################################################################################
# SETUP APPLICATION
##########################################################################################
st.set_page_config(
    page_title="RandomMovingPoint",
    page_icon=":tornado:",
    layout="wide"
)

if 'readme_info_random_moving_point' not in st.session_state:
    st.session_state.readme_info_random_moving_point = readme('random_moving_point')
with st.expander('README', expanded=False):
    st.markdown(st.session_state.readme_info_random_moving_point)

#########################################################################################
# USEFUL FUNCTIONS
#########################################################################################

def random_coordinate():
    return np.round(np.random.rand(), 2)

def randomly_initialize_points():
    for j in range(st.session_state.nb_points):
        st.session_state[f'x_point_{j}'] = random_coordinate()
        st.session_state[f'y_point_{j}'] = random_coordinate()
    st.session_state.start_x = random_coordinate()
    st.session_state.start_y = random_coordinate()
    initialize_random_moving_point()

def initialize_random_moving_point():
    st.session_state.random_moving_point = random_moving_point.RandomMovingPoint(
        points=get_starting_points(),
        start_x=st.session_state.start_x,
        start_y=st.session_state.start_y,
        alpha=st.session_state.alpha
    )
    st.session_state.visited_points = [(st.session_state.start_x, st.session_state.start_y)]

def make_n_steps(n: int):
    new_steps = st.session_state.random_moving_point.n_steps(n)
    st.session_state.visited_points.extend(new_steps)


def get_starting_points():
    return[
        (st.session_state[f'x_point_{j}'], st.session_state[f'y_point_{j}'])
        for j in range(st.session_state.nb_points)
    ]


#########################################################################################
# INPUT PARAMETERS
#########################################################################################

if 'nb_points' not in st.session_state:
    st.session_state.nb_points = 3
if 'alpha' not in st.session_state:
    st.session_state.alpha = 0.5
if 'x_point_0' not in st.session_state:
    randomly_initialize_points()
if 'random_moving_point' not in st.session_state:
    initialize_random_moving_point()
if 'nb_steps' not in st.session_state:
    st.session_state.nb_steps = 100


c1, c2 = st.columns([0.3, 0.7])
with c1:
    visualization_method = st.selectbox(
        label='How to visualize the results',
        options=[
            'Manually step around',
            'Immediately show the result',
            'Animate the results'
        ],
        label_visibility='collapsed'
    )

    st.number_input(
        label='Number of steps',
        min_value=1,
        key='nb_steps'
    )

    if visualization_method == 'Manually step around':
        c11, c12 = st.columns(2)
        c11.button(
            label='1 Step',
            on_click=lambda: make_n_steps(1),
            use_container_width=True
        )
        c12.button(
            label='N Step',
            on_click=lambda: make_n_steps(st.session_state.nb_steps),
            use_container_width = True
        )

    if visualization_method == 'Animate the results':
        c11, c12 = st.columns(2)
        c11.button(
            label='Run animation',
            key='animate_button'
        )
        c12.number_input(
            label='Number of frames',
            min_value=0, step=1,
            value=120,
            placeholder='Number of frames',
            label_visibility='collapsed',
            key='nb_frames'
        )

with c2:
    c21, c22 = st.columns(2)
    c21.number_input(
        label='Number of points',
        min_value=3,
        step=1,
        key='nb_points',
        on_change=randomly_initialize_points,
        placeholder='Number of points',
        label_visibility='collapsed'
    )
    c22.button(
        label='Randomly initialize points',
        on_click=randomly_initialize_points,
        use_container_width=True
    )

    c21, c22, c23 = st.columns([1, 1, 2])
    c21.number_input(
        label='Start x',
        min_value=0.00, max_value=1.0,
        step=0.01,
        key='start_x',
        on_change=initialize_random_moving_point
    )
    c22.number_input(
        label='Start y',
        min_value=0.00, max_value=1.0,
        step=0.01,
        key='start_y',
        on_change=initialize_random_moving_point
    )
    c23.number_input(
        label='Alpha',
        min_value=0.01, max_value=0.99,
        step=0.01,
        key='alpha',
        on_change=initialize_random_moving_point
    )

    with st.expander('Adjust the position of the starting points'):
        col1, col2, col3, col4 = st.columns(4)
        for i in range(st.session_state.nb_points):
            col_x, col_y = (col1, col2) if i % 2 == 0 else (col3, col4)
            col_x.number_input(
                label=f'Point {i+1}: X-coordinate',
                min_value=0.0, max_value=1.0, step=0.01,
                key=f'x_point_{i}',
                on_change=initialize_random_moving_point
            )
            col_y.number_input(
                label=f'Point {i+1}: Y-coordinate',
                min_value=0.0, max_value=1.0, step=0.01,
                key=f'y_point_{i}',
                on_change=initialize_random_moving_point
            )


#########################################################################################
# FIGURE
#########################################################################################

# [
#             'Manually step around',
#             'Immediately show the result',
#             'Animate the results'
#         ]

if visualization_method != "Manually step around":
    initialize_random_moving_point()
    make_n_steps(st.session_state.nb_steps)

fig = px.scatter(
    x=[p[0] for p in get_starting_points()],
    y=[p[1] for p in get_starting_points()]
)
fig.update_layout(showlegend=False)
fig.update_xaxes(visible=False, range=[-0.05, 1.05])
fig.update_yaxes(visible=False, range=[-0.05, 1.05])
plotly_chart = st.empty()

if visualization_method == "Animate the results":
    if st.session_state.animate_button:
        xs = [p[0] for p in st.session_state.visited_points]
        ys = [p[1] for p in st.session_state.visited_points]

        def update_plot():
            splits = np.linspace(0, len(xs), min(st.session_state.nb_frames + 1, len(xs)), dtype=int)

            copy_fig = go.Figure(fig)
            for i, split in enumerate(splits[1:]):
                copy_fig = go.Figure(fig)
                copy_fig.add_scatter(x=xs[:split], y=ys[:split], mode='markers')
                copy_fig.add_scatter(x=[xs[split-1]], y=[ys[split-1]], mode='markers')
                plotly_chart.plotly_chart(copy_fig)
                time.sleep(0.01)
            return copy_fig

        fig = update_plot()

else:
    fig.add_scatter(
        x=[p[0] for p in st.session_state.visited_points],
        y=[p[1] for p in st.session_state.visited_points],
        mode='markers'
    )
    fig.add_scatter(
        x=[st.session_state.visited_points[-1][0]],
        y=[st.session_state.visited_points[-1][1]],
    )

plotly_chart.plotly_chart(fig)
