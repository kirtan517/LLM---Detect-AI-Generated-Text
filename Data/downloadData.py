import os
import kaggle
import tqdm


dataset_names = ["radek1/llm-generated-essays","alejopaullier/daigt-external-dataset","thedrcat/daigt-proper-train-dataset",
                 "thedrcat/daigt-v2-train-dataset","carlmcbrideellis/llm-7-prompt-training-dataset",
                 "nbroad/daigt-data-llama-70b-and-falcon180b","darraghdog/hello-claude-1000-essays-from-anthropic",
                 "kingki19/llm-generated-essay-using-palm-from-google-gen-ai","nbroad/persaude-corpus-2"]


for dataset_name in tqdm.tqdm(dataset_names, desc='Downloading datasets'):
    directory_name = dataset_name.split('/')[-1]
    final_direcotry_name = os.path.join(directory_name)
    if not os.path.exists(final_direcotry_name):
        os.makedirs(final_direcotry_name)
    else:
        continue
    kaggle.api.dataset_download_files(dataset_name, path=final_direcotry_name, unzip=True)


#%%
