let priceChart;

async function searchStock() {
    const symbol = document.getElementById('stockSymbol').value.trim();
    if (!symbol) return;

    try {
        // Fetch stock data
        const response = await fetch(`/api/stock/${symbol}`);
        const result = await response.json();

        if (!result.success) {
            alert('Error fetching stock data');
            return;
        }

        updateStockInfo(result.data);
        await updateChart('1y');
    } catch (error) {
        console.error('Error:', error);
        alert('Error fetching stock data');
    }
}

function updateStockInfo(data) {
    document.getElementById('symbol').textContent = data.symbol;
    document.getElementById('price').textContent = formatCurrency(data.price);
    
    const changeElement = document.getElementById('change');
    changeElement.textContent = formatPercentage(data.change);
    changeElement.className = `value ${data.change >= 0 ? 'positive' : 'negative'}`;
    
    document.getElementById('volume').textContent = formatNumber(data.volume);
    document.getElementById('marketCap').textContent = formatCurrency(data.marketCap);
    document.getElementById('peRatio').textContent = formatNumber(data.peRatio, 2);
    document.getElementById('high52').textContent = formatCurrency(data.fiftyTwoWeekHigh);
    document.getElementById('low52').textContent = formatCurrency(data.fiftyTwoWeekLow);
}

async function updateChart(period) {
    const symbol = document.getElementById('stockSymbol').value.trim();
    if (!symbol) return;

    try {
        const response = await fetch(`/api/history/${symbol}?period=${period}`);
        const result = await response.json();

        if (!result.success) {
            alert('Error fetching historical data');
            return;
        }

        createChart(result.data);
    } catch (error) {
        console.error('Error:', error);
        alert('Error fetching historical data');
    }
}

function createChart(data) {
    const ctx = document.getElementById('priceChart').getContext('2d');
    
    if (priceChart) {
        priceChart.destroy();
    }

    priceChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.dates,
            datasets: [{
                label: 'Price',
                data: data.prices,
                borderColor: '#2962ff',
                backgroundColor: 'rgba(41, 98, 255, 0.1)',
                borderWidth: 2,
                fill: true,
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                x: {
                    grid: {
                        color: 'rgba(255, 255, 255, 0.1)'
                    },
                    ticks: {
                        color: '#a0a0a0'
                    }
                },
                y: {
                    grid: {
                        color: 'rgba(255, 255, 255, 0.1)'
                    },
                    ticks: {
                        color: '#a0a0a0'
                    }
                }
            }
        }
    });
}

async function exportData() {
    const symbol = document.getElementById('stockSymbol').value.trim();
    if (!symbol) return;

    try {
        window.location.href = `/api/export/${symbol}`;
    } catch (error) {
        console.error('Error:', error);
        alert('Error exporting data');
    }
}

// Utility functions
function formatCurrency(value) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 2
    }).format(value);
}

function formatNumber(value, decimals = 0) {
    return new Intl.NumberFormat('en-US', {
        minimumFractionDigits: decimals,
        maximumFractionDigits: decimals
    }).format(value);
}

function formatPercentage(value) {
    return `${(value >= 0 ? '+' : '')}${value.toFixed(2)}%`;
}
