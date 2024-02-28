import argparse
from PIL import Image, ImageDraw
import numpy as np
from sklearn.cluster import MiniBatchKMeans

def extract_edge_length(image):
    width, height = image.size
    if width > height:
        return height
    else:
        return width
def extract_palette(image, n_clusters=5):
    image = image.resize((100, 100))
    image_np = np.array(image)
    pixels = image_np.reshape(-1, image_np.shape[2])[:, :3]
    kmeans = MiniBatchKMeans(n_clusters=n_clusters).fit(pixels)
    common_colors = kmeans.cluster_centers_
    palette = ['#%02x%02x%02x' % (int(color[0]), int(color[1]), int(color[2])) for color in common_colors]

    print([palette])
    
    return palette

def extract_palette_and_edge_length(image_path, n_clusters=5):
    image = Image.open(image_path)
    edge_length = extract_edge_length(image)
    palette = extract_palette(image, n_clusters)
    return palette, edge_length

def attach_palette(image_path, palette, position, edge_length, border_width=10, border_color='black', output_path=None):
    image = Image.open(image_path)
    # Calculate the size of each palette square based on the edge length and number of colors
    palette_square_size = edge_length // len(palette)
    
    if position in ['top', 'bottom']:
        palette_height = palette_square_size + 2 * border_width
        palette_image = Image.new('RGB', (edge_length, palette_height))
    else:  # 'left', 'right'
        palette_width = palette_square_size + 2 * border_width
        palette_image = Image.new('RGB', (palette_width, edge_length))
    
    draw = ImageDraw.Draw(palette_image)
    for i, color in enumerate(palette):
        if position in ['top', 'bottom']:
            # Draw border rectangle
            draw.rectangle(
                [i * palette_square_size, 0, (i + 1) * palette_square_size, palette_height], 
                fill=border_color
            )
            # Draw color rectangle
            draw.rectangle(
                [i * palette_square_size + border_width, border_width, 
                 (i + 1) * palette_square_size - border_width, palette_height - border_width], 
                fill=color
            )
        else:  # 'left', 'right'
            # Draw border rectangle
            draw.rectangle(
                [0, i * palette_square_size, palette_width, (i + 1) * palette_square_size], 
                fill=border_color
            )
            # Draw color rectangle
            draw.rectangle(
                [border_width, i * palette_square_size + border_width, 
                 palette_width - border_width, (i + 1) * palette_square_size - border_width], 
                fill=color
            )
            
    if position == 'top':
        final_image = Image.new('RGB', (image.width, image.height + palette_square_size))
        final_image.paste(palette_image, (0, 0))
        final_image.paste(image, (0, palette_square_size))
    elif position == 'bottom':
        final_image = Image.new('RGB', (image.width, image.height + palette_square_size))
        final_image.paste(image, (0, 0))
        final_image.paste(palette_image, (0, image.height))
    elif position == 'left':
        final_image = Image.new('RGB', (image.width + palette_square_size, image.height))
        final_image.paste(palette_image, (0, 0))
        final_image.paste(image, (palette_square_size, 0))
    else:  # 'right'
        final_image = Image.new('RGB', (image.width + palette_square_size, image.height))
        final_image.paste(image, (0, 0))
        final_image.paste(palette_image, (image.width, 0))
    
    if output_path:
        final_image.save(output_path)
    else:
        final_image.show()

def main():
    parser = argparse.ArgumentParser(description='Attach a color palette to an image.')
    parser.add_argument('image_path', type=str, help='Path to the input image')
    parser.add_argument('--clusters', type=int, default=5, help='Number of color clusters')
    parser.add_argument('--position', choices=['left', 'right', 'top', 'bottom'], default='right', help='Position of the color palette')
    parser.add_argument('--border_width', type=int, default=2, help='Width of the border around color squares')
    parser.add_argument('--output', type=str, help='Path to the output image', default=None)
    args = parser.parse_args()

    palette, edge_length = extract_palette_and_edge_length(args.image_path, args.clusters)
    attach_palette(args.image_path, palette, args.position, edge_length, args.border_width, 'black', args.output)

if __name__ == "__main__":
    main()