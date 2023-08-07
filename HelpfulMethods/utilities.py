
#####################
### Image Loading ###
#####################

def load_image(img_path):
    return sitk.ReadImage("{}".format(img_path))

# img : the sitk loaded image (ex. using load_image())
def img_as_numpy(img):
    return sitk.GetArrayFromImage(img)

# img : the sitk loaded image (ex. using load_image())
def get_ijk_to_ras_mtx(img):
    origin             = np.array(img.GetOrigin())
    spacing            = np.array(img.GetSpacing())
    origin             = np.expand_dims(origin,1)
    spacing            = np.expand_dims(spacing,1)
    direction          = np.array(img.GetDirection()).reshape(3,3)
    d                  = np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])
    ijkToRASDirections = np.matmul(direction, d)
    R                  = np.matmul(ijkToRASDirections, np.diag(np.expand_dims(spacing.T,1)[0][0]))
    t                  = np.matmul(direction, origin).T
    ijkToRas           = np.zeros((4,4))
    ijkToRas[0:3, 0:3] = R
    ijkToRas[0:3, 3]   = t
    ijkToRas[3, 3]     = 1
    return ijkToRas

# img : the sitk loaded image in numpy format (ex. using img_as_numpy())
# ijk_to_ras_mtx : the 4x4 matrix converting from IJK to RAS coordinates (ex. using get_ijk_to_ras_mtx())
# ras_points (output) : n x 3 matrix
def get_img_content_in_ras(img_np, ijk_to_ras_mtx):
    #
    points_kji = np.where(img_np > 0)
    points_kji = np.array([points_kji[0], points_kji[1], points_kji[2]])
    points_kji = points_kji.T
    #
    points_ijk = np.zeros_like(points_kji)
    points_ijk[:,0] = points_kji[:,2]
    points_ijk[:,1] = points_kji[:,1]
    points_ijk[:,2] = points_kji[:,0]
    #
    ijk_homogeneous = np.ones((points_Ijk.shape[0], points_Ijk.shape[1] + 1))
    ijk_homogeneous[:,:-1] = points_Ijk
    #
    ras_points = ijk_homogeneous.dot(ijk_to_ras_mtx.T)[:,0:3]
    #
    return ras_points


###############################
### Visualization in Open3D ###
###############################

# fpath : a path to the point-cloud points that have shape n x 3
# color: gray is default color
def load_as_point_cloud(fpath, color=[230/255, 230/255, 230/255], scale=1.0):
    x             = np.load(fpath)
    source        = o3d.geometry.PointCloud()
    source.points = o3d.utility.Vector3dVector(x)
    source.paint_uniform_color(color)
    return source


# poses : a numpy array with shape (n, 4, 4) of pose matrices
def get_pose_representations(poses, colors=None, orientation=False, size=10):
    point_clouds = []
    for i in range(poses.shape[0]):
        p  = poses[i]

        # represent as a coordinate frame
        if orientation:
            rep = o3d.geometry.TriangleMesh.create_coordinate_frame(size=size)
            rep.transform(p)
        # represent as a sphere
        else:
            rep = o3d.geometry.TriangleMesh().create_sphere(radius=1.0)
            rep.translate(p[:3,3], relative=False)

        # assign a color
        if colors is not None:
            rep.paint_uniform_color(colors[i])
        
        point_clouds.append(rep)

    return point_clouds


################
### Examples ###
################

def load_img_and_save_in_ras():
    import numpy as np
    import SimpleITK as sitk

    img_path       = "bronchialTree.nii.gz"
    img            = load_image(img_path)
    img_np         = img_as_numpy(img)
    ijk_to_ras_mtx = get_ijk_to_ras_mtx(img)
    ras            = get_img_content_in_ras(img_np, ras)
    np.save("airway.npy", ras)


def open3d_example():
    import numpy as np
    import open3d as o3d
    
    # load the airway point cloud (RAS coordinates saved from get_img_content_in_ras())
    ptcld_f = "airway.npy"
    airway_ptcld  = load_as_point_cloud(ptcld_f)

    # load the start poses puncture(s)
    puncture_files = ["start1.txt", "start2.txt"]
    ps = np.zeros((len(puncture_files), 4, 4))
    for i in range(len(puncture_files)):
        ps[i] = np.loadtxt(puncture_files[i])

    puncture = get_pose_representations(ps, orientation=True)

    # load the target
    t = np.loadtxt("target.txt")
    T = np.eye(4)
    T[:3,3] = t
    target = get_pose_representations(np.array([T]))

    # visualize
    o3d.visualization.draw_geometries([airway_ptcld] + puncture + target)





