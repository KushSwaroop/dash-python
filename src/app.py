from dash import Dash, html, dash_table, dcc, Input, Output, State
import pandas as pd
import plotly.express as px

# Load data )
border_deaths_df = pd.read_csv("./data/border_deaths_by_discoverer.csv")
death_by_age_df = pd.read_csv("./data/death_by_age.csv")
deaths_by_gender_df = pd.read_csv("./data/deaths_by_gender.csv")
deaths_nationality_df = pd.read_csv("./data/deaths_nationality.csv")
death_type_df = pd.read_csv("./data/deathtype.csv")
mental_health_df = pd.read_csv("./data/mental_health_conditions_research.csv")
#ecuador_melted_df=pd.read_csv("./data/deaths_nationality_ecuador_melted.csv")

''' linear reg model
X_ecuador= df4_ecuador_melted["Year"]
y_ecuador=df4_ecuador_melted["Ecuador"]
Xtrain, Xtest, ytrain, ytest = train_test_split(X_ecuador,y_ecuador, test_size=0.2, random_state=1)
model1=LinearRegression().fit(Xtrain, ytrain)
model1_r2 = model1.score(Xtrain, ytrain)
print(f"model1 R2 = {model1_r2}")
'''

# Create figures
fig1 = px.line(border_deaths_df, x="discoverer", y=["2018", "2019", "2020", "2021", "2022"])
fig2 = px.line(death_by_age_df, x="age group", y=["fy 2018", "fy 2019", "fy 2020", "fy 2021", "fy 2022"], range_y=(0, 500))
fig3 = px.line(deaths_by_gender_df, x="gender", y=["2018", "2019", "2020", "2021", "2022"])
fig4 = px.line(deaths_nationality_df, x="nationality", y=['fy_2018', 'fy_2019', 'fy_2020', 'fy_2021', 'fy_2022'])
fig5 = px.line(death_type_df, x="type of death", y=['fy 2018', 'fy 2019', 'fy 2020', 'fy 2021', 'fy 2022'])
fig6 = px.scatter(mental_health_df, x="status", y="mental_condition", size="percentage", color="status")
#plt.scatter(Xtrain, ytrain);

app = Dash(__name__)

app.layout = html.Div([
    dcc.Store(id="theme-store", data={"dark": False}),
    html.Button("Toggle Theme", id="theme-toggle", className="px-4 py-2 m-4 bg-gray-200 text-black rounded"),
    html.Div(id="theme-content", children=[
        html.H1("Border Deaths and Mental Health Statistics", className="text-3xl font-bold text-center my-4"),
        html.Div([
            html.Div([
                html.H2("Border Deaths by Discoverer", className="text-xl font-semibold my-2"),
                dcc.Graph(figure=fig1),
            ], className="w-full md:w-1/2 p-4"),
            html.Div([
                html.H2("Deaths by Age", className="text-xl font-semibold my-2"),
                dcc.Graph(figure=fig2),
            ], className="w-full md:w-1/2 p-4"),
        ], className="flex flex-wrap"),
        html.Div([
            html.Div([
                html.H2("Deaths by Gender", className="text-xl font-semibold my-2"),
                dcc.Graph(figure=fig3),
            ], className="w-full md:w-1/2 p-4"),
            html.Div([
                html.H2("Deaths by Nationality", className="text-xl font-semibold my-2"),
                dcc.Graph(figure=fig4),
            ], className="w-full md:w-1/2 p-4"),
        ], className="flex flex-wrap"),
        html.Div([
            html.Div([
                html.H2("Types of Deaths", className="text-xl font-semibold my-2"),
                dcc.Graph(figure=fig5),
            ], className="w-full md:w-1/2 p-4"),
            html.Div([
                html.H2("Mental Health Conditions", className="text-xl font-semibold my-2"),
                dcc.Graph(figure=fig6),
            ], className="w-full md:w-1/2 p-4"),
        ], className="flex flex-wrap"),
    ], className="container mx-auto")
], id="main-content", className="bg-white text-black")

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Border Deaths and Mental Health Statistics</title>
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            .dark-theme {
                background-color: #1a202c;
                color: #cbd5e0;
            }
            .dark-theme .bg-gray-800 {
                background-color: #a0aec0;
            }
            .dark-theme .bg-white {
                background-color: #2d3748;
            }
        </style>
    </head>
    <body>
        <div id="react-entry-point">
            {%app_entry%}
        </div>
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

@app.callback(
    Output("main-content", "className"),
    Output("theme-toggle", "className"),
    Output("theme-store", "data"),
    Input("theme-toggle", "n_clicks"),
    State("theme-store", "data"),
    prevent_initial_call=True
)
def toggle_theme(n_clicks, theme_data):
    if theme_data["dark"]:
        return "bg-white text-black", "px-4 py-2 m-4 bg-gray-800 text-white rounded", {"dark": False}
    else:
        return "dark-theme", "px-4 py-2 m-4 bg-gray-200 text-black rounded", {"dark": True}

if __name__ == '__main__':
    app.run_server(debug=True)
