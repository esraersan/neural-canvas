import numpy as np
from scipy.stats import spearmanr
from scipy.spatial.distance import pdist, squareform


def compute_rdm(embeddings: np.ndarray) -> np.ndarray:
    """
    Compute a Representational Dissimilarity Matrix.

    Parameters
    ----------
    embeddings : np.ndarray, shape (n_images, n_features)
        One row per image, one column per feature.

    Returns
    -------
    rdm : np.ndarray, shape (n_images, n_images)
        Pairwise correlation distances between all image embeddings.
    """
    return squareform(pdist(embeddings, metric='correlation'))


def rsa_correlation(rdm1: np.ndarray, rdm2: np.ndarray) -> float:
    """
    Compute RSA score between two RDMs.
    Spearman correlation of their upper triangles only.

    Parameters
    ----------
    rdm1, rdm2 : np.ndarray, shape (n_images, n_images)

    Returns
    -------
    float : Spearman r between -1 and 1
    """
    assert rdm1.shape == rdm2.shape, "RDMs must be same shape"
    n = rdm1.shape[0]
    idx = np.triu_indices(n, k=1)
    return spearmanr(rdm1[idx], rdm2[idx]).statistic