from flask import Flask, render_template, request, jsonify
import requests, json
app = Flask(__name__)

# Created by Adrian Zmenda (adiq.eu)
# Project under MIT License

channels = {
  'pasha': 'pashaBiceps',
  'Snax': 'snaxik',
  'Byali': 'byalli',
  'TaZ': 'g5taz',
  'neo': 'neog5',
  'Izak': 'izakooo'
}

@app.route("/")
def index():
    return render_template('index.html', test=channels)

@app.route("/_get_status", methods=['POST'])
def getStatus():
    if request.form['channel']:
      try:
        api = requests.get('https://api.twitch.tv/kraken/streams/'+request.form['channel'])
        api = api.json()
      except:
        return jsonify(success=False)

      if api:
        try:
          return jsonify(success=True, online=True, channel=request.form['channel'], title=api['stream']['channel']['status'], game=api['stream']['channel']['game'], url=api['stream']['channel']['url'], viewers=api['stream']['viewers'], preview=api['stream']['preview']['medium'])
        except:
          return jsonify(success=True, online=False, channel=request.form['channel'])

      else:
        return jsonify(success=False)
    else:
      return jsonify(success=False)

if __name__ == "__main__":
    app.run()
