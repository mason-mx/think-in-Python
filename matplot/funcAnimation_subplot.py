import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.animation as animation
import string
import numpy as np


def clean_up_artists(axis, artist_list):
    """
    try to remove the artists stored in the artist list belonging to the 'axis'.
    :param axis: clean artists belonging to these axis
    :param artist_list: list of artist to remove
    :return: nothing
    """
    for artist in artist_list:
        try:
            # fist attempt: try to remove collection of contours for instance
            while artist.collections:
                for col in artist.collections:
                    artist.collections.remove(col)
                    try:
                        axis.collections.remove(col)
                    except ValueError:
                        pass

                artist.collections = []
                axis.collections = []
        except AttributeError:
            pass

        # second attempt, try to remove the text
        try:
            artist.remove()
        except (AttributeError, ValueError):
            pass


def update_plot(frame_index, data_list, fig, axis, n_cols, n_rows, number_of_contour_levels, v_min, v_max,
                changed_artists):
    """
    Update the the contour plots of the time step 'frame_index'

    :param frame_index: integer required by animation running from 0 to n_frames -1. For initialisation of the plot,
    call 'update_plot' with frame_index = -1
    :param data_list: list with the 3D data (time x 2D data) per subplot
    :param fig: reference to the figure
    :param axis: reference to the list of axis with the axes per subplot
    :param n_cols: number of subplot in horizontal direction
    :param n_rows: number of subplot in vertical direction
    :param number_of_contour_levels: number of contour levels
    :param v_min: minimum global data value. If None, take the smallest data value in the 2d data set
    :param v_max: maximum global data value. If None, take the largest value in the 2d data set
    :param changed_artists: list of lists of artists which need to be updated between the time steps
    :return: the changed_artists list
    """

    nr_subplot = 0  # keep the index of the current subplot  (nr_subplot = 0,1,  n_cols x n_rows -1)
    # loop over the subplots
    for j_col in range(n_cols):
        for i_row in range(n_rows):

            # set a short reference to the current axis
            ax = axis[i_row][j_col]

            # for the first setup call, add and empty list which can hold the artists belonging to the current axis
            if frame_index < 0:
                # initialise the changed artist list
                changed_artists.append(list())
            else:
                # for the next calls of update_plot, remove all artists in the list stored in changed_artists[nr_subplot]
                clean_up_artists(ax, changed_artists[nr_subplot])

            # get a reference to 2d data of the current time and subplot
            data_2d = data_list[nr_subplot][frame_index]

            # manually set the levels for better contour range control
            if v_min is None:
                data_min = np.nanmin(data_2d)
            else:
                data_min = v_min
            if v_max is None:
                data_max = np.nanmax(data_2d)
            else:
                data_max = v_max

            # set the contour levels belonging to this subplot
            levels = np.linspace(data_min, data_max, number_of_contour_levels + 1, endpoint=True)

            # create the contour plot
            cs = ax.contourf(data_2d, levels=levels, cmap=cm.rainbow, zorder=0)
            cs.cmap.set_under("k")
            cs.cmap.set_over("k")
            cs.set_clim(v_min, v_max)

            # store the contours artists to the list of artists belonging to the current axis
            changed_artists[nr_subplot].append(cs)

            # set some grid lines on top of the contours
            ax.xaxis.grid(True, zorder=0, color="black", linewidth=0.5, linestyle='--')
            ax.yaxis.grid(True, zorder=0, color="black", linewidth=0.5, linestyle='--')

            # set the x and y label on the bottom row and left column respectively
            if i_row == n_rows - 1:
                ax.set_xlabel(r"Index i ")
            if j_col == 0:
                ax.set_ylabel(r"Index j")

            # set the changing time counter in the top left subplot
            if i_row == 0 and j_col == 1:
                # set a label to show the current time
                time_text = ax.text(0.6, 1.15, "{}".format("Time index : {:4d}".format(frame_index)),
                                    transform=ax.transAxes, fontdict=dict(color="black", size=14))

                # store the artist of this label in the changed artist list
                changed_artists[nr_subplot].append(time_text)

            # for the initialisation call only, set of a contour bar
            if frame_index < 0:
                # the first time we add this  (make sure to pass -1 for the frame_index
                cbar = fig.colorbar(cs, ax=ax)
                cbar.ax.set_ylabel("Random number {}".format(nr_subplot))
                ax.text(0.0, 1.02, "{}) {}".format(string.ascii_lowercase[nr_subplot],
                                                   "Random noise {}/{}".format(i_row, j_col)),
                                         transform=ax.transAxes, fontdict=dict(color="blue", size=12))

            nr_subplot += 1

    return changed_artists


def main():
    n_pixels_x = 50
    n_pixels_y = 30
    number_of_time_steps = 100
    number_of_contour_levels = 10
    delay_of_frames = 1000
    n_rows = 3  # number of subplot rows
    n_cols = 2  # number of subplot columns

    min_data_value = 0.0
    max_data_value = 1.0

    # list containing the random plot per sub plot. Insert you own data here
    data_list = list()
    for j_col in range(n_cols):
        for i_row in range(n_rows):
            data_list.append(np.random.random_sample((number_of_time_steps, n_pixels_x, n_pixels_y)))

    # set up the figure with the axis
    fig, axis = plt.subplots(nrows=n_rows, ncols=n_cols, sharex=True, sharey=True, figsize=(12,8))
    fig.subplots_adjust(wspace=0.05, left=0.08, right=0.98)

    # a list used to store the reference to the axis of each subplot with a list of artists which belong to this subplot
    # this list will be returned and will be updated every time plot which new artists
    changed_artists = list()

    # create first image by calling update_plot with frame_index = -1
    changed_artists = update_plot(-1, data_list, fig, axis, n_cols, n_rows, number_of_contour_levels,
                                                 min_data_value, max_data_value, changed_artists)

    # call the animation function. The fargs argument equals the parameter list of update_plot, except the
    # 'frame_index' parameter.
    ani = animation.FuncAnimation(fig, update_plot, frames=number_of_time_steps,
                                  fargs=(data_list, fig, axis, n_cols, n_rows, number_of_contour_levels, min_data_value,
                                         max_data_value, changed_artists),
                                  interval=delay_of_frames, blit=False, repeat=True)

    plt.show()

if __name__ == "__main__":
    main()
