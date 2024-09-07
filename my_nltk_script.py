import nltk
import os
BASE_DIR = '/home/mrkalihacker/Desktop/vaishu'
NLTK_DATA_DIR = os.path.join(BASE_DIR, 'nltk_data')
nltk.data.path.append(NLTK_DATA_DIR)
# download nltk utilities
print("started1")
nltk.download('averaged_perceptron_tagger')
print("started2")
nltk.download('wordnet')
print("started4")
nltk.download('omw-1.4')
print("completed")

