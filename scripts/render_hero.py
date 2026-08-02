#!/usr/bin/env python3
"""Render the README hero from a generated background and audited graph data."""

from __future__ import annotations

import argparse
import base64
import html
import json
import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ASSET_DIR = ROOT / "assets" / "hero"


def straight_points(a, b, steps=48):
    x1, y1 = a
    x2, y2 = b
    return [
        (x1 + (x2 - x1) * index / steps, y1 + (y2 - y1) * index / steps)
        for index in range(steps + 1)
    ]


def ambient_graph(width, height, seed):
    rng = random.Random(seed)
    points = []
    # Sparse overlays only: the generated background remains the dominant field.
    for side, count in (("left", 22), ("right", 16)):
        for _ in range(count):
            if side == "left":
                x = rng.uniform(0.05, 0.47) * width
                center = 0.52 * height + 0.10 * height * math.sin(x / width * math.pi * 2.4)
                y = center + rng.gauss(0, 0.18 * height)
            else:
                x = rng.uniform(0.57, 0.98) * width
                center = 0.49 * height + 0.08 * height * math.sin(x / width * math.pi * 3.1)
                y = center + rng.gauss(0, 0.22 * height)
            y = min(max(y, 0.12 * height), 0.88 * height)
            points.append((x, y, side, rng.choice(("#20B2AA", "#4C78FF", "#9932CC", "#F59E0B"))))

    edges = set()
    for i, point in enumerate(points):
        candidates = []
        for j, other in enumerate(points):
            if i == j or point[2] != other[2]:
                continue
            distance = math.hypot(point[0] - other[0], point[1] - other[1])
            candidates.append((distance, j))
        for distance, j in sorted(candidates)[:2]:
            if distance < 0.19 * width:
                edges.add(tuple(sorted((i, j))))
    return points, sorted(edges)


def svg_path(points):
    start = points[0]
    return f"M {start[0]:.1f} {start[1]:.1f} " + " ".join(
        f"L {x:.1f} {y:.1f}" for x, y in points[1:]
    )


def render_svg(data, background_path, overlay_path, final_path):
    width = data["canvas"]["width"]
    height = data["canvas"]["height"]
    palette = data["palette"]
    label_scale = data["canvas"].get("label_scale", 1.0)
    nodes = {node["id"]: node for node in data["nodes"]}
    ambient, ambient_edges = ambient_graph(width, height, data["canvas"]["seed"])

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        "<defs>",
        '<filter id="glow" x="-300%" y="-300%" width="700%" height="700%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>',
        '<style>.label{font-family:"Segoe UI",Inter,Arial,sans-serif;fill:#e8f2f7;paint-order:stroke;stroke:#020817;stroke-width:4px;stroke-linejoin:round}.edge{fill:none;stroke:#79dfe5;stroke-width:1.15;opacity:.28}.question-edge{fill:none;stroke:#f59e0b;stroke-width:1.1;stroke-dasharray:6 8;opacity:.42}</style>',
        "</defs>",
        '<g id="ambient" opacity="0.55">',
    ]
    for i, j in ambient_edges:
        a, b = ambient[i], ambient[j]
        parts.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#63cbd7" stroke-width="0.65" opacity="0.14"/>')
    for x, y, _, color in ambient:
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.6" fill="{color}" opacity="0.46"/>')
    parts.append("</g><g id=\"semantic-edges\">")
    for edge in data["edges"]:
        source, target = nodes[edge["from"]], nodes[edge["to"]]
        points = straight_points((source["x"], source["y"]), (target["x"], target["y"]))
        css_class = "question-edge" if edge.get("style") == "question" else "edge"
        parts.append(f'<path class="{css_class}" d="{svg_path(points)}" data-relation="{html.escape(edge["relation"])}"/>')
    parts.append("</g><g id=\"semantic-nodes\">")
    for node in data["nodes"]:
        color = palette[node["kind"]]
        parts.append(f'<circle cx="{node["x"]}" cy="{node["y"]}" r="{node["radius"] + 6}" fill="{color}" opacity="0.16" filter="url(#glow)"/>')
        parts.append(f'<circle cx="{node["x"]}" cy="{node["y"]}" r="{node["radius"]}" fill="{color}" stroke="#d8ffff" stroke-width="0.8" stroke-opacity="0.56"/>')
        anchor = node.get("anchor", "start")
        x = node["x"] + node.get("label_dx", 14)
        y = node["y"] + node.get("label_dy", -10)
        font_size = node.get("font_size", 18) * label_scale
        parts.append(f'<text class="label" x="{x}" y="{y}" font-size="{font_size:.1f}" text-anchor="{anchor}">{html.escape(node["label"])}</text>')
    parts.append("</g></svg>")
    overlay = "\n".join(parts)
    overlay_path.write_text(overlay, encoding="utf-8")

    encoded = base64.b64encode(background_path.read_bytes()).decode("ascii")
    standalone = overlay.replace(
        "</defs>",
        "</defs>\n" + f'<image href="data:image/png;base64,{encoded}" x="0" y="0" width="{width}" height="{height}" preserveAspectRatio="xMidYMid slice"/>',
        1,
    )
    final_path.write_text(standalone, encoding="utf-8")


