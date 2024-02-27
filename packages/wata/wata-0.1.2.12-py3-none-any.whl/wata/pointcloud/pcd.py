from wata.pointcloud.utils import utils
from wata.pointcloud.utils import move_pcd

class PointCloudProcess:

    @staticmethod
    def cut_pcd(points, pcd_range):
        return utils.cut_pcd(points, pcd_range)

    @staticmethod
    def show_pcd(path, point_size=1, background_color=[0, 0, 0], pcd_range=None, bin_num_features=None,create_coordinate=True, create_plane=True, type='open3d'):
        utils.show_pcd(path, point_size, background_color, pcd_range, bin_num_features,create_coordinate, create_plane, type)

    @staticmethod
    def show_pcd_from_points(points, point_size=1, background_color=[0, 0, 0], colors=None, create_coordinate=True, create_plane=True, type='open3d'):
        utils.show_pcd_from_points(points, point_size, background_color, colors, create_coordinate, create_plane, type)

    @staticmethod
    def get_points(path, num_features=3):
        return utils.get_points(path, num_features)

    @staticmethod
    def add_boxes(points, gt_boxes=None, ref_boxes=None, ref_labels=None, ref_scores=None, point_colors=None, draw_origin=True, type='open3d'):
        utils.add_boxes(points, gt_boxes, ref_boxes, ref_labels, ref_scores, point_colors, draw_origin, type)

    @staticmethod
    def pcd2bin(pcd_dir, bin_dir, num_features=4):
        utils.pcd2bin(pcd_dir, bin_dir, num_features)

    @staticmethod
    def xyzrpy2RTmatrix(dx, dy, dz, roll, pitch, yaw):
        return move_pcd.xyzrpy2RTmatrix(dx, dy, dz, roll, pitch, yaw)
    
    @staticmethod
    def RTmatrix2xyzrpy(RTmatrix):
        return move_pcd.RTmatrix2xyzrpy(RTmatrix)

    @staticmethod
    def move_pcd_with_RTmatrix(points, RTmatrix):
        return move_pcd.move_pcd_with_RTmatrix(points, RTmatrix)

    @staticmethod
    def move_pcd_with_xyzrpy(points, dx, dy, dz, roll, pitch, yaw):
        return move_pcd.move_pcd_with_xyzrpy(points, dx, dy, dz, roll, pitch, yaw)
