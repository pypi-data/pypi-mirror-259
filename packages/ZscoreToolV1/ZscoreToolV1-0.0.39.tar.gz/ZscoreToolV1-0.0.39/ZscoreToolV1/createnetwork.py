# import tools
import numpy as np
import pandas as pd
import scanpy as sc
import umap.umap_ as umap
from scipy.stats import zscore
from tqdm import tqdm
from adjustText import adjust_text
from numpy import where
from sklearn.cluster import DBSCAN
from matplotlib import pyplot as plt
import os
import warnings

warnings.filterwarnings("ignore")

# define functions
def CoExpression(countmtx, network_name, min_cells, saveoutput):
    # make output folders
    if not os.path.isdir('./Results/'):
        os.mkdir('./Results/')
    if not os.path.isdir('./Results/01. Network/'):
        os.mkdir('./Results/01. Network/')
    if not os.path.isdir('./Results/01. Network/' + network_name):
        os.mkdir('./Results/01. Network/' + network_name)

    # extract raw countmatrix
    df = countmtx
    col_sums = (df != 0).sum(axis=0)
    col_sums.to_csv('./Results/01. Network/' + network_name + '/genes.csv') # export list of the genes and total counts

    # filter for genes  
    df = df.loc[:, col_sums >= min_cells] 
    nCells, nGenes = df.shape

    # generating count table, only include cells with at least 2 counts of a gene
    greater_than_1 = df > 1
    row_indices = [np.where(greater_than_1[col])[0] for col in df.columns]
    CoExprMat = np.zeros((len(row_indices), df.shape[1]), dtype=float)

    print("Generating co-expression matrix of " + str(nGenes) + " genes expressed in " + str(nCells) + " cells.")
    # subset table for geneX-positive cells and sum the counts 
    with tqdm(total=len(row_indices), leave=True) as pbar:
        for i, indices in enumerate(row_indices):
            if len(indices) > 0:
                sub = df.values[indices, :]
                CoExprMat[i,:] = (sub.sum(axis=0) / len(indices))
            pbar.update(1) 
    pbar.close()
    
    # zscore by column
    CoExprMat = pd.DataFrame(CoExprMat).dropna(axis=0) 
    CoExprMat_Z = zscore(CoExprMat, axis=0)
    CoExprMat_Z.columns=df.columns
    CoExprMat_Z.index=df.columns
    CoExprMat_Z = CoExprMat_Z.dropna(axis=1).T

    # export z-score table
    if saveoutput==True:
        print("Saving z-scored co-expression matrix")
        CoExprMat_Z.to_csv('./Results/01. Network/' + network_name + '/coexpmat_z.csv')

    return CoExprMat_Z

def ComputeUMAP(coexpmat):
    print("Running UMAP...")
    # Create a UMAP reduction
    reducer = umap.UMAP(
            n_neighbors=15,#15
            min_dist=0.3, # 0.3
            n_components=2,
            metric='euclidean',
            n_epochs=100, # 100
            spread = 3.0, #3
            random_state=42
        )
    umap_result = reducer.fit_transform(coexpmat)
    umap_result = pd.DataFrame(umap_result, columns=['x', 'y'])
    umap_result.index = coexpmat.columns
    return umap_result

def VisualizeNetwork(umap_result, network_name, genes):
    # Visualize the UMAP result
    print("Plotting UMAP and saving to pdf")
    plt.scatter(umap_result['x'], umap_result['y'], s=0.8, c="black", alpha=0.4, linewidths=0)
    plt.show()
    plt.savefig("./Results/01. Network/" + network_name + "/UMAP.pdf", format = "pdf", transparent = True)
    plt.close()

    # add gene names to the plot
    label_df = umap_result[umap_result.index.isin(genes)]
    plt.scatter(umap_result['x'], umap_result['y'], s=0.5, color='grey', alpha=0.4, linewidths=0)
    plt.scatter(label_df['x'], label_df['y'], s=0.5, color='red', label="Labels")
    texts = [plt.text(x, y, label) for label, x, y in zip(label_df.index, label_df['x'], label_df['y'])]
    adjust_text(texts, arrowprops=dict(arrowstyle='->', color='red'), force_text=(0.1, 0.1))
    plt.show()
    plt.savefig("./Results/01. Network/" + network_name + "/UMAP_geneannotation.pdf", format = "pdf", transparent = True)
    plt.close()

def ClusterGenes(umap_data, network_name, eps, min_samples):
    print("Running DCSCAN clustering...")
    model = DBSCAN(eps=eps, min_samples=min_samples)
    yhat = model.fit_predict(umap_data)
    clusters = np.unique(yhat)
    colors = plt.cm.rainbow(np.linspace(0, 1, len(clusters)))
    print("Printing UMAP with clustering to a pdf")

    for cluster, color in zip(clusters, colors):
        row_ix = where(yhat == cluster)
        plt.scatter(umap_data['x'].iloc[row_ix], umap_data['y'].iloc[row_ix], s=0.3, linewidth=0, label=f'Cluster {cluster}', c=[color])
        cluster_center = np.mean(umap_data.iloc[row_ix], axis=0)
        plt.text(cluster_center[0], cluster_center[1], str(cluster), fontsize=8, color='black', ha='center', va='center')
        
        plt.savefig("./Results/01. Network/" + network_name + "/UMAP_geneclustering.pdf", format = "pdf", transparent = True)
    plt.show()
    plt.close()
    return yhat

def ExportClustering(umap_data, network_name, coexpmat, cluster_annotation):
    umap_data['cluster'] = cluster_annotation
    umap_data.to_csv('./Results/01. Network/' + network_name + '/Cluster_annotation.csv')

    for cluster in np.unique(cluster_annotation):
        row_ix = where(cluster_annotation == cluster)
        res_zscore_sub = coexpmat.iloc[row_ix] 
        result_mean = res_zscore_sub.mean(axis = 0)
        result_sum = res_zscore_sub.sum(axis = 0)
    
        result_df = pd.DataFrame({'mean': result_mean, 'sum': result_sum})
        result_df.to_csv('./Results/01. Network/' + network_name + '/Cluster' + str(cluster) + '.csv')











