from matplotlib import pyplot as plt
import pandas as pd

def create_price_history_chart(data):
    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['Price'], label='Price History', color='blue')
    plt.title('Stock Price History')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig('price_history_chart.png')
    plt.close()

def create_asx200_performance_chart(data):
    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['ASX200'], label='ASX200 Performance', color='green')
    plt.title('ASX200 Performance')
    plt.xlabel('Date')
    plt.ylabel('Index Value')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig('asx200_performance_chart.png')
    plt.close()