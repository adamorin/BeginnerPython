import pandas as pd
import numpy as np
from scipy import stats
import smirnov_grubbs as grubbs
'''
reads = [[1,2,3],[1.1, 2.1, 3.1],[7,8,9]]
reads1 = [1,1,100]
ids = [11, 12, 1300]
dic = {"id": ids, "reads": reads1}

#df = pd.DataFrame(data = dic)
#z = stats.zscore([1,1,1,2], axis=1)
z1 = stats.zscore([[1,1,1,1],[1.1,1.1,1.1,1.1],[1,1,1,1],[1.3,1.3,1.3,1.13],[10,1,1,1]])

data = pd.Series([1, 8, 9, 10, 9])
newdata = grubbs.test(data, alpha=0.05)
outlier = grubbs.min_test_indices([240,240.1, 242, 230, 244], alpha=0.05)


'''
A = [[1,2,3],[4,5,6],[7,8,9]]
b = np.array(A)
for col in b.T:
    print(col)