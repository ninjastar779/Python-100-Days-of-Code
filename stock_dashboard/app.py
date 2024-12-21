from flask import Flask, render_template, jsonify, request, send_file
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stock/<symbol>')
def get_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        
        # Basic stock information
        stock_data = {
            'symbol': symbol.upper(),
            'name': info.get('longName', ''),
            'price': info.get('currentPrice', 0),
            'change': info.get('regularMarketChangePercent', 0),
            'volume': info.get('volume', 0),
            'marketCap': info.get('marketCap', 0),
            'peRatio': info.get('trailingPE', 0),
            'fiftyTwoWeekHigh': info.get('fiftyTwoWeekHigh', 0),
            'fiftyTwoWeekLow': info.get('fiftyTwoWeekLow', 0)
        }
        return jsonify({'success': True, 'data': stock_data})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/history/<symbol>')
def get_historical_data(symbol):
    try:
        period = request.args.get('period', '1y')
        stock = yf.Ticker(symbol)
        hist = stock.history(period=period)
        
        data = {
            'dates': hist.index.strftime('%Y-%m-%d').tolist(),
            'prices': hist['Close'].tolist(),
            'volumes': hist['Volume'].tolist()
        }
        return jsonify({'success': True, 'data': data})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/export/<symbol>')
def export_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period='1y')
        
        # Convert to CSV
        output = io.StringIO()
        hist.to_csv(output)
        
        # Create response
        mem = io.BytesIO()
        mem.write(output.getvalue().encode('utf-8'))
        mem.seek(0)
        output.close()
        
        return send_file(
            mem,
            mimetype='text/csv',
            as_attachment=True,
            download_name=f'{symbol}_historical_data.csv'
        )
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
