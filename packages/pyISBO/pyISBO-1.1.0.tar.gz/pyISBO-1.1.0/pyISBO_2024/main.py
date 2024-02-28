from SBO_pulp.AutoRegression import AR
import pandas as pd

data = pd.read_excel("D:\\正事专用文件夹\\学习资料\\仿真优化\\pyISO\\pyISBO\\OperationData.xlsx")
parameterInfo = pd.read_excel("D:\\正事专用文件夹\\学习资料\\仿真优化\\pyISO\\pyISBO\\OperationData.xlsx", 1)
y = data.pop("y")
m = AR(parameterInfo, "neg_mean_squared_error")
m.fit(data, y)
m.MIP_transform()
print(m.MIP.variables())
print(m.MIP.coefficients())
m.optimize()
print(m.optimizedParameter)
print(m.output)