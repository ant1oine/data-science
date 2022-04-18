# Import Libraries
# pip install pandas
# pip install matplotlib
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create Pandas Data Frame from csv data 
df = pd.read_csv('usa-feb.csv')

# Trimming CSV file to extract only dates and vaccination doses
df = df[['date', 'total_vaccinations']]
df.date = pd.to_datetime(df.date)

a = df.date # X axis values
b = df.total_vaccinations # Y axis Values

x,y = [], []

# Extract data for each date sequentially to create animation
def animate(i):
	x.append(a[i])
	y.append(b[i])
	plt.plot(x,y, 'r-')

# Change background color of plot and file
plt.rcParams.update({
	'axes.facecolor':'black',
	'figure.facecolor':'lightgray',
	})

# Adjust figure shape and size
fig = plt.figure(figsize=(12,3))

# Add a title
plt.title('Vaccine Doses in US', fontdict={'weight':'bold'})

# Define Y Axis limit 
plt.ylim(0,700_000_000)

ani = FuncAnimation(fig, animate, interval=100)

# Display animation
plt.show()

