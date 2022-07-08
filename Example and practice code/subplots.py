import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
from matplotlib.offsetbox import AnchoredText

# Set the path to where ffmpeg.exe can be found
plt.rcParams['animation.ffmpeg_path'] = 'C:\\Users\\20200964\\ffmpeg-2022-07-04-git-dba7376d59-full_build\\bin\\ffmpeg.exe'

# Just some metadata
metadata = dict(title='Animation Test', artist='A.K.')
# Important: fps is defined here
writer = FFMpegWriter(fps=10, metadata=metadata)


# The function that is plotted every frame
def func1(xrange, A):
    return np.sin(xrange) * A


def func2(xrange, A):
    return np.cos(xrange) * A

# Set up the figure
# Figsize as (x, y), real size of the graph independent of values in it
fig = plt.figure(figsize=(8, 4))
# ax = fig.gca()

# The range of x values for which an y value will be calculated (using func)
# Second parameter +stepsize because end is exclusive, start is inclusive
stepsize_x = 0.1
xrange = np.arange(0, 5+stepsize_x, stepsize_x)

###########
# Subplot 1
###########

ax1 = plt.subplot(1, 2, 1)

# Set up line
# Third parameter defines line color and type (for example: dashed)
# https://matplotlib.org/2.1.2/api/_as_gen/matplotlib.pyplot.plot.html
line1, = plt.plot([], [], 'b-')

plt.title('Sin wave with varying amplitude')
plt.xlabel('t (s)')
plt.ylabel('s (m)')

# Set limits of x-axis equal to xrange
plt.xlim(xrange[0], xrange[-1])
# Set limits of y-axis manually
plt.ylim(-1.5, 1.5)


## TWO OPTIONS FOR GRID BELOW, IF 2 IS LEFT UNCOMMENTED THEN IT GETS PRIORITY
# 1] Auto-generate a grid
plt.grid()

# 2] Manually set a grid, gridline at every value in set_xticks() and set_yticks()
# ax1.set_xticks(np.arange(0, 1, 0.1))
# ax1.set_yticks(np.arange(0, 1., 0.1))
# plt.grid()


############
# Subplot 2
############

ax2 = plt.subplot(1, 2, 2)

# Set up line
# Third parameter defines line color and type (for example: dashed)
# https://matplotlib.org/2.1.2/api/_as_gen/matplotlib.pyplot.plot.html
line2, = plt.plot([], [], 'b-')

plt.title('Cos wave with varying amplitude')
plt.xlabel('t (s)')
plt.ylabel('s (m)')

# Set limits of x-axis equal to xrange
plt.xlim(xrange[0], xrange[-1])
# Set limits of y-axis manually
plt.ylim(-1.5, 1.5)

## TWO OPTIONS FOR GRID BELOW, IF 2 IS LEFT UNCOMMENTED THEN IT GETS PRIORITY
# 1] Auto-generate a grid
plt.grid()

# 2] Manually set a grid, gridline at every value in set_xticks() and set_yticks()
# ax2.set_xticks(np.arange(0, 1, 0.1))
# ax2.set_yticks(np.arange(0, 1., 0.1))
# plt.grid()


# Create the label to indicate current value (updated every frame in loop below)
at1 = AnchoredText("Placeholder text", prop=dict(size=12), frameon=True, loc='upper left')
at1.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax1.add_artist(at1)

# Create the label to indicate current value (updated every frame in loop below)
at2 = AnchoredText("Placeholder text", prop=dict(size=12), frameon=True, loc='upper left')
at2.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax2.add_artist(at2)

# Second parameter is name of generated file
# Third parameter is dpi
with writer.saving(fig, 'sinCosWave.mp4', 200):
    # Parameter that is different every frame
    # Provide the relevant values here (for example as np.arange() or manual list)
    stepsize_A = 0.02
    for A in np.arange(0.5, 1.5+stepsize_A, stepsize_A):
        # Update the label that indicates current value
        # Round value to exactly X decimal places (defined by .Xf)
        at1.txt.set_text(f'A = {"{:.2f}".format(A)}')
        at2.txt.set_text(f'A = {"{:.2f}".format(A)}')
        plt.draw()

        ##################
        # Update subplot 1
        ##################

        # Calculate y values for this frame
        ydata1 = func1(xrange, A)

        # Update the line
        line1.set_data(xrange, ydata1)

        ##################
        # Update subplot 2
        ##################

        # Calculate y values for this frame
        ydata2 = func2(xrange, A)

        # Update the line
        line2.set_data(xrange, ydata2)


        # Add frame to the video
        writer.grab_frame()