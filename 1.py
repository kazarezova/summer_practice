import pandas as pd

df = pd.read_csv("DESeq2_results_unpaired.tsv", sep="\t", index_col=0)
df = df.loc[df['baseMean']>5]
getype = pd.read_csv("genes_type.tsv", sep="\t", index_col=0)
df = df.join(getype)
df = df.sort_values('padj')
# df.to_csv("DESeq2_padj_sorted_annotated.tsv", sep="\t")

# выбираем самые дифф
df = df.loc[df['Gene type']=='protein_coding']
# df = df.loc[df['padj']==0]
# df['abs l2FC'] = abs(df['log2FoldChange'])
# df = df.sort_values('abs l2FC', ascending=False)
# df = df.iloc[:10]
# print(df)
# df.to_csv("10 most diff.tsv", sep="\t")

# выбираем самые не дифф
df = df.loc[df['padj']>0.99]
df['abs l2FC'] = abs(df['log2FoldChange'])
df = df.sort_values('abs l2FC')
df = df.iloc[:10]
print(df)
df.to_csv("10 least diff.tsv", sep="\t")
