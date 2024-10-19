import os
from datasets import load_dataset

class WikiTextFromHuggingFace:
    def __init__(self, dataset_name="wikitext", subset_name="wikitext-103-raw-v1", local_dir="wikitext_custom"):
        self.local_dir = local_dir
        self.dataset_name = dataset_name
        self.subset_name = subset_name
        self.data_cache_dir = os.path.join(os.getcwd(), self.local_dir)
        os.makedirs(self.data_cache_dir, exist_ok=True)
        self.text_file_path = os.path.join(self.data_cache_dir, "wikitext.txt")
        self.load_dataset()

    def load_dataset(self):
        print(f"Loading dataset {self.dataset_name} ({self.subset_name})")
        dataset = load_dataset(self.dataset_name, self.subset_name, split="train")
        with open(self.text_file_path, 'w', encoding='utf-8') as file:
            for line in dataset:
                file.write(line['text'] + '\n')
        print(f"Dataset saved to {self.text_file_path}")
        print(f"Total number of lines in the dataset: {len(dataset)}")

# Usage
wikitext = WikiTextFromHuggingFace()
