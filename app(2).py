import gradio as gr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

devices = pd.DataFrame({
    "Device": ["PLC-01", "Sensor-12", "RTU-05", "Gateway-02", "Camera-08"],
    "Status": ["Online", "Online", "Warning", "Offline", "Online"],
    "Risk Score": [15, 25, 70, 90, 40]
})

def risk_assessment():
    return devices

def threat_prediction():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    attacks = [8, 12, 15, 18, 25, 32]
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(months, attacks, marker='o')
    ax.set_title("AI-Based Threat Prediction")
    ax.set_xlabel("Month")
    ax.set_ylabel("Predicted Attacks")
    ax.grid(True)
    return fig

def network_traffic():
    traffic = np.random.randint(50, 200, 10)
    fig, ax = plt.subplots(figsize=(6,4))
    ax.bar(range(len(traffic)), traffic)
    ax.set_title("Network Traffic Analysis")
    ax.set_xlabel("Network Nodes")
    ax.set_ylabel("Traffic (MB)")
    return fig

with gr.Blocks(title="Industrial IoT Cyber Security Dashboard") as demo:
    gr.Markdown("# Industrial IoT Cyber Security Dashboard")
    gr.Dataframe(value=risk_assessment(), label="Connected Devices")
    gr.Plot(value=threat_prediction)
    gr.Plot(value=network_traffic)

demo.launch()
