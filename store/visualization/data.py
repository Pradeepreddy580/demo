import matplotlib.pyplot as plt
import base64
from io import BytesIO
def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph
def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(12,5))
    plt.title('name / price')
    plt.bar(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('name')
    plt.ylabel('price')
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_line(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(12,5))
    plt.title('name / price')
    plt.plot(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('name')
    plt.ylabel('Price')
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_pie(x,y):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(12,7))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('equal')
    ax.pie(y, labels=x, autopct='%1.2f%%')
    plt.show()
    graph = get_graph()
    return graph