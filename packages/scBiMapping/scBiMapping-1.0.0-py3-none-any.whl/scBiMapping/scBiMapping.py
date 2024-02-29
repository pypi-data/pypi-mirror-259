# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 15:36:49 2023

@author: qiuteng1
"""
from sklearn.cluster import KMeans 
from numpy import * 
import numpy as np
from scipy.sparse.linalg import eigs
from scipy import sparse
from scipy.sparse import *   
from sklearn.preprocessing import normalize
 
def scBiMapping(adata,n_embedding = 30,clustering_cells_only = True,normalization = True): 
        if adata.X.min() < 0:
            errstate('the input matrix is regarded as a similarity matrix and thus should not contain negtive values')   
        if issparse(adata.X) == False:
            adata.X = csr_matrix(adata.X)
        eps = 0.0000000001
        Dx = diags(np.ravel(1/(adata.X.sum(axis = 1)+eps)))
        # print(Dx); print(csr_matrix(adata.X.sum(axis = 1)).shape)
        y = (Dx@csr_matrix(adata.X.sum(axis = 1))).T # row vector
        Dy = diags(np.ravel((1/(sqrt((y@adata.X).T.toarray())+eps))))
        C = sqrt(Dx)@adata.X@Dy
        _,vals,evec = sparse.linalg.svds(C, k=n_embedding,return_singular_vectors = "vh",random_state =0) # evec (k*Ny): Unitary matrix having right singular vectors as rows.
        V = Dy@evec.T; # eigenvectors for features
        U = Dx@adata.X@V; # eigenvectors for cells
        if normalization:
            U = normalize(U, axis=1, norm='l2');   # normalize each row to unit norm
        
        # save result
        if clustering_cells_only:  
                adata.obsm['U'] = U
        else:
                if normalization:
                    V = normalize(V, axis=1, norm='l2')
                adata.obsm['U'] = U
                adata.uns['V'] = V        
        return adata