# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Data for the services
name = "Macro Conseil & Assistance"
tagline = "Expertise in Cybersecurity and IT Services"
services = {
    "Cybersecurity": [
        {"Service": "Vulnerability Management", "Description": "Identify, analyze, and fix security flaws."},
        {"Service": "Risk Assessment", "Description": "Perform risk assessments to identify potential threats."}
    ],
    "IT Services": [
        {"Service": "IT Infrastructure Setup", "Description": "Design and deploy IT infrastructures."},
        {"Service": "Cloud Migration", "Description": "Assist with seamless migration to cloud platforms."}
    ]
}

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html', name=name, tagline=tagline, services=services)

# Serve static files (CSS and JS) from the root directory
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.getcwd(), filename)

if __name__ == '__main__':
    app.run(debug=True)