import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
coastalcount = pd.read_csv('Synopsis Survey.csv')
Total_percent_change= round(((coastalcount.loc[32]['Total']/coastalcount.loc[0]['Total'])*100),2)
Total_percent_change
coastalcount = pd.read_csv('Synopsis Survey.csv')
coastalcountchart = px.line(coastalcount, x = "Year", y = ['Total','East', 'West'],
                            color_discrete_sequence=['#f28482','#d4d4d4','#b6c5d1'], 
                            title = "Manatee on the Florida Coasts",
                            labels={"value": "Number of Manatees", "variable": "Coast", "Year":''})
coastalcountchart.update_layout(margin=dict(l=2, r=2, t=32, b=30),paper_bgcolor='#f1faee', plot_bgcolor = '#FFFFFF',  legend=dict(x=0,y=1.0,bgcolor='rgba(255, 255, 255, 0)'))
coastalcountchart.add_annotation(x=2005, y=5500,
            text=("Total Population Increase of " + str(Total_percent_change) + "%"),
            showarrow=False)
coastalcountchart
mortalitycause = pd.read_csv('Manatee Mortality Rates.csv')
mortalitycause
mortalitycausesum = mortalitycause.sum(axis=0, skipna=True)
mortalitycausesum 
colors = ['a',] * 7 
colors[0] = 'b'
mortalitycausechart = px.bar(x = ['Watercraft', 'Perinatal', 'Natural', 'Not Necropsied', 'Cold Stress', 'Other: Human', 'Flood/Gate Lock'], y = [654,619,585,540,270,78,32], labels={"x": "Cause of Death", "y": "Number of Manatee Deaths"}, color = colors, color_discrete_sequence = ['#f28482','#e5e5e5'], title = 'Watercrafts are the number one cause of Manatee death')
mortalitycausechart.update_layout(margin=dict(l=2, r=2, t=32, b=30),paper_bgcolor='#f1faee', plot_bgcolor = '#FFFFFF', showlegend=False)
mortalitycausechart
# load dataset already stored as dataframe
manateeTrackerdf = pd.read_csv('Manatee_Sightings.csv')
manateeTrackerdf['Total Number of Manatees'] = manateeTrackerdf['NUMBER_ADULT_MANATEES'] + manateeTrackerdf['NUMBER_CALF_MANATEES']
manateeTrackerdf
# create plot
manateeTracker = px.scatter_mapbox(manateeTrackerdf, lon ='X', lat = 'Y', color = 'ACTIVITY', size='Total Number of Manatees',title = 'Manatee Tracker', labels = {'ACTIVITY':'Activity'}, hover_data = {'ACTIVITY': True,'Total Number of Manatees':True,'X':False, 'Y': False})
manateeTracker.update_layout(mapbox_style="open-street-map",margin={"r":0,"t":0,"l":0,"b":0},paper_bgcolor='#f1faee')
sidebarstyle = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '25%',
    'padding': '15px 15px',
    'background-color': '#457b9d'}

mainpagestyle = {
    'margin-left': '27%',
    'margin-right': '3%',
    'padding': '5px 5px',
    'background-color': '#f1faee'}

textstyle = {
    'textAlign': 'center',
    'color': '#1d3557'}

sidebartextstyle= {
    'textAlign': 'justified',
    'color': '#edf6f9'}

sidebar = html.Div([html.H2('About', style=sidebartextstyle),
                    html.Hr(),
                    html.P('This dashboard was created to bring attention to the Save the Manatee Club, a non-profit organization established by Jimmy Buffett in 1981. Save the Manatee works to protect and resuce this large marine mammal species through raising money, education, and increasing awareness. The number one cause of manatee death is due to human activities. We now need to protect this threatened species for future generations.', style=sidebartextstyle),
                    html.H3('Live Webcam', style=sidebartextstyle),
                    html.Iframe(src="https://www.youtube.com/embed/-2v0b1uJBMs"),
                    html.Iframe(src="https://www.youtube.com/embed/MlPYbPeLpLc"),
                    html.A(html.Button('Final Reflection!'),href='https://docs.google.com/document/d/1V68aLQz3ZGlRs48LezARQowZXLN3Jh4Elip2_Rmp7Lk/edit?usp=sharing')
                   ],style=sidebarstyle)

firstrow = dbc.Row([dbc.Col(dcc.Graph(figure= manateeTracker), md=12,)])

secondrow = dbc.Row([dbc.Col(dcc.Graph(figure= coastalcountchart), md=6), 
                     dbc.Col(dcc.Graph(figure= mortalitycausechart), md=6)])

mainpage = html.Div([html.H2('Save the Manatee', style=textstyle),
                     html.H4('Can you help?', style=textstyle), 
                     html.Hr(), 
                     firstrow, 
                     html.Br(),
                     html.P('Check out where manatees are and what they are doing!',style=textstyle),
                     html.Hr(),
                     secondrow,
                     html.Br(),
                     html.P('As shown manatee population in Florida has continued to grow over the past 20 years, but the species just recently became no longer endangered. In 2017, manatees were classified as "vulnerable" by the International Union for Conservation of Nature (IUCN) and as threatened by the U.S. Fish & Wildlife Service and at the state level by the Florida Fish & Wildlife Conservation Commission (FWC). This means they are not endangered but are still in danger and humans should be cautious in their prescence. The graph on the left analyzes the number one cause of manatee death which is by Watercraft.',style=textstyle)
                    ], style=mainpagestyle)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([sidebar, mainpage])


if __name__ == '__main__':
    app.run_server()
