import pandas as pd
import plotly.express as px

def plot_sov_pie_chart(sov_data, keyword):
    """Generates and returns an interactive Plotly pie chart for E-SoV."""
    e_sov_data = {k: v for k, v in sov_data.items() if v > 0}
    if not e_sov_data: return None
    
    df_sov = pd.DataFrame(list(e_sov_data.items()), columns=['Brand', 'E-SoV (%)'])
    
    fig = px.pie(df_sov, values='E-SoV (%)', names='Brand', title="Engagement-Weighted Share of Voice",
                 hole=0.4, color_discrete_sequence=px.colors.sequential.Viridis)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig

def plot_sopv_bar_chart(sopv_data, mentioned_brands):
    """Generates and returns an interactive Plotly bar chart for SoPV."""
    data_to_plot = {k: v for k, v in sopv_data.items() if k in mentioned_brands}
    if not data_to_plot: return None
        
    df_sopv = pd.DataFrame(list(data_to_plot.items()), columns=['Brand', 'SoPV (%)']).sort_values('SoPV (%)', ascending=False)

    fig = px.bar(df_sopv, x='Brand', y='SoPV (%)', title='Share of Positive Voice (SoPV)',
                 color='SoPV (%)', color_continuous_scale='RdYlGn', range_color=[0, 100],
                 labels={'SoPV (%)': 'Positive Mentions (%)'})
    fig.update_layout(yaxis=dict(range=[0, 100]))
    return fig