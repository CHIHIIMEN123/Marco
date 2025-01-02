# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
from flask import Flask, render_template

# Créer l'application Flask
app = Flask(__name__)

class MacroConseilAssistance:
    def __init__(self):
        self.name = "Macro Conseil & Assistance"
        self.tagline = "Expertise in Cybersecurity and IT Services"
        self.services = {
            "Cybersecurity": [
                {"Service": "Vulnerability Management", "Description": "Identify, analyze, and fix security flaws in IT and OT infrastructure."},
                {"Service": "Risk Assessment", "Description": "Perform risk assessments to identify potential threats."},
                {"Service": "Security Audit & Compliance", "Description": "Conduct audits for cybersecurity standards."},
                {"Service": "Penetration Testing", "Description": "Simulate real-world attacks to uncover vulnerabilities."},
                {"Service": "Incident Management", "Description": "Manage and resolve security incidents quickly."},
                {"Service": "Cloud Security", "Description": "Secure public, private, or hybrid cloud infrastructures."},
                {"Service": "IoT and OT Security", "Description": "Protect IoT and OT environments with vulnerability management."},
            ],
            "IT Services": [
                {"Service": "IT Infrastructure Setup", "Description": "Design and deploy IT infrastructures tailored to business needs."},
                {"Service": "System Administration", "Description": "Provide system monitoring and troubleshooting."},
                {"Service": "Cloud Migration", "Description": "Assist with seamless migration to cloud platforms."},
                {"Service": "IT Support & Maintenance", "Description": "Offer technical support and routine maintenance."},
                {"Service": "Data Backup & Recovery", "Description": "Provide reliable data backup solutions."},
                {"Service": "Network Security", "Description": "Enhance network resilience with security measures."},
                {"Service": "Software Development", "Description": "Deliver custom software solutions for business needs."},
            ],
        }

    def get_services(self):
        return self.services

company = MacroConseilAssistance()

# Route pour afficher la page d'accueil avec les services
@app.route('/')
def home():
    services = company.get_services()
    return render_template('index.html', name=company.name, tagline=company.tagline, services=services)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)