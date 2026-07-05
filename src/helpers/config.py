import os
from dataclasses import dataclass


@dataclass
class Settings:
	VECTOR_DB_BACKEND: str = "QDRANT"
	VECTOR_DB_DISTANCE_METHOD: str = "COSINE"
	VECTOR_DB_PATH: str = "qdrant_db"


def get_settings() -> Settings:
	return Settings(
		VECTOR_DB_BACKEND=os.getenv("VECTOR_DB_BACKEND", "QDRANT"),
		VECTOR_DB_DISTANCE_METHOD=os.getenv("VECTOR_DB_DISTANCE_METHOD", "COSINE"),
		VECTOR_DB_PATH=os.getenv("VECTOR_DB_PATH", "qdrant_db"),
	)