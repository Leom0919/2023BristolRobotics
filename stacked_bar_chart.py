import matplotlib.pyplot as plt

# Stacked percentages for each texture
textures = ['Felt', 'Mesh', 'Nylon', 'Acrylic', 'Fashion Fabric',
            'Fur', 'Canvas', 'Wool', 'Cotton', 'Wood']

traction_percentages = [23.4, 22.9, 21.9, 23.9, 22.1, 18.1, 21.9, 18.1, 20.0, 21.9]
roughness_percentages = [21.6, 23.9, 26.2, 23.1, 27.4, 21.5, 28.4, 29.4, 27.5, 25.3]
fineness_percentages = [23.3, 23.1, 24.8, 20.7, 23.1, 22.2, 23.8, 24.8, 23.2, 21.9]
hardness_percentages = [9.9, 22.1, 19.3, 21.0, 19.0, 26.8, 18.8, 18.8, 20.5, 21.4]
temperature_percentages = [21.8, 8.0, 7.9, 11.3, 8.5, 11.3, 7.2, 8.9, 8.7, 9.6]

# Set up the figure and axis
fig, ax = plt.subplots()

# Plot the stacked bars
ax.bar(textures, traction_percentages, label='Traction', color='b')
ax.bar(textures, roughness_percentages, bottom=traction_percentages, label='Roughness', color='g')
ax.bar(textures, fineness_percentages, bottom=[i+j for i,j in zip(traction_percentages, roughness_percentages)],
       label='Fineness', color='r')
ax.bar(textures, hardness_percentages, bottom=[i+j+k for i,j,k in zip(traction_percentages, roughness_percentages, fineness_percentages)],
       label='Hardness', color='orange')
ax.bar(textures, temperature_percentages, bottom=[i+j+k+l for i,j,k,l in zip(traction_percentages, roughness_percentages, fineness_percentages, hardness_percentages)],
       label='Temperature', color='purple')

# Set y-axis limits to 0-100%
ax.set_ylim(0, 100)

# Add a legend
ax.legend()

# Add labels and title
ax.set_xlabel('Texture')
ax.set_ylabel('Percentage')
ax.set_title('100% Stacked Bar Chart for Different Textures')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Display the plot
plt.tight_layout()
plt.show()
