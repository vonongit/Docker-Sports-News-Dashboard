from flask import Flask, jsonify
from flask_cors import CORS
import requests
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# API Keys (we'll use free tiers)
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', 'demo')  # We'll get this later
NEWS_API_KEY = os.getenv('NEWS_API_KEY', 'demo')  # We'll get this later

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'sports-news-api',
        'timestamp': datetime.now().isoformat()
    }), 200

@app.route('/api/nba/scores', methods=['GET'])
def get_nba_scores():
    """Get live NBA scores"""
    try:
        # Using free NBA API
        url = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"
        response = requests.get(url, timeout=5)
        data = response.json()
        
        games = []
        for event in data.get('events', []):
            competition = event['competitions'][0]
            game = {
                'id': event['id'],
                'date': event['date'],
                'status': competition['status']['type']['description'],
                'home_team': {
                    'name': competition['competitors'][0]['team']['displayName'],
                    'abbreviation': competition['competitors'][0]['team']['abbreviation'],
                    'score': competition['competitors'][0]['score'],
                    'logo': competition['competitors'][0]['team']['logo']
                },
                'away_team': {
                    'name': competition['competitors'][1]['team']['displayName'],
                    'abbreviation': competition['competitors'][1]['team']['abbreviation'],
                    'score': competition['competitors'][1]['score'],
                    'logo': competition['competitors'][1]['team']['logo']
                }
            }
            games.append(game)
        
        return jsonify(games), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/nfl/scores', methods=['GET'])
def get_nfl_scores():
    """Get live NFL scores"""
    try:
        # Using free ESPN NFL API
        url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"
        response = requests.get(url, timeout=5)
        data = response.json()
        
        games = []
        for event in data.get('events', []):
            competition = event['competitions'][0]
            game = {
                'id': event['id'],
                'date': event['date'],
                'status': competition['status']['type']['description'],
                'home_team': {
                    'name': competition['competitors'][0]['team']['displayName'],
                    'abbreviation': competition['competitors'][0]['team']['abbreviation'],
                    'score': competition['competitors'][0]['score'],
                    'logo': competition['competitors'][0]['team']['logo']
                },
                'away_team': {
                    'name': competition['competitors'][1]['team']['displayName'],
                    'abbreviation': competition['competitors'][1]['team']['abbreviation'],
                    'score': competition['competitors'][1]['score'],
                    'logo': competition['competitors'][1]['team']['logo']
                }
            }
            games.append(game)
        
        return jsonify(games), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/weather', methods=['GET'])
def get_weather():
    """Get weather for Charlotte, NC"""
    try:
        # Using free OpenWeather API
        url = f"https://api.openweathermap.org/data/2.5/weather?q=Charlotte,NC,US&appid={WEATHER_API_KEY}&units=imperial"
        response = requests.get(url, timeout=5)
        data = response.json()
        
        weather = {
            'temperature': round(data['main']['temp']),
            'feels_like': round(data['main']['feels_like']),
            'description': data['weather'][0]['description'].title(),
            'icon': data['weather'][0]['icon'],
            'humidity': data['main']['humidity'],
            'wind_speed': round(data['wind']['speed'])
        }
        
        return jsonify(weather), 200
    except Exception as e:
        return jsonify({'error': str(e), 'message': 'Using demo data'}), 200

@app.route('/api/news', methods=['GET'])
def get_news():
    """Get top news headlines"""
    try:
        # Using free NewsAPI
        url = f"https://newsapi.org/v2/top-headlines?country=us&pageSize=5&apiKey={NEWS_API_KEY}"
        response = requests.get(url, timeout=5)
        data = response.json()
        
        articles = []
        for article in data.get('articles', []):
            articles.append({
                'title': article['title'],
                'description': article.get('description', ''),
                'url': article['url'],
                'source': article['source']['name'],
                'published_at': article['publishedAt']
            })
        
        return jsonify(articles), 200
    except Exception as e:
        return jsonify({'error': str(e), 'message': 'Using demo data'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
