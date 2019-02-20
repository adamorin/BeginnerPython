import pandas as pd

InputData = {"col1": [1,2,3], "col2":[4,5,6]}
InputDataSet = pd.DataFrame(data=InputData)

OutputDataSet = InputDataSet
OutputDataSet.col2 += 3

#myDict = {"col1": [1,2,3], "col2":[4,5,6]}
print(OutputDataSet)

InputDataSet.plot()

#Running from SQL
# =============================================================================
# EXEC sp_execute_external_script 
# @language = N'Python',
# @script=N'
# import pandas as pd
# 
# #InputData = {"col1": [1,2,3], "col2":[4,5,6]}
# #InputDataSet = pd.DataFrame(data=InputData)
# 
# OutputDataSet = InputDataSet
# OutputDataSet["col3"] = OutputDataSet["col2"]/10
# 
# #myDict = {"col1": [1,2,3], "col2":[4,5,6]}
# print(OutputDataSet)
# ',
# @input_data_1=N'SELECT top 100 mtr_oi as col1, kwh as col2 from ElecReadings'
# WITH RESULT SETS (([col1] int, [col2] int, [col3] int));
# 
# GO
# =============================================================================


 