#importing libraries
import pandas as pd
import plotly.express as px

#main code
iss_url = 'http://api.open-notify.org/iss-now.json'
#data_frame
df = pd.read_json(iss_url)

#prepare for plotting
df['latitude'] = df.loc['latitude', 'iss_position']
df['longitude'] = df.loc['longitude', 'iss_position']
df.reset_index(inplace=True)
df = df.drop(['index', 'message'], axis=1)

#plotting
plot = px.scatter_geo(df, lat = 'latitude', lon = 'longitude')
plot.show()
