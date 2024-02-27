import numpy as np
from pathlib import Path
import os
import tqdm
import glob
from wata.file.utils import utils as file
from wata.pointcloud.utils.load_pcd import get_points_from_pcd_file
from wata.pointcloud.utils.o3d_visualize_utils import open3d_draw_scenes, show_pcd_from_points_by_open3d
from wata.pointcloud.utils.qtopengl_visualize_utils import show_pcd_from_points_by_qtopengl

def cut_pcd(points, pcd_range):
    x_range = [pcd_range[0], pcd_range[3]]
    y_range = [pcd_range[1], pcd_range[4]]
    z_range = [pcd_range[2], pcd_range[5]]
    mask = (x_range[0] <= points[:, 0]) & (points[:, 0] <= x_range[1]) & (y_range[0] < points[:, 1]) & (
            points[:, 1] <= y_range[1]) & (z_range[0] < points[:, 2]) & (points[:, 2] <= z_range[1])
    points = points[mask]
    return points


def get_points(path, num_features):
    pcd_ext = Path(path).suffix
    if pcd_ext == '.bin':
        num_features = 4 if num_features is None else num_features
        points = np.fromfile(path, dtype=np.float32).reshape(-1, num_features)
    elif pcd_ext == ".npy":
        points = np.load(path)
    elif pcd_ext == ".pcd":
        num_features = 3 if num_features is None else num_features
        points = get_points_from_pcd_file(path, num_features=num_features)
    else:
        raise NameError("Unable to handle {} formatted files".format(pcd_ext))
    return points[:, 0:num_features]


def pcd2bin(pcd_dir, bin_dir, num_features=4):
    file.mkdir_if_not_exist(bin_dir)
    pcd_list = glob.glob(pcd_dir + "./*.pcd")
    for pcd_path in tqdm.tqdm(pcd_list):
        filename, _ = os.path.splitext(pcd_path)
        filename = filename.split("\\")[-1]
        points = get_points_from_pcd_file(pcd_path, num_features=num_features)
        points = points[:, 0:num_features].astype(np.float32)
        bin_file = os.path.join(bin_dir, filename) + '.bin'
        points.tofile(bin_file)
    print("==> The bin file has been saved in \"{}\"".format(bin_dir))


def show_pcd(path, point_size=1, background_color=[0, 0, 0], pcd_range=None, bin_num_features=None,create_coordinate=True, create_plane=True, type='open3d'):
        points = get_points(path, num_features=bin_num_features)
        if pcd_range:
            points = cut_pcd(points, pcd_range)
        show_pcd_from_points(points=points, point_size=point_size, background_color=background_color,create_coordinate=create_coordinate, create_plane=create_plane,
                                               type=type)

def show_pcd_from_points(points, point_size=1, background_color=[0, 0, 0], colors=None, create_coordinate=True, create_plane=True, type='open3d'):
        if type == 'open3d':
            show_pcd_from_points_by_open3d(
                            points=points, point_size=point_size,
                            background_color=background_color,
                            create_coordinate=create_coordinate,
                            create_plane=create_plane,
                            colors=colors
                            )
        elif type == 'qtopengl':
            show_pcd_from_points_by_qtopengl(
                            points=points,
                            point_size=point_size, 
                            background_color=background_color,
                            create_coordinate=create_coordinate, 
                            create_plane=create_plane
                            )
        elif type == 'matplotlib':
             pass
        elif type == 'mayavi':
            pass
        elif type == 'vispy':
            pass

def add_boxes(points, gt_boxes=None, ref_boxes=None, ref_labels=None, ref_scores=None, point_colors=None,
                  draw_origin=True, type='open3d'):
        if type == 'open3d':
            open3d_draw_scenes(
                points=points,
                gt_boxes=gt_boxes,
                ref_boxes=ref_boxes,
                ref_labels=ref_labels,
                ref_scores=ref_scores,
                point_colors=point_colors,
                draw_origin=draw_origin
            )
        elif type == 'qtopengl':
            pass
        elif type == 'matplotlib':
             pass
        elif type == 'mayavi':
            pass
        elif type == 'vispy':
            pass