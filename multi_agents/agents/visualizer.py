import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from .utils.views import print_agent_output

class VisualizerAgent:
    def __init__(self, websocket=None, stream_output=None, headers=None):
        self.websocket = websocket
        self.stream_output = stream_output
        self.headers = headers or {}

    async def create_visualizations(self, draft_state: dict):
        task = draft_state.get("task")
        topic = draft_state.get("topic")
        research_data = draft_state.get("draft")

        if self.websocket and self.stream_output:
            await self.stream_output("logs", "creating_visualizations", f"Creating visualizations for the topic: {topic}", self.websocket)
        else:
            print_agent_output(f"Creating visualizations for the topic: {topic}", agent="VISUALIZER")

        # Extract data from research_data and create a DataFrame
        # This is a simplified example; you'd need to adapt this to your actual data structure
        df = pd.DataFrame(research_data)

        # Create a figure with subplots
        fig = make_subplots(rows=2, cols=2, subplot_titles=("Chart 1", "Chart 2", "Chart 3", "Chart 4"))

        # Add traces to subplots (example visualizations)
        fig.add_trace(go.Bar(x=df['x'], y=df['y1'], name="Bar Chart"), row=1, col=1)
        fig.add_trace(go.Scatter(x=df['x'], y=df['y2'], mode='lines', name="Line Chart"), row=1, col=2)
        fig.add_trace(go.Pie(labels=df['categories'], values=df['values'], name="Pie Chart"), row=2, col=1)
        fig.add_trace(go.Heatmap(z=df['matrix'], name="Heatmap"), row=2, col=2)

        # Update layout and save the figure
        fig.update_layout(height=800, width=800, title_text=f"Visualizations for {topic}")
        fig.write_html(f"visualizations_{topic.replace(' ', '_')}.html")

        return {"visualizations": f"visualizations_{topic.replace(' ', '_')}.html"}

    async def run(self, draft_state: dict):
        return await self.create_visualizations(draft_state)
