# app.py
import random

# Sample dataset
songs = [
    {"title": "Shake It Off", "singer": "Taylor Swift", "mood": "happy"},
    {"title": "Love Story", "singer": "Taylor Swift", "mood": "romantic"},
    {"title": "Someone Like You", "singer": "Adele", "mood": "sad"},
    {"title": "Rolling in the Deep", "singer": "Adele", "mood": "energetic"},
    {"title": "Perfect", "singer": "Ed Sheeran", "mood": "romantic"},
    {"title": "Shape of You", "singer": "Ed Sheeran", "mood": "party"},
    {"title": "Calm Down", "singer": "Rema", "mood": "calm"},
    {"title": "Happy Vibes", "singer": "Arijit Singh", "mood": "energetic"},
    {"title": "Tum Hi Ho", "singer": "Arijit Singh", "mood": "romantic"},
]

def recommend_song(mood, singer):
    # First priority → Singer + Mood
    matches = [s for s in songs if s["mood"] == mood and s["singer"].lower() == singer.lower()]
    if matches:
        return random.choice(matches)

    # Second priority → Same Mood
    mood_matches = [s for s in songs if s["mood"] == mood]
    if mood_matches:
        return random.choice(mood_matches)

    # Third priority → Any song by singer
    singer_matches = [s for s in songs if s["singer"].lower() == singer.lower()]
    if singer_matches:
        return random.choice(singer_matches)

    # Last → Any song
    return random.choice(songs)

if __name__ == "__main__":
    print("🎵 Welcome to VibeTune 🎶")
    mood = input("Enter your mood (happy, sad, energetic, calm, romantic, party): ")
    singer = input("Enter your favorite singer: ")

    song = recommend_song(mood, singer)
    print(f"✅ Recommended Song: '{song['title']}' by {song['singer']}")
