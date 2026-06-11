import gradio as gr
import pandas as pd

from db import (
    get_total_users,
    get_total_messages,
    get_all_messages
)


def load_dashboard():

    users = get_total_users()

    messages = get_total_messages()

    rows = get_all_messages()

    df = pd.DataFrame(
    rows,
    columns=[
        "user_id",
        "prompt",
        "response",
        "input_tokens",
        "cached_input_tokens",
        "output_tokens",
        "cost_usd",
        "created_at"
    ]
)

    return users, messages, df


with gr.Blocks() as demo:

    gr.Markdown("# Sandbox Agent Admin Dashboard")

    total_users = gr.Number(
        label="Total Users"
    )

    total_messages = gr.Number(
        label="Total Messages"
    )

    table = gr.Dataframe()

    btn = gr.Button(
        "Refresh"
    )

    btn.click(
        fn=load_dashboard,
        outputs=[
            total_users,
            total_messages,
            table
        ]
    )

demo.launch()