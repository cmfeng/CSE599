# 1. Name: FindMax

What it does: find the maximum element in a certain column

Input (with type information): column name S, String

Output (with type information): N,Integer or a float number(depends on the type of that column)

How it interacts with other components pieces: Pseudo code if one component is max

    load the data file to data

    colu = data[input column name'S']

    return max(colu)
 
# 2. Name: FindMean

What it does: find the average element in a certain column

Input (with type information): column name S, String

Output (with type information): N,Integer or a float number(depends on the type of that column)

How it interacts with other components pieces: Pseudo code if one component is average

     load the data file to data

     colu = data[input column name'S']

     return average(colu)

     
# 3. Name: CmpAnuualShort

What it does: find the average element in a certain column of annual members and short-term members seperately

Input (with type information): column name S, String

Output (with type information): two Integers or a float numbers(depends on the type of that column)

How it interacts with other components pieces: Pseudo code if one component is FindMean(the second component in this file)

     load the data file to data

     isolate the data of annual members in column S as column A

     isolate the data of short-term members in column S as column B

     return FindMean(A)

     return FindMean(B)
     
# 4. Name: PlotDurationStation

What it does: plot trip duration vs start time for a certain start station

Input (with type information): start station name S, String

Output (with type information): a pdf file with the figure

How it interacts with other components pieces: Pseudo code if one component is DatetimeIndex:

    load data file to data

    time = pd.DatetimeIndex(data['starttime'])

    isolate the duration and start time data for the input start station

    plot(starttime, tripduration)

    save plot to pdf
    
# 5. Name: PlotStartBirth

What it does: plot trip start time vs member birthyear for certain user type

Input (with type information): usertype, String

Output (with type information): a pdf file with the figure

How it interacts with other components pieces: Pseudo code if one component is DatetimeIndex:

    load data file to data

    time = pd.DatetimeIndex(data['starttime'])

    isolate the starttime and birthyear data for the input user type
    
    plot(birthyear, starttime)