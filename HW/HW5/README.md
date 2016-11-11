Design, documentation, unit tests and doing it all in style  
Outline a design for a Pronto Data Analyst Tool (PDAT).  The user will need to be able to explore aspects of the Pronto data.  The user will interact with the program by typing in commands at a prompt.  A central ‘driver’ component will accept input from the user and decide what to do.  


List 5 commands and their use cases.  There is no wrong or right answer, just fun ideas.  E.g., plot a scatterplot of some column against another and save to a PDF file, plot_x_vs_y.  
Create a Markdown document ‘Design.md’ which contains a component design specification that addresses your five use cases.  Be sure to include the Name, What it does, Input (with type information), Output (with type information), How it interacts with other components pieces.  
Implement one component from the PDAT, the plot_x_vs_y piece.  The function should accept a data frame, two column names and an output filename for the PDF file.  It needs to be completely, but not excessively, documented, pass a PEP8 style check and be a free standing function in a file.  
Finally, (1 pt) is awarded for at least two unit tests of the plot_x_vs_y piece.  