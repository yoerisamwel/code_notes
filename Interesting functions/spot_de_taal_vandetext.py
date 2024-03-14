from galactic import GalacticDataset

# Loading a dataset from Hugging Face
dataset = GalacticDataset.from_hugging_face_stream(
    "tiiuae/falcon-refinedweb", split="train",
    dedup_fields=["content"], max_samples=5000,
)

# Detecting the language from the text in the dataset
language_distribution = dataset.detect_language(field="content")
print(language_distribution)

# Detecting the personal information from the text in the dataset
pii_information = dataset.detect_pii(fields=["content"])
print(pii_information)

# Getting embeddings and clusters from the dataset
embeddings = dataset.get_embeddings(input_field="content")
clusters = dataset.cluster(n_clusters=10)
cluster_info = dataset.get_cluster_info()
print(cluster_info)