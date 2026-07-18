class AiSlidesDeckBuilderClient:
    def build_outline(self, topic: str, slide_count: int = 5) -> dict:
        slides = [{"slide": 1, "title": f"Introduction to {topic}", "bullets": ["Overview", "Why it matters", "Key context"]}]
        for i in range(2, slide_count):
            slides.append({"slide": i, "title": f"Key Point {i-1}: {topic} Deep Dive", "bullets": ["Analysis", "Evidence", "Impact"]})
        slides.append({"slide": slide_count, "title": "Conclusion & Next Steps", "bullets": ["Summary", "Action items", "Q&A"]})
        return {"slides_outline": slides}
