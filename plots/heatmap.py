from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



data = pd.read_table('HeatMapTable', header=0, index_col=0, delim_whitespace=True)

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


new_index = []

for i in data.index.values:
    new_index.append(miR_list[i])

data['new_index'] = new_index
data.set_index('new_index', inplace=True)
data.sort_index(inplace=True, ascending = True)

mean = data.median(axis=1)
maximal = data.max(axis=1)-data.median(axis=1)

indexes = data.index

for i in indexes:
    data.loc[i] = (data.loc[i]-mean.loc[i])/maximal.loc[i]

Fig=plt.figure(figsize=(8, 5))
ax = Fig.add_subplot(1, 1, 1)
a = ax.imshow(data, cmap=plt.get_cmap('PRGn'), interpolation=None, vmin=-1, vmax=1)

plt.text(-9.5, 5, 'miRNAs', rotation='vertical')
plt.text(5, 17.5, 'Control')
plt.text (18, 17.5, "Friedreich's ataxia")
plt.xlim(-0.5, 29.5)
plt.xticks(np.linspace(0, 29, 30, endpoint=True), probes, rotation='vertical')
plt.ylim(12.5, -0.5)
plt.yticks(np.linspace(0, 12, 13, endpoint=True), mirs)
plt.subplots_adjust(left=0.22, bottom=0, right=1, top=1, wspace=0, hspace=0)
Fig.colorbar(a, shrink=0.4)


Fig.savefig('heatmap_python.png')




#scatter_plot

deseq = pd.read_table("DEseqResults1.xls", header=0, index_col=0, delim_whitespace=True)
deseq['color'] = np.where(deseq['pval']<0.05, 'red', 'grey')

Fig2=plt.figure(figsize=(8, 5))
ax2= Fig2.add_subplot(1, 1, 1)
a = ax2.scatter(np.log2(deseq['baseMean']), deseq['log2FoldChange'],
                c = deseq['color'], alpha=0.5)
ax2.axvline(5.0, 0, 4, color='grey', alpha=0.5)
plt.xlabel('log2baseMean')
plt.ylabel('log2FoldChange')
plt.ylim(-10, 10)
deseq.set_index('id', inplace=True)


plt.text(np.log2(deseq.loc[u'hsa-miR-490-3p']['baseMean']), deseq.loc[u'hsa-miR-490-3p']['log2FoldChange'], u'hsa-miR-490-3p', fontsize=8)
plt.text(np.log2(deseq.loc[u'hsa-miR-196a-5p']['baseMean']), deseq.loc[u'hsa-miR-196a-5p']['log2FoldChange']-0.2, u'hsa-miR-196a-5p', fontsize=8)
plt.text(np.log2(deseq.loc[u'hsa-miR-196b-5p']['baseMean'])-1, deseq.loc[u'hsa-miR-196b-5p']['log2FoldChange']-0.5, u'hsa-miR-196b-5p', fontsize=8)
plt.text(np.log2(deseq.loc[u'hsa-miR-425-5p']['baseMean']), deseq.loc[u'hsa-miR-425-5p']['log2FoldChange']+0.3, u'hsa-miR-425-5p', fontsize=8)
plt.text(np.log2(deseq.loc[u'hsa-miR-377-5p']['baseMean']), deseq.loc[u'hsa-miR-377-5p']['log2FoldChange']-0.2, u'hsa-miR-377-5p', fontsize=8)
plt.text(np.log2(deseq.loc[u'hsa-miR-3607-5p']['baseMean']), deseq.loc[u'hsa-miR-3607-5p']['log2FoldChange']-0.4, u'hsa-miR-3607-5p', fontsize=8)
plt.text(np.log2(deseq.loc[u'hsa-miR-193a-3p']['baseMean'])-3.5, deseq.loc[u'hsa-miR-193a-3p']['log2FoldChange'], u'hsa-miR-193a-3p', fontsize=8)
plt.text(np.log2(deseq.loc[u'hsa-miR-7641']['baseMean']), deseq.loc[u'hsa-miR-7641']['log2FoldChange']+0.1, u'hsa-miR-7641', fontsize=8)
plt.text(np.log2(deseq.loc[u'hsa-miR-224-5p']['baseMean']), deseq.loc[u'hsa-miR-224-5p']['log2FoldChange'], u'hsa-miR-224-5p', fontsize=8)
plt.text(np.log2(deseq.loc[u'hsa-miR-148a-3p']['baseMean']), deseq.loc[u'hsa-miR-148a-3p']['log2FoldChange'], u'hsa-miR-148a-3p', fontsize=8)
plt.text(np.log2(deseq.loc[u'hsa-miR-10a-3p']['baseMean']), deseq.loc[u'hsa-miR-10a-3p']['log2FoldChange'], u'hsa-miR-10a-3p', fontsize=8)
plt.text(np.log2(deseq.loc[u'hsa-miR-212-5p']['baseMean'])-2.5, deseq.loc[u'hsa-miR-212-5p']['log2FoldChange'], u'hsa-miR-212-5p', fontsize=8)
plt.text(np.log2(deseq.loc[u'hsa-miR-10a-5p']['baseMean'])-2, deseq.loc[u'hsa-miR-10a-5p']['log2FoldChange'], u'hsa-miR-10a-5p', fontsize=8)
plt.show()

Fig2.savefig('scatterplot_python.png')