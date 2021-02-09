import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("MathsMarks.csv")
data = df["Math_score"].tolist()
fig = ff.create_distplot([data], ["Math_score"], show_hist = False)
#fig.show()
mean = statistics.mean(data)
standard_deviation = statistics.stdev(data)
print("Mean = " + str(mean))
print("Standard Deviation = " + str(standard_deviation))

def random_set_of_mean(counter):
    dataSet = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return(mean)

meanList = []
for i in range(0, 1000):
    set_of_means = random_set_of_mean(100)
    meanList.append(set_of_means)
standardDeviationOfSample = statistics.stdev(meanList)
meanOfSample = statistics.mean(meanList)
print("Mean of the sample = " + str(meanOfSample))
print("Standard Deviation of the sample = " + str(standardDeviationOfSample))

figOfSample = ff.create_distplot([meanList], ["Student Marks"], show_hist = False)
figOfSample.show()

first_std_deviation_of_sample_start, first_std_deviation_of_sample_end = meanOfSample - standardDeviationOfSample, meanOfSample + standardDeviationOfSample
second_std_deviation_of_sample_start, second_std_deviation_of_sample_end = meanOfSample - 2*standardDeviationOfSample, meanOfSample + 2*standardDeviationOfSample
third_std_deviation_of_sample_start, third_std_deviation_of_sample_end = meanOfSample - 3*standardDeviationOfSample, meanOfSample + 3*standardDeviationOfSample

df_of_school_sample_1 = pd.read_csv("School_1_Sample.csv") 
data_of_school_sample_1 = df["Math_score"].tolist() 
mean_of_school_sample_1 = statistics.mean(data) 
print("Mean of sample 1:- ",mean_of_school_sample_1)

fig_of_sample_1 = ff.create_distplot([meanList], ["student marks"], show_hist = False) 
fig_of_sample_1.add_trace(go.Scatter(x = [meanOfSample, meanOfSample], y = [0, 0.17], mode = "lines", name = "MEAN")) 
fig_of_sample_1.add_trace(go.Scatter(x = [mean_of_school_sample_1, mean_of_school_sample_1], y = [0, 0.17], mode = "lines", name = "MEAN OF STUDENTS WHO HAD MATH LABS")) 
fig_of_sample_1.add_trace(go.Scatter(x = [first_std_deviation_of_sample_end, first_std_deviation_of_sample_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 END")) 
fig_of_sample_1.add_trace(go.Scatter(x = [second_std_deviation_of_sample_end, second_std_deviation_of_sample_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 END")) 
fig_of_sample_1.add_trace(go.Scatter(x = [third_std_deviation_of_sample_end, third_std_deviation_of_sample_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 3 END")) 
fig_of_sample_1.show()

z_score_of_school_sample_1 = (mean_of_school_sample_1 - meanOfSample) / standardDeviationOfSample
print("The Z-Score of School Sample 1 = " + str(z_score_of_school_sample_1))

df_of_school_sample_2 = pd.read_csv("School_2_Sample.csv") 
data_of_school_sample_2 = df["Math_score"].tolist() 
mean_of_school_sample_2 = statistics.mean(data) 
print("Mean of sample 2:- ",mean_of_school_sample_2)

fig_of_sample_2 = ff.create_distplot([meanList], ["student marks"], show_hist = False) 
fig_of_sample_2.add_trace(go.Scatter(x = [meanOfSample, meanOfSample], y = [0, 0.17], mode = "lines", name = "MEAN")) 
fig_of_sample_2.add_trace(go.Scatter(x = [mean_of_school_sample_2, mean_of_school_sample_2], y = [0, 0.17], mode = "lines", name = "MEAN OF STUDENTS WHO USED THE APP")) 
fig_of_sample_2.add_trace(go.Scatter(x = [first_std_deviation_of_sample_end, first_std_deviation_of_sample_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 END")) 
fig_of_sample_2.add_trace(go.Scatter(x = [second_std_deviation_of_sample_end, second_std_deviation_of_sample_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 END")) 
fig_of_sample_2.add_trace(go.Scatter(x = [third_std_deviation_of_sample_end, third_std_deviation_of_sample_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 3 END")) 
fig_of_sample_2.show()

z_score_of_school_sample_2 = (mean_of_school_sample_2 - meanOfSample) / standardDeviationOfSample
print("The Z-Score of School Sample 2 = " + str(z_score_of_school_sample_2))

df_of_school_sample_3 = pd.read_csv("School_3_Sample.csv") 
data_of_school_sample_3 = df["Math_score"].tolist() 
mean_of_school_sample_3 = statistics.mean(data) 
print("Mean of sample 3:- ",mean_of_school_sample_3)

fig_of_sample_3 = ff.create_distplot([meanList], ["student marks"], show_hist = False) 
fig_of_sample_3.add_trace(go.Scatter(x = [meanOfSample, meanOfSample], y = [0, 0.17], mode = "lines", name = "MEAN")) 
fig_of_sample_3.add_trace(go.Scatter(x = [mean_of_school_sample_3, mean_of_school_sample_3], y = [0, 0.17], mode = "lines", name = "MEAN OF STUDENTS WHO WERE ENFORCED TO TAKE EXTRA CLASSES")) 
fig_of_sample_3.add_trace(go.Scatter(x = [first_std_deviation_of_sample_end, first_std_deviation_of_sample_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 END")) 
fig_of_sample_3.add_trace(go.Scatter(x = [second_std_deviation_of_sample_end, second_std_deviation_of_sample_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 END")) 
fig_of_sample_3.add_trace(go.Scatter(x = [third_std_deviation_of_sample_end, third_std_deviation_of_sample_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 3 END")) 
fig_of_sample_3.show()

z_score_of_school_sample_3 = (mean_of_school_sample_3 - meanOfSample) / standardDeviationOfSample
print("The Z-Score of School Sample 3 = " + str(z_score_of_school_sample_3))
