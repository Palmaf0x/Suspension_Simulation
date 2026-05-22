import matplotlib
from Suspension_Simulation.physics.equations import plotting_data
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
matplotlib.use('TkAgg')
                      
fig,ax = plt.subplots()
x = plotting_data[0]
y = plotting_data[1]
                                  
ax.set_xlim(min(x),max(x))
ax.set_ylim(min(y),max(y))

                                  
graph, = ax.plot([], [], 'r-')

                                        
def update(frame) :
    graph.set_data(x[:frame], y[:frame])
    return graph,

                        
anim = FuncAnimation(
    fig= fig,
    func= update,
    frames= len(x),
    interval = 50,
    repeat=True
)
                            
plt.xlabel("Time in (s)")
plt.ylabel("Position (m)")
plt.title("Oscillation simulation graph 1")
plt.grid(True)
anim.save("graph_test.gif", writer= "pillow", fps=20)
plt.show()