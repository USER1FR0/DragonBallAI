from configs.config import BaseConfig
from flask import request
import requests

BASE = BaseConfig.DB_API_URL

class GalleryService:
    
    @staticmethod
    def get_characters(page=1,limit=10, **filters):

        params = {"page": page, "limit": limit, **{k: v for k, v in filters.items() if v}}
        
        try:
            r = requests.get(f"{BASE}/characters", params=params, timeout=8, verify=False)
            r.raise_for_status()
            data = r.json()

            if isinstance(data, list):
                return {"items": data, "meta": {"currentPage": 1, "totalPages": 1}}
            return data          
        except requests.RequestException as e:
            print(f"[GalleryService] get_characters: {e}")
            return {
                "items": [],
                "meta": {}
            }
    
    @staticmethod
    def get_character(character_id):
        """Detalle completo de un personaje por ID"""
        try:
            r = requests.get(f"{BASE}/characters/{character_id}", timeout=8)
            r.raise_for_status()
            return r.json()
        except requests.RequestException as e:
            print(f"[GalleryService] get_character: {e}")
            return None
            
        
        
        
        