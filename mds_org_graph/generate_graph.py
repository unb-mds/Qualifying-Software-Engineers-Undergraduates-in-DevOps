import requests
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import os
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import json
import subprocess

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
                else:
                    print(f"A URL da foto de {username} não retornou uma imagem PNG ou JPEG válida.")
            else:
                print(f"Erro ao tentar baixar a foto de {username}: {img_response.status_code}")
    else:
        print(f"Erro ao obter informações para {username}: {response.json()}")
    return None

if not os.path.exists("photos"):
    os.makedirs("photos")

repos = get_repos(ORG_NAME)
print(f"Repos encontrados: {len(repos)}")

relations = []
excluded_contributors = {"arthurbdiniz", "devto-bot"}

for repo in repos:
    contributors = get_contributors(repo)
    print(f"{repo}: {len(contributors)} contribuidores")
    contributors = [contrib for contrib in contributors if contrib not in excluded_contributors]
    contributor_names = [get_user_name(contrib) for contrib in contributors if get_user_name(contrib)]
    for i, contrib1 in enumerate(contributor_names):
        for contrib2 in contributor_names[i + 1:]:
            relations.append((contrib1, contrib2))

relations = [(c1, c2) for c1, c2 in relations if c1 and c2]

df = pd.DataFrame(relations, columns=["Contribuidor 1", "Contribuidor 2"])
df.to_csv("relations.csv", index=False)

user_photos = {}
for user in df["Contribuidor 1"].unique():
    photo_path = download_user_photo(user)
    if photo_path:
        user_photos[user] = photo_path

print("Fotos baixadas com sucesso!")

# Executar  posteriormente
G = nx.Graph()
G.add_edges_from(relations)

plt.figure(figsize=(28, 20))  
pos = nx.spring_layout(G, k=12.0, seed=42, iterations=2000)

with open("pos.json", "w") as f:
    json.dump({node: pos[node].tolist() for node in pos}, f)

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

def adjust_label_and_node_overlap(label_positions, node_positions, threshold=0.05, offset=0.03, max_iterations=200):
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
        
        for label1, pos1 in label_positions.items():
            for label2, pos2 in label_positions.items():
                if label1 != label2:
                    dx = pos2[0] - pos1[0]
                    dy = pos2[1] - pos1[1]
                    distance = (dx**2 + dy**2)**0.5
                    if distance < threshold:
                        force_x = dx / distance if distance != 0 else 0.1
                        force_y = dy / distance if distance != 0 else 0.1
                        label_positions[label2] = (
                            pos2[0] + force_x * offset,
                            pos2[1] + force_y * offset,
                        )
                        adjusted = True
        
        if not adjusted:
            break
    return label_positions

pos = adjust_overlap(pos)  

label_positions = {node: (coord[0], coord[1] - 0.04) for node, coord in pos.items()}
label_positions = adjust_label_and_node_overlap(label_positions, pos)

nx.draw_networkx_nodes(G, pos, node_size=500, node_color="gray", alpha=1.0)
nx.draw_networkx_edges(G, pos, width=0.6, alpha=0.5, edge_color="gray")
nx.draw_networkx_labels(G, label_positions, font_size=9, font_color="black")

for node, (x, y) in pos.items():
    if node in user_photos:
        img_path = user_photos[node]
        img = plt.imread(img_path)
        imagebox = OffsetImage(img, zoom=0.06)  
        ab = AnnotationBbox(imagebox, (x, y), frameon=False)
        plt.gca().add_artist(ab)

downloads_folder = os.path.expanduser("~/Downloads")
os.makedirs(downloads_folder, exist_ok=True)

plt.axis("off")  
plt.tight_layout()  
downloads_folder = os.path.expanduser("~/Downloads")
os.makedirs(downloads_folder, exist_ok=True)

output_path = os.path.join(downloads_folder, "generate_graph.jpeg")
plt.savefig(output_path, dpi=300) 
print(f"Gráfico salvo em: {output_path}")

subprocess.run(["code", output_path])