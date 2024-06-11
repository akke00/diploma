# from datasets import load_dataset
# from pinecone import Pinecone
# import os
# from getpass import getpass
# from pinecone import ServerlessSpec
# import time
# from tqdm.auto import tqdm
# from langchain.embeddings.openai import OpenAIEmbeddings
#
# # initialize connection to pinecone (get API key at app.pinecone.io)
# api_key = os.getenv("PINECONE_API_KEY") or getpass("Enter your Pinecone API key: ")
#
# # configure client
# pc = Pinecone(api_key=api_key)
#
# spec = ServerlessSpec(
#     cloud="aws", region="us-west-2"
# )
#
# # get API key from top-right dropdown on OpenAI website
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or getpass("Enter your OpenAI API key: ")
# model_name = 'text-embedding-ada-002'
#
# embed = OpenAIEmbeddings(
#     model=model_name,
#     openai_api_key=OPENAI_API_KEY
# )
#
# def indexing(index_name):
#     batch_size = 100
#
#     texts = []
#     metadatas = []
#
#     # connect to index
#     index = pc.Index(index_name)
#     time.sleep(1)
#
#     for i in tqdm(range(0, len(data), batch_size)):
#         # get end of batch
#         i_end = min(len(data), i + batch_size)
#         batch = data.iloc[i:i_end]
#         # first get metadata fields for this record
#         metadatas = [{
#             'title': record['title'],
#             'text': record['context']
#         } for j, record in batch.iterrows()]
#         # get the list of contexts / documents
#         documents = batch['context']
#         # create document embeddings
#         embeds = embed.embed_documents(documents)
#         # get IDs
#         ids = batch['id']
#         # add everything to pinecone
#         index.upsert(vectors=zip(ids, embeds, metadatas))
#     return 1
# def creating_index(index_name, dimension, metric)->int:
#
#     index_name = index_name
#     existing_indexes = [
#         index_info["name"] for index_info in pc.list_indexes()
#     ]
#     # check if index already exists (it shouldn't if this is first time)
#     if index_name not in existing_indexes:
#         # if does not exist, create index
#         pc.create_index(
#             index_name,
#             dimension=dimension,  # dimensionality of ada 002
#             metric=metric,
#             spec=spec
#         )
#
#         # wait for index to be initialized
#         while not pc.describe_index(index_name).status['ready']:
#             time.sleep(1)
#         indexing(index_name)
#     return 1
#
# def get_data():
#     data = load_dataset('squad', split='train')
#     data = data.to_pandas()
#     data.drop_duplicates(subset='context', keep='first', inplace=True)
#     return data
#
# def delete_index(index_name):
#     if (int(input("Press 1 if you want to delete index: ")) == 1):
#         pc.delete_index("langchain-retrieval-agent")
#
# if __name__ == '__main__':
#     data = get_data()
#
#     creating_index("langchain-retrieval-agent", 1536, 'dotproduct')
#
#     # connect to index
#     index = pc.Index("langchain-retrieval-agent")
#     time.sleep(1)
#     # view index stats
#     print(index.describe_index_stats())
#
#     delete_index("langchain-retrieval-agent")




