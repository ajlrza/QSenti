import numpy as np
import json, os, random, asyncio
from QSenti.qsenti_dataclasses import NormalCacheEntry, NormalCacheStore

class HilbertSpace:

    hilbert_space = np.array([1, 0], dtype=np.complex128)

    def __init__(self, normal_cache: NormalCacheEntry):

        '''
            Instantiates the HilbertSpace class along with the follow: hilbert_cache, hilbert_space_vector_id,
            hilbert_space_vector. The vector ID is a randomized 8-digit integer that serves as the key for 
            vector mapping.
        '''

        self.normal_cache: NormalCacheEntry
        self.hilbert_space_vector = np.array([], dtype=np.complex128)

        self.processed_data = {}

        for index, data in enumerate(self.normal_cache):

            self.hilbert_space_vector_id = random.randint(10000000, 99999999)

            if data == "date":
                self.processed_data[self.hilbert_space_vector_id] = {"date": data}
            else:
                continue

            if (self.hilbert_cache[index][-2:] - 30 == 0):
                self.processed_data[self.hilbert_space_vector_id]["operation"] = 1

            elif (self.hilbert_cache[index][-2:] - 30 >= 1):
                self.processed_data[self.hilbert_space_vector_id]["operation"] = 2

    def linear_comb(self, processed_data: dict, vector, data) -> None:

        self.processed_data[vector][data] = self.processed_data[list(self.processed_data.index(vector) + 1)][data]  + self.processed_data[vector][data]

    def dot_prod(self, processed_data: dict, vector, data) -> None:

        H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])

        self.processed_data[vector][data] = np.dot(H, self.processed_data[vector][data])
        self.processed_data[vector][data] = np.dot(self.processed_data[list(self.processed_data.index(vector) - 1)][data], 
                                                                       self.processed_data[vector][data])
        
    def perform_operation(self) -> int:

        '''
            Performs mathematical operations with numba.jit class decorator for optimized
            CPU process. 
        '''

        for vector, data in enumerate(self.processed_data):

            if (data["operation"] == 1):

                self.hilbert_space_vector = np.array([1+2j, 3-4j])

                if (list(self.processed_data).index(vector) + 1 < len(list(self.processed_data))):

                    if (self.processed_data[vector][data][0][-2:] - 30 == 0):
                        self.dot_prod(self.processed_data, vector, data)

                    elif (self.processed_data[vector][data][0][-2:] - 30 >= 1):
                        self.linear_comb(self.processed_data, vector, data)

            elif (data["operator"] == 2):

                self.hilbert_space_vector = np.array([1+2j, 3-4j])

                if (list(self.processed_data).index(vector) + 1 < len(list(self.processed_data))):

                    if (self.processed_data[vector][data][0][-2:] - 30 == 0):
                        self.dot_prod(self.processed_data, vector, data)

                    elif (self.processed_data[vector][data][0][-2:] - 30 >= 1):
                        self.linear_comb(self.processed_data, vector, data)

        self.hilbert_space_vector = np.array([1+2j, 3-4j])
        self.hilbert_space = np.append(self.hilbert_space_vector, self.hilbert_space_vector_id)

        return self.hilbert_space_vector_id

    def lookup_space(self) -> np.ndarray:

        '''
            Returns the hilbert space to the Synapse object.
        '''

        return self.hilbert_space


hilbert_cache = {}

normal_token_cache = {}
normal_embeddings_cache = {}
normal_conversation_cache = {}


def load_to_cache(Conversation: str | list[str], Label: str) -> None:

    '''
        Appends the recent data retrieved from the application to the in-memory cache, 
        this data includes both the user's and the agent's interaction including the metadata.
    '''

    #metadata get date, i need a metadata

    normal_conversation_cache["Indentifier here"] = (Conversation, Label)

    def transform_hilbert_cache(self):

        '''
            Offloads the hilbert space mathematical operations to the HilbertSpace class.
            The instantiated Synapse's hilbert cache gets updated with the resulting vector
            and its corresponding vector ID.
        '''

        space = HilbertSpace(self.hilbert_cache)
        self.hilbert_cache[f"{space.perform_operation()}"] = space.hilbert_space_vector

    def get_data(self, key):
        
        if key in self.normal_conversation_cache:
            return self.normal_conversation_cache[key] # Cache Hit
        pass

        # SOON
        #self.synapse_normal_embeddings_cache[key] = data

def score_conversation(session: str | list[str]):

    conversation: None | Conversation = None

    if isinstance(session, list[str]):
        Conversation = Conversation(role=session[])

    Senti = QuantumSentimentor()

    pass