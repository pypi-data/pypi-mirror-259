from annoy import AnnoyIndex
import os


class Vector:
    def __init__(self, vector_dimension, index_file='vector_db.index', metric='angular'):
        self.vector_dimension = vector_dimension
        self.index_file = index_file
        self.metric = metric
        self.index = AnnoyIndex(vector_dimension, metric)
        # Attempt to load an existing .index file if it exists
        if os.path.exists(index_file):
            print("Loading existing .index file...")
            self.index.load(index_file)  # Load the index
        else:
            print("No existing .index file found. A new one will be created.")

    def add_item(self, item_id, vector):
        self.index.add_item(item_id, vector)

    def build_index(self, n_trees=10):
        print("Building the .index file...")
        self.index.build(n_trees)
        self.index.save(self.index_file)
        print(f".index file built and saved to {self.index_file}")

    def get_nns_by_vector(self, vector, n_neighbors=5, include_distances=True):
        return self.index.get_nns_by_vector(vector, n_neighbors, include_distances=include_distances)
