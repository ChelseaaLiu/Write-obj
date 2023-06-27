import pyvista as pv

glb_filename = r"C:\Users\Chelsea\Documents\Mol\mol-data\test.glb"

pl = pv.Plotter()
pl.import_gltf(glb_filename)
pl.camera.zoom(1.1)
pl.show()