def load_font(size, bold=False):
    candidates = [
        Path("C:/Windows/Fonts/seguisb.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf"),
        Path("C:/Windows/Fonts/arial.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def hex_rgba(value, alpha=255):
    value = value.lstrip("#")
    return tuple(int(value[index:index + 2], 16) for index in (0, 2, 4)) + (alpha,)


def render_png(data, background_path, final_path, supersample=2):
    width = data["canvas"]["width"]
    height = data["canvas"]["height"]
    scale = supersample
    palette = data["palette"]
    label_scale = data["canvas"].get("label_scale", 1.0)
    nodes = {node["id"]: node for node in data["nodes"]}
    background = Image.open(background_path).convert("RGB").resize((width * scale, height * scale), Image.Resampling.LANCZOS)
    overlay = Image.new("RGBA", background.size, (0, 0, 0, 0))
    ambient_layer = Image.new("RGBA", background.size, (0, 0, 0, 0))
    ambient_draw = ImageDraw.Draw(ambient_layer)
    ambient, ambient_edges = ambient_graph(width, height, data["canvas"]["seed"])
    for i, j in ambient_edges:
        a, b = ambient[i], ambient[j]
        ambient_draw.line((a[0] * scale, a[1] * scale, b[0] * scale, b[1] * scale), fill=(99, 203, 215, 34), width=max(1, scale))
    for x, y, _, color in ambient:
        radius = 1.6 * scale
        ambient_draw.ellipse((x * scale - radius, y * scale - radius, x * scale + radius, y * scale + radius), fill=hex_rgba(color, 118))
    overlay.alpha_composite(ambient_layer)

    edge_layer = Image.new("RGBA", background.size, (0, 0, 0, 0))
    edge_draw = ImageDraw.Draw(edge_layer)
    for edge in data["edges"]:
        source, target = nodes[edge["from"]], nodes[edge["to"]]
        points = straight_points((source["x"], source["y"]), (target["x"], target["y"]), steps=72)
        scaled = [(x * scale, y * scale) for x, y in points]
        if edge.get("style") == "question":
            for index in range(0, len(scaled) - 1, 4):
                edge_draw.line(scaled[index:min(index + 2, len(scaled))], fill=(245, 158, 11, 105), width=max(2, scale))
        else:
            edge_draw.line(scaled, fill=(121, 223, 229, 68), width=max(2, scale))
    overlay.alpha_composite(edge_layer)

    glow = Image.new("RGBA", background.size, (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    for node in data["nodes"]:
        radius = (node["radius"] + 4) * scale
        x, y = node["x"] * scale, node["y"] * scale
        glow_draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=hex_rgba(palette[node["kind"]], 155))
    glow = glow.filter(ImageFilter.GaussianBlur(7 * scale))
    overlay.alpha_composite(glow)

    draw = ImageDraw.Draw(overlay)
    for node in data["nodes"]:
        color = palette[node["kind"]]
        radius = node["radius"] * scale
        x, y = node["x"] * scale, node["y"] * scale
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=hex_rgba(color), outline=(216, 255, 255, 150), width=max(1, scale))
        font = load_font(round(node.get("font_size", 18) * label_scale * scale), bold=node["kind"] == "synthesis")
        tx = (node["x"] + node.get("label_dx", 14)) * scale
        ty = (node["y"] + node.get("label_dy", -10)) * scale
        anchor = "rm" if node.get("anchor") == "end" else "lm"
        draw.text((tx, ty), node["label"], font=font, anchor=anchor, fill=(232, 242, 247, 226), stroke_width=2 * scale, stroke_fill=(2, 8, 23, 225))

    composed = Image.alpha_composite(background.convert("RGBA"), overlay)
    composed = composed.resize((width, height), Image.Resampling.LANCZOS).convert("RGB")
    composed.save(final_path, optimize=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--asset-dir", type=Path, default=DEFAULT_ASSET_DIR)
    args = parser.parse_args()
    asset_dir = args.asset_dir.resolve()
    data = json.loads((asset_dir / "graph.json").read_text(encoding="utf-8"))
    background = asset_dir / "background.png"
    render_svg(data, background, asset_dir / "overlay.svg", asset_dir / "hero-hidden-structure.svg")
    render_png(data, background, asset_dir / "hero-hidden-structure.png")
    print(asset_dir / "overlay.svg")
    print(asset_dir / "hero-hidden-structure.svg")
    print(asset_dir / "hero-hidden-structure.png")


if __name__ == "__main__":
    main()
