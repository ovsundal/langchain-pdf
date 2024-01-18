from langchain.chains import ConversationalRetrievalChain
from app.chat.chains.streamable import StreamableChain


# mixin
class StreamingConversationalRetrievalChain(StreamableChain, ConversationalRetrievalChain):
    pass