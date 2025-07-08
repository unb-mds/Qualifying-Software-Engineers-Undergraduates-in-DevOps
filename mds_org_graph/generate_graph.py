import requests
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import os
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.patches as patches
from PIL import Image, ImageDraw

BASE_URL = "https://api.github.com"
ORG_NAME = "unb-mds"
TOKEN = "seu_token"

headers = {"Authorization": f"Bearer {TOKEN}"}

def get_repos(org_name):
    url = f"{BASE_URL}/orgs/{org_name}/repos"
    repos = []
    page = 1

    while True:
        response = requests.get(url, headers=headers, params={"page": page, "per_page": 100})
        if response.status_code != 200:
            print(f"Erro ao obter repositórios: {response.json()}")
            break
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1

    return [repo["name"] for repo in repos]

def get_contributors(repo_name):
    url = f"{BASE_URL}/repos/{ORG_NAME}/{repo_name}/contributors"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Erro ao obter contribuidores para {repo_name}: {response.json()}")
        return []
    return [contributor["login"] for contributor in response.json()]

def get_user_name(username):
    return username  

def download_user_photo(username):
    url = f"{BASE_URL}/users/{username}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        photo_url = data.get("avatar_url")
        if photo_url:
            img_response = requests.get(photo_url)
            if img_response.status_code == 200:
                content_type = img_response.headers.get("Content-Type")
                if "image/png" in content_type or "image/jpeg" in content_type:
                    img_data = img_response.content
                    extension = "png" if "image/png" in content_type else "jpg"
                    photo_path = f"photos/{username}.{extension}"
                    with open(photo_path, "wb") as file:
                        file.write(img_data)
                    return photo_path
    return None

if not os.path.exists("photos"):
    os.makedirs("photos")

repos = get_repos(ORG_NAME)
relations = []
excluded_contributors = {"arthurbdiniz", "devto-bot"}

for repo in repos:
    contributors = get_contributors(repo)
    contributors = [contrib for contrib in contributors if contrib not in excluded_contributors]
    contributor_names = [get_user_name(contrib) for contrib in contributors if get_user_name(contrib)]
    for i, contrib1 in enumerate(contributor_names):
        for contrib2 in contributor_names[i + 1:]:
            relations.append((contrib1, contrib2))

df = pd.DataFrame(relations, columns=["Contribuidor 1", "Contribuidor 2"])
df.to_csv("relations.csv", index=False)

user_photos = {}
for user in df["Contribuidor 1"].unique():
    photo_path = download_user_photo(user)
    if photo_path:
        user_photos[user] = photo_path

def round_image(image_path, output_size=(50, 50)):
    try:
        img = Image.open(image_path).convert("RGBA")
        img = img.resize(output_size, Image.Resampling.LANCZOS)

        mask = Image.new('L', output_size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + output_size, fill=255)

        rounded_img = Image.new('RGBA', output_size)
        rounded_img.paste(img, (0, 0), mask)
        
        return rounded_img
    except Exception as e:
        print(f"Erro ao processar a imagem {image_path}: {e}")
        return None

def add_image_to_graph(ax, image, pos, zoom=0.3):
    img = OffsetImage(image, zoom=zoom)
    ab = AnnotationBbox(img, pos, frameon=False, pad=0)
    ax.add_artist(ab)

G = nx.Graph()
G.add_edges_from(relations)

plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G, k=1.2, seed=42, iterations=200)

def adjust_overlap(positions, threshold=0.1, max_iterations=100):
    for _ in range(max_iterations):
        adjusted = False
        for node1, pos1 in positions.items():
            for node2, pos2 in positions.items():
                if node1 != node2:
                    dx = pos2[0] - pos1[0]
                    dy = pos2[1] - pos1[1]
                    distance = (dx**2 + dy**2)**0.5
                    if distance < threshold:
                        force = (threshold - distance) / distance if distance != 0 else 0.1
                        positions[node2] = (pos2[0] + dx * force, pos2[1] + dy * force)
                        adjusted = True
        if not adjusted:
            break
    return positions

def adjust_label_and_node_overlap(label_positions, node_positions, threshold=0.05, offset=0.05, max_iterations=200):
    for _ in range(max_iterations):
        adjusted = False
        for label, label_pos in label_positions.items():
            for node, node_pos in node_positions.items():
                dx = label_pos[0] - node_pos[0]
                dy = label_pos[1] - node_pos[1]
                distance = (dx**2 + dy**2)**0.5
                if distance < threshold:
                    force_x = dx / distance if distance != 0 else 0.1
                    force_y = dy / distance if distance != 0 else 0.1
                    label_positions[label] = (
                        label_pos[0] + force_x * offset,
                        label_pos[1] + force_y * offset,
                    )
                    adjusted = True
        if not adjusted:
            break
    return label_positions

pos = adjust_overlap(pos)  
label_positions = {node: (coord[0], coord[1] - 0.05) for node, coord in pos.items()}
label_positions = adjust_label_and_node_overlap(label_positions, pos)

ax = plt.gca()
nx.draw_networkx_nodes(G, pos, node_size=50, node_color="gray", alpha=1.0)
nx.draw_networkx_edges(G, pos, width=0.1, alpha=0.5, edge_color="gray")
nx.draw_networkx_labels(G, label_positions, font_size=3, font_color="black")

for node, (x, y) in pos.items():
    if node in user_photos:
        image_path = user_photos[node]
        rounded_img = round_image(image_path)
        add_image_to_graph(ax, rounded_img, (x, y))

plt.axis("off")
plt.tight_layout()
plt.savefig(os.path.expanduser("~/Downloads/graph.png"), dpi=300)