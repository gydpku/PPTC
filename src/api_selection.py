from openai.embeddings_utils import get_embedding, cosine_similarity
import openai, backoff
import os
import pickle
import numpy as np
from src import api_doc, openai_api, utils

global api_embeddings
global K
api_embeddings = None
K = None


def get_topk(scores, k=10):
    sorted_idx = sorted(range(len(scores)), key=lambda k: scores[k], reverse=True)
    topk_idx = sorted_idx[:k]
    return topk_idx

def get_embedding(text):
    print(f"Getting embedding for {text}")
    response = openai_api.embeddings_with_backoff(
        input=text,
        engine='text-embedding-ada-002'
    )
    embeddings = response['data'][0]['embedding']
    return embeddings

def get_api_embedding(args):
    apis = api_doc.get_all_APIs(args)
    api_desc_list = api_doc.get_API_desc(apis)
    api_embeddings = [get_embedding(d) for d in api_desc_list]
    return api_embeddings

def select_api(query, k=10):
    global api_embeddings
    query_embedding = get_embedding(query)
    scores = [cosine_similarity(query_embedding, e) for e in api_embeddings]
    topk_idx = get_topk(scores, k=k)
    return topk_idx

def get_selected_apis(instruction, args):
    topk_idx = select_api(instruction, k=K)
    apis = api_doc.get_all_APIs(args)
    selected_apis = [apis[x] for x in topk_idx]
    must_apis = api_doc.get_must_APIs(args)
    ans = []
    cnt = 0
    for api in selected_apis:
        if api not in must_apis:
            ans.append(api)
            cnt += 1
            if cnt == len(selected_apis) - len(must_apis):
                break
    ans.extend(must_apis)
    return ans

def get_all_apis(args):
    apis = api_doc.get_all_APIs(args)
    return apis

def prepare_embedding(args):
    global api_embeddings, K
    if args.api_update:
        embedding_path = f"update_api_embeddings.pkl"
    elif args.api_lack:
        embedding_path = f"lack_api_embeddings.pkl"
    else:
        embedding_path = f"api_embeddings.pkl"
    if os.path.exists(embedding_path):
        api_embeddings = utils.read_list(embedding_path)
    else:
        api_embeddings = get_api_embedding(args)
        utils.write_list(api_embeddings, embedding_path)
    K = args.api_topk


if __name__ == '__main__':
    pass


