import matplotlib.pyplot as plt
import matplotlib.animation as anim

def updateframe(fig, ax, image, vardata):
    return anim.FuncAnimation(fig, animate, vardata.time.values, ax, image, vardata, blit=False)

def animate(t, ax, image, vardata):
    print(t)
    ax.set_title("time = %s"%t)
    image.set_array(vardata.sel(time=t))
    return image, 