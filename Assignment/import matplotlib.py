import matplotlib.pyplot as plt

# Example valuation data
values = {
    "Discounted Cash Flow": [80, 120],
    "Comparable Companies": [90, 110],
    "Precedent Transactions": [85, 130],
    "LBO Analysis": [95, 125],
    "Analyst Targets": [100, 140]
}

# Sort for visual consistency
methods = list(values.keys())
min_values = [v[0] for v in values.values()]
max_values = [v[1] for v in values.values()]
ranges = [max_val - min_val for min_val, max_val in zip(min_values, max_values)]

# Plot
fig, ax = plt.subplots(figsize=(10, 5))
y_positions = range(len(methods))

# Draw bars
for i, (method, val_range) in enumerate(values.items()):
    ax.barh(i, val_range[1] - val_range[0], left=val_range[0], height=0.4, color="#5DADE2", edgecolor='black')

# Add method labels to the y-axis
ax.set_yticks(y_positions)
ax.set_yticklabels(methods)

# Format axes
ax.set_xlabel('Valuation ($ millions)')
ax.set_title('Valuation Football Field')
ax.grid(True, axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()

# Show plot
plt.show()
