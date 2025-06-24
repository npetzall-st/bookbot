def get_word_count(text: str) -> int:
    return len(text.split())

def get_character_stats(text: str) -> dict[str, int]:
    stats = {}
    for c in text.lower():
        stats[c] = stats.get(c, 0) + 1
    return stats

def sort_character_stats(stats: dict[str, int]) -> list[dict]:
    stats_list = [{"char": k, "num": v} for k, v in stats.items()]
    stats_list.sort(key=lambda item: item["num"], reverse=True)
    return stats_list