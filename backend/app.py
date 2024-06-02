from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import time
import os

app = Flask(__name__)
CORS(app)

# Define the path to the JSON file
json_file_path = os.path.join(os.path.dirname(__file__), 'filtered_data.json')

# Load music data from JSON file
with open(json_file_path, 'r') as f:
    music_data = json.load(f)

def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    i = 0
    j = 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1

def brute_force_search(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            return i
    return -1

def measure_time_brute_force(text, pattern, iterations=10000, repetitions=5):
    times = []
    for _ in range(repetitions):
        start_time = time.perf_counter()
        for _ in range(iterations):
            brute_force_search(text, pattern)
        end_time = time.perf_counter()
        average_time_ms = ((end_time - start_time) / iterations) * 1000
        times.append(average_time_ms)
    return sum(times) / len(times)

def measure_time_kmp(text, pattern, iterations=10000, repetitions=5):
    times = []
    for _ in range(repetitions):
        start_time = time.perf_counter()
        for _ in range(iterations):
            kmp_search(text, pattern)
        end_time = time.perf_counter()
        average_time_ms = ((end_time - start_time) / iterations) * 1000
        times.append(average_time_ms)
    return sum(times) / len(times)

@app.route('/api/autocomplete')
def autocomplete():
    query = request.args.get('q', '').lower()
    results = [music for music in music_data if query in (music["Track Name"] + " " + music["Artist Name(s)"]).lower()]
    return jsonify(results)

@app.route('/api/compare', methods=['POST'])
def compare():
    data = request.get_json()
    text = data['text']
    pattern = data['pattern']

    kmp_time = measure_time_kmp(text, pattern)
    brute_force_time = measure_time_brute_force(text, pattern)

    return jsonify({
        'kmp_time': kmp_time,
        'brute_force_time': brute_force_time
    })

if __name__ == '__main__':
    app.run(debug=True)
