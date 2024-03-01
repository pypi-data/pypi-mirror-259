
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

#== HammadML ==================================================================#

import os
import logging
import sys
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

#==============================================================================#

class Index:
    """
    A class to handle the loading, building, querying, and storing of a LlamaIndex.
    """

    def __init__(self, data_directory: str, persist_dir: str = "./storage", openai_api_key: str = None):
        """
        Initializes the LlamaIndex with specified data directory, persistence directory, and optionally an OpenAI API key.

        Args:
            data_directory (str): The directory containing the data to index.
            persist_dir (str): The directory to persist index data.
            openai_api_key (str, optional): OpenAI API key for authentication. If not provided, attempts to use the environment variable.
        """
        self.data_directory = data_directory
        self.persist_dir = persist_dir
        self.openai_api_key = openai_api_key or os.getenv('OPENAI_API_KEY')
        self._validate_api_key()
        self._setup_logging()
        self.index = self._load_or_create_index()

    def _validate_api_key(self):
        """
        Validates the OpenAI API key and sets it as an environment variable if not already set.
        """
        if not self.openai_api_key:
            raise ValueError("OpenAI API key must be provided or set as an environment variable.")
        os.environ['OPENAI_API_KEY'] = self.openai_api_key

    def _setup_logging(self):
        """
        Sets up the logging for the script.
        """
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
        logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

    def _load_or_create_index(self):
        """
        Loads an existing index from the persistence directory or creates a new one from the data directory.

        Returns:
            The loaded or newly created VectorStoreIndex.
        """
        if not os.path.exists(self.persist_dir):
            documents = SimpleDirectoryReader(self.data_directory).load_data()
            index = VectorStoreIndex.from_documents(documents)
            index.storage_context.persist(persist_dir=self.persist_dir)
        else:
            storage_context = StorageContext.from_defaults(persist_dir=self.persist_dir)
            index = load_index_from_storage(storage_context)
        return index

    def query(self, question: str):
        """
        Queries the index with a specified question.

        Args:
            question (str): The question to query the index with.

        Returns:
            The results of the query.
        """
        query_engine = self.index.as_query_engine()
        return query_engine.query(question)

#==============================================================================#