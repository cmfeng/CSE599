"""
This function accepts a data frame,
two column names and an output filename for the PDF file,
and output a figure in a pdf file.
"""
# import the plot module
import matplotlib.pyplot as plt


def plot_x_vs_y(dataframe, columnx, columny, filename):
    figure = plt.plot(dataframe[columnx], dataframe[columny])
    # set the x and y labels
    plt.xlabel(columnx)
    plt.ylabel(columny)
    # save the figure to pdf file
    plt.savefig("%s.pdf" % filename)
