from langchain_text_splitters import TokenTextSplitter

text = """
Generative AI is a type of artificial intelligence that creates new, original content—such as text, images, video, audio, or code—by learning patterns from existing data. Unlike traditional AI that classifies or analyzes data, GenAI uses deep learning models to generate novel outputs that resemble the training data.
 
Key Aspects of Generative AI:

How it Works: These models (e.g., GANs, Transformers) are trained on massive datasets to understand underlying structures and probabilities. When prompted, they predict and generate new, human-like content.
"""

#cl100k_base is a tokenizer encoding provided by OpenAI’s tiktoken library.
text_splitter = TokenTextSplitter(
    encoding_name="cl100k_base",
    chunk_size=100,
    chunk_overlap=20
)

chunks = text_splitter.split_text(text)

print(f"total chunks {len(chunks)}")

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n")