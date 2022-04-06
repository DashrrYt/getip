from flask import Flask, request, render_template
import requests 

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
  userip = "1.0.0.0"
  target = request.args.get('target_ip') 
  if target is None: 
    data = requests.get("https://api.freegeoip.app/json/?apikey=628c8330-b595-11ec-9657-43bfc64ad2ed").json()
    ip = data["ip"]
    country_code = data["country_code"]
    country_name = data["country_name"]
    region_code = data["region_code"]
    region_name = data["region_name"]
    city = data["city"]
    zip_code = data["zip_code"]
    time_zone = data["time_zone"]
    lat = data["latitude"]
    lon = data["longitude"]
  else: 
    data = requests.get(f"https://api.freegeoip.app/json/{target}?apikey=628c8330-b595-11ec-9657-43bfc64ad2ed").json()
    ip = data["ip"]
    country_code = data["country_code"]
    country_name = data["country_name"]
    region_code = data["region_code"]
    region_name = data["region_name"]
    city = data["city"]
    zip_code = data["zip_code"]
    time_zone = data["time_zone"]
    lat = data["latitude"]
    lon = data["longitude"]
  return render_template("app.html", userip=userip, country_code=country_code, country_name=country_name, region_code=region_code, region_name=region_name, city=city, zip_code=zip_code, time_zone=time_zone, lat=lat, lon=lon, ip=ip)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0")