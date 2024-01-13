from django.apps import AppConfig
import torch
from transformers import pipeline



class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

    def ready(self) -> None:
            global device
            global model
            global extractor
            global classifier
            classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')

            device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

            model = torch.load('./trained_model/simModel.pth').to(device)
            extractor = torch.load('./trained_model/ext.pth')

            
            return super().ready()