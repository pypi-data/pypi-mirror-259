import json


def serialize(node):
    elements = _serialize(node)
    result = {"nodes": [], "edges": []}
    for el in elements:
        if el.get("position"):
            result["nodes"].append(el)
        else:
            result["edges"].append(el)
    return result


def _serialize(node, order=0):
    elements = []
    node_type = node.__class__.__name__.lower()
    node_element = {}
    node_element["id"] = node.name()
    node_element["type"] = node_type
    if node_type == "job":
        node_element.update(get_job_attrs(node))
    elif node_type == "task":
        node_element.update(get_task_attrs(node))
    elif node_type == "upload":
        node_element.update(get_upload_attrs(node))

    node_element["num_children"] = len(node.children)
    node_element["num_parents"] = len(node.parents)
    node_element["num_ancestors"] = node.count_ancestors()
    node_element["num_descendants"] = node.count_descendents()

    elements.append({"data": node_element, "position": {"x": 0, "y": order}})

    # edges
    for c in node.children:
        edge_element = {}
        edge_element["source"] = c.name()
        edge_element["target"] = node.name()
        edge_element["type"] = "edge"
        elements.append({"data": edge_element})

    # nodes
    for i, c in enumerate(node.children):
        if c.is_original(node):
            elements.extend(_serialize(c, i))

    return elements


def get_job_attrs(job):
    attrs = {}
    attrs["comment"] = job.comment()
    attrs["author"] = job.author()
    attrs["created_at"] = job.created_at()
    attrs["schema_version"] = job.schema_version()
    attrs["metadata"] = job.metadata()
    attrs["location"] = job.location()
    attrs["project"] = job.project()
    stat = job.status()
    attrs["status"] = "SUCCESS" if stat == "100" else stat
    return attrs


def get_task_attrs(task):
    attrs = {}
    attrs["commands"] = [dict(c) for c in task.commands()]
    attrs["outputs"] = task.outputs()
    attrs["hardware"] = task.hardware()
    attrs["env"] = task.env()
    attrs["lifecycle"] = task.lifecycle()
    attrs["attempts"] = task.attempts()
    attrs["initial_state"] = task.initial_state()
    stat = task.status()
    attrs["status"] = "SUCCESS" if stat == "100" else stat
    return attrs


def get_upload_attrs(upload):
    attrs = {}
    attrs["files"] = upload.files()
    attrs["outputs"] = upload.outputs()
    attrs["initial_state"] = upload.initial_state()
    stat = upload.status()
    attrs["status"] = "SUCCESS" if stat == "100" else stat
    return attrs
