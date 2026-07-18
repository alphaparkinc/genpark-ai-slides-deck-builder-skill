from client import AiSlidesDeckBuilderClient
client = AiSlidesDeckBuilderClient()
result = client.build_outline("AI Agent Market Landscape 2026", slide_count=4)
for slide in result['slides_outline']:
    print(f"Slide {slide['slide']}: {slide['title']}")
    print(f"  Bullets: {', '.join(slide['bullets'])}")
