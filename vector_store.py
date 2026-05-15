import faiss
import numpy as np

def create_index(vectors):
    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(vectors))

    return index


def search(index, chunks, query_vector, k=3):
    distances, indices = index.search(query_vector, k)
    sorted_indices = sorted(indices[0])
    matched_chunks = [chunks[i] for i in sorted_indices]
    return matched_chunks

