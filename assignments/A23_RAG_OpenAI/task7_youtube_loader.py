from langchain_community.document_loaders import YoutubeLoader

video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

loader = YoutubeLoader.from_youtube_url(
    video_url,
    add_video_info=True
)

docs = loader.load()

print("Transcript Loaded")

print(docs[0].page_content[:1000])