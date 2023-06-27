import pyvista as pv

def main():
    out_obj_path = r"C:\Users\Chelsea\Documents\Mol\read-obj\read-obj\Assets\obj\test1"
    glb_path = r"C:\Users\Chelsea\Documents\Mol\mol-data"
    tmp_filename = "test"
    tmp_filename = "test_10"
    tmp_filenames = ["test", "test_10"]
    # WriteObj(out_obj_path, glb_path, tmp_filename)
    for tmp_filename in tmp_filenames:
        # ShowGltf(glb_path, tmp_filename)
        WriteObj(out_obj_path, glb_path, tmp_filename)


def WriteObj(out_obj_path, glb_path, tmp_filename):
    glb_filename = f"{glb_path}/{tmp_filename}.glb"

    pl = pv.Plotter()
    pl.import_gltf(glb_filename)
    pl.camera.zoom(1.1)
    pl.export_obj(f"{out_obj_path}/{tmp_filename}.obj")


def ShowGltf(glb_path, tmp_filename):
    glb_filename = f"{glb_path}/{tmp_filename}.glb"
    pl = pv.Plotter()
    pl.import_gltf(glb_filename)
    pl.camera.zoom(1.1)
    print(pl.center)
    # pl.show()

if __name__ == "__main__":
    main()