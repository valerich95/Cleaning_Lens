
import torch
import numpy as np
from glob import glob
from PIL import Image
import torchvision.transforms as T
import cv2
import os
import re
from .models import ResponseDataModel
from .apps import model , extractor , device

def extract_embeddings(img_dirs, model, device , tfms):
    transformed = torch.stack([tfms(Image.open(img_dir)) for img_dir in img_dirs])
    new_batch = {'pixel_values': transformed.to(device)}
    with torch.no_grad():
        embeddings = model(**new_batch).last_hidden_state[:, 0].cpu()

    return embeddings

def compute_scores(emb_one, emb_two):
    """Computes cosine similarity between two vectors."""
    scores = torch.nn.functional.cosine_similarity(emb_one, emb_two)
    return scores

def fetch_similar(img_path, folder_dir, tfms, model, device, top_k=6):
    """Fetches the `top_k` similar images with `image` as the query."""
    img_dirs = glob(f'{folder_dir}/*')
    # Prepare the input query image for embedding computation.
    embeddings = extract_embeddings(img_dirs, model, device, tfms)
    transformed = tfms(Image.open(img_path)).unsqueeze(0)
    new_batch = {"pixel_values": transformed.to(device)}

    # Comute the embedding.
    with torch.no_grad():
        query_embeddings = model(**new_batch).last_hidden_state[:, 0].cpu()

    sim_scores = compute_scores(embeddings, query_embeddings)
    most_similar = torch.argsort(sim_scores, descending=True)[:top_k].numpy()
    similar_dirs = np.array(img_dirs)[most_similar].tolist()
    return similar_dirs

def ai_similarity(products_list , input_query_model):

    folder_dir = './img'
    img_path = './reference/reference.jpg'
    if not os.path.exists(img_path):
        raise Exception("Your image file path is incorrect")

    tfms = T.Compose(
        [
                T.Resize((extractor.size['width'], extractor.size['height'])),
                T.ToTensor(),
                T.Normalize(mean=extractor.image_mean, std=extractor.image_std),
        ]
    )

    similar = fetch_similar(img_path, folder_dir, tfms, model, device, top_k=10)
    for similar_img in similar[:6]:
        i = int(re.findall(r'\d\d' , similar_img)[0])
        data = products_list[i]
        # data['dirs'] = f'{folder_dir}/{i}'        
        data['input_query_model'] = input_query_model
        response_model = ResponseDataModel.objects.create(**data)

    return True
