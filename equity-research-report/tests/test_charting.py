import pytest
from src.charting import create_price_history_chart

def test_create_price_history_chart():
    # Sample data for testing
    sample_data = {
        'dates': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'prices': [100, 102, 101]
    }
    
    # Call the function to create a chart
    chart = create_price_history_chart(sample_data['dates'], sample_data['prices'])
    
    # Check if the chart is created successfully
    assert chart is not None
    assert 'figure' in chart  # Assuming the chart is a dictionary with a 'figure' key
    assert len(chart['figure']['data']) > 0  # Ensure there is data in the chart

def test_create_price_history_chart_empty_data():
    # Test with empty data
    sample_data = {
        'dates': [],
        'prices': []
    }
    
    chart = create_price_history_chart(sample_data['dates'], sample_data['prices'])
    
    # Check if the chart handles empty data gracefully
    assert chart is not None
    assert 'figure' in chart
    assert len(chart['figure']['data']) == 0  # Ensure no data in the chart

# Additional tests can be added as needed for more coverage