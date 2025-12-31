"""
Simple Flask Application with CI/CD Pipeline
"""
from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Home page route."""
    return render_template('index.html')


@app.route('/api/health')
def health_check():
    """Health check endpoint for deployment verification."""
    return jsonify({
        'status': 'healthy',
        'message': 'Flask app is running!'
    })


@app.route('/api/info')
def app_info():
    """Application information endpoint."""
    return jsonify({
        'app': 'Flask CI/CD Demo',
        'version': '1.0.0',
        'author': 'DevOps Engineer'
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
