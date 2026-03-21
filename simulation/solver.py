import matplotlib
from Suspension_Simulation.physics import plotting_data
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
matplotlib.use('TkAgg')
# creation of the axes
fig,ax = plt.subplots()
x = plotting_data[0]
y = plotting_data[1]
# setting the the FOV of the graph
ax.set_xlim(min(x),max(x))
ax.set_ylim(min(y),max(y))

# creation of the object animation
graph, = ax.plot([], [], 'r-')

# creation of the function for animation
def update(frame) :
    graph.set_data(x[:frame], y[:frame])
    return graph,

# function for plotting 
anim = FuncAnimation(
    fig= fig,
    func= update,
    frames= len(x),
    interval = 500,
    repeat=True
)
# customisation of the graph
plt.xlabel("Time in (s)")
plt.ylabel("Position (m)")
plt.title("Oscillation simulation graph 1")
plt.grid(True)
anim.save("graph_test.gif", writer= "pillow", fps=20)
plt.show()