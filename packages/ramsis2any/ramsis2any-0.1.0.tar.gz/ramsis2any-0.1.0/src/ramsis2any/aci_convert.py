import dataclasses
import itertools
import jinja2
import pathlib

import xmltodict

import numpy as np


@dataclasses.dataclass
class BodyMass:
    name: str
    value: float


def parse_bodymasses(xmldata: dict) -> list[BodyMass]:
    bodymasses = []
    for entry in xmldata["RAMSISModelNode"]["BodyMasses"]["BodyMass"]:
        try:
            bodymasses.append(BodyMass(name=entry["@name"], value=float(entry["@value"])))
        except ValueError:
            continue
    return bodymasses

def ensure_list(x: list | dict) -> list:
    if isinstance(x, dict):
        return [x]
    return x


def contact_id(x: dict) -> str:
    return x["@contact"] + "_" + (x["@geoObject"] or "TBD")

def get_all_contacts(frames) -> set[str]:
    contacts = set()
    for frame in frames:
        for collision in ensure_list(frame["Collision"]):
            contacts.add(contact_id(collision))

    return contacts


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def get_contact_masks(xmldata: dict) -> dict[str, np.ndarray]:
    frames = xmldata["RAMSISModelNode"]["Frames"]["Frame"]
    last_frame = int(xmldata["RAMSISModelNode"]["Frames"]["Frame"][-1]["@frameNum"])
    contact_arrays = {k: np.zeros(last_frame, dtype=int) for k in get_all_contacts(frames)}

    for frame, next_frame in pairwise(frames):
        current_frame_idx = int(frame["@frameNum"]) -1 
        next_frame_idx = int(next_frame["@frameNum"]) -1
        for collision in ensure_list(frame["Collision"]):
            contact_arrays[contact_id(collision)][current_frame_idx:next_frame_idx] = 1
    return contact_arrays


def main(filename, target, template = None):
    with open(filename) as fd:
        xmldata = xmltodict.parse(fd.read())

    if template is None:
        env = jinja2.Environment(loader=jinja2.PackageLoader("ramsis2any"))
        template = env.get_template("ramsis-data.any.jinja")
    else:
        template = jinja2.Template(pathlib.Path(template).read_text())

    pathlib.Path(target).write_text(
        template.render(
            contact_masks=get_contact_masks(xmldata),
            body_masses=parse_bodymasses(xmldata)
    ))

