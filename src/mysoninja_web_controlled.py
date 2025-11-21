#!/data/data/com.termux/files/usr/bin/python3
import os
import sys
import json
import threading
import time
import random
import subprocess
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ========== ENHANCED WEB-CONTROLLED MODULES ==========

class WebPhishingGenerator:
    def __init__(self):
        self.active_campaigns = []
        self.ngrok_url = None
        self.templates = {
            "facebook": {"name": "Facebook Login", "urgency": "high"},
            "gmail": {"name": "Gmail Access", "urgency": "critical"},
            "instagram": {"name": "Instagram Copyright", "urgency": "medium"},
            "linkedin": {"name": "LinkedIn Job Alert", "urgency": "high"},
            "microsoft": {"name": "Microsoft Security", "urgency": "critical"}
        }
    
    def generate_phishing_page(self, platform, target_email=None, custom_message=None, enable_ngrok=False):
        campaign_id = f"web_phish_{int(time.time())}"
        
        # AI-generated content
        ai_content = self._generate_ai_content(platform, target_email, custom_message)
        
        campaign = {
            "id": campaign_id,
            "platform": platform,
            "status": "GENERATED",
            "phishing_url": f"http://phish-{campaign_id}.local:8080",
            "ngrok_url": self.ngrok_url,
            "ai_content": ai_content,
            "credentials_file": f"web_data/{campaign_id}_creds.txt",
            "generated_at": time.time(),
            "visitors": 0,
            "credentials_captured": 0
        }
        
        if enable_ngrok and self.ngrok_url:
            campaign["live_url"] = f"{self.ngrok_url}/{campaign_id}"
        
        self.active_campaigns.append(campaign)
        return campaign
    
    def _generate_ai_content(self, platform, target_email, custom_message):
        subjects = {
            "facebook": ["Security Alert: Unusual Login Attempt", "Action Required: Verify Your Account"],
            "gmail": ["Google Security: Verify Your Identity", "Critical: Account Access Review"],
            "instagram": ["Copyright Claim: Action Required", "Your Content Has Been Reported"]
        }
        
        return {
            "subject": random.choice(subjects.get(platform, ["Security Alert"])),
            "message": custom_message or f"Your {platform} account requires immediate attention.",
            "urgency": self.templates[platform]["urgency"],
            "call_to_action": "Click here to secure your account",
            "branding": f"{platform} Security Team",
            "ai_confidence": f"{random.randint(85, 98)}%"
        }
    
    def start_ngrok(self, port=8080):
        try:
            # Check if ngrok is installed
            result = subprocess.run(["ngrok", "version"], capture_output=True, text=True)
            if result.returncode != 0:
                return {"error": "Ngrok not installed. Run: pkg install ngrok"}
            
            # Start ngrok tunnel
            ngrok_process = subprocess.Popen([
                "ngrok", "http", str(port),
                "--log=stdout",
                "--log-level=debug"
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Wait for ngrok to start and get URL
            time.sleep(3)
            
            # Get ngrok public URL
            try:
                response = requests.get("http://localhost:4040/api/tunnels")
                tunnels = response.json()
                public_url = tunnels["tunnels"][0]["public_url"]
                self.ngrok_url = public_url
                return {"success": True, "ngrok_url": public_url}
            except:
                return {"error": "Failed to get ngrok URL"}
                
        except Exception as e:
            return {"error": f"Ngrok error: {str(e)}"}

class WebTargetManager:
    def __init__(self):
        self.targets_file = "web_data/targets.json"
        self.targets = self._load_targets()
    
    def _load_targets(self):
        try:
            os.makedirs("web_data", exist_ok=True)
            if os.path.exists(self.targets_file):
                with open(self.targets_file, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {"ips": [], "domains": [], "emails": [], "credentials": []}
    
    def save_targets(self):
        try:
            with open(self.targets_file, 'w') as f:
                json.dump(self.targets, f, indent=2)
            return True
        except:
            return False
    
    def add_target_ip(self, ip, description=""):
        target = {"ip": ip, "description": description, "added": time.time()}
        self.targets["ips"].append(target)
        self.save_targets()
        return target
    
    def add_target_domain(self, domain, description=""):
        target = {"domain": domain, "description": description, "added": time.time()}
        self.targets["domains"].append(target)
        self.save_targets()
        return target
    
    def add_target_email(self, email, description=""):
        target = {"email": email, "description": description, "added": time.time()}
        self.targets["emails"].append(target)
        self.save_targets()
        return target

class WebNetworkAttacker:
    def __init__(self):
        self.scan_results = []
        self.active_scans = {}
    
    def web_nmap_scan(self, target, scan_type="quick"):
        scan_id = f"scan_{int(time.time())}"
        
        scan_commands = {
            "quick": f"nmap -T4 -F {target}",
            "comprehensive": f"nmap -sS -sV -sC -O -T4 {target}",
            "stealth": f"nmap -sS -T2 {target}",
            "vulnerability": f"nmap --script vuln {target}"
        }
        
        scan_data = {
            "id": scan_id,
            "target": target,
            "type": scan_type,
            "command": scan_commands[scan_type],
            "status": "RUNNING",
            "started_at": time.time(),
            "progress": "0%",
            "results": ""
        }
        
        # Start scan in background thread
        thread = threading.Thread(target=self._run_web_scan, args=(scan_data,))
        thread.daemon = True
        thread.start()
        
        self.active_scans[scan_id] = scan_data
        return scan_data
    
    def _run_web_scan(self, scan_data):
        try:
            # Simulate scan progress
            for i in range(5):
                time.sleep(2)
                scan_data["progress"] = f"{((i+1)/5)*100}%"
            
            # Simulate realistic results
            open_ports = random.sample([22, 80, 443, 21, 25, 53, 110, 143, 993, 995, 8080, 8443], random.randint(2, 6))
            services = {
                22: "ssh", 80: "http", 443: "https", 21: "ftp", 
                25: "smtp", 53: "dns", 8080: "http-proxy", 8443: "https-alt"
            }
            
            results = f"Nmap scan report for {scan_data['target']}\\n"
            results += "PORT     STATE SERVICE\\n"
            for port in sorted(open_ports):
                service = services.get(port, "unknown")
                results += f"{port}/tcp  open  {service}\\n"
            
            scan_data["results"] = results
            scan_data["status"] = "COMPLETED"
            scan_data["completed_at"] = time.time()
            
            self.scan_results.append(scan_data.copy())
            
        except Exception as e:
            scan_data["status"] = "FAILED"
            scan_data["error"] = str(e)

class QuantumAI:
    def __init__(self):
        self.intelligence_level = 1.0
        self.attack_plans = []
    
    def generate_attack_plan(self, targets):
        plan_id = f"plan_{int(time.time())}"
        
        plan = {
            "id": plan_id,
            "targets": targets,
            "blue_team_strength": random.randint(3, 8),
            "success_probability": f"{random.randint(75, 95)}%",
            "estimated_time": f"{random.randint(5, 30)} minutes",
            "ai_confidence": f"{random.randint(85, 98)}%",
            "recommended_actions": [
                "Start with network reconnaissance to map attack surface",
                "Deploy targeted phishing campaigns based on discovered services",
                "Attempt credential spraying against SSH and web services",
                "Use discovered vulnerabilities for initial access",
                "Establish persistence and move laterally"
            ]
        }
        self.attack_plans.append(plan)
        return plan
    
    def evolve(self):
        self.intelligence_level += random.uniform(0.1, 0.5)
        new_capabilities = random.sample([
            "Advanced Evasion Techniques",
            "Behavioral Prediction", 
            "Automated Tool Selection",
            "Real-time Adaptation"
        ], random.randint(1, 3))
        
        return {
            "success": True,
            "new_intelligence": round(self.intelligence_level, 2),
            "message": f"QUANTUM AI EVOLVED TO LEVEL {self.intelligence_level:.2f}",
            "new_capabilities": new_capabilities
        }

class WirelessAttacker:
    def __init__(self):
        self.active_attacks = []
    
    def start_wireless_attack(self, attack_type, bssid):
        attack_id = f"wireless_{int(time.time())}"
        
        attack_data = {
            "id": attack_id,
            "type": attack_type,
            "bssid": bssid,
            "status": "RUNNING",
            "started_at": time.time()
        }
        
        # Simulate wireless attack
        thread = threading.Thread(target=self._run_wireless_attack, args=(attack_data,))
        thread.daemon = True
        thread.start()
        
        self.active_attacks.append(attack_data)
        return attack_data
    
    def _run_wireless_attack(self, attack_data):
        try:
            time.sleep(8)  # Simulate attack duration
            
            # Simulate results based on attack type
            if attack_data["type"] == "wpa2":
                attack_data["results"] = f"WPA2 handshake captured for {attack_data['bssid']}"
            elif attack_data["type"] == "wps":
                attack_data["results"] = f"WPS PIN cracked for {attack_data['bssid']}"
            elif attack_data["type"] == "evil_twin":
                attack_data["results"] = f"Evil twin deployed for {attack_data['bssid']}"
            else:
                attack_data["results"] = f"Deauthentication attack completed on {attack_data['bssid']}"
            
            attack_data["status"] = "COMPLETED"
            
        except Exception as e:
            attack_data["status"] = "FAILED"
            attack_data["error"] = str(e)

# ========== ENHANCED CORE ==========
class MysoninjaWebControlled:
    def __init__(self):
        self.phishing = WebPhishingGenerator()
        self.targets = WebTargetManager()
        self.network = WebNetworkAttacker()
        self.ai = QuantumAI()
        self.wireless = WirelessAttacker()
    
    def get_dashboard_stats(self):
        return {
            "total_targets": len(self.targets.targets["ips"]) + len(self.targets.targets["domains"]),
            "active_phishing": len(self.phishing.active_campaigns),
            "completed_scans": len(self.network.scan_results),
            "ai_intelligence": self.ai.intelligence_level
        }

web_core = MysoninjaWebControlled()

# ========== ENHANCED WEB ROUTES ==========

@app.route('/')
def dashboard():
    return render_template('demon_dashboard.html')

@app.route('/api/dashboard/stats')
def dashboard_stats():
    return jsonify(web_core.get_dashboard_stats())

@app.route('/api/targets/get')
def get_all_targets():
    return jsonify(web_core.targets.targets)

@app.route('/api/targets/<target_type>/add', methods=['POST'])
def add_target(target_type):
    data = request.json
    if target_type == 'ip':
        target = web_core.targets.add_target_ip(data.get('ip'), data.get('description', ''))
    elif target_type == 'domain':
        target = web_core.targets.add_target_domain(data.get('domain'), data.get('description', ''))
    elif target_type == 'email':
        target = web_core.targets.add_target_email(data.get('email'), data.get('description', ''))
    else:
        return jsonify({"error": "Invalid target type"})
    
    return jsonify({"success": True, "target": target})

@app.route('/api/phishing/generate', methods=['POST'])
def generate_phishing():
    data = request.json
    campaign = web_core.phishing.generate_phishing_page(
        data.get('platform', 'facebook'),
        data.get('target_email'),
        data.get('custom_message'),
        data.get('enable_ngrok', False)
    )
    return jsonify(campaign)

@app.route('/api/ngrok/start', methods=['POST'])
def start_ngrok():
    result = web_core.phishing.start_ngrok()
    return jsonify(result)

@app.route('/api/network/scan', methods=['POST'])
def start_network_scan():
    data = request.json
    scan = web_core.network.web_nmap_scan(data.get('target'), data.get('type', 'quick'))
    return jsonify(scan)

@app.route('/api/network/scans/<scan_id>')
def get_scan_status(scan_id):
    scan = web_core.network.active_scans.get(scan_id, {})
    return jsonify(scan)

@app.route('/api/ai/generate-plan', methods=['POST'])
def generate_ai_plan():
    data = request.json
    targets = data.get('targets', [])
    plan = web_core.ai.generate_attack_plan(targets)
    return jsonify(plan)

@app.route('/api/ai/evolve', methods=['POST'])
def evolve_ai():
    result = web_core.ai.evolve()
    return jsonify(result)

@app.route('/api/wireless/attack', methods=['POST'])
def start_wireless_attack():
    data = request.json
    attack = web_core.wireless.start_wireless_attack(
        data.get('attack_type'),
        data.get('bssid')
    )
    return jsonify(attack)

if __name__ == '__main__':
    print("🗡️ 冥忍 MYSŌNINJA ULTIMATE - OONI DEMON EDITION")
    print("🔮 Created by MysteryAK & Knightdale")
    print("🌐 Ngrok Integration: ACTIVE")
    print("🌑 Access: http://127.0.0.1:5000")
    print("😈 Let the cyber warfare begin...")
    app.run(host='127.0.0.1', port=5000, debug=False)
