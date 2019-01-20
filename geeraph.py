import webbrowser
import os

def show(x, y=False):

    if not y:
        t = [p[0] for p in x]
        y = [p[1] for p in x]
        x = t

    # set up output graph file
    graph_html = "graph.html"
    out_file   = open(graph_html, 'w')

    # read the template and parse in the data
    template = open("template.html").read().strip()
    x_str = f"[{','.join([str(d) for d in x])}]"
    y_str = f"[{','.join([str(d) for d in y])}]"

    # create template with data
    template = template.replace("\"XXX\"", x_str).replace("\"YYY\"", y_str)
    out_file.write(template)
    out_file.close()

    # render template in browser
    dir_path = os.path.dirname(os.path.realpath(__file__))
    url = "file://" + dir_path + "/" + graph_html
    webbrowser.open_new_tab(url)
