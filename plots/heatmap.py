from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



data = pd.read_table('HeatMapTable', header=0, index_col=0, delim_whitespace=True)
#data = np.log(data)
# print(data.columns, data.iloc[0])
miR_list = {u'hsa-miR-490-3p' : 0,
            u'hsa-miR-196a-5p' : 1,
            u'hsa-miR-196b-5p' : 2,
            u'hsa-miR-425-5p' : 3,
            u'hsa-miR-377-5p' : 4,
            u'hsa-miR-3607-5p' : 5,
            u'hsa-miR-193a-3p' : 6,
            u'hsa-miR-7641' : 7,
            u'hsa-miR-224-5p' : 8,
            u'hsa-miR-148a-3p' : 9,
            u'hsa-miR-10a-3p' : 10,
            u'hsa-miR-212-5p' : 11,
            u'hsa-miR-10a-5p': 12}

mirs = [u'hsa-miR-490-3p', u'hsa-miR-196a-5p', u'hsa-miR-196b-5p',
        u'hsa-miR-425-5p', u'hsa-miR-377-5p', u'hsa-miR-3607-5p',
        u'hsa-miR-193a-3p', u'hsa-miR-7641', u'hsa-miR-224-5p',
        u'hsa-miR-148a-3p', u'hsa-miR-10a-3p', u'hsa-miR-212-5p',
        u'hsa-miR-10a-5p']

probes = list(data.columns.values)
print(probes)
#data['new_index'] = 0
#for index, row in data.iterrows():
#    row['new_index'] = miR_list[index]
# print(miR_list[data.index.values])
new_index = []

for i in data.index.values:
    new_index.append(miR_list[i])
print(new_index)
#data2 = data.df.set_index(miR_list[data.index.values])
data['new_index'] = new_index
data.set_index('new_index', inplace=True)
data.sort_index(inplace=True, ascending = False)
print(data)
mean = data.max(axis=1)
# print(pd.DataFrame(mean))
# data2 = data.div(pd.DataFrame(mean), axis = 'rows')
indexes = data.index
#print(indexes)
for i in indexes:
    data.loc[i] = data.loc[i]/mean.loc[i]

print (data.index)

plt.imshow(data, interpolation=None)
# plt.xlabel('patients')
plt.ylabel('miRNAs')
plt.text(3, 20, 'Control')
plt.text (17, 20, "Friedreich's ataxia")
plt.xlim(-0.5, 29.5)
plt.xticks(np.linspace(0, 29, 30, endpoint=True), probes, rotation='vertical')
plt.ylim(12.5, -0.5)
plt.yticks(np.linspace(0, 12, 13, endpoint=True), mirs)

plt.colorbar()
plt.show()