import uuid
import requests
from enum import Enum


class Events(Enum):
    DATASET_DOWNLOADED = 'dataset.downloaded'
    DATASET_LOADED = 'dataset.loaded'
    DATASET_AI_QUERIED = 'dataset.ai_queried'


class AnalyticsService:
    def __init__(self) -> None:
        self.__track_event_url = 'https://us-central1-osyris-1a1e5.cloudfunctions.net/trackEvent'
        self.anonymous_id = str(uuid.uuid4())

    def track(self, event: str, properties: dict):
        try:
            res = requests.post(self.__track_event_url, json={
                "event": event, "properties": properties, "anonymousId": self.anonymous_id})
        except Exception as e:
            print(e)